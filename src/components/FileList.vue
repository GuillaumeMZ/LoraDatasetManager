<script setup lang="ts">
    import { ref } from "vue";

    import Listbox from "primevue/listbox";

    import { useDatasetStore } from "../stores/datasetStore";
    import { DatasetItem } from "../types/dataset";

    const store = useDatasetStore();

    const selectedItem = ref(); //type is same as files[x]
    //TODO: watch selectedItem to change the displayed image if needed

    //iconClass and iconColor could be refactored into one func
    //+ they need to be renamed
    const iconClass = (item: DatasetItem): string => {
        switch(item.itemType) {
            case "directory": return 'pi-folder';
            case "orphanedTags": return "pi-pencil";
            case "parentedTags": return "pi-pencil";
            case "taggedImage": return "pi-image";
            case "unknownFile": return "pi-file";
            case "untaggedImage": return "pi-image";
        }
    };

    const iconColor = (item: DatasetItem): string => {
        switch(item.itemType) {
            case "directory": return 'orange';
            case "orphanedTags": return "red";
            case "parentedTags": return "green";
            case "taggedImage": return "green";
            case "unknownFile": return "orange";
            case "untaggedImage": return "red";
        }
    };
</script>

<template>
    <Listbox v-model="selectedItem" :options="store.datasetItems" optionLabel="name">
        <template #option="slotProps">
            <i :class="['pi', iconClass(slotProps.option)]"></i>
            <p :style="{ color: iconColor(slotProps.option) }">{{ slotProps.option.name }}</p>
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

    .p-listbox-item p {
        color: red;
    }
</style>