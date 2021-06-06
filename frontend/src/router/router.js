import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('../views/v-home'),
    name: '/home'
  },
  {
    path: '/login',
    component: () => import('../views/v-authorization'),
    name: 'login'
  },
  {
    path: '/leaders',
    component: () => import('../views/v-table-leaders'),
    name: 'leaders'
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router;