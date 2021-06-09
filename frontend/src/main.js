import { createApp } from 'vue'
import App from './App.vue'
import router from './router/router'
import store from './vuex/store'
import axios from 'axios'
import './assets/tailwind.css'

axios.defaults.baseURL = 'http://127.0.0.1:8000';

if (store.state.user.token) {
    axios.defaults.headers["Authorization"] =
        "Bearer " + store.state.user.token;

}

const app = createApp(App)
app.use(router)
app.use(store)
app.mount('#app')
