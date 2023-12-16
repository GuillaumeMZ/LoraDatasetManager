export type Dataset = {
    name: string,
    path: string,
    items: [DatasetItem]
};

export type DatasetItem =
      { Directory: string }
    | { UnknownFile: string }
    | { UntaggedImage: string }
    | { OrphanedTags: string }
    | { ValidItem: [string, string, TaggedImage] }
;

export type TaggedImage = any;