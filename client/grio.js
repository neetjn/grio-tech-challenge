import '@/assets/styles/main.scss'

import Vue from 'vue'
import App from './components/App.vue'
import Router from './router'

new Vue({
  Router,
  el: '#root',
  render: h => h(App)
}).$mount('#root')
