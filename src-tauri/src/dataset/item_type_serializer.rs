use serde::{Serializer, ser::SerializeStruct};

use super::dataset::DatasetItemType;
use DatasetItemType::{Directory, UnknownFile, UntaggedImage, OrphanedTags, ParentedTags, TaggedImage};

pub fn serialize_dataset_item_type<S: Serializer>(
    value: &DatasetItemType,
    serializer: S
) -> Result<S::Ok, S::Error> {
    match value {
        item_type @ (Directory | UnknownFile | UntaggedImage | OrphanedTags | ParentedTags) => {
            let mut s = serializer.serialize_struct("DatasetItemType", 1)?;
            s.serialize_field("itemType", item_type)?;
            s.end()
        }
        TaggedImage(path, taglist) => {
            let mut s = serializer.serialize_struct("DatasetItemType", 3)?;
            s.serialize_field("itemType", "taggedImage")?;
            s.serialize_field("path", path)?;
            s.serialize_field("tags", &taglist.tags)?;
            s.end()
        }
    }
}