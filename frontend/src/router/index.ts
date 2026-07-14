import { createRouter, createWebHistory } from 'vue-router'
import CertificateList from '../views/CertificateList.vue'

const routes = [
  {
    path: '/',
    redirect: '/certificates',
  },
  {
    path: '/certificates',
    name: 'Certificates',
    component: CertificateList,
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router