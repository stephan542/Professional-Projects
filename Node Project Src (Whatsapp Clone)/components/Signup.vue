<template>
  <v-container fluid>
    <v-layout row wrap>
      <v-flex xs12 class="text-xs-center" mt-5>
        <h1>Sign Up</h1>
      </v-flex>
      <v-flex xs12 sm6 offset-sm3 mt-3>
        <form @submit.prevent="userSignUp">
          <v-layout column>
            <v-flex>
              <v-alert type="error" dismissible v-model="alert">
                {{ error }}
              </v-alert>
            </v-flex>
            <v-flex>
              <v-text-field
                name="email"
                label="Email"
                id="email"
                type="email"
                v-model="email"
                color="primary"
                required></v-text-field>
            </v-flex>
            <v-flex>
              <v-text-field
                name="password"
                label="Password"
                id="password"
                type="password"
                color="primary"
                v-model="password"
                required></v-text-field>
            </v-flex>
            <v-flex>
              <v-text-field
                name="confirmPassword"
                label="Confirm Password"
                id="confirmPassword"
                type="password"
                color="primary"
                v-model="passwordConfirm"
                :rules="[comparePasswords]"
                required
                ></v-text-field>
            </v-flex>
            <v-flex class="text-xs-center" mt-5>
              <v-btn color="primary" type="submit" :disabled="loading">Sign Up</v-btn>
            </v-flex>
            <v-flex class="text-xs-center" pt-3>
              <p>Already have an account, <router-link style="color: red"  to="/signin">Log in</router-link></p>
            </v-flex>
          </v-layout>
        </form>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      email: "",
      password: "",
      passwordConfirm: "",
      alert: false
    };
  },
  computed: {
    comparePasswords() {
      return this.password === this.passwordConfirm
        ? true
        : "Passwords don't match";
    },
    error() {
      return this.$store.state.error;
    },
    loading() {
      return this.$store.state.loading;
    }
  },
  methods: {
    userSignUp() {
      if (this.comparePasswords !== true) {
        return;
      }
      this.$store.dispatch("userSignUp", {
        email: this.email,
        password: this.password
      });
    }
  },
  watch: {
    error (value) {
      if (value) {
        this.alert = true
      }
    },
    alert (value) {
      if (!value) {
        this.$store.commit('setError', null)
      }
    }
  }
};
</script>