import Vue from 'vue'
import Router from 'vue-router'
import firebase from 'firebase'

// This is where you out the routes else they won't work
const routerOptions = [
  { path: '/', component: 'LandingPage' },
  { path: '/home', component: 'Home' },
  { path: '/addcard', component: 'AddCard', meta: { requiresAuth: true } },
  { path: '/message', component: 'Message', meta: { requiresAuth: true } },
  { path: '/cardview/:id', component: 'ViewCard' },
  { path: '/signup', component: 'Signup' },
  { path: '/signin', component: 'Signin' },
  { path: '/support', component: 'Support' },
  { path: '/saved', component: 'Saved' },
  { path: '/search', component: 'Search' },
  { path: '*', component: 'NotFound' },
  { path: '/verifyID', component: 'Verification'}
]

const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes
})

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth)
  const isAuthenticated = firebase.auth().currentUser
  if (requiresAuth && !isAuthenticated) {
    next('/signin')
  } else {
    next()
  }
})

export default router
