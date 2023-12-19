import { defineStore } from "pinia";
import { Dataset, DatasetItem, Image } from "../types/dataset";

//https://runthatline.com/pinia-typescript-type-state-actions-getters/
export const useDatasetStore = defineStore("dataset", {
    state: (): Dataset => ({
        name: "",
        path: "",
        items: []
    }),
    getters: {
        datasetName: (state) => state.name,
        datasetPath: (state) => state.path,
        datasetItems: (state): DatasetItem[] => state.items,
        images: (state): Image[] => state.items.filter(item => item.itemType === "image") as Image[]
        
    }
});