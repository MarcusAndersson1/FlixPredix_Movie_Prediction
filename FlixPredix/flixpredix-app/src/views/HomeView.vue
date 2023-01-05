<template>
<body>
    <h1 id="head">Features, pick you must:</h1>
    <br>
    <v-container class="home">
        <v-row align-h="start">
            <v-col>
                <BudgetSlide required @emit-result="budgetresult"></BudgetSlide>
                <br>
                <RegionSelect required @emit-result="regionresult"></RegionSelect>
            </v-col>
            <v-col>
                <GenreSelect  required @emit-result="genreresult"></GenreSelect>
                <br>
                <RunTimeSelect required @emit-result="runtimeresult"></RunTimeSelect>
                <br>
                <h1 v-if="predictedScore">Predicted score is: {{ predictedScore }}</h1>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-btn @click="submit" :color="isHovering ? '#C22020' : undefined" class="mx-auto" id="sub"> Submit </v-btn>
            </v-col>
            <v-col>
            </v-col>
        </v-row>
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
            axios.post(process.env.VUE_APP_SERVER_ENDPOINT + '/consumer/predict', {
                    genres: this.movieGenre,
                    budget: this.movieBudget,
                    runtime: this.movieRuntime,
                    regions: this.movieRegion
                })
                .then((response) => {
                    console.log(response)
                    this.predictedScore = response.data["score"].toFixed(2)
                })
        },
        budgetresult(budget) {
        this.movieBudget = budget;
        },
        genreresult(genre) {
        this.movieGenre = genre;
        },
        runtimeresult(runtime) {
        this.movieRuntime = runtime;
        },
        regionresult(region) {
        this.movieRegion = region;
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
#sub {
    color: white;
    background-color: #861515;
    
}
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
