<template>
  <v-app>
    <!-- Navigation Bar -->
    <v-toolbar app fixed light dense class="secondary">
      <!-- Mobile View Start -->
      <v-layout align-center justify-space-between row fill-height class="hidden-md-and-up">
        <v-flex v-show="appBar">
          <v-btn icon @click.stop="rightDrawer = !rightDrawer">
            <v-icon>menu</v-icon>
          </v-btn>
        </v-flex>

        <v-flex v-show="appBar" class="mx-5">
          <router-link to="/home" tag="span" style="cursor: pointer">
            <v-btn class="primary--text headline font-weight-bold" flat>INNZ</v-btn>
          </router-link>
        </v-flex>

        <v-flex v-show="!appBar">
          <v-text-field
            placeholder="Search..."
            v-model="search"
            append-icon="search"
            @click:append="display"
          ></v-text-field>
        </v-flex>

        <v-flex v-show="!appBar">
          <v-btn icon v-on:click="appBar = true">
            <v-icon>clear</v-icon>
          </v-btn>
        </v-flex>

        <v-flex v-show="appBar">
          <v-btn icon v-on:click="appBar = !appBar">
            <v-icon>search</v-icon>
          </v-btn>
        </v-flex>

      </v-layout>

      <!-- Mobile View End -->
      <!-- Destop View Start -->
      <v-toolbar-title class="hidden-sm-and-down">
        <router-link to="/home" tag="span" style="cursor: pointer">
          <h1 class="primary--text headline pl-1 font-weight-bold">INNZ</h1>
        </router-link>
      </v-toolbar-title>

      <!-- Search bar -->
      <v-text-field
        class="pl-3 mt-2 hidden-sm-and-down"
        placeholder="Search..."
        v-model="search"
        append-icon="search"
        @click:append="display"
      ></v-text-field>
      <v-spacer></v-spacer>

      <v-btn
        class="hidden-sm-and-down primary--text"
        flat
        v-for="item in menuItems"
        :key="item.title"
        :to="item.path"
      >{{item.title}}</v-btn>

      <!-- Signout Button -->
      <v-btn
        class="hidden-sm-and-down primary--text"
        flat
        @click="userSignOut"
        v-for="item in specialItem"
        :key="item.title"
      >Sign Out</v-btn>
    </v-toolbar>

    <!-- Side Navigation Start-->
    <v-navigation-drawer temporary v-model="rightDrawer" fixed app class="primary">
      <v-list class="primary" dark>
        <v-list-tile>
          <v-list-tile-title>
            <h1 class="title">INNZ</h1>
          </v-list-tile-title>
        </v-list-tile>

        <v-divider></v-divider>

        <v-list-tile v-for="item in menuItems" :key="item.title" :to="item.path">
          <v-list-tile-title>{{ item.title }}</v-list-tile-title>
        </v-list-tile>

        <v-list-tile v-for="special in specialItem" :key="special.title">
          <v-list-tile-title @click="userSignOut">{{ special.title }}</v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>

    <!-- Side Navigation End -->
    <!-- Content, DO NOT EDIT!!! -->
    <v-content>
      <router-view></router-view>
    </v-content>

    <!-- <v-footer :fixed="fixed" app>
      <span>&copy; 2017</span>
    </v-footer>-->
  </v-app>
</template>

<script>
import router from "./router";
export default {
  data() {
    return {
      clipped: true,
      drawer: true,
      fixed: true,
      miniVariant: false,
      left: true,
      rightDrawer: false,
      search: "",
      appBar: true
    };
  },
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    menuItems() {
      if (this.isAuthenticated) {
        return [
          { title: "Become a Host", path: "/addcard" },
          { title: "Saved", path: "/saved" },
          { title: "Messages", path: "/messages" },
          { title: "Support", path: "/support" }
        ];
      } else {
        return [
          { title: "Sign Up", path: "/signup" },
          { title: "Sign In", path: "/signin" },
          { title: "Support", path: "/support" }
        ];
      }
    },
    specialItem() {
      if (this.isAuthenticated) {
        return [{ title: "Sign Out" }];
      }
    }
  },
  methods: {
    display() {
      // sets search to user input
      this.$store.state.search = this.search;
      // filters and go to filtered result
      router.push("/search");
    },
    userSignOut() {
      this.$store.dispatch("userSignOut");
    }
  }
};
</script>

<style scoped>
.ml-6 {
  margin-left: 10%;
}
</style>

