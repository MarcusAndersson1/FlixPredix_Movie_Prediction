<template>
<v-hover v-slot:default="{ isHovering, props }">
    <v-card class="mx-auto" id="run" max-width="700" max-height="100" v-bind="props" :color="isHovering ? '#C22020' : undefined">
        <v-row class="mb-6" justify="space-between">
            <v-col class="text-center">
                <span class="text-subheading"> RUNTIME: </span>
                <span class="text-h5 font-weight-light mx-auto" v-text="runtime"></span>
                <span class="subheading font-weight-light mx-auto mr-">min</span>
                <v-slider v-model="runtime" :color="color" track-color="white" :ticks="tickLabels" :max="270" step="10" show-ticks="always" tick-size="3">
                    <template v-slot:prepend>
                        <v-btn size="small" variant="text" icon="mdi-minus" :color="color" @click="decrement"></v-btn>
                    </template>
                    <template v-slot:append>
                        <v-btn size="small" variant="text" icon="mdi-plus" :color="color" @click="increment"></v-btn>
                    </template></v-slider>
            </v-col>
        </v-row>
    </v-card>
</v-hover>
</template>

<script>
export default {

    data: () => ({
        runtime: 0,
        interval: null
    }),
    computed: {
        color() {
            if (this.runtime < 30) return 'white'
            if (this.runtime < 60) return 'pink'
            if (this.runtime < 90) return 'purple'
            if (this.runtime < 120) return 'indigo'
            if (this.runtime < 150) return 'blue'
            if (this.runtime < 180) return 'cyan'
            if (this.runtime < 210) return 'green'
            if (this.runtime < 240) return 'yellow'
            if (this.runtime < 270) return 'orange'
            else return 'red'
        },
        animationDuration() {
            return `${100 / this.runtime}s`
        },
    },
    name: 'RunTimeSelect',
    props: {
        runtimes: {
            type: Number
        }
    },
    mounted() {
    this.$emit("emit-result",this.runtime)
    },

    methods: {
        decrement() {
            this.runtime--
            this.$emit("emit-result",this.runtime)
        },
        increment() {
            this.runtime++
            this.$emit("emit-result",this.runtime)
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

#run {
    color: white;
    background-color: #861515;

}
</style>
