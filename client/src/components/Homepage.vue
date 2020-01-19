<template>
<div class="homepage">
  <div class='navbar'>
    <ul>
      <li><a href="/home">Home</a></li>
      <li><a href="/contact">Contact</a></li>
      <li><a href="/about">About</a></li>
    </ul>
  </div>
  <div class="logo">
    <div class="header">
      <span id="first">Schedule</span><span id="second">Fighter</span>
    </div>
    <p id="description"> A warrior that helps you build your schedule in 5 minutes!</p>
  </div>

  <p>Join us!</p>
  <button>Sign Up</button>
  <p>Already have an account?</p>
  <button> Login </button>
</div>
</template>

<script>
export default {
  name: 'homepage'
}
</script>

<style scoped>
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #002855;
}

li {
  float: right;
}

li a {
  float: right;
  display: block;
  color: #DAAA00;
  text-align: center;
  padding: 14px 16px;
}

li a:hover {
  background-color: #111;
}

.navbar {
  margin-bottom: 20px;
}

.logo {
  margin-top: 80px;
}

.header {
  font-size: 80px;
  margin-bottom: 50px;
}

#first {
  color: #002855;
}

#second {
  color: #B3A369;
  font-weight: bold;
}

#description {
  margin-top: 20px;
}
</style>
