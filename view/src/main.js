import { createApp } from 'vue'
import App from './App.vue'
import router from './router/router'

import './assets/default.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'

const app = createApp(App)

app
    .use(router)
    .mount('#app')