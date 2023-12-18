<script setup lang="ts">
    import { ref } from "vue";

    import Image from "primevue/image";
    import Galleria from "primevue/galleria";

    const activeIndex = ref();

    const props = defineProps(["images"]);
    
</script>

<template>
    <Galleria v-model:activeIndex="activeIndex" :value="props.images" :numVisible="5" :showItemNavigators="true">
        <template #item="slotProps">
            <Image :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" preview />
        </template>
        <template #thumbnail="slotProps">
            <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" />
        </template>
    </Galleria>
</template>

<style>
    /* TODO: clean css */
    .p-galleria {
        width: 100%;
        height: 100%;
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
    }

    .p-image {
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

    .p-galleria-item-nav {
        z-index: 2;
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

    .p-image-action {
        z-index: 1;
    }
</style>