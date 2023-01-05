<template>
<v-hover v-slot:default="{ isHovering }">
    <v-card class="mx-auto" id="reg" max-width="450" max-height="270" :color="isHovering ? '#C22020' : undefined">
        <v-card-title>REGION</v-card-title>
        <v-card-text>
                <v-row>
                    <v-col cols="2" sm="0" md="6">
                        <v-checkbox-group column>
                            <v-checkbox label="Africa" color="red" value="AF" v-model="regions" hide-details></v-checkbox>
                            <v-checkbox label="United Kingdom" color="red" value="UK" v-model="regions" hide-details></v-checkbox>
                            <v-checkbox label="Asia" color="red" value="AS" v-model="regions" hide-details></v-checkbox>
                            <v-checkbox label="Europe" color="red" value="EU" v-model="regions" hide-details></v-checkbox>
                        </v-checkbox-group>
                    </v-col>
                    <v-col cols="2" sm="0" md="6">
                        <v-checkbox-group column>
                            <v-checkbox label="Oceania" color="red" value="OC" v-model="regions" hide-details></v-checkbox>
                            <v-checkbox label="North America" color="red" value="NA" v-model="regions" hide-details></v-checkbox>
                            <v-checkbox label="South America" color="red" value="SA" v-model="regions" hide-details></v-checkbox>
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
            regions: []
        }
    },
    watch: {
        regions(new_regions) {
            this.$emit("emit-result",new_regions)
        }
    },
    name: 'RegionSelect',
    mounted() {
        this.$emit("emit-result",this.region)
    },
}
</script>
<style>
#reg {
    color: white;
    background-color: #861515;
    
}

</style>