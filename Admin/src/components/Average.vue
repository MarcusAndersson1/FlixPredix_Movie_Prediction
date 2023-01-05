<template>
    <div class="max-w-full mx-4 py-6 sm:mx-auto sm:px-6 lg:px-8">
        <div class="inline-block  float-left align-bottom bg-white rounded-lg text-left overflow-hidden shadow transform transition-all mb-4 w-full sm:w-1/3 sm:my-8">
            <div class="bg-white p-5">
                <div class="sm:flex sm:items-start">
                    <div class="text-center sm:mt-0 sm:ml-2 sm:text-left">
                        <h3 class="text-sm leading-6 font-medium text-gray-400">Avg. Budget</h3>
                        <p class="text-3xl font-bold text-black">{{budget}}</p>
                    </div>
                </div>
            </div>
        </div>
      </div>
  </template>
<script>
import axios from 'axios';

export default {
  name: "Avg",
  data () {
    return{
    budget: 0,    
    }
  },
  async mounted() {

    try{
      const response = await axios.get("http://localhost:8080/admin/getAvgBudget");
      this.budget = response.data
      console.log(this.features)
      this.loaded = true;

    }catch (e){
      console.log(e);
    }
  },
};
</script>

