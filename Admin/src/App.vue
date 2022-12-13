<script setup>
import { RouterLink, RouterView } from "vue-router";
import HeaderVue from "./components/Header.vue";
</script>

<template>
  <div>
  <HeaderVue></HeaderVue>
  <RouterView />
  </div>

</template>

<style scoped>

</style>
