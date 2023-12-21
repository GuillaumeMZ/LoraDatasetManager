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
            case "unknownFile": return { icon: "pi-file", color: "orange" }
            case "tags": return { icon: "pi-pencil", color: item.imageFileName === undefined ? "red" : "green" }
            case "image": return { icon: "pi-image", color: item.tagFileName === undefined ? "red" : "green" }
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

<style scoped>
    .p-listbox {
        width: 100%;
        height: 100%;
        border: none;
        border-radius: 0%;
        padding: 0.5em;
    }

    .p-listbox :deep(.p-listbox-item) {
        display: flex;
        align-items: center;
        row-gap: 10px;
        column-gap: 10px;
    }

    p {
        overflow: hidden;
        text-overflow: ellipsis;
    }
</style>