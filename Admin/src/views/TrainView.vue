<script>
import Header from "../components/Header.vue"
import File from "../components/FileUpload.vue"

export default {
  components: {
    Header,
    File
  }
}
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