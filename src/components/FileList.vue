<script setup lang="ts">
    import { ref } from "vue";

    import Listbox from "primevue/listbox";

    import { useDatasetStore } from "../stores/datasetStore";

    const store = useDatasetStore();

    const selectedItem = ref(); //type is same as files[x]
</script>

<template>
    <Listbox v-model="selectedItem" :options="store.datasetItems" optionLabel="name"/>
</template>

<style scoped>
    .p-listbox {
        border: none;
    }
</style>