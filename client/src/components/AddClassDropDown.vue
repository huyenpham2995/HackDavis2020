<template>
<div>
  <h1> Add Classes </h1>
  <label for="component-dropdown"> Plan for: </label>
  <dropdown id="system-dropdown" :options="systemOptions"></dropdown>
  <dropdown id="season-dropdown" :options="seasonOptions"></dropdown>
  <dropdown id="year-dropdown" :options="yearOptions"></dropdown>
</div>
</template>

<script>
import Dropdown from '@/components/Dropdown'
let currentYear = new Date().getFullYear()

export default {
  name: 'Filters',
  components: {
    'dropdown': Dropdown
  },

  data() {
    var years = new Array(9)
    var j = 0
    for (var i = currentYear - 4; i < currentYear + 5; i++) {
      years[j] = i;
      j = j + 1;
    }

    let systems = ['Quarter', 'Semester'];
    let seasons = ['Fall', 'Winter', 'Spring', 'Summer'];

    return {
      //selectedYear: currentYear,
      yearOptions: years,
      seasonOptions: seasons,
      systemOptions: systems
    }
  }
}
</script>

<style scoped>
.filters {
  width: 800px;
  margin: 0 auto;
}

.filter {
  text-align: left;
}

.result {
  margin-top: 30px;
  text-align: left;
}

label {
  display: inline-block;
  margin-right: 20px;
}

#system-dropdown {
  display: inline-block;
  margin-right: 10px;
}

#season-dropdown {
  display: inline-block;
  margin-right: 10px;
}

#year-dropdown {
  display: inline-block;
}
</style>
