<template>
<div class="dropdown">
  <select>
    <option v-for="option in options" :value="option" v-bind:key="option">{{ option }}</option>
  </select>
</div>
</template>

<script>
export default {
  name: 'Dropdown',
  props: {
    options: {
      type: Array,
      required: true
    }
  }
}
</script>

<style scoped></style>
