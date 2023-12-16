use std::{collections::HashSet, ffi::OsStr};
use std::fs::read_dir;
use std::path::PathBuf;
use std::vec::Vec;

use serde::{Serialize, Deserialize};

use super::TaggedImage;

#[derive(Serialize, Deserialize)]
pub struct Dataset {
    name: String,
    path: PathBuf,
    items: Vec<DatasetItem> 
}

//TODO: Conflicts are not taken into account.
#[derive(Serialize, Deserialize)]
pub enum DatasetItem {
    Directory(PathBuf),
    UnknownFile(PathBuf),
    UntaggedImage(PathBuf),
    OrphanedTags(PathBuf),
    ValidItem(PathBuf, PathBuf, TaggedImage) //.0: image, .1: tags
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

//This is clearly not clean at all. TODO: clean this !!!
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
            result.push(DatasetItem::ValidItem(image_file.clone(), image_tags_file.clone(), TaggedImage {})); //TODO: fill the TaggedImage
            known_files.insert(image_tags_file.clone());
        } else {
            result.push(DatasetItem::UntaggedImage(image_file.clone()));
        }
        
        known_files.insert(image_file.clone());
    }

    let remaining_files: HashSet<&PathBuf> = all_files.difference(&known_files).collect();
    for file in remaining_files {
        if file.is_dir() {
            result.push(DatasetItem::Directory(file.clone()));
        } else if option_osstr_to_string(file.extension()) == "txt" {
            result.push(DatasetItem::OrphanedTags(file.clone()));
        } else {
            result.push(DatasetItem::UnknownFile(file.clone()));
        }
    }

    result
}

fn option_osstr_to_string(option_osstr: Option<&OsStr>) -> String {
    option_osstr.unwrap().to_os_string().into_string().unwrap()
}