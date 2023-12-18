export type Dataset = {
    name: string,
    path: string,
    items: DatasetItem[]
};

export type DatasetItem =
      DirectoryItemType
    | UnknownFileItemType
    | UntaggedImageItemType
    | OrphanedTagsItemType
    | ParentedTagsItemType
    | TaggedImageItemType
;

export type DirectoryItemType = { 
    name: string,
    itemType: "directory" 
};

export type UnknownFileItemType = { 
    name: string,
    itemType: "unknownFile"
};

export type UntaggedImageItemType = { 
    name: string,
    itemType: "untaggedImage"
};

export type OrphanedTagsItemType = { 
    name: string,
    itemType: "orphanedTags"
};

export type ParentedTagsItemType = { 
    name: string,
    itemType: "parentedTags"
};

export type TaggedImageItemType = { 
    name: string,
    itemType: "taggedImage",
    path: string,
    tags: string[]
};