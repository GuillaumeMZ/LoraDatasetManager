<script setup lang="ts">
import { computed, ref } from "vue";
import { convertFileSrc } from "@tauri-apps/api/tauri";

import Galleria from "primevue/galleria";

import DatasetEditorMenu from "../components/DatasetEditorMenu.vue";
import { useDatasetStore } from "../stores/datasetStore";
import { ValidItem } from "../types/dataset";

const store = useDatasetStore();

const activeIndex = ref();

const images = computed(() => {
    const validItems = store.datasetItems.filter(item => "ValidItem" in item) as ValidItem[];
    
    return validItems.map(item => ({
        itemImageSrc: convertFileSrc(item.ValidItem[0]),
        thumbnailImageSrc: convertFileSrc(item.ValidItem[0]),
        alt: "test",
        title: "test"
    }));
});

</script>

<template>
    <!-- <DatasetEditorMenu /> -->
    <Galleria v-model:activeIndex="activeIndex" :value="images" :numVisible="5" :showItemNavigators="true">
        <template #item="slotProps">
            <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" />
        </template>
        <template #thumbnail="slotProps">
            <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" />
        </template>
    </Galleria>
</template>

<style>
    .p-galleria {
        width: 100%;
        height: 100vh;
    }

    .p-galleria-content {
        width: 100%;
        height: 100%;
    }

    .p-galleria-item-wrapper {
        width: 100%;
        flex-grow: 1;
    }

    .p-galleria-item-container {
        width: 100%;
        height: 100%;
    }

    .p-galleria-item {
        width: 100%;
        height: 100%;
        position: relative;
    }

    img {
        position: absolute;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        object-fit: contain;
    }

    .p-galleria-thumbnail-wrapper {
        width: 100%;
        height: 100px;
    }

    .p-galleria-thumbnail-container {
        width: 100%;
        height: 100%;
    }

    .p-galleria-thumbnail-item-content {
        width: 140px;
        height: 100px;
        position: relative;
    }
</style>