<template>
<v-hover v-slot:default="{ isHovering }">
    <v-card class="mx-auto" id="gen" max-width="700" max-height="280" :color="isHovering ? '#C22020' : undefined">
        <v-card-title hide-details>GENRE</v-card-title>
        <v-card-text>
                <v-row>
                    <v-col cols="4" sm="3" md="3">
                        <v-checkbox-group column>
                            <v-checkbox label="Action" color="red" value="action" v-model="genres" hide-details></v-checkbox>
                            <v-checkbox label="Adventure" color="red" value="adventure" v-model="genres" hide-details></v-checkbox>
                            <v-checkbox label="Comedy" color="red" value="comedy" v-model="genres" hide-details></v-checkbox>
                        </v-checkbox-group>
                    </v-col>
                    <v-col cols="4" sm="3" md="3">
                        <v-checkbox-group column>
                            <v-checkbox label="Drama" color="red" value="drama" v-model="genres" hide-details></v-checkbox>
                            <v-checkbox label="Fantasy" color="red" value="fantasy" v-model="genres" hide-details></v-checkbox>
                            <v-checkbox label="Horror" color="red" value="horror" v-model="genres" hide-details></v-checkbox>
                        </v-checkbox-group>
                    </v-col>
                    <v-col cols="4" sm="3" md="3">
                        <v-checkbox-group v-model="ex7" column>
                            <v-checkbox label="Musical" color="red" value="musical" v-model="genres" hide-details></v-checkbox>
                            <v-checkbox label="Mystery" color="red" value="mystery" v-model="genres" hide-details></v-checkbox>
                            <v-checkbox label="Romance" color="red" value="romance" v-model="genres" hide-details></v-checkbox>
                        </v-checkbox-group>
                    </v-col>
                    <v-col cols="4" sm="3" md="3">
                        <v-checkbox-group v-model="ex7" column>
                            <v-checkbox label="Sci-Fi" color="red" value="science_fiction" v-model="genres" hide-details></v-checkbox>
                            <v-checkbox label="Thriller" color="red" value="thriller" v-model="genres" hide-details></v-checkbox>
                            <v-checkbox label="Western" color="red" value="western" v-model="genres" hide-details></v-checkbox>
                        </v-checkbox-group>
                    </v-col>
                </v-row>
        </v-card-text>
    </v-card>
</v-hover>
</template>

<script>
export default {
    data() {
        return {
            ex7: 'white',
            genres: []
        }
    },
    watch: {
        genres(new_genres) {
            this.$emit("emit-result",new_genres)
        }
    },
    name: 'GenreSelect',
    mounted() {
        this.$emit("emit-result",this.genres)
    },
}
</script>
<style>
#gen {
    color: white;
    background-color: #861515;
    
}
</style>