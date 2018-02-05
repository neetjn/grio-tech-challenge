import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export const router = new Router({
  routes: [
    { path: '/', component: require('./routes/Home.vue') },
    { path: '/search', component: require('./routes/Search.vue') }
  ]
})
