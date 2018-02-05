import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import Home from '@/router/routes/Home.vue'
import Search from '@/router/routes/Search.vue'

export default new Router({
  routes: [
    { path: '/', component: Home },
    { path: '/search', component: Search }
  ]
})
