<script setup lang="ts">
    import { ref } from 'vue';

    import Menubar from 'primevue/menubar';

    import router from "../router";

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
        }
    ]);
</script>

<template>
    <Menubar :model="menuItems" />
</template>