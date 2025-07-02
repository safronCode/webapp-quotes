import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      meta: {title: 'QuoteHub'},
      component: () => import('@/views/HubPage.vue'),
    },
    {
      path: '/top',
      name: 'top',
      meta: {title: 'TopHub'},
      component: () => import('@/views/TopPage.vue'),
    }
  ],
})

export default router
