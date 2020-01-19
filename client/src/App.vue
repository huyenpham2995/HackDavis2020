<template>
<div id="app">
  <!--<Home />-->
  <AddQuarter />
</div>
</template>

<script>
//import Home from './components/Home.vue'
import AddQuarter from './components/AddQuarter.vue'

export default {
  name: 'app',
  components: {
    //Home
    AddQuarter
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 30px;
}
</style>
