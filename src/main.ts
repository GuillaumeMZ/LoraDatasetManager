import { createApp } from "vue";
import { createPinia } from "pinia";
import PrimeVue from "primevue/config";
import 'primevue/resources/themes/lara-dark-green/theme.css';
import ToastService from "primevue/toastservice";

import "./styles.scss";
import App from "./App.vue";
import router from "./router";

createApp(App)
    .use(router)
    .use(createPinia())
    .use(PrimeVue)
    .use(ToastService)
    .mount("#app");