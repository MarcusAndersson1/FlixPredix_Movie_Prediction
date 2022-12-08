<template>
    <body class="frontpage">
      <br>
    <v-container>


      <h1 class="name">FLIXPREDIX</h1>



      <v-row>
        <v-col>
          <v-btn class="pauseRound" size= "150" :color="color" theme="dark" icon elevation="15" @click="toggle">               
            <v-icon size="150" :icon="isPlaying ? 'mdi-pause' : 'mdi-pause'"></v-icon>             
          </v-btn>
        </v-col>
        <div class="trigger" v-bind:style="{ 'background-image': 'url(' + hover + ')' }">
        <v-col>
            <v-btn class="playRound" size= "190" :color="color" theme="dark" icon elevation="15" @click="toggle">               
              <v-icon size="190" :icon="isPlaying ? 'mdi-pause' : 'mdi-play'"></v-icon>             
            </v-btn>
          </v-col>
          </div>
        <v-col>
            <v-btn class="stopRound" size= "150" :color="color" theme="dark" icon elevation="15" @click="toggle">               
              <v-icon size="150" :icon="isPlaying ? 'mdi-pause' : 'mdi-stop'"></v-icon>             
            </v-btn>
        </v-col>
      </v-row>
      
      <div class="hidden"><img src="@/assets/flixpredix_spotlights.png" alt=""></div>
    </v-container>

      <div class="HELP"></div>
    </body>
</template>



  <script>



  /*
      <div class="trigger" v-bind:style="{ 'background-image': 'url(' + hover + ')' }">
        <v-btn class="pause" stacked elevation="15" prepend-icon="mdi-math-norm-box" variant="tonal" size="150"></v-btn>

        <v-btn class="play" stacked elevation="15" prepend-icon="mdi-play-box-outline" variant="tonal" size="180"></v-btn>    
      
        <v-btn class="stop" stacked elevation="15" prepend-icon="mdi-checkbox-intermediate" variant="tonal" size="150"></v-btn>
      </div>

      <div class="hidden"><img src="@/assets/flixpredix_spotlights.png" alt=""></div>

      <a href="/home">
      <v-btn elevation="9" icon>BAJS</v-btn>
      <div class="triangle"></div>
    </a>
  
      <v-btn elevation="9" icon x-large prepend-icon="mdi-vuetify">NAJS</v-btn>
  
  
  
  */
  </script>
  
  <style>
.frontpage {
    background-image: url('@/assets/flixpredix_frontpage.png');
    background-repeat: no-repeat;
    background-size: 100% 100%;
    margin-top: 0px;
  }
  .margin {
    margin-top: 0px;
  }
.name {
     font-family: "aliens_and_cows";
     font-size: 150px;
     margin-top: 100px;
     margin-bottom: 80px;

}
.HELP {
  margin: 500px 650px;
  height:0;
  width:0;
  border-top: 80px solid transparent;
  border-right: 100px solid transparent;
  border-bottom: 80px solid transparent;
  border-left: 150px solid transparent;
}
.play {
  font-size: 150px;
  margin: 100px 30px;
}
.stop {
  font-size: 120px;
  margin: 10px 30px;
}
.pause {
  font-size: 120px;
  margin: 10px 30px;
}
.playRound {
  font-size: 200px;
  margin: 10px 30px;
}
.stopRound {
  font-size: 200px;
  margin: 10px 30px;
}
.pauseRound {
  font-size: 200px;
  margin: 10px 30px;
}
.hidden { display: none; }
.trigger:hover + .hidden { display: inline; }
  </style>
