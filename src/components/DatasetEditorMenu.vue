<script setup lang="ts">
    import { PropType, ref } from 'vue';

    import Menubar from 'primevue/menubar';

    import router from "../router";

    const props = defineProps({
        showSidepanel: {
            type: Function as PropType<() => void>,
            required: true
        }
    });

    const menuItems = ref([
        {
            label: "File",
            items: [
                {
                    label: "Save current image"
                },
                {
                    label: "Save all opened images"
                },
                {
                    separator: true
                },
                {
                    label: "Close Editor",
                    command: () => {
                        router.push("/");
                    }
                }
            ]
        },
        {
            label: "View",
            items: [
                {
                    label: "File Explorer",
                    command: () => {
                        props.showSidepanel();
                    }
                }
            ]
        }
    ]);
</script>

<template>
    <Menubar :model="menuItems" />
</template>

<style scoped>
    .p-menubar {
        border-radius: 0%;
    }
</style>