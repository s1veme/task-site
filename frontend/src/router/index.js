import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('../views/v-home')
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
