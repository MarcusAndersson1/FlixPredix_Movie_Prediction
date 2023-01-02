<script>
import BarChart from '../components/FeaturesDisplay.vue'
import AvrageVue from '../components/Average.vue';

export default {
  name: "App",
  components: {
    BarChart,
    AvrageVue
  },
  methods: {
    
  },
  // data() {
  //   return chartConfig;
  // },
  mounted() {
  },
};
</script>

<template>
  <div>
    <AvrageVue></AvrageVue>
    <BarChart />
  </div>
</template>