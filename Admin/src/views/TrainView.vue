<script>
import File from "../components/FileUpload.vue";
import axios from "axios";

export default {
  methods: {
    async replaceModel() {
      let file = document.getElementById("joblibInput").files[0];
      let formData = new FormData()
      formData.append('file', file)
      console.log(file);
      axios
        .post(import.meta.env.VITE_APP_SERVER_ENDPOINT + "/admin/upload", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          }
        })
        .then((response) => {
          console.log(response);
        });
    },
    async trainModel() {
      let file = document.getElementById("csvInput").files[0];
      let formData = new FormData()
      formData.append('file', file)
      axios
        .post(import.meta.env.VITE_APP_SERVER_ENDPOINT + "/admin/train", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          }
        })
        .then((response) => {
          console.log(response);
        });
    },
    async validateModel() {
      let file = document.getElementById("csvInput").files[0];
      let formData = new FormData()
      formData.append('file', file)
      axios
        .post(import.meta.env.VITE_APP_SERVER_ENDPOINT + "/admin/validate", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          }
        })
        .then((response) => {
          alert("Verification completed\nMSE score: " + response.data.mse + "\nR2 score: " + response.data.r2 );
        });
    },
    selectModel(model) {
      console.log(model);
      axios
        .post(import.meta.env.VITE_APP_SERVER_ENDPOINT + "/admin/activate", {
          version: model.version,
        })
        .then((response) => {
          console.log(response);
        });
    },
  },
  mounted() {
    console.log(import.meta.env.VITE_APP_SERVER_ENDPOINT + "/admin/models")
    axios
      .get(import.meta.env.VITE_APP_SERVER_ENDPOINT + "/admin/models", {})
      .then((response) => {
        console.log(response);
        this.models = response.data.models;
      });
  },
  components: {
    File,
  },
  data() {
    return {
      models: [],
    };
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
          id="csvInput"
          accept=".csv"
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
      <br />
      <div>
        <input
          id="joblibInput"
          type="file"
          accept=".joblib"
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

    <div
      class="overflow-x-auto max-w-lg border-2 border-purple-500 rounded mx-auto bg-purple-50"
    >
      <table class="table w-full">
        <!-- head -->
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
          </tr>
        </thead>
        <tbody>
          <!-- row 1 -->
          <tr
            class="border border-purple-500 border-t-0 border-l-0 border-r-0"
            v-for="model in models"
            v-bind:key="model.version"
            @click="selectModel(model)"
          >
            <th>
              {{ model.version }}
            </th>
            <th>{{ model.name }}</th>
            <th>
              <button
                @click="replaceModel()"
                class="bg-transparent hover:bg-blue-500 text-black-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded"
              >
                Use
              </button>
            </th>
          </tr>
        </tbody>
      </table>
    </div>

    <br />
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
