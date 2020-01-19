<template>
  <div class="home">
    <Banner/>
    <UserInfo/>
    <div class="academicInfo">
      <Term v-for="(term, index) in terms" v-bind:key="index" :termName="term" :termClass="classes[index]"/>
      <Term :termName="newTerm" :termClass="[]"/>
    </div>
  </div>
</template>

<script>
import Banner from './Banner.vue'
import UserInfo from './UserInfo.vue'
import Term from './Term.vue'

export default {  
  name: 'Home',
  components: {
    Banner,
    UserInfo,
    Term
  },
  data () {
    return {
      terms: ['Fall 2018', 'Winter 2019', 'Spring 2019', 'Fall 2019', 'Winter 2020', 'Spring 2020', 'temp'],
      classes: [['ECS 36C: Data Structures and Algorithms', 'MAT 108: Intro to Abstract Math', 'ECS 154A: Computer Architecture'],
        ['ECS 127: Cryptography', 'ECS 140A: Programming Languages', 'ECS 120: Theory of Computation', 'ECH 001: Design of Coffee'],
        ['ECS 150: Operating Systems', 'ECS 122A: Algorithms Design', 'MUS 116: Music of The Beatles'],
        ['ECS 189E: iOS App Development', 'ECS 132: Probability and Statistics', 'ECS 175: Computer Graphics'],
        ['ECS 189G: Machine Learning', 'ECS 164: Human-Computer Interaction', 'UWP 104: Business Writing', 'COM 110: Hong Kong Cinema'],
        [],
        []
      ]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.academicInfo {
  display: inline-grid;
  grid-template-columns: 1fr 1fr 1fr;
  margin: 0 auto;
  width: 80vw;
  height: 70vh;
  overflow: scroll;
  overflow-x: hidden;
  scrollbar-width: none;
  border-radius: 20px;
  background-color: #00356B;
  border: dotted rgb(104, 103, 99) 5px;
  justify-items: center;
}
/* .academicInfo:active {
  overflow-y: visible;
} */

::-webkit-scrollbar {
  width: 30px;
}

::-webkit-scrollbar-track {
  background: rgba(224, 229, 233, 0.541);
  border: solid rgba(68, 62, 62, 0.596) 2px;
  border-radius: 7px;
  outline: none;
}

::-webkit-scrollbar-thumb {
  background:#B3A369;
  border-radius: 7px;
  width: 25px;
}

h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
