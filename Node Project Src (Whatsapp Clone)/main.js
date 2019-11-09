// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueCarousel from 'vue-carousel'
import { store } from './store'
import firebase from 'firebase'
import VueResource from 'vue-resource'
import * as VueGoogleMaps from 'vue2-google-maps'
import VeeValidate from 'vee-validate';
import VueFuse from 'vue-fuse'

import {
  Vuetify,
  VApp,
  VNavigationDrawer,
  VFooter,
  VList,
  VBtn,
  VIcon,
  VGrid,
  VToolbar,
  VForm,
  VTextField,
  VAlert,
  VCard,
  VCheckbox,
  VProgressLinear,
  VDivider,
  VImg,
  VSelect,
  VRadioGroup,
  VTabs,
  VAvatar,
  VBottomNav,
  VDatePicker,
  VSnackbar,
  VStepper,
  VSwitch,
  VBottomSheet,
  VSubheader,
  VMenu,
  transitions
} from 'vuetify'
import '../node_modules/vuetify/src/stylus/app.styl'

Vue.use(VueCarousel)
Vue.use(VueResource)
Vue.use(VeeValidate)
Vue.use(VueFuse)
Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyDJLnZ9GlytJ87G_EnJIcFxrV9cYD92ia4',
    libraries: 'places' // necessary for places input
  }
})
Vue.use(Vuetify, {
  components: {
    VApp,
    VNavigationDrawer,
    VFooter,
    VList,
    VBtn,
    VIcon,
    VGrid,
    VToolbar,
    VForm,
    VTextField,
    VAlert,
    VCard,
    VCheckbox,
    VProgressLinear,
    VDivider,
    VImg,
    VSelect,
    VRadioGroup,
    VTabs,
    VAvatar,
    VBottomNav,
    VDatePicker,
    VSnackbar,
    VStepper,
    VSwitch,
    VBottomSheet,
    VSubheader,
    VMenu,  
    transitions
  },
  theme: {
    primary: '#ED1344',
    secondary: '#FFFFFF',
    accent: '#757575',
    error: '#FF5252',
    info: '#2196F3',
    success: '#4CAF50',
    warning: '#FFC107'
  }
})

Vue.config.productionTip = false
Vue.config.devtools = true
Vue.config.debug = true

firebase.initializeApp({
  apiKey: 'AIzaSyA9fnwPTrP1dUflFx7HkWNgzG9h_4qt6KA',
  authDomain: 'campuscomforts-e77c1.firebaseapp.com',
  databaseURL: 'https://campuscomforts-e77c1.firebaseio.com',
  projectId: 'campuscomforts-e77c1',
  storageBucket: 'campuscomforts-e77c1.appspot.com',
  messagingSenderId: '711933323605'
})

/* eslint-disable no-new */
const unsubscribe = firebase.auth()
  .onAuthStateChanged((firebaseUser) => {
    new Vue({
      el: '#app',
      router,
      store,
      render: h => h(App),
      created () {
        if (firebaseUser) {
          store.dispatch('autoSignIn', firebaseUser)
        }
      }
    })
    unsubscribe()
  })
