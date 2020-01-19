<template>
<div class="addSem">
  <Banner />
  <AddClassDropDown />
  <ClassTable />
  <button class="addButton" type="button"> Add </button>

</div>
</template>

<script>
import Banner from './Banner.vue'
import AddClassDropDown from './AddClassDropDown.vue'
import ClassTable from './ClassTable.vue'
export default {
  name: 'AddQuarter',
  components: {
    Banner,
    AddClassDropDown,
    ClassTable
  }
}
</script>

<style scoped>
.addButton {
  background-color: #002855;
  color: #DAAA00;
  margin-top: 20px;
  font-size: 15px;
  font-weight: bold;
  display: block;
  height: 40px;
  width: 100px;
  margin-left: 10%;
  box-shadow: 3px 3px 3px rgba(0, 0, 0, 0.5);
}
</style>
