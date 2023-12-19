use std::{collections::HashSet, ffi::OsStr};
use std::fs::read_dir;
use std::path::PathBuf;
use std::vec::Vec;

use serde::Serialize;

use super::{Taglist, item_type_serializer::serialize_dataset_item_type};

#[derive(Serialize)]
#[serde(rename_all = "camelCase")]
pub struct Dataset {
    name: String,
    path: PathBuf,
    items: Vec<DatasetItem> 
}

#[derive(Serialize)]
#[serde(rename_all = "camelCase")]
pub struct DatasetItem {
    name: String,
    #[serde(flatten, serialize_with = "serialize_dataset_item_type")]
    item_type: DatasetItemType
}

//TODO: Conflicts are not taken into account.
#[derive(Serialize)]
#[serde(rename_all = "camelCase")]
pub enum DatasetItemType {
    Directory,
    UnknownFile,
    Tags(Taglist, Option<String>), //what about UnattachedTags ?
    Image(PathBuf, Option<String>)
}

impl Dataset {
    pub fn from_path(path: PathBuf) -> Self {
        Dataset {
            name: option_osstr_to_string(path.file_name()),
            path: path.clone(),
            items: load_items_from_path(&path)
        }
    }
}

const RECOGNIZED_IMAGE_FORMATS: [&str; 5] = ["jpg", "jpeg", "png", "bmp", "webp"];

// This is clearly not clean at all. TODO: clean this !!!
fn load_items_from_path(path: &PathBuf) -> Vec<DatasetItem> {
    let all_files: HashSet<PathBuf> = read_dir(&path)
                                            .unwrap()
                                            .map(Result::unwrap)
                                            .map(|x| x.path())
                                            .collect();


    let image_files: HashSet<&PathBuf>  = all_files
                                            .iter()
                                            .filter(|path| path.extension().is_some() && RECOGNIZED_IMAGE_FORMATS.contains(&option_osstr_to_string(path.extension()).as_str()))
                                            .collect();
    
    let mut known_files = HashSet::<PathBuf>::new();

    let mut result = Vec::new();

    for image_file in image_files {
        let image_tags_file = image_file.with_extension("txt");

        if image_tags_file.exists() {
            result.push(DatasetItem {name: option_osstr_to_string(image_file.file_name()), item_type: DatasetItemType::Image(image_file.clone(), image_tags_file.file_name().map(osstr_to_string))});
            result.push(DatasetItem {name: option_osstr_to_string(image_tags_file.file_name()), item_type: DatasetItemType::Tags(Taglist::new(), image_file.file_name().map(osstr_to_string))}); //TODO: fill the tags
            known_files.insert(image_tags_file.clone());
        } else {
            result.push(DatasetItem {name: option_osstr_to_string(image_file.file_name()), item_type: DatasetItemType::Image(image_file.clone(), None)});
        }
        
        known_files.insert(image_file.clone());
    }

    let remaining_files: HashSet<&PathBuf> = all_files.difference(&known_files).collect();
    for file in remaining_files {
        if file.is_dir() {
            result.push(DatasetItem {name: option_osstr_to_string(file.file_name()), item_type: DatasetItemType::Directory});
        } else if file.extension().is_some() && option_osstr_to_string(file.extension()) == "txt" {
            result.push(DatasetItem {name: option_osstr_to_string(file.file_name()), item_type: DatasetItemType::Tags(Taglist::new(), None)}); //TODO: fill the tags
        } else {
            result.push(DatasetItem {name: option_osstr_to_string(file.file_name()), item_type: DatasetItemType::UnknownFile});
        }
    }

    result
}

fn option_osstr_to_string(option_osstr: Option<&OsStr>) -> String {
    osstr_to_string(option_osstr.unwrap())
}

fn osstr_to_string(osstr: &OsStr) -> String {
    osstr.to_os_string().into_string().unwrap()
}