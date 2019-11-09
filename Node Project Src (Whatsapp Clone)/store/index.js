import Vue from "vue";
import Vuex from "vuex";
import firebase from "firebase";
import router from "@/router";

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    card: {
      // Basic Info
      title: "",
      description: "",
      homeType: "",
      singleShared:"",
      bedroom: "",
      beds: "",
      baths: "",
      // amenities
      basics: [],
      safety: [],
      accesability: [],
      // Location 
      address: "",
      stateParish: "",
      country: "",
      // Rules
      rules: "",
      yesNo: false,
      yesNo_1: false,
      yesNo_2: false,
      //Pricing
      price: "",
      selectedDate: [] 
    },
    cards: [],
    post: [],
    submitted: false,
    imageUrl: "",
    image: "",
    user: null,
    error: null,
    loading: false,
    search: "",
    activechat : '',
    getchats:[],
    chat_message:{},
    currentuser:null,
    pinging:null,
    newmessage_count:0,
    payment:null,
  },
  // Setters
  mutations: {
    setUser(state, payload) {
      state.user = payload;
    },
    setError(state, payload) {
      state.error = payload;
    },
    setLoading(state, payload) {
      state.loading = payload;
    },
    getCards(state, payload) {
      state.cards = payload;
    },
    getUser(state){
      Vue.http
      .get("https://innz-dev.firebaseio.com/users.json")
      .then(data => {
        return data.json();
      })
      .then(data => {
        for(let key in data) {
          if(key!=null &&  key!=0){
            if (data[key].email == state.user.email){
                state.currentuser = {
                  Name:data[key].firstname+" "+data[key].lastname,
                  FirstName:data[key].firstname,
                  Lastname:data[key].lastname,
                  Email:data[key].email
                }
                break;
              }
         }
        } 
      });
    },
    getChats(state){
     
      Vue.http
        .get("https://innz-dev.firebaseio.com/Chats.json")
        .then(data => {
          return data.json();
        })
        .then(data => {
          var allchats = [];
         
          
          for(let key in data) {
            if(key!=null &&  key!=0){
              allchats.push({
                  From:data[key].From,
                  To:data[key].To,
                  Date:data[key].Date,
                  Message:data[key].Message,
                  Read:data[key].Read
              });
           }
          }
          allchats.sort(function(a,b){
            return (new Date(a.Date)).getTime() - (new Date(b.Date)).getTime()
          })
          if(state.getchats.length<allchats.length && state.getchats.length>0){
              state.newmessage_count = state.newmessage_count+allchats.length-state.getchats.length;
          }
          if(state.getchats.length<allchats.length){
            for(let i = state.getchats.length;i<allchats.length;i++){
              state.getchats.push(allchats[i]);
            }
          }
        });
    },
    getPosts(state) {
      Vue.http
        .get("https://innz-dev.firebaseio.com/posts.json")
        .then(data => {
          return data.json();
        })
        .then(data => {
          var cardsArray = [];
          
          for (let key in data) {
            data[key].id = key;
            cardsArray.push(data[key]);
          }
          state.cards = cardsArray;
        });
    }
  },
  actions: {
    userSignUp({ commit }, payload) {
      commit("setLoading", true);
      firebase
      
        .auth()
        
        .createUserWithEmailAndPassword(payload.email, payload.password)
        .then(firebaseUser => {
          
          commit("setUser", {
            
            email: firebaseUser.user.email
            
          });
          commit("getUser");
          commit("setLoading", false);
          router.push("/home");
        })
        .catch(error => {
          commit("setError", error.message);
          commit("setLoading", false);
        });
    },
    userSignIn({ commit }, payload) {
      commit("setLoading", true);
      firebase
        .auth()
        .signInWithEmailAndPassword(payload.email, payload.password)
        .then(firebaseUser => {
          commit("setUser", {
            email: firebaseUser.user.email
          });
          commit("getUser");
          commit("setLoading", false);
          commit("setError", null);
          router.push("/home");
        })
        .catch(error => {
          commit("setError", error.message);
          commit("setLoading", false);
        });
    },
    autoSignIn({ commit }, payload) {
      commit("setUser", {
        email: payload.email
      });
      commit("getUser");
    },
    userSignOut({ commit }) {
      firebase.auth().signOut();
      commit("setUser", null);
      router.push("/");
    },
    post() {
      Vue.http
        .post(
          "https://innz-dev.firebaseio.com/posts.json",
          this.state.card
        )
        .then(data => {
          this.state.submitted = true;
        });
    },
    pay() {
      Vue.http
        .post(
          "https://innz-dev.firebaseio.com/payments.json",
          this.state.payment
        )
        .then(data => {
          this.state.submitted = true;
        });
    },
    chat(){
      Vue.http
        .post(
          "https://innz-dev.firebaseio.com/Chats.json",
          this.state.chat_message
        )
        .then(data => {
          this.state.submitted = true;
        });
    },
    getChats(context){
      context.commit("getChats");
    },
    getPosts(context) {
      context.commit("getPosts");
    },
    // filteredList(){
    //   var card = this.state.card;
    //   console.log(this.state.search)
    //   return this.state.cards.filter((card) => {
    //     return card.stateParish.match(this.state.search);
    //   })
    // }
  },
  getters: {
    isAuthenticated(state) {
      return state.user !== null && state.user !== undefined;
    }
  }
});
