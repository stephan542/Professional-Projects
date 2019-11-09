<template>
  <v-layout row wrap>
    <!-- Filter Buttons -->
    <div v-for="buttonName in buttonNames" :key="buttonName.name" ma-5>
      <v-btn outline color="primary">{{buttonName.name}}</v-btn>
    </div>
    <v-text-field placeholder="Search..." v-model="search" append-icon="search"></v-text-field>
     <!-- <VueFuse
          placeholder="Search Books of the Bible"
          event-name="results"
          :list="this.$store.state.cards"
          :keys="['country']"
          defaultAll
        
        /> -->

    <v-btn @click="runSearch">click me</v-btn>
    <!-- spacer -->
    <v-flex xs12 md12 lg12></v-flex>

    <!-- Card Template -->
    <v-flex v-for="card in results" :key="card.title" xs12 sm4 lg3 md3 class="ma-3">
      <router-link style="text-decoration: none" :to="'/cardview/' + card.id">
        <v-card hover>
          <v-img class="whitetext" height="200px" src="/static/test.jpg">
            <v-container fill-height fluid class="pa-1">
              <v-layout fill-height wrap>
                <v-flex xs12 align-content-start flexbox>
                  <v-card-actions>
                    <v-icon large>add_circle</v-icon>
                  </v-card-actions>
                </v-flex>
              </v-layout>
            </v-container>
          </v-img>
          <v-card-title primary-title>
            <div>
              <span class="grey--text">{{card.homeType}} • {{card.beds}} beds</span>
              <h3 class="headline mb-0">{{card.title}}</h3>
              <div>{{card.price}} per month</div>
            </div>
          </v-card-title>
          <v-card-actions>
            <v-icon>star_rate</v-icon>
          </v-card-actions>
        </v-card>
      </router-link>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  data() {
    return {
      buttonNames: [
        { name: "Dates" },
        { name: "Home Type" },
        { name: "Price" },
        { name: "Location" },
        { name: "More Filters" }
      ],
      results: [],
      search: ""
    };
  },
  created() {
    this.$store.dispatch("getPosts");

    this.$on("results", results => {
      this.results = results;
    });
  },
  methods: {
    runSearch() {
      this.$search(
        this.search,
        this.$store.state.cards,
        { keys: ["country", "stateParish"], minMatchCharLength: 2 },
      ).then(result => {
        this.results = result;
      });
    }
  }
};
</script>
