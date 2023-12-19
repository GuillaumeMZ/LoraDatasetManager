<script setup lang="ts">
    import { ref } from "vue";

    import Listbox from "primevue/listbox";

    import { useDatasetStore } from "../stores/datasetStore";

    const store = useDatasetStore();

    const selectedItem = ref(); //type is same as files[x]
    //TODO: watch selectedItem to change the displayed image if needed

    const datasetItemStyles: { [id: string]: { icon: string, color: string } } = {
        "directory": { icon: "pi-folder", color: "orange" },
        "orphanedTags": { icon: "pi-pencil", color: "red" },
        "parentedTags": { icon: "pi-pencil", color: "green" },
        "taggedImage": { icon: "pi-image", color: "green" },
        "unknownFile": { icon: "pi-file", color: "orange" },
        "untaggedImage": { icon: "pi-image", color: "red" }
    }
</script>

<template>
    <Listbox v-model="selectedItem" :options="store.datasetItems" optionLabel="name">
        <template #option="slotProps">
            <i :class="['pi', datasetItemStyles[slotProps.option.itemType].icon]"></i>
            <p :style="{ color: datasetItemStyles[slotProps.option.itemType].color }">{{ slotProps.option.name }}</p>
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