<template>
<!--Author:Stephan Witter -->
<!--Date : 1/2/2019 update-->
<!--Messengger UI-->
    <v-layout class="content_specs">
    <v-card light color="white" class="content_specs">
      <!--main container-->

        <!--Actve user name display-->
          <!--get the active friend for Veux-->
          <v-subheader class="text-uppercase placeright" permanent>
                  <v-icon class="mobile_back"
                  @click="mobile_view"
                  >arrow_back_ios</v-icon>
                  <br>
                 <h2>{{this.$store.state.activechat}}</h2>
            </v-subheader>
            <br>
        <v-divider  v-if="this.$store.state.activechat!=''"></v-divider>

        <!--main sub container-->
        <v-container permanent flat fluid class="scroll-y stylescroll subcon subcon_height" 
            v-bind:style="this.$store.state.activechat==''?'display:none':'display:block'">
          <v-layout column class="subcon_height">
          <br>

            <!--display each chat-->
            <v-flex permanent absolute flat fluid v-for="chat in getchat(this.$store.state.activechat)" 
                      :key="chat.Form+''+Math.random()" @click="getchat(chat.From)" >

                      <!--display today divider-->
                      <div v-if="iscurentd(chat)">
                          <br><h4 class="daybreaker"><span>Today</span></h4>
                      </div>

                    <!--display message and header depending on the date-->
                    <div class="text-xs-right" v-if="chat.From == user">
                        <!--places the chatt either on the right or the left -->
                        <!--below places and show the user messages-->
                        <v-subheader class="justify-end" v-if="getcdate(chat) != ''">
                          <!--prints the date of the user message above message-->
                          <h5 >{{getcdate(chat)}}</h5>
                        </v-subheader>
                        <!--format the message in a btton format-->
                        <v-btn light color="#D32F2F" class="custom-btn">                     
                          <pre class="custom-message" >{{displayMessage(chat.Message)}}</pre>
                        </v-btn>
                    </div>
                    <!--below places and show the friend messages-->
                    <div class="text-xs-left" v-else>
                        <v-subheader class="justify-start" v-if="getcdate(chat) != ''">
                          <!--prints the date of the friend's message above message-->
                          <h5>{{getcdate(chat)}}</h5>
                        </v-subheader>
                        <!--format the message in a btton format-->
                        <v-btn light color="accent" class="custom-btn">
                          <pre class="custom-message">{{displayMessage(chat.Message)}}</pre>
                        </v-btn>
                    </div>
            </v-flex>
          </v-layout>
        </v-container>
        <v-fab-transition>
              <v-btn v-show="!hidden" color="primary" class="smlword" dark absolute large right fab @click="gotolast()" style="gotolast" >
                  {{getnewmessage_count(newmessage_count)}}
              </v-btn>
        </v-fab-transition>
        <!--display message input and loading that the foot of the page-->
        <v-container permanent fixed flat fluid class="message_con">
            <!--display message input-->
            <v-footer permanent absolute color="primary" class="message_specs"
              v-if="this.$store.state.activechat!=''">
                    <!--formats the message box-->
                    <v-textarea solo class="getMessage" full-width
                    v-bind:placeholder="'Message '+this.$store.state.activechat.split(' ')[0]"
                    append-icon="send" v-model="new_message" 
                    @click:append="sendMessage()"
                    rows="2"
                    style="border:none"
                    clearable
                    >
                    </v-textarea>
            </v-footer>
        </v-container>

        <!--display navigation drawer to the left contain friends-->
        <v-layout>
            <!--use to place navigation drawer to the right-->
            <v-navigation-drawer v-model='drawer' permanent fixed color="secondary"  
              class="stylescroll2 drawer_specs" >
                <!--toolbar within the nag drawer-->
                <v-toolbar permanent fixed flat class="transparent" light>
                  <v-flex sm12 md12 xs12 xl12 lg12>
                  <v-text-field solo  class="caption convsearch" full-width v-model="converse"
                      placeholder="Find people and conversation" prepend-inner-icon="search"
                      @keyup.delete="getsearch(false)" @keyup.enter="getsearch(false)"
                      @click:prepend-inner="getsearch(false)" clearable @click:clear="getsearch(true)">
                  </v-text-field>
                  </v-flex>
                </v-toolbar>

                <!--default to hold data in place-->
                <v-toolbar flat></v-toolbar>

                <!--used to displayed person chat in the nag drawer-->
                <v-container fluid>
                  <v-list-tile class="custom-hover" ripple v-for="person in getchatnames()" :key="person"
                   @click="setactivechat(person)">
                      <v-list-tile-action>
                        <!--displays an avatar for the firend-->
                            <v-avatar color="primary" size=32>
                                <v-icon dark >account_circle</v-icon>  
                            </v-avatar>
                      </v-list-tile-action>
                      <v-list-tile-content>
                        <!--display the friend name-->
                        <v-list-tile-title class="subheading">
                          {{person}}
                        </v-list-tile-title>
                        <!--display the last message in the chat between user and friend-->
                        <v-list-tile-title class="caption">
                          {{lastmessage(person).Message}}
                          <span style="float:right">{{getdtime(lastmessage(person).Date)}}</span>
                        </v-list-tile-title>
                      </v-list-tile-content>
                  </v-list-tile>
                
                </v-container>
            </v-navigation-drawer>
        </v-layout>
    </v-card>
    </v-layout>
