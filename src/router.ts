import { getCurrent } from "@tauri-apps/api/window";
import { createRouter, createWebHashHistory } from "vue-router";

import { useDatasetStore } from "./stores/datasetStore";
import Home from "./components/Home.vue";
import DatasetEditor from "./components/DatasetEditor.vue";

const routes = [
    { 
        path: "/",
        component: Home,
        beforeEnter: (_to: any, _from: any) => {
            //TODO: should we clear the store here ?
            getCurrent().setTitle("Welcome - LoraDatasetManager");
        }
    },
    { 
        path: "/datasetEditor", 
        component: DatasetEditor,
        beforeEnter: (_to: any, _from: any) => {
            const store = useDatasetStore();
            getCurrent().setTitle(`Dataset "${store.name}" (${store.path}) - LoraDatasetManager`);
        }
    }
];

export default createRouter({
    history: createWebHashHistory(),
    routes
});
