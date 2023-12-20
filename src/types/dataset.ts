export type Dataset = {
    name: string,
    path: string,
    items: DatasetItem[]
};

export type DatasetItem =
      Directory
    | Unknown
    | Tags
    | Image
;

export type Directory = { 
    name: string,
    itemType: "directory" 
};

export type Unknown = { 
    name: string,
    itemType: "unknownFile"
};

export type Image = { 
    name: string,
    itemType: "image",
    path: string,
    tagFileName ?: string
};

export type Tags = { 
    name: string,
    itemType: "tags",
    tags: string,
    imageFileName?: string
};