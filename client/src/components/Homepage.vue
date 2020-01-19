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

  <div class="sign">
    <p id="des">Join us!</p>
    <button>Sign Up</button>
    <button> Login </button>
  </div>

  <div class="bottom-container">
    <p class="last-signature">© 2020 Schedule Fighter Team</p>
  </div>
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

button {
  align-self: center;
  margin-left: 30%;
  margin-right: 30%;
  margin-top: 20px;
  margin-bottom: 20px;
  background-color: #002855;
  color: #DAAA00;
  font-size: 15px;
  font-weight: bold;
  display: block;
  height: 40px;
  width: 150px;
  box-shadow: 3px 3px 3px rgba(0, 0, 0, 0.5);
}

.navbar {
  margin-bottom: 20px;
}

.logo {
  margin-top: 80px;
  margin-bottom: 200px;
}

.header {
  font-size: 80px;
  margin-bottom: 50px;
}

.sign {
  margin-left: 30%;
  margin-right: 30%;
  margin-top: 50px;
}

#first {
  color: #002855;
}

#second {
  color: #B3A369;
  font-weight: bold;
}

#description {
  font-size: 20px;
  font-weight: bold;
  margin-top: 20px;
}

#des {
  font-size: 15px;
  color: #002855;
  margin-right: 10%;
  margin-top: 20px;
}

.bottom-container {
  background-color: #002855;
  padding-top: 5px;
  padding-bottom: 5px;
}

.last-signature {
  color: #DAAA00;
  padding: 10px 0;
  font-size: 0.75rem;
}
</style>
