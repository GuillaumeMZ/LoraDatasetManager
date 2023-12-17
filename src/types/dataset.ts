export type Dataset = {
    name: string,
    path: string,
    items: DatasetItem[]
};

export type Directory     = { Directory: string };
export type UnknownFile   = { UnknownFile: string };
export type UntaggedImage = { UntaggedImage: string };
export type OrphanedTags  = { OrphanedTags: string };
export type ValidItem     = { ValidItem: [string, string, TaggedImage] };

export type DatasetItem =
      Directory
    | UnknownFile
    | UntaggedImage
    | OrphanedTags
    | ValidItem
;

export type TaggedImage = any;