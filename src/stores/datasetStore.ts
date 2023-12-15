import { defineStore } from "pinia";

export const useDatasetStore = defineStore("dataset", {
    state: () => ({
        name: "",
        path: ""
    }),
    getters: {
        datasetName: (state) => state.name,
        datasetPath: (state) => state.path
    },
    actions: {
        setName(name: string) {
            this.name = name;
        }
    }
});