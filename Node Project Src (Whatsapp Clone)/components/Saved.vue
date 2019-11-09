<template>
    <v-layout align-center justify-center fill-height row wrap>
        <v-flex class="font-weight-bold display-2" xs12>
            <p class="pl-5 pt-5 accent--text">Saved</p>
        </v-flex>
    <v-flex v-for="img in img" :key="img.src" xs12 sm4 lg3 md3 class="ma-3">
        <v-card hover>
          <v-img class="tint" height="200px" :src="img.src">
             <v-container fill-height fluid>
            <v-layout fill-height column>
              <v-flex xs12 class="pt-6">
                <span class="title secondary--text">Ocho Rios</span>
              </v-flex>
               <v-flex xs12 class="pa-0 ma-0">
                <span class="sub-heading secondary--text">5 homes</span>
              </v-flex>
            </v-layout>
          </v-container>
          </v-img>
        </v-card>
    </v-flex>
    </v-layout>
</template>

<script>
  export default {
    data() {
      return {
       img: [
            {src: '/static/Img-1.jpg'},
            {src: '/static/Img-2.jpg'},
            {src: '/static/Img-3.jpg'},
            {src: '/static/Img-4.jpg'},
            {src: '/static/Img-5.jpg'},
            {src: '/static/Img-6.jpg'}
       ]
      }
    }
  };
</script>

<style scoped>
.pt-6{
  padding-top: 40%;
}
.tint:before{
   background: rgba(0,255,255, 0.5);
}
</style>
