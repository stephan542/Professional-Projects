<template>
  <v-container>
    <v-layout>
      <v-flex>
        <p class="font-weight-black display-3 accent--text">We need to identify you</p>
        <p class="font-weight-bold display-1 accent--text">What kind of ID will you like to use</p>
        <v-radio-group v-model="radios">
          <v-radio label="Passport" value="radio-1"></v-radio>
          <v-radio label="Government ID" value="radio-2"></v-radio>
          <v-radio label="Driver's licence" value="radio-3"></v-radio>
        </v-radio-group>
         <p class="font-weight-bold title">Your ID will never be shared with anyone</p>
      <v-btn class="primary">Next</v-btn>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
export default {
  data() {
    radios: "radio-1";
  }
};
</script>
