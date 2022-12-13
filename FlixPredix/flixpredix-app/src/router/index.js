import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import StartPage from '../views/StartPage.vue'
import CredentialsPage from '../views/CredentialsPage.vue'

const routes = [
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  {
    path: '/credits',
    name: 'credits',
    component: CredentialsPage
  },
  {
    path: '/start',
    name: 'start',
    component: StartPage
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
