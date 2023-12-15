use std::path::PathBuf;

use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize)]
pub struct Dataset {
    name: String,
    path: PathBuf
}

impl Dataset {
    pub fn from_path(path: PathBuf) -> Self {
        Dataset {
            name: path.file_name().unwrap().to_os_string().into_string().unwrap(),
            path
        }
    }
}