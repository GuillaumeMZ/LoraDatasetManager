<script setup lang="ts">
    import Button from 'primevue/button';

    import router from '../router';
    import { useDatasetStore } from '../stores/datasetStore';

    const store = useDatasetStore();
</script>

<template>
    <div id="root">
        <div>
            <p>{{ store.datasetName }}</p>
            <Button label="Go to Home" @click="router.push('/')" />
        </div>
    </div>
</template>

<style scoped>
    #root {
        width: 100vw;
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>