import { defineStore } from "pinia";
import { DatasetItem } from "../types/dataset";

//https://runthatline.com/pinia-typescript-type-state-actions-getters/
export const useDatasetStore = defineStore("dataset", {
    state: () => ({
        name: "",
        path: "",
        items: undefined as unknown as DatasetItem[] //There is probably a better way to do this
    }),
    getters: {
        datasetName: (state) => state.name,
        datasetPath: (state) => state.path,
        datasetItems: (state) => state.items
    }
});