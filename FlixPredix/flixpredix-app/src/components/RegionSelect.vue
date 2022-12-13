<template>
<v-hover v-slot:default="{ isHovering, props }">
    <v-card class="mx-auto" id="reg" max-width="450" max-height="250" v-bind="props" :color="isHovering ? '#C22020' : undefined">
        <v-card-title>REGION</v-card-title>
        <v-card-text>
                <v-row>
                    <v-col cols="2" sm="0" md="6">
                        <v-radio-group v-model="ex7" column>
                            <v-radio label="Africa" color="red" value="0"></v-radio>
                            <v-radio label="Antarctica" color="red" value="1"></v-radio>
                            <v-radio label="Asia" color="red" value="2"></v-radio>
                            <v-radio label="Europe" color="red" value="3"></v-radio>
                        </v-radio-group>
                    </v-col>
                    <v-col cols="2" sm="0" md="6">
                        <v-radio-group v-model="ex7" column>
                            <v-radio label="Oceania" color="red" value="4"></v-radio>
                            <v-radio label="North America" color="red" value="5"></v-radio>
                            <v-radio label="South America" color="red" value="6"></v-radio>
                        </v-radio-group>
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
        }
    },
    name: 'GenreSelect',
    props: {
        msg: String
    },
}
</script>
<style>
#reg {
    color: white;
    background-color: #861515;
    
}

</style>