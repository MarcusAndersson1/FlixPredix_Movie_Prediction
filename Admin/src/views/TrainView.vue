<script>
import Header from "../components/Header.vue";
import File from "../components/FileUpload.vue";

export default {
  mounted() {
    const inputElement = document.getElementById("dropzone-file");

    let data;
    function handleFiles() {
      const reader = new FileReader();

      reader.onload = () => {
        console.log(reader.result);
      };

      reader.readAsBinaryString(this.files[0].slice(0,50));

    }
    inputElement.addEventListener("change", handleFiles, false);

  },

  components: {
    Header,
    File,
  },
};
</script>


<template>
  <main>
    <header>
      <Header />
    </header>

    <File />
  </main>
</template>

<style scoped>
</style>