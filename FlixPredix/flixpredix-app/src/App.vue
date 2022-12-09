<template>
  <nav>
    <router-link to="/frontPage">FrontPage</router-link> |
    <router-link to="/home">Home</router-link> |
    <router-link to="/about">About</router-link> |
    
  </nav>
  <router-view/>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #831212;
  background-color: #831212;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #ffffff;
}

nav a.router-link-exact-active {
  color: #42b983;
}
@font-face {
  font-family: "aliens_and_cows";
  src: local("aliens_and_cows"),
   url(./assets/fonts/aliens_and_cows_trial.ttf) format("truetype");
}
</style>
