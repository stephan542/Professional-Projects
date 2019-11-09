<template>
  <v-layout row wrap class="secondary">
    <v-bottom-sheet v-model="sheet">
      <v-btn color="pink" slot="activator" dark fixed bottom right fab>
        <v-icon>import_contacts</v-icon>
      </v-btn>
      <v-list>
        <v-layout align-center justify-center row fill-height>
          <v-card flat>
            <v-card-title>
              <div class="center">
                <p class="ma-0 font-weight-black headline">{{card.price | currency}}</p>
                <p class="caption">per month</p>
              </div>
            </v-card-title>
            <hr class="mx-4">
            <!-- Dates -->
            <v-card-title>
              <p class="font-weight-bold grey--text">Dates</p>
            </v-card-title>
            <v-card-actions>
              <v-menu
                ref="menu"
                :close-on-content-click="false"
                v-model="menu"
                :nudge-right="40"
                :return-value.sync="date"
                lazy
                transition="scale-transition"
                offset-y
                full-width
                max-width="290px"
                min-width="290px">
                <v-text-field
                  slot="activator"
                  v-model="date"
                  label="Picker in menu"
                  prepend-icon="event"
                  readonly
                ></v-text-field>
                <v-date-picker v-model="date" type="month" no-title scrollable>
                  <v-spacer></v-spacer>
                  <v-btn flat color="primary" @click="menu = false">Cancel</v-btn>
                  <v-btn flat color="primary" @click="$refs.menu.save(date)">OK</v-btn>
                </v-date-picker>
              </v-menu>

              <v-spacer></v-spacer>

              <v-menu
                ref="menu2"
                :close-on-content-click="false"
                v-model="menu2"
                :nudge-right="40"
                :return-value.sync="date2"
                lazy
                transition="scale-transition"
                offset-y
                full-width
                max-width="290px"
                min-width="290px">
                <v-text-field
                  slot="activator"
                  v-model="date2"
                  label="Picker in menu"
                  prepend-icon="event"
                  readonly
                ></v-text-field>
                <v-date-picker v-model="date2" type="month" no-title scrollable>
                  <v-spacer></v-spacer>
                  <v-btn flat color="primary" @click="menu2 = false">Cancel</v-btn>
                  <v-btn flat color="primary" @click="$refs.menu2.save(date2)">OK</v-btn>
                </v-date-picker>
              </v-menu>
            </v-card-actions>
            <hr class="mx-4">
            <v-card-title>
              <p class="font-weight-bold grey--text">Occupants</p>
            </v-card-title>
            <v-card-actions>
              <v-select label="How Many?" v-model.lazy="card.homeType" :items="info"></v-select>
            </v-card-actions>
            <v-btn
              @click="calDate()"
              v-on:click="hide_show = !hide_show"
              v-show="hide_show"
              class="center"
              color="primary"
            >Next</v-btn>
            <div v-show="!hide_show">
              <v-card-actions>
                <p>{{card.price}} x {{calDateNum}}</p>
                <v-spacer></v-spacer>
                <p>{{card.price * calDateNum}}</p>
              </v-card-actions>
              <hr>  
              <v-card-actions>
                <p>Service fee</p>
                <p>10</p>
              </v-card-actions>
            </div>
            <v-btn @click="custRoute()" v-show="!hide_show" class="center" color="primary">Book</v-btn>
          </v-card>
        </v-layout>
      </v-list>
    </v-bottom-sheet>

    <!-- Slideshow/Carousel -->
    <v-flex class="lg6 md6 hidden-sm-and-down">
      <div class="boxy">
        <v-container>
          <v-card>
            <!-- Carousel Start -->
            <carousel :perPage="1" navigationEnabled>
              <slide>
                <v-img src="/static/edit.jpg" height="80vh"></v-img>
              </slide>
              <slide>
                <v-img src="/static/edit.jpg" height="80vh"></v-img>
              </slide>
            </carousel>
            <!-- Carousel End -->
          </v-card>
        </v-container>
      </div>
    </v-flex>
    <!-- Desktop View-->
    <v-flex class="lg6 md6 hidden-sm-and-down">
      <v-container>
        <!-- Title -->
        <p class="title pt-5">{{card.type}}</p>
        <v-layout row wrap justify-center>
          <v-flex>
            <p class="display-2 font-weight-bold">{{card.title}}</p>
            <p class="title font-weight-medium grey--text">{{card.stateParish}}</p>
            <p class="title font-weight-medium">{{card.price | currency}}</p>
          </v-flex>
          <v-flex>
            <v-avatar slot="activator" size="60px" class="center">
              <img
                src="https://images.unsplash.com/photo-1533973427779-4b8c2eb4c3cd?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=e1abef187f1165f83a418d2e8dda88f4&auto=format&fit=crop&w=1050&q=80"
                alt="Avatar"
              >
            </v-avatar>
            <!-- Insert {{card.name}} -->
            <p class="text-xs-center">Bevelerly</p>
          </v-flex>
        </v-layout>

        <!-- Home Info -->
        <v-layout row wrap class="pt-5">
          <v-flex>
            <v-icon class="center-icon" large>home</v-icon>
            <p class="text-xs-center">{{card.homeType}}</p>
          </v-flex>
          <v-flex>
            <v-icon class="center-icon" large>hotel</v-icon>
            <p class="text-xs-center">Bedrooms</p>
            <p class="text-xs-center">{{card.bedroom}}</p>
          </v-flex>
          <v-flex>
            <v-icon class="center-icon" large>people</v-icon>
            <p class="text-xs-center">Sleeps</p>
            <p class="text-xs-center">{{card.beds}}</p>
          </v-flex>
          <v-flex>
            <v-icon class="center-icon" large>hot_tub</v-icon>
            <p class="text-xs-center">Baths</p>
            <p class="text-xs-center">{{card.baths}}</p>
          </v-flex>
          <!-- <v-flex>
            <v-icon class="center-icon" large>brightness_3</v-icon>
            <p class="text-xs-center">Min Nights</p>
          </v-flex>-->
        </v-layout>

        <!-- Description -->
        <p class="py-4 subheading font-weight-light">{{card.description}}</p>

        <hr>

        <!-- Amenities -->
        <p class="headline font-weight-bold pt-4">Amenties</p>
        <v-layout align-center justify-space-between row fill-height wrap>
          <v-flex xs12>
            <!-- Basics -->
            <p class="font-weight-medium pt-1">Basics</p>
          </v-flex>
          <v-flex v-for="(item, index) in this.card.basics" :key="index">
            <v-card flat width="120">
              <v-card-title class="subheading font-weight-light">{{item}}</v-card-title>
            </v-card>
          </v-flex>
          <v-flex xs12>
            <!-- Safety -->
            <p class="font-weight-medium pt-1">Safety</p>
          </v-flex>
          <v-flex v-for="(item, index) in this.card.safety" :key="index">
            <v-card flat width="120">
              <v-card-title class="subheading font-weight-light">{{item}}</v-card-title>
            </v-card>
          </v-flex>
        </v-layout>
        <hr>

        <!-- Accessability -->
        <p class="headline font-weight-medium pt-4">Accessability</p>

        <v-layout row>
          <v-flex v-for="(item, index) in this.card.accesability" :key="index">
            <v-card flat>
              <v-card-title class="subheading font-weight-light">{{item}}</v-card-title>
            </v-card>
          </v-flex>
        </v-layout>

        <hr>

        <!-- Availability -->
        <p class="headline font-weight-medium pa-4">Availability</p>
        <v-layout row wrap>
          <v-flex v-for="(item, index) in this.card.selectedDate" :key="index">
            <v-card flat width="150">
              <v-card-title class="subheading font-weight-light">{{item}}</v-card-title>
            </v-card>
          </v-flex>
        </v-layout>
        <hr>
        <!-- House Rules -->
        <p class="headline font-weight-medium pa-4">House Rules</p>
        <v-layout row wrap>
          <v-layout column>
            <v-flex v-for="choice in choices" :key="choice.view">
              <v-card flat width="150">
                <v-card-title class="subheading font-weight-light">{{choice.view}}</v-card-title>
              </v-card>
            </v-flex>
          </v-layout>
          <v-layout column>
            <v-flex>
              <v-card flat width="150">
                <v-card-title class="subheading font-weight-light">{{card.yesNo}}</v-card-title>
              </v-card>
            </v-flex>
          </v-layout>
        </v-layout>
        <hr>
        <!-- Reviews -->
        <p class="headline font-weight-medium ma-2">Reviews</p>

        <v-layout align-center justify-start row class="mt-5">
          <v-flex xs1 class="mr-3 mb-2">
            <v-avatar slot="activator" size="60px" class="center">
              <img
                src="https://images.unsplash.com/photo-1533973427779-4b8c2eb4c3cd?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=e1abef187f1165f83a418d2e8dda88f4&auto=format&fit=crop&w=1050&q=80"
                alt="Avatar"
              >
            </v-avatar>
          </v-flex>

          <v-flex>
            <p class="font-weight-black ma-0">Olivia</p>
            <p class>November 2018</p>
          </v-flex>
        </v-layout>

        <p>Arlene’s home was impeccable. It was clean, spacious and had all the amenities we would ever need. Alicia was also so warm and welcoming. 6 stars in my opinion . Don’t hesitate to book.</p>

        <!-- Review Response -->
        <v-layout align-center justify-start row class="ml-4">
          <v-flex xs1 class="mr-3 mb-2">
            <v-avatar slot="activator" size="60px" class="center">
              <img
                src="https://images.unsplash.com/photo-1533973427779-4b8c2eb4c3cd?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=e1abef187f1165f83a418d2e8dda88f4&auto=format&fit=crop&w=1050&q=80"
                alt="Avatar"
              >
            </v-avatar>
          </v-flex>

          <v-flex>
            <p class="font-weight-black ma-0">Catherine</p>
            <p class="ma-0">November 2018</p>
          </v-flex>
        </v-layout>

        <p class="ml-4">Thank you, Olivia. Looking forward to hosting you and yours soon.</p>

        <hr>
        <!-- Location -->
        <p class="headline font-weight-medium ma-2">Location</p>
        <gmap-autocomplete @place_changed="setPlace"></gmap-autocomplete>
        <gmap-map :center="center" :zoom="12" style="width:100%;  height: 400px;"></gmap-map>
      </v-container>

      <!-- Information Ends -->
    </v-flex>
    <!-- Desktop View End -->
    <!-- MOBILE VIEW START -->
    <v-flex class="xs12 hidden-md-and-up">
      <v-flex class="xs12">
        <!-- Carousel Start -->
        <carousel perPage="1">
          <slide>
            <v-img src="/static/edit.jpg" height="50vh"></v-img>
          </slide>
          <slide>
            <v-img src="/static/edit.jpg" height="50vh"></v-img>
          </slide>
        </carousel>
        <!-- Carousel End -->
      </v-flex>
      <!-- Information -->
      <v-flex class="xs12">
        <v-container>
          <v-layout row wrap justify-center>
            <v-flex xs8>
              <p class="display-1 font-weight-bold">{{card.title}}</p>
              <p class="title font-weight-medium grey--text">{{card.stateParish}}</p>
              <p class="title font-weight-medium">{{card.price}}</p>
            </v-flex>
            <v-flex xs4>
              <v-avatar slot="activator" size="60px" class="center">
                <img
                  src="https://images.unsplash.com/photo-1533973427779-4b8c2eb4c3cd?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=e1abef187f1165f83a418d2e8dda88f4&auto=format&fit=crop&w=1050&q=80"
                  alt="Avatar"
                >
              </v-avatar>
              <p class="text-xs-center">Bevelerly</p>
            </v-flex>
          </v-layout>
          <!-- Home Info -->
          <v-layout row wrap class="pt-5">
            <v-flex>
              <v-icon class="center-icon" large>home</v-icon>
              <p class="text-xs-center">{{card.propertyType}}</p>
            </v-flex>
            <v-flex>
              <v-icon class="center-icon" large>hotel</v-icon>
              <p class="text-xs-center">Bedrooms</p>
              <p class="text-xs-center">{{card.beds}}</p>
            </v-flex>
            <v-flex>
              <v-icon class="center-icon" large>people</v-icon>
              <p class="text-xs-center">Sleeps</p>
              <p class="text-xs-center">{{card.guestAccomodation}}</p>
            </v-flex>
            <v-flex>
              <v-icon class="center-icon" large>hot_tub</v-icon>
              <p class="text-xs-center">Baths</p>
              <p class="text-xs-center">{{card.baths}}</p>
            </v-flex>
          </v-layout>
          <p>{{card.description}}</p>

          <hr>

          <!-- Amenities -->
          <p class="headline font-weight-bold pt-4">Amenties</p>
          <v-layout align-center justify-space-between row fill-height wrap>
            <v-flex xs12>
              <!-- Basics -->
              <p class="font-weight-medium pt-1">Basics</p>
            </v-flex>
            <v-flex v-for="(item, index) in this.card.basics" :key="index">
              <v-card flat width="120">
                <v-card-title class="subheading font-weight-light">{{item}}</v-card-title>
              </v-card>
            </v-flex>
            <v-flex xs12>
              <!-- Safety -->
              <p class="font-weight-medium pt-1">Safety</p>
            </v-flex>
            <v-flex v-for="(item, index) in this.card.safety" :key="index">
              <v-card flat width="120">
                <v-card-title class="subheading font-weight-light">{{item}}</v-card-title>
              </v-card>
            </v-flex>
          </v-layout>
          <hr>

          <!-- Accesability -->
          <p class="headline font-weight-medium pt-4">Accessability</p>

          <v-layout row>
            <v-flex v-for="(item, index) in this.card.accesability" :key="index">
              <v-card flat>
                <v-card-title class="subheading font-weight-light">{{item}}</v-card-title>
              </v-card>
            </v-flex>
          </v-layout>

          <hr>

          <!-- Availability -->
          <p class="headline font-weight-medium pa-4">Availability</p>
          <v-layout row wrap>
            <v-flex v-for="(item, index) in this.card.selectedDate" :key="index">
              <v-card flat width="150">
                <v-card-title class="subheading font-weight-light">{{item}}</v-card-title>
              </v-card>
            </v-flex>
          </v-layout>
          <hr>

          <!-- House Rules -->
          <p class="headline font-weight-medium pa-4">House Rules</p>
          <v-layout row wrap>
            <v-layout column>
              <v-flex v-for="choice in choices" :key="choice.view">
                <v-card flat width="150">
                  <v-card-title class="subheading font-weight-light">{{choice.view}}</v-card-title>
                </v-card>
              </v-flex>
            </v-layout>
            <v-layout column>
              <v-flex>
                <v-card flat width="150">
                  <v-card-title class="subheading font-weight-light">{{card.yesNo}}</v-card-title>
                </v-card>
              </v-flex>
            </v-layout>
          </v-layout>
          <hr>
          <!-- Reviews -->
          <p class="headline font-weight-medium ma-2">Reviews</p>

          <v-layout align-center justify-start row class="mt-5">
            <v-flex xs1 class="mr-5 mb-2">
              <v-avatar slot="activator" size="60px" class="center">
                <img
                  src="https://images.unsplash.com/photo-1533973427779-4b8c2eb4c3cd?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=e1abef187f1165f83a418d2e8dda88f4&auto=format&fit=crop&w=1050&q=80"
                  alt="Avatar"
                >
              </v-avatar>
            </v-flex>

            <v-flex>
              <p class="font-weight-black ma-0">Olivia</p>
              <p class>November 2018</p>
            </v-flex>
          </v-layout>

          <p>Arlene’s home was impeccable. It was clean, spacious and had all the amenities we would ever need. Alicia was also so warm and welcoming. 6 stars in my opinion . Don’t hesitate to book.</p>

          <!-- Review Response -->
          <v-layout align-center justify-start row class="ml-4">
            <v-flex xs1 class="mr-5 mb-2">
              <v-avatar slot="activator" size="60px" class="center">
                <img
                  src="https://images.unsplash.com/photo-1533973427779-4b8c2eb4c3cd?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=e1abef187f1165f83a418d2e8dda88f4&auto=format&fit=crop&w=1050&q=80"
                  alt="Avatar"
                >
              </v-avatar>
            </v-flex>

            <v-flex>
              <p class="font-weight-black ma-0">Catherine</p>
              <p class="ma-0">November 2018</p>
            </v-flex>
          </v-layout>

          <p class="ml-4">Thank you, Olivia. Looking forward to hosting you and yours soon.</p>

          <!-- Location -->
          <p class="headline font-weight-medium ma-2">Location</p>
          <gmap-autocomplete @place_changed="setPlace"></gmap-autocomplete>
          <gmap-map :center="center" :zoom="12" style="width:100%;  height: 400px;"></gmap-map>
        </v-container>
        <!-- Information Ends -->
      </v-flex>
    </v-flex>
    <!-- Mobile View End -->
  </v-layout>
