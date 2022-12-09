<template>
<v-card class="mx-auto" max-width="600" max-height="200" color="#B52C2C">
    <v-card-title>GENRE</v-card-title>
    <v-card-text>
        <v-container>
            <v-row>
                <v-col cols="4" sm="3" md="3">
                    <v-radio-group v-model="ex7" column>
                        <v-radio label="Action" color="red" value="1"></v-radio>
                        <v-radio label="Adventure" color="red" value="2"></v-radio>
                        <v-radio label="Comedy" color="red" value="3"></v-radio>
                    </v-radio-group>
                </v-col>
                <v-col cols="4" sm="3" md="3">
                    <v-radio-group v-model="ex7" column>
                        <v-radio label="Drama" color="red" value="4"></v-radio>
                        <v-radio label="Fantasy" color="red" value="5"></v-radio>
                        <v-radio label="Horror" color="red" value="6"></v-radio>
                    </v-radio-group>
                </v-col>
                <v-col cols="4" sm="3" md="3">
                    <v-radio-group v-model="ex7" column>
                        <v-radio label="Musical" color="red" value="7"></v-radio>
                        <v-radio label="Mystery" color="red" value="8"></v-radio>
                        <v-radio label="Romance" color="red" value="9"></v-radio>
                    </v-radio-group>
                </v-col>
                <v-col cols="4" sm="3" md="3">
                    <v-radio-group v-model="ex7" column>
                        <v-radio label="Sci-Fi" color="red" value="10"></v-radio>
                        <v-radio label="Thriller" color="red" value="11"></v-radio>
                        <v-radio label="Western" color="red" value="12"></v-radio>
                    </v-radio-group>
                </v-col>
            </v-row>
        </v-container>
    </v-card-text>
</v-card>
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
