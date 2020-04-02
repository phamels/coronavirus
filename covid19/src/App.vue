<template>
  <div id="app">
    <div class="jumbotron">
      <h1 class="display-4">Covid19 Country Statistics</h1>
      <p class="lead">Latest Covid19 / Coronavirus statistics per country</p>
      <hr class="my-4">
      <p class="lead">
        <a class="btn btn-primary" href="https://github.com/phamels/coronavirus" role="button" target="github">GitHub Code</a>&nbsp;
        <a class="btn btn-primary" href="/covid19.json" role="button">JSON Data</a>
      </p>
    </div>
    <div class="container">
      <CountryStats></CountryStats>
    </div>
  </div>
</template>

<script>
import CountryStats from './components/CountryStats.vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

export default {
  name: 'App',
  components: {
    CountryStats
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
