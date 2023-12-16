<script setup lang="ts">
    import { invoke } from '@tauri-apps/api/tauri';
    import { open } from '@tauri-apps/api/dialog';
    import Button from 'primevue/button';

    import { useDatasetStore } from "../stores/datasetStore";
    import router from '../router';

    const store = useDatasetStore();

    const openDatasetSelector = async () => {
        const selectedDatasetPath = await open({
            directory: true,
            multiple: false,
            title: "Select a dataset"
        });

        if(selectedDatasetPath === null) {
            return;
        }

        // this should be refactored into a separated function when other dataset opening methods will be added
        //TODO: Dataset interface (remove any)
        const dataset: any = await invoke('load_dataset', { datasetPath: selectedDatasetPath });
        console.log(dataset);
        store.$state = dataset;
        
        router.push("/datasetEditor");
    };
</script>

<template>
    <div id="home">
        <Button label="Open a Dataset" @click="openDatasetSelector"/>
    </div>
</template>

<style scoped>
    div {
        width: 100vw;
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>