</template>

<script>
import moment from "moment";
import router from "../router";
export default {
  data() {
    return {
      card: {},
      info: ["1", "2", "3", "4", "5"],
      // Bottom Sheets
      sheet: false,
      // Maps
      id: this.$route.params.id,
      center: { lat: 18.0179, lng: 76.8099 },
      names: [{ title: "title", name: "Google" }],
      // date
      menu: false,
      menu2: false,
      modal: false,
      date: new Date().toISOString().substr(0, 7),
      date2: new Date().toISOString().substr(0, 7),
      // House Rules
      choices: [{ view: "Smoking Allowed" }],
      // Hide/Show
      hide_show: true,
      calDateNum: 0
    };
  },
  // Gets Data and Creates Cards
  created() {
    this.$http
      .get(
        "https://campuscomforts-e77c1.firebaseio.com/posts/" + this.id + ".json"
      )
      .then(function(data) {
        return data.json();
      })
      .then(function(data) {
        this.card = data;
      });
  },
  mounted() {
    this.geolocate();
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
  computed: {
    selected() {
      return this.card.selected;
    }
  },
  methods: {
    // receives a place object via the autocomplete component
    setPlace(place) {
      this.currentPlace = place;
    },
    // sets cordinates
    geolocate: function() {
      navigator.geolocation.getCurrentPosition(position => {
        this.center = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        };
      });
    },
    calDate() {
      var a = moment(this.date2); //now
      var b = moment(this.date);

      console.log(a.diff(b, "days"));
      console.log(a.diff(b, "weeks"));
      console.log(a.diff(b, "months"));

      this.calDateNum = a.diff(b, "months");
    },
    custRoute() {
      router.push("/verifyID");
    }
  }
};
</script>

<style scoped>
.center {
  margin: 0 auto;
  display: block;
}
.center-icon {
  display: flex;
  margin: 0 auto;
}
.boxy {
  position: fixed;
  width: 50%;
}
</style>

