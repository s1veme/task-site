import { createRouter, createWebHistory } from 'vue-router'
import store from '@/vuex/store'
import { useToast } from 'vue-toastification'

const toast = useToast()

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
    name: 'leaders',
  },
  {
    path: '/tasks',
    component: () => import('../views/v-tasks'),
    name: 'tasks',
    meta: {
      isAuth: true
    }
  },
  {
    path: '/task/:id',
    component: () => import('../views/v-task-info'),
    name: 'task',
    meta: {
      isAuth: true
    }
  },
  {
    path: '/profile/:username',
    component: () => import('../views/v-profile'),
    name: 'profile',
    meta: {
      isAuth: true
    }
  },
  {
    path: '/user_email_activate',
    component: () => import('../views/v-confrim-email'),
    name: 'email-activate'
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.isAuth)) {
    if (store.state.user.token) {
      next()
      return
    }
    toast.error('Пожалуйста, авторизуйтесь!')
    router.push('/')
  } else {
    next()
  }
})



export default router;