</template>

<script>
import Vue from 'vue';
import Rx from 'rx-lite'

let observer = Rx.Observable.interval(1000);

//These values are use to format data within the code,not to be displayed
let temp=0;
let previousTime='';
let recp='';
//month shorten
let month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"];
let moment = require('moment');
let audio  = new Audio('http://soundbible.com/mp3/A-Tone-His_Self-1266414414.mp3');


window.onresize = function(){
  if(window.innerWidth>768){
      document.querySelectorAll(".drawer_specs")[0].style.left = "0"; 
      document.querySelectorAll(".drawer_specs")[0].style.visibility = "visible"; 
  }
};



export default {
  name: 'ChatHomepage',
  data(){
    return{
      converse:'',
      new_message:'',
      drawer:null,
      extrasearch:false,
      user:this.$store.state.currentuser.Name,
      hidden:true,
      newmessage_count:0
    }
  },
  mounted(){
    let msgBar = document.getElementsByClassName("subcon")[0];
    
    msgBar.addEventListener("scroll",function(){
      if( msgBar.scrollTop >= msgBar.scrollHeight-400){
        gotolast();
        alert(this.hidden);
      }
    });
  },
  created(){
    this.$store.state.pinging = observer.subscribe(int => this.$store.dispatch("getChats")); 
  },
  destroyed(){
    this.$store.state.pinging.dispose();
    msgBar.removeEventListener("scroll",this.handleScroll);
  },
  methods:{
  gotolast(){
     let msgBar = document.getElementsByClassName("subcon")[0];
     msgBar.scrollTop = msgBar.scrollHeight;
     this.hidden = true;
     this.newmessage_count = 0;
     this.$store.state.newmessage_count  = 0;
  },
  getnewmessage_count(y){
    if(y==0){
      return "New Message";
    }else{
      return y;
    }
  },
  displayMessage(m){
     let formatmessage = '';
      for(let i=0;i<m.length;i++){
       formatmessage += m[i];
        if((i+1)%(Math.ceil(window.innerWidth*0.05))<=0){
          formatmessage += '\n';
          }
      }
      return formatmessage;
  },
  getsearch(s){

      let pers = document.querySelectorAll('.custom-hover');
      let ctname = this.getchatnames();
      if(s == true || this.converse==''){
        pers.forEach(el=>{el.style.display = 'block'});
      }else{
        for(let i = 0;i<ctname.length;i++){
         if(ctname[i].toUpperCase().includes(this.converse.toUpperCase()) || 
          ctname[i].toUpperCase() == this.converse.toUpperCase()){
              pers[i].style.display = 'block';
          }else{
             pers[i].style.display = 'none';
          }
        }
    }
    this.converse = ""
    document.querySelectorAll(".custom-hover").forEach(element =>{
          element.style.borderLeft = "0px solid white";
    });
  },
  iscurentd(d){
    //return true or false whether the date is current
      let currentd = moment();
      let testcurrentd = moment(d.Date);
      
      if((moment.duration(currentd.diff(testcurrentd))).asHours() <=24 && temp==0){
         temp++;
         return true;
      }else{
        return false;
      }
         
    },
    createchat(){
      let newdat = moment();
      let formatd = newdat.year()+"-"+(newdat.month()<9?'0':'')+(newdat.month()+1)+"-"+
      (newdat.date()<=9?'0':'')+newdat.date()+"T"+(newdat.hours()<=9?'0':'')+newdat.hours()+":"+
      (newdat.minutes()<=9?'0':'')+newdat.minutes()+":"+(newdat.seconds()<=9?'0':'')+newdat.seconds();

      let formatmessage =''

      let newMessage = {
       From:this.user,
       To:this.$store.state.activechat,
       Date: formatd,
       Message:this.new_message,
       Read:true
      }

      return newMessage;
    },
   sendMessage(){
     //creates message and sends it to the database
  
     this.$store.state.chat_message = this.createchat();
     this.$store.state.getchats.push(this.$store.state.chat_message);
     this.new_message = "";
     
     this.$store.dispatch("chat");
     
     
   },
   getchat(k){
       //gets all the cahts of a specific person
        let chats = [];
        this.$store.state.getchats.forEach(element=>{
          if((element.From == k || element.To == k) && (element.From == this.user || element.To == this.user)){
            chats.push(element);
          }
        });
        return chats;
    },
    getchatnames(){
      //get all the name of person that are in a chat
      temp=0;
      let visited = [];
        this.$store.state.getchats.forEach(element => {
          if(!visited.includes(element.To) && element.From == this.user){
               visited.push(element.To);
             } 
          if(!visited.includes(element.From) && element.To == this.user){
             visited.push(element.From);
          }
          });
            return visited.reverse(); //reverse the order because of sorting b time
    },
    getdtime(d){
      //get the time in a 12 hours format
      if(d==''){
        return d
      }
      let uncurrent = moment(d);
      let currentd = moment();
      let prefix = month[uncurrent.month()] +" "+ uncurrent.date();

      if((moment.duration(currentd.diff(uncurrent))).asYears() <=1){
         if(uncurrent.hours()>12){
            return prefix + "   "+(uncurrent.hours()-12) + ":"+(uncurrent.minutes() <10?"0":"")+
                    uncurrent.minutes()+" PM";
         }else{
           if(uncurrent.hours() == 0){
              return prefix + "   "+"12:"+(uncurrent.minutes() <10?"0":"")+uncurrent.minutes()+" AM";
           }else{
                return prefix + "   "+(uncurrent.hours()) + ":"+(uncurrent.minutes() <10?"0":"")+
                      uncurrent.minutes()+" AM";
            }
         }
      }else{
            return prefix + ","+ uncurrent.years()
      }
     
    },
    getcdate(d){
        //get date and time in a displayable format

         if(this.$store.state.newmessage_count!=0){
           if(this.newmessage_count<this.$store.state.newmessage_count){
              this.hidden = false
              this.newmessage_count = this.$store.state.newmessage_count;
              audio.play();
           }
           
         }

         let uncurrent = moment(d.Date);
         let currentd = moment();
         let previousd = moment(previousTime);
         let prefix;

         let dif = Math.abs((moment.duration(previousd.diff(uncurrent))).asMinutes());
         let sameuser = d.From == recp;
         previousTime = d.Date;
         recp = d.From;

          if(dif <= 1 && dif!=0 && sameuser){
              return '';
           }
         
        prefix = month[uncurrent.month()]+" "+uncurrent.date()+", "+uncurrent.year();

         if(uncurrent.hours()>12){
            return prefix + " "+(uncurrent.hours() -12) + ":"+(uncurrent.minutes() <10?"0":"")+
              uncurrent.minutes()+" PM";
          }else{
             if(uncurrent.hours() == 0){
                return prefix + " "+ "12:"+(uncurrent.minutes() <10?"0":"")+uncurrent.minutes()+" AM";
             }else{
                return prefix + " "+ (uncurrent.hours()) + ":"+(uncurrent.minutes() <10?"0":"")+
                uncurrent.minutes()+" AM";
            }
          }
    },
   setactivechat(k){
     //set the the active person converstion to the main|display and get if the user is typing
     //also set the previous time a message was sent
     if(window.innerWidth<=768){
        document.querySelectorAll(".drawer_specs")[0].style.left = "-100vw"; 
        document.querySelectorAll(".drawer_specs")[0].style.visibility = "hidden"; 
     }

      document.querySelectorAll(".custom-hover").forEach(element =>{
          element.style.borderLeft = "4px solid #EEEEEE";
      });

      let names = this.getchatnames();
      for(let i=0;i<names.length;i++){
        if(names[i] == k){
            document.querySelectorAll(".custom-hover")[i].style.borderLeft = "4px solid #D32F2F";
            i = names.length;
          }
      }

        this.$store.state.activechat = k;
        this.$store.state.displayEmojis = false;
        previousTime = this.getchat(k)[0].Date;
        temp=0;
        this.hidden = true;
    },
    lastmessage(p){
      //get the last message of a person
      let chats = [];
        this.$store.state.getchats.forEach(element=>{
          if(element.From == p || element.To == p){
            chats.push(element);
            if(this.$store.state.newmessage_count!=0){
                audio.play();
             }
            }
        });
        if(this.$store.state.isTyping){
          return {Message:'typing ...',Date:''}
        }else{
           return chats[chats.length-1];
        }
       
    },
    mobile_view(){
       document.querySelectorAll(".drawer_specs")[0].style.left= "0";  
       document.querySelectorAll(".drawer_specs")[0].style.visibility = "visible";
       this.hidden = true;
       this.$store.state.newmessage_count = 0;
    }
  }
  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

@media (min-width: 769px) {.drawer_specs{transition:0.5s;top:50px;width:30vw !important;height:90vh!important;background:#EEEEEE}.placeright{margin-left:30vw}
.subcon{ width:68vw; margin-left:30vw;}.mobile_back{display:none}.message_specs{top:83vh;width:67vw;margin-left:31vw}};
@media (min-width: 300px) and (max-width: 768px)  {.drawer_specs{transition:0.5s;top:50px;width:100vw !important;height:90vh!important;background:#EEEEEE}
.mobile_back{display:block}.message_specs{top:83vh;width:95vw;margin-left:2vw}}

.drawerheight{height: 500px;min-height:560px;max-height:800px;}
.daybreaker{width:100%;text-align:center;border-bottom:1px solid gray;line-height:0.1em;margin:10px 0 20px}
.daybreaker span{background:white;padding:0 10px;color:gray; }
.custom-hover:hover{background:rgb(221, 221, 221)}.custom-hover{background:#EEE;border-left:4px solid#EEE}
.gotolast{top:80vh}.sml_word{font-size:8px}

.stylescroll::-webkit-scrollbar {width: 10px;}
.stylescroll::-webkit-scrollbar-thumb {background: #666;border-radius: 20px;}
.stylescroll::-webkit-scrollbar-track {box-shadow: inset 0 0 6px rgba(0,0,0,0.3);-webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);background: #ddd;border-radius: 20px;}

.content_specs{width:100vw;padding:0;margin:0;height:91vh;}
.subcon_height{height:60vh;}
.custom-message{text-align:left;color:white}.roundedvcard{border-radius: 50%;background:#EEE;}
.message_con{padding:30px 5px 0 5px;}
.custom-btn{text-transform: none;font-weight:600;margin-bottom:5px;margin-top:0;height:inherit;min-height:36px;}
.getMessage:nth-child(1)>:nth-child(1)>:nth-child(1){background:#EEEEEE !important;border:none!important;padding:0;margin:0;}
.getMessage:nth-child(1)>:nth-child(1)>:nth-child(1)>:nth-child(1)>:nth-child(1){margin-right:1.2%;resize: none;}

</style>
