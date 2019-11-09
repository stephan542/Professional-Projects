<template>
  <!-- Carousel -->
  <v-layout row wrap>
    <v-flex class="xs12 hidden-sm-and-down">
      <carousel perPage="1" paginationActiveColor="#ED1344" navigationEnabled>
        <slide>
          <img src="@/assets/Slide-1.jpg" alt height="100%" width="100%">
        </slide>
        <slide>
          <img src="@/assets/Slide-1.jpg" alt height="100%" width="100%">
        </slide>
      </carousel>
    </v-flex>

    <!-- <v-flex xs12>
         <v-text-field 
          label="Search"
          type="text"
          v-model="search"
        >
        </v-text-field>
    </v-flex>-->
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
              <p class="black--text">{{card.price}} per month</p>
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
      search: ""
    };
  },
  created() {
    this.$store.dispatch("getPosts");
  }
};
</script>
