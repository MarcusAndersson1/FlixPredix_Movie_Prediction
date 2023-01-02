<template>
  <div class="container">
    <Bar v-if="loaded" :data="chartData" :options="options" />
  </div>
</template>

<script>
import { Bar } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from "chart.js";
import axios from "axios";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
);

export default {
  name: "BarChart",
  components: { Bar },
  data: () => ({
    loaded: false,
    chartData: {
        labels: [],
        datasets: [
          {
            label: 'Genres',
            backgroundColor: '#2596be',
            data: []
          }
        ]
      },
    options:{
      responsive: true,
        plugins: {
            title: {
                display: false,
                text: 'Chart.js'
            }
        },
        scales: {
            x: {
                display: true
            },
            y: {
                display: true
            }
        }
    }
  }),
  async mounted() {
    this.loaded = false;

    try{
      const response = await axios.get("http://localhost:8080/admin/getGenres");
      let list = Array.from(response.data)

      let half = Math.floor(list.length / 2)

      let genres = list.slice(0, half);
      let values = list.slice(half, list.length);

      this.chartData.labels = genres
      this.chartData.datasets[0].data = values

      this.loaded = true;

    }catch (e){
      console.log(e);
    }
  },
};
</script>