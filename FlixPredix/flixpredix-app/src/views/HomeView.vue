<template>
<body>
    <br/>
    <h1 id="head">Features, pick you must:</h1>
    <br>
    <v-container class="home">
        <v-row align-h="start">
            <v-col>
                <BudgetSlide />                
                <br>
                <RegionSelect />
            </v-col>
            <v-col>
                <GenreSelect />
                <br>
                <RunTimeSelect/>
            </v-col>
        </v-row>
    </v-container>
    <div class="HELP"></div>
</body>
</template>

<script>
// @ is an alias to /src
import BudgetSlide from '@/components/BudgetSlide.vue'
import GenreSelect from '@/components/GenreSelect.vue'
import RegionSelect from '@/components/RegionSelect.vue'
import RunTimeSelect from '@/components/RunTimeSelect.vue'

export default {
    name: 'HomeView',
    components: {
        BudgetSlide,
        GenreSelect,
        RegionSelect,
        RunTimeSelect
    },
}
</script>

<style>
body {
    background-image: url('@/assets/flixpredix_gradient.png');
    background-repeat: no-repeat;
    background-size: 100% 100%;
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
  height:0;
  width:0;
  border-top: 80px solid transparent;
  border-right: 100px solid transparent;
  border-bottom: 80px solid transparent;
  border-left: 150px solid transparent;
}
</style>
