import '@/assets/styles/main.scss'

import Vue from 'vue'
import App from './components/App.vue'
import router from './router'

import axios from 'axios'

const API_HOST = process.env.api_host || 'http://127.0.0.1'
const API_PORT = process.env.api_port || 3300

Vue.prototype.$http = axios
// # TODO: create a service description -- pull links from apiroot
Vue.prototype.$grio = {
  v1: {
    root: `${API_HOST}:${API_PORT}/api/rest/v1/`,
    people: `${API_HOST}:${API_PORT}/api/rest/v1/people/`,
    person: `${API_HOST}:${API_PORT}/api/rest/v1/`
  }
}

new Vue({
  router,
  render: h => h(App)
}).$mount('#root')
