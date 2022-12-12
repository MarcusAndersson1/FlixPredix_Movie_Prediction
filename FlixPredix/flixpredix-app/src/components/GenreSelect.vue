<template>
<v-hover v-slot:default="{ isHovering, props }">
    <v-card class="mx-auto" id="gen" max-width="700" max-height="300" v-bind="props" :color="isHovering ? '#C22020' : undefined">
        <v-card-title>GENRE</v-card-title>
        <v-card-text>
            <v-container>
                <v-row>
                    <v-col cols="4" sm="3" md="3">
                        <v-checkbox-group v-model="ex7" column>
                            <v-checkbox label="Action" color="red" value="1" hide-details></v-checkbox>
                            <v-checkbox label="Adventure" color="red" value="2" hide-details></v-checkbox>
                            <v-checkbox label="Comedy" color="red" value="3" hide-details></v-checkbox>
                        </v-checkbox-group>
                    </v-col>
                    <v-col cols="4" sm="3" md="3">
                        <v-checkbox-group v-model="ex7" column>
                            <v-checkbox label="Drama" color="red" value="4" hide-details></v-checkbox>
                            <v-checkbox label="Fantasy" color="red" value="5" hide-details></v-checkbox>
                            <v-checkbox label="Horror" color="red" value="6" hide-details></v-checkbox>
                        </v-checkbox-group>
                    </v-col>
                    <v-col cols="4" sm="3" md="3">
                        <v-checkbox-group v-model="ex7" column>
                            <v-checkbox label="Musical" color="red" value="7" hide-details></v-checkbox>
                            <v-checkbox label="Mystery" color="red" value="8" hide-details></v-checkbox>
                            <v-checkbox label="Romance" color="red" value="9" hide-details></v-checkbox>
                        </v-checkbox-group>
                    </v-col>
                    <v-col cols="4" sm="3" md="3">
                        <v-checkbox-group v-model="ex7" column>
                            <v-checkbox label="Sci-Fi" color="red" value="10" hide-details></v-checkbox>
                            <v-checkbox label="Thriller" color="red" value="11" hide-details></v-checkbox>
                            <v-checkbox label="Western" color="red" value="12" hide-details></v-checkbox>
                        </v-checkbox-group>
                    </v-col>
                </v-row>
            </v-container>
        </v-card-text>
    </v-card>
</v-hover>
</template>

<script>
export default {
    data() {
        return {
            ex7: 'white',
        }
    },
    name: 'GenreSelect',
    props: {
        msg: String
    },
}
</script>
<style>
#gen {
    color: white;
    background-color: #861515;
    
}
</style>