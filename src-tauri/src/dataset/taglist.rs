use std::vec::Vec;

//Could this be converted into a tuple-struct ?
pub struct Taglist {
    tags: Vec<String>
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
}