<template>
<body>
    <h1>Select the features for your prediction:</h1>
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
    background-color: #3A1414;
}
</style>
