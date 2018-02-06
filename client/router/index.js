import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import Home from '@/router/routes/Home.vue'
import About from '@/router/routes/About.vue'

export default new Router({
  routes: [
    { path: '/', component: Home },
    { path: '/about', component: About }
  ]
})
