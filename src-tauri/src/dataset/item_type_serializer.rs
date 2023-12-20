use serde::{Serializer, ser::SerializeStruct};

use super::dataset::DatasetItemType;
use DatasetItemType::{Directory, UnknownFile, Image, Tags};

pub fn serialize_dataset_item_type<S: Serializer>(
    value: &DatasetItemType,
    serializer: S
) -> Result<S::Ok, S::Error> {
    match value {
        Directory | UnknownFile => {
            let mut s = serializer.serialize_struct("DatasetItemType", 1)?;
            s.serialize_field("itemType", value)?;
            s.end()
        }
        Image(path, tag_file_name) => {
            let len = if tag_file_name.is_none() { 2 } else { 3 };

            let mut s = serializer.serialize_struct("DatasetItemType", len)?;
            s.serialize_field("itemType", "image")?;
            s.serialize_field("path", path)?;

            if tag_file_name.is_some() {
                s.serialize_field("tagFileName", tag_file_name)?;
            }
            
            s.end()
        },
        Tags(taglist, image_file_name) => {
            let len = if image_file_name.is_none() { 2 } else { 3 };

            let mut s = serializer.serialize_struct("DatasetItemType", len)?;
            s.serialize_field("itemType", "tags")?;
            s.serialize_field("tags", &taglist.tags.join(", "))?;

            if image_file_name.is_some() {
                s.serialize_field("imageFileName", image_file_name)?;
            }
            
            s.end()
        }
    }
}