<script setup lang="ts">
    import { computed, Ref, ref } from "vue";

    import Image from "primevue/image";
    import Textarea from "primevue/textarea";
    import Galleria from "primevue/galleria";

    import { useDatasetStore } from "../stores/datasetStore";
    import { Tags } from "../types/dataset";

    const store = useDatasetStore();
    
    const activeIndex: Ref<number> = ref(0);
        
    const props = defineProps(["images"]);
    const tags = computed({
        //TODO: clean
        get() {
            const currentImage = store.images[activeIndex.value];
            const tagsItem = store.items.find(item => item.itemType === "tags" && item.imageFileName !== undefined && item.imageFileName === currentImage.name) as Tags | undefined;
            
            return tagsItem?.tags;
        },
        set(newTags) {
            const currentImage = store.images[activeIndex.value];
            const tagsItem = store.items.find(item => item.itemType === "tags" && item.imageFileName !== undefined && item.imageFileName === currentImage.name) as Tags | undefined;
        
            if(tagsItem !== undefined && newTags !== undefined) {
                tagsItem.tags = newTags;
            }
        }
    });
</script>

<template>
    <Galleria v-model:activeIndex="activeIndex" :value="props.images" :numVisible="5" :showItemNavigators="true">
        <template #item="slotProps">
            <Image :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" preview />
            <div id="tags">
                <Textarea v-if="slotProps.item.tagFileName !== undefined" v-model="tags" />
                <p v-else>This image is not tagged... yet.</p>
            </div>
        </template>
        <template #thumbnail="slotProps">
            <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" />
        </template>
    </Galleria>
</template>

<style scoped>
    /* TODO: clean css */
    .p-galleria {
        width: 100%;
        height: 100%;
    }

    .p-galleria :deep(.p-galleria-content) {
        width: 100%;
        height: 100%;
    }

    .p-galleria :deep(.p-galleria-item-wrapper) {
        width: 100%;
        flex-grow: 1;
    }

    .p-galleria :deep(.p-galleria-item-container) {
        width: 100%;
        height: 100%;
        align-items: center;
    }

    .p-galleria :deep(.p-galleria-item) {
        width: 100%;
        height: 100%;
    }

    .p-image {
        flex: 1 1 0px;
        height: 100%;
        position: relative;
    }

    .p-image :deep(img) {
        position: absolute;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        object-fit: contain;
    }

    .p-galleria :deep(.p-galleria-item-nav) {
        position: static;
    }

    .p-galleria :deep(.p-galleria-thumbnail-wrapper) {
        width: 100%;
        height: 100px;
    }

    .p-galleria :deep(.p-galleria-thumbnail-container) {
        width: 100%;
        height: 100%;
    }

    .p-galleria :deep(.p-galleria-thumbnail-item-content) {
        width: 140px;
        height: 100px;
        position: relative;
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
        padding: 10px;
    }

    p {
        text-align: center;
    }
</style>