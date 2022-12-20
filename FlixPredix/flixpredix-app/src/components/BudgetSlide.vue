<template>
<v-hover v-slot:default="{ isHovering, props }">
    <v-card class="mx-auto" id="bud" max-width="450" max-height="115" v-bind="props" :color="isHovering ? '#C22020' : undefined">
        <br>
        <v-row class="mb-6" justify="space-between">
            <v-col class="text-center">
                <span class="text-subheading"> BUDGET: </span>
                <span class="text-h5 font-weight-light mx-auto" v-text="budget"></span>
                <span class="subheading font-weight-light mx-auto mr-">$</span>

                <v-slider v-model="budget" :color="color" track-color="white" min="1000" max="400000000" :step="1000">
                    <template v-slot:prepend>
                        <v-btn size="small" variant="text" icon="mdi-minus" :color="color" @click="decrement"></v-btn>
                    </template>
                    <template v-slot:append>
                        <v-btn size="small" variant="text" icon="mdi-plus" :color="color" @click="increment"></v-btn>
                    </template>
                </v-slider>
            </v-col>
        </v-row>
    </v-card>
</v-hover>
</template>

<script>
export default {
    data: () => ({
        budget: 1000,
        interval: null
    }),

    computed: {
        color() {
            if (this.budget < 10000) return 'blue'
            if (this.budget < 100000) return 'green'
            if (this.budget < 1000000) return 'yellow'
            if (this.budget < 10000000) return 'orande'
            if (this.budget < 100000000) return 'red'
            else return 'red'
        },
        animationDuration() {
            return `${100 / this.budget}s`
        },
    },
    name: 'BudgetSlide',
    props: {
        budgets: {
            type: Number
        }
    },
    mounted() {
    this.$emit("emit-result",this.budget)
    },

    methods: {
        decrement() {
            this.budget--
            this.$emit("emit-result",this.budget)
        },
        increment() {
            this.budget++
            this.$emit("emit-result",this.budget)
        }
    },
}
</script>

<style>
@keyframes metronome-example {
    from {
        transform: scale(.5);
    }

    to {
        transform: scale(1);
    }
}

.v-avatar--metronome {
    animation-name: metronome-example;
    animation-iteration-count: infinite;
    animation-direction: alternate;
}

#bud {
    color: white;
    background-color: #861515;
}
</style>
