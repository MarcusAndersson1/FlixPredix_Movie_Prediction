<script>
import File from "../components/FileUpload.vue";
import axios from "axios";

export default {
<<<<<<< HEAD
  methods: {
    async replaceModel(){},
    async trainModel(){},
    async validateModel(){},
=======
  methods:{

>>>>>>> 0b721c8dd7e3f37be5ff6022d5d4cea75a2880ad
  },
  mounted() {
    
  },
  components: {
    File,
  },
};
</script>

<template>
  <main>
    <br />
    <!-- calidate och train nedanför(ladda upp csv) -->
    <div
      class="p-6 max-w-lg mx-auto bg-purple-40 rounded-xl shadow-md flex items-center space-x-4"
    >
      <div>
        <input
          type="file"
          class="file-input file-input-bordered w-full max-w-xs"
        />
      </div>

      <button
        @click="validateModel()"
        class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded"
      >
        Validate Model
      </button>
      <button
        @click="trainModel()"
        class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded"
      >
        Train Model
      </button>
    </div>
    <div
      class="p-6 max-w-lg mx-auto bg-purple-40 rounded-xl shadow-lg flex items-center space-x-4"
    >
      <!-- byt ut modell(ladda upp modell) -->
      <br/>
      <div>
        <input
          type="file"
          class="file-input file-input-bordered w-full max-w-xs"
        />
      </div>
      <button
        @click="replaceModel()"
        class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded"
      >
        Replace Model
      </button>
    </div>
    <br />
    <button
      class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 border border-blue-700 rounded"
    >
      Felix
    </button>

    <button
      class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded"
    >
      Train Model
    </button>
  </main>
</template>

<style scoped>
main {
  text-align: center;
}

button {
  margin: 5px;
}
</style>
