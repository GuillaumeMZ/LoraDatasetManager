<script setup lang="ts">
    import { computed, ref } from "vue";

    import Sidebar from "primevue/sidebar";

    import DatasetEditorMenu from "../components/DatasetEditorMenu.vue";
    import DatasetGalleria from "../components/DatasetGalleria.vue";
    import FileList from "../components/FileList.vue";
    import { useDatasetStore } from "../stores/datasetStore";

    import { convertFileSrc } from "@tauri-apps/api/tauri";
    import { TaggedImageItemType } from "../types/dataset";

    const sidebarVisible = ref(false); 

    const store = useDatasetStore();

    const images = computed(() => {
        const taggedImages: TaggedImageItemType[]  = store.datasetItems.filter(item => item.itemType === "taggedImage") as TaggedImageItemType[];
        return taggedImages.map(item => ({
            itemImageSrc: convertFileSrc(item.path),
            thumbnailImageSrc: convertFileSrc(item.path),
            alt: item.name,
            title: item.name
        }));
    });
</script>

<template>
    <div id="root">
        <DatasetEditorMenu :showSidepanel="() => {sidebarVisible = true;}" />
        <Sidebar v-model:visible="sidebarVisible" header="Files">
            <FileList/>
        </Sidebar>
        <DatasetGalleria v-if="images.length !== 0" :images="images"/>
        <div id="no-images" v-else>
            <p>It looks like there is no image in the dataset you have selected... 😔</p>
            <router-link to="/">Go back to the main menu</router-link>
        </div>
    </div>
</template>

<style scoped>
    #root {
        width: 100vw;
        height: 100vh;
        display: flex;
        flex-direction: column;
    }

    #no-images {
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
</style>