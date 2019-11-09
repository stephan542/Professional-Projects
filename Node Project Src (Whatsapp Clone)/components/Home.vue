<template>
  <v-layout align-center justify-center row wrap>
    <!-- Filter Buttons -->
    <div v-for="buttonName in buttonNames" :key="buttonName.name" ma-5>
      <v-btn outline color="primary">{{buttonName.name}}</v-btn>
    </div>

    <!-- spacer -->
    <v-flex xs12 md12 lg12></v-flex>

    <!-- Card Template -->
    <v-flex v-for="card in this.$store.state.cards" :key="card.title" xs12 sm4 lg3 md3 class="pa-2">
      <v-card hover>
        <v-img class="whitetext" height="200px" src="/static/test.jpg">
          <v-layout column fill-height>
            <v-card-title>
              <v-btn icon>
                <v-icon large>favorite_border</v-icon>
              </v-btn>
            </v-card-title>
          </v-layout>
        </v-img>
        <router-link style="text-decoration: none" :to="'/cardview/' + card.id">
          <v-card-title primary-title>
            <div>
              <span class="grey--text">{{card.homeType}} • {{card.beds}} beds</span>
              <h3 class="headline mb-0 black--text">{{card.title}}</h3>
              <p class="black--text">{{card.price | currency}} per month</p>
            </div>
          </v-card-title>
          <v-card-actions>
            <v-icon>star_rate</v-icon>
          </v-card-actions>
        </router-link>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  data() {
    return {
      buttonNames: [
        { name: "Home Type" },
        { name: "Price" },
        { name: "Location" },
        { name: "More Filters" }
      ]
    };
  },
  created() {
    this.$store.dispatch("getPosts");
  },
  filters: {
    currency: function(value) {
      var formatter = new Intl.NumberFormat("en-JA", {
        style: "currency",
        currency: "JMD",
        minimumFractionDigits: 0
      });
      return formatter.format(value);
    }
  },
};
</script>
