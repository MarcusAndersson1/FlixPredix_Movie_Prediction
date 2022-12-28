<script>
import File from "../components/FileUpload.vue";
import axios from "axios";

function saveToDb(data) {}

export default {
  methods: {
    async getDbRows() {
      const response = await axios.get("http://localhost:4000/get");
      if (response.data) {
        console.log(response);
      } else {
        console.log("nothing");
      }
    },
    async replaceModel(){},
    async trainModel(){},
    async validateModel(){},
  },
  mounted() {
    const inputElement = document.getElementById("dropzone-file");

    let data;
    function handleFiles() {
      const reader = new FileReader();

      reader.onload = () => {
        saveToDb(reader.result);
        console.log(reader.result.slice(0, 50));
      };

      reader.readAsBinaryString(this.files[0]);
    }
    inputElement.addEventListener("change", handleFiles, false);
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
      @click="getDbRows()"
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
