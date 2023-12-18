<script setup lang="ts">
    import { ref } from 'vue';

    import Menubar from 'primevue/menubar';

    import router from "../router";

    const props = defineProps(["showSidepanel"]); //TODO: typing

    const menuItems = ref([
        {
            label: "File",
            items: [
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

<style>
    .p-menubar {
        border-radius: 0%;
    }
</style>