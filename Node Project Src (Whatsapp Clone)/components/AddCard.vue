<template>
 
    <v-layout row wrap>
      <!-- Confimation -->
      <v-snackbar v-model="this.$store.state.submitted" :timeout="1200" bottom>
        <p>Successful</p>
      </v-snackbar>

      <v-container>
        <v-stepper v-model="step">
          <v-stepper-header>
            <v-stepper-step :complete="step > 1" step="1">Basics</v-stepper-step>

            <v-divider></v-divider>

            <v-stepper-step :complete="step > 2" step="2">Location</v-stepper-step>

            <v-divider></v-divider>

            <v-stepper-step :complete="step > 3" step="3">Amenities</v-stepper-step>

            <v-divider></v-divider>

            <v-stepper-step :complete="step > 4" step="4">House Rules</v-stepper-step>

            <v-divider></v-divider>

            <v-stepper-step :complete="step > 5" step="5">Pricing and Availability</v-stepper-step>
          </v-stepper-header>
          <!-- BASICS -->
          <v-stepper-items>
            <v-stepper-content step="1">
              <v-text-field label="Give your home a name." v-model.lazy="card.title"></v-text-field>

              <v-text-field
                label="Give a description of your home."
                v-model.lazy="card.description"
                :rules="['Required']"
              ></v-text-field>

              <v-select
                label="What type of home is it?"
                v-model.lazy="card.homeType"
                :items="info[3].items"
              ></v-select>

              <v-select
                label="Is this single or shared?"
                v-model.lazy="card.singleShared"
                :items="info[0].items"
              ></v-select>

              <v-select
                label="How many Bedrooms?"
                v-model.lazy="card.bedroom"
                :items="info[1].items"
              ></v-select>

              <v-select label="How many Beds?" v-model.lazy="card.beds" :items="info[1].items"></v-select>

              <v-select label="How many Baths?" v-model.lazy="card.baths" :items="info[1].items"></v-select>

              <v-btn @click="step = 2" :class="btnColor">Next</v-btn>
            </v-stepper-content>

            <!-- LOCATION-->
            <v-stepper-content step="2">
              <v-text-field label="What is the home address?" v-model.lazy="card.address"></v-text-field>

              <v-select
                label="What state/parish is the home located?"
                v-model.lazy="card.stateParish"
                :items="info[5].items"
              ></v-select>

              <v-select
                label="Which Country is the home located?"
                v-model.lazy="card.country"
                :items="info[6].items"
              ></v-select>

              <v-btn @click="step = 1" :class="btnColor">Previous</v-btn>

              <v-btn @click="step = 3" :class="btnColor">Next</v-btn>
            </v-stepper-content>
            <!-- AMENITIES -->
            <v-stepper-content step="3">
              <v-layout row>
                <v-flex xs4>
                  <!-- Basics -->
                  <p class="title">Basics</p>
                  <v-checkbox
                    v-model.lazy="card.basics"
                    :color="btnColor"
                    label="Essentials"
                    value="Essentials"
                    hint="Towels, bed sheets, soap, toilet paper, and pillows"
                    persistent-hint
                  ></v-checkbox>

                  <v-checkbox v-model="card.basics" color="primary" label="Wifi" value="Wifi"></v-checkbox>

                  <v-checkbox
                    v-model.lazy="card.basics"
                    :color="btnColor"
                    label="Closet/drawers"
                    value="Closet/drawers"
                  ></v-checkbox>

                  <v-checkbox v-model="basics" :color="btnColor" label="TV" value="TV"></v-checkbox>

                  <v-checkbox
                    v-model.lazy="card.basics"
                    :color="btnColor"
                    label="Air Conditioning"
                    value="Air Conditioning"
                  ></v-checkbox>

                  <v-checkbox
                    v-model.lazy="card.basics"
                    :color="btnColor"
                    label="Desk/workspace"
                    value="Desk/workspace"
                  ></v-checkbox>

                  <v-checkbox
                    v-model.lazy="card.basics"
                    :color="btnColor"
                    label="Private entrance"
                    value="Private entrance"
                  ></v-checkbox>

                  <v-btn @click="step = 2" :class="btnColor">Previous</v-btn>
                  <v-btn @click="step = 4" :class="btnColor">Next</v-btn>
                </v-flex>

                <v-flex xs4>
                  <p class="title">Safety amenities</p>

                  <v-checkbox
                    v-model.lazy="card.safety"
                    :color="btnColor"
                    label="Smoke detector"
                    value="Smoke detector"
                    hint="Detects for smoke and fire inside a house/room"
                    persistent-hint
                  ></v-checkbox>

                  <v-checkbox
                    v-model.lazy="card.safety"
                    :color="btnColor"
                    label="Carbon monoxide detector"
                    value="Carbon monoxide detector"
                  ></v-checkbox>

                  <v-checkbox
                    v-model.lazy="card.safety"
                    :color="btnColor"
                    label="First aid kit"
                    value="First aid kit"
                  ></v-checkbox>

                  <v-checkbox
                    v-model.lazy="card.safety"
                    :color="btnColor"
                    label="Fire extinguisher"
                    value="Fire extinguisher"
                  ></v-checkbox>

                  <v-checkbox
                    v-model.lazy="card.safety"
                    :color="btnColor"
                    label="Lock on bedroom door"
                    value="Lock on bedroom door"
                    hint="Private room can be locked for safety and privacy"
                    persistent-hint
                  ></v-checkbox>
                </v-flex>
                <v-flex xs4>
                  <p class="title">Accesability</p>
                  <v-checkbox
                    v-model.lazy="card.accesability"
                    :color="btnColor"
                    label="Wheelchair access"
                    value="Wheelchair access"
                  ></v-checkbox>
                </v-flex>
              </v-layout>
            </v-stepper-content>
            <!-- HOUSE RULES -->
            <v-stepper-content step="4">
              <v-layout row wrap>
                <v-flex xs3>
                  <p class="title pt-4 font-weight-bold">Is smoking allowed?</p>
                  <p class="title pt-4 font-weight-bold">Is there noise on the property??</p>
                  <p class="title pt-4 font-weight-bold">Is events or parities allowed??</p>
                </v-flex>
                <v-flex>
                  <v-switch
                    color="primary"
                    :label="`Switch : ${card.yesNo.toString()}`"
                    v-model="card.yesNo"
                  ></v-switch>

                  <v-switch
                    color="primary"
                    :label="`Switch : ${card.yesNo_1.toString()}`"
                    v-model="card.yesNo_1"
                  ></v-switch>
                  <v-switch
                    color="primary"
                    :label="`Switch : ${card.yesNo_2.toString()}`"
                    v-model="card.yesNo_2"
                  ></v-switch>
                </v-flex>
              </v-layout>
              <v-text-field label="Additional rules" v-model.lazy="card.rules"></v-text-field>

              <v-btn @click="step = 3" :class="btnColor">Previous</v-btn>
              <v-btn @click="step = 5" :class="btnColor">Next</v-btn>
            </v-stepper-content>
            <!-- Pricing and Availability -->
            <v-stepper-content step="5">
              <v-layout row wrap>
                <v-flex xs12>
                  <v-text-field
                    label="Price"
                    hint="This is per-month basis"
                    v-model.lazy="card.price"
                    type="number"
                    
                  ></v-text-field>
                </v-flex>
                <v-flex>
                  <p>How long can a student stay for?</p>
                  <p class="caption">You can select multiple choices</p>
                  <v-checkbox
                    v-model.lazy="card.selectedDate"
                    :color="btnColor"
                    label="3 Months"
                    value="3 Months"
                  ></v-checkbox>
                  <v-checkbox
                    v-model.lazy="card.selectedDate"
                    :color="btnColor"
                    label="6 Months"
                    value="6 Months"
                  ></v-checkbox>
                  <v-checkbox
                    v-model.lazy="card.selectedDate"
                    :color="btnColor"
                    label="9 Months"
                    value="9 Months"
                  ></v-checkbox>
                  <v-checkbox
                    v-model.lazy="card.selectedDate"
                    :color="btnColor"
                    label="12 Months"
                    value="12 Months"
                  ></v-checkbox>
                </v-flex>
              </v-layout>

              <!-- Submit Button -->
              <v-btn @click="step = 4" :class="btnColor">Previous</v-btn>
              <v-btn v-on:click.prevent="post" :class="btnColor">Finish</v-btn>
            </v-stepper-content>
          </v-stepper-items>
        </v-stepper>
        <!-- Submit Button -->
        <!-- <v-btn v-on:click.prevent="post" :class="btnColor">Finish</v-btn> -->
        <!-- <input type='file' accept='image/*' @change='onFilePicked'>
        <img :src='imageUrl' height='150'>-->
      </v-container>
    </v-layout>
