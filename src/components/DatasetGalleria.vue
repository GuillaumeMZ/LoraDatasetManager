<script setup lang="ts">
    import { Ref, ref } from "vue";

    import Image from "primevue/image";
    import Textarea from "primevue/textarea";
    import Galleria from "primevue/galleria";

    const activeIndex: Ref<number> = ref(0);

    const props = defineProps(["images"]);
    const text = ref();
</script>

<template>
    <Galleria v-model:activeIndex="activeIndex" :value="props.images" :numVisible="5" :showItemNavigators="true">
        <template #item="slotProps">
            <Image :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" preview />
            <div id="tags">
                <Textarea v-if="slotProps.item.tagFileName !== undefined" v-model="text" />
                <p v-else>This image is not tagged... yet.</p>
            </div>
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
        align-items: center;
    }

    .p-galleria-item {
        width: 100%;
        height: 100%;
    }

    .p-image {
        flex: 1 1 0px;
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
        position: static;
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

    #tags {
        flex: 1 1 0px;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    textarea {
        width: 100%;
        height: 100%;    
        border-radius: 0;
        resize: none;
    }

    p {
        text-align: center;
    }

</style>