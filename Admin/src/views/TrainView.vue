<script>

import File from "../components/FileUpload.vue";
import axios from "axios"

function saveToDb(data) {
  
}

export default {
  methods:{

  },
  mounted() {
    const inputElement = document.getElementById("dropzone-file");

    let data;
    function handleFiles() {
      const reader = new FileReader();

      reader.onload = () => {
        saveToDb(reader.result)
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


    <br>
    <File />
    <br>
    <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 border border-blue-700 rounded">
      Felix
    </button>

    <button @click="getDbRows()" class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">
      Train Model
    </button>
</main>
</template>

<style scoped>
  main{
    text-align: center;
  }

  button{
    margin: 5px;
  }
</style>