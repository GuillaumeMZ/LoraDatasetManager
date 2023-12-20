use std::{fs::File, io::Read};
use std::path::Path;
use std::vec::Vec;

use serde::{Serialize, Deserialize};

//Should this be converted into a tuple-struct ?
#[derive(Serialize, Deserialize)]
pub struct Taglist {
    pub tags: Vec<String> //temporary
}

impl Taglist {
    pub fn new() -> Self {
        Taglist {
            tags: Vec::new()
        }
    }

    pub fn from_string(source: &String) -> Self {
        Taglist {
            //TODO: write a real parser which can detect errors
            tags: source
                    .split(",")
                    .map(str::trim)
                    .filter(|x| !x.is_empty())
                    .map(str::to_string)
                    .collect()
        }
    }

    pub fn from_file(path: &Path) -> Self {
        let mut file_contents = String::new();
        File::open(path).unwrap()
                        .read_to_string(&mut file_contents)
                        .unwrap();
        
        Taglist::from_string(&file_contents)
    }
}