</template>

<script>
import firebase from "firebase";

export default {
  data() {
    return {
      btnColor: "primary",
      step: 0,
      yesNo: true,
      info: [
        /*0*/ { items: ["Single", "Shared"] },
        /*1*/ { items: ["1", "2", "3", "4", "5"] },
        /*2*/ { items: ["Essentials"] },
        /*3*/ { items: ["Apartment", "House", "Attached Unit", "Flat"] },
        /*4*/ {
          items: ["Apartment", "Condonium", "Loft", "Serviced Apartment"]
        },
        {
          /*5*/ items: [
            "Kingston",
            "St. Andrew",
            "Portland",
            "St. Thomas",
            "St. Catherine",
            "St. Mary",
            " St. Ann",
            "Manchester",
            "Clarendon",
            "Hanover",
            "Westmoreland",
            "St. James",
            "Trelawny",
            "St. Elizabeth"
          ]
        },
        {
          /*6*/ items: [
            "Anguilla",
            "Antigua and Barbuda",
            "Aruba",
            "Bahamas",
            "Barbados",
            "British Virgin Islands",
            "Cayman Islands",
            "Cuba",
            "Dominica",
            "Dominican Republic",
            "Grenada",
            "Guadeloupe",
            "Haiti",
            "Jamaica",
            "Martinique",
            "Montserrat",
            "Netherlands Antilles",
            "Puerto Rico",
            "Saint Kitts & Nevis",
            "Saint Lucia",
            "Saint Martin",
            "Saint Vincent",
            "Trinidad & Tobago",
            "Turks & Caicos Islands",
            "US Virgin Islands"
          ]
        }
      ]
    };
  },
  computed: {
    card() {
      return this.$store.state.card;
    }
  },

  methods: {
    //Posting to Firebase
    post() {
      this.$store.dispatch("post");
    }

    //Uploading Images to Firebase
    // onFilePicked(event) {
    //   const files = event.target.files;

    //   let filename = files[0].name;

    //   console.log(filename);

    //   if (filename.lastIndexOf(".") <= 0) {
    //     return alert("Please add a valid file!");
    //   }

    //   const fileReader = new FileReader();

    //   fileReader.addEventListener("load", () => {
    //     this.imageUrl = fileReader.result;
    //   });

    //   fileReader.readAsDataURL(files[0]);

    //   this.image = files[0];

    //   var storageRef = firebase.storage().ref();

    //   var imagesRef = storageRef.child("images");

    //   storageRef.child("images/" + filename.name).put(files[0]);
    // }
  },
 
};
</script>
