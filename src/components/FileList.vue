<script setup lang="ts">
    import { Ref, ref } from "vue";

    import Listbox from "primevue/listbox";

    import { useDatasetStore } from "../stores/datasetStore";
    import { DatasetItem } from "../types/dataset";

    const store = useDatasetStore();

    const selectedItem: Ref<DatasetItem | undefined> = ref();
    //TODO: watch selectedItem to change the displayed image if needed

    const getDatasetItemStyles = (item: DatasetItem) => {
        switch(item.itemType) {
            case "directory": return { icon: "pi-folder", color: "orange" }
            case "orphanedTags": return { icon: "pi-pencil", color: "red" }
            case "parentedTags": return { icon: "pi-pencil", color: "green" }
            case "taggedImage": return { icon: "pi-image", color: "green" }
            case "unknownFile": return { icon: "pi-file", color: "orange" }
            case "untaggedImage": return { icon: "pi-image", color: "red" }
        }
    }
</script>

<template>
    <Listbox v-model="selectedItem" :options="store.datasetItems" optionLabel="name">
        <template #option="slotProps">
            <i :class="['pi', getDatasetItemStyles(slotProps.option).icon]"></i>
            <p :style="{ color: getDatasetItemStyles(slotProps.option).color }">{{ slotProps.option.name }}</p>
        </template>
    </Listbox>
</template>

<style>
    .p-listbox {
        border: none;
    }

    .p-listbox-item {
        display: flex;
        align-items: center;
        row-gap: 10px;
        column-gap: 10px;
    }
</style>