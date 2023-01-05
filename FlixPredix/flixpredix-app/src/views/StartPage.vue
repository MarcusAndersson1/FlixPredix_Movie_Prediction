<template>
    <body class="frontpage">
      <br>
      <h1 class="name mx-auto">FLIXPREDIX</h1>
    <v-container>
      <v-row>
        <v-col></v-col>
        <v-col></v-col>
        <v-col class="pauseRound">
          <v-btn size= "110" :color="color" theme="dark" icon elevation="15" @click="toggle">               
            <v-icon size="110" :icon="isPlaying ? 'mdi-pause' : 'mdi-pause'" color="#831212"></v-icon>             
          </v-btn>
        </v-col>
        <v-col class="playRound">
            <v-btn size= "150" :color="color" theme="dark" icon elevation="15" @click="toggle" href="/#/home">               
              <v-icon size="150" :icon="isPlaying ? 'mdi-pause' : 'mdi-play'" color="#831212"></v-icon>             
            </v-btn>
          </v-col>
        <v-col class="stopRound">
            <v-btn size= "110" :color="color" theme="dark" icon elevation="15" @click="toggle" href="/#/credits">               
              <v-icon size="110" :icon="isPlaying ? 'mdi-pause' : 'mdi-stop'" color="#831212"></v-icon>             
            </v-btn>
        </v-col>
        <v-col></v-col>
        <v-col></v-col>
      </v-row> 
    </v-container>
    <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
    </body>
</template>



  <script>


/*<div class="HELP"></div>*/
  /*
      v-bind:style="{ 'background-image': 'url(' + require('@/assets/flixpredix_frontpage_with_spotlight.png') + hover + ')' }"
      v.bind:style="{'background-image': 'url(' + require('./link/to/image.png') + ')'}"

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
    margin-top: 10px;
    color: #831212;
    background-color: #831212;
  }
  .frontpage:hover {
    background-image: url('@/assets/flixpredix_frontpage_with_spotlight.png');
  }
  .margin {
    margin-top: 0px;
  }
.name {
     font-family: "SWs";
     font-size: 100px;
     margin-top: 50px;
     margin-bottom: 0px;

}
.HELP {
  margin: 400px 650px;
  height:0;
  width:0;
  border-top: 80px solid transparent;
  border-right: 100px solid transparent;
  border-bottom: 80px solid transparent;
  border-left: 150px solid transparent;
}
.play {
  font-size: 150px;
  margin: 70px 30px;
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
  /*margin: 10px 30px;*/
}
.stopRound {
  font-size: 200px;
  margin-left: 30px;
  /*margin: 10px 50px;*/
}
.pauseRound {
  font-size: 200px;
  margin-right: 30px;
  /*margin: 10px 0px;*/
}
.hidden { display: none; }
.trigger:hover + .hidden { display: inline; }
  </style>
