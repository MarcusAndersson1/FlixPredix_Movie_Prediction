<template>
<body>
    <h1 id="head">Features, pick you must:</h1>
    <br>
    <v-container class="home">
        <v-row align-h="start">
            <v-col>
                <BudgetSlide v-model="movieBudget" required></BudgetSlide>
                <br>
                <RegionSelect v-model="movieRegion" required></RegionSelect>
            </v-col>
            <v-col>
                <GenreSelect v-model="movieGenre" required></GenreSelect>
                <br>
                <RunTimeSelect v-model="movieRuntime" required></RunTimeSelect>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-btn @click="submit"> Submit </v-btn>
            </v-col>
            <v-col>
            </v-col>
        </v-row>
        <h1 v-if="predictedScore">Predicted score is: {{ predictedScore }}</h1>
    </v-container>
</body>
</template>

<script>
var audio = new Audio('https://s.cdpn.io/1202/Star_Wars_original_opening_crawl_1977.mp3');
    audio.pause();
/*<div class="HELP"></div>*/
// @ is an alias to /src
import BudgetSlide from '@/components/BudgetSlide.vue'
import GenreSelect from '@/components/GenreSelect.vue'
import RegionSelect from '@/components/RegionSelect.vue'
import RunTimeSelect from '@/components/RunTimeSelect.vue'
//import ErrorAlert from '@/components/ErrorAlert.vue'
//import SuccessAlert from '@/components/SuccessAlert.vue'
import axios from 'axios'

export default {
    name: 'HomeView',
    components: {
        BudgetSlide,
        GenreSelect,
        RegionSelect,
        RunTimeSelect,
        //ErrorAlert,
        //SuccessAlert,

    },
    data: () => ({
        movieGenre: '',
        movieBudget: null,
        movieRuntime: null,
        movieRegion: '',
        predictedScore: null
    }),
    methods: {
        submit() {
            axios.post('http://127.0.0.1:8080/predict', {
                    movie_genre: this.movieGenre,
                    movie_budget: this.movieBudget,
                    movie_runtime: this.movieRuntime,
                    movie_region: this.movieRegion
                })
                .then((response) => {
                    console.log(response)
                    this.predictedScore = response.data.class
                })
        },
        clear() {
            this.movieGenre = ''
            this.movieBudget = null
            this.movieRuntime = null
            this.movieRegion = ''
        }
    }
}
</script>

<style>
body {
    background-image: url('@/assets/flixpredix_gradient.png');
    background-repeat: no-repeat;
    background-size: cover;
    margin-top: 10px;
}

#head {
    font-family: "StarWars";
    font-size: 50px;
    margin-top: 50px;
    margin-bottom: 0px;
    color: white
}

.HELP {
    margin: 400px 650px;
    height: 0;
    width: 0;
    border-top: 80px solid transparent;
    border-right: 100px solid transparent;
    border-bottom: 80px solid transparent;
    border-left: 150px solid transparent;
}
</style>
