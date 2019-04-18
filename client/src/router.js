import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Room from './views/Room.vue'
import Prediction from './views/Prediction.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/:room',
      name: 'room',
      component: Room
    },
    {
      path: '/:room/prediction',
      name: 'prediction',
      component: Prediction
    }
  ]
})
