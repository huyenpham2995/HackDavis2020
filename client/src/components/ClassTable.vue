
<template>
<div>
  <md-table v-model="classes" md-card @md-selected="onSelect" md-fixed-header>
    <md-table-row slot="md-table-row" slot-scope="{ item }" md-selectable="multiple" md-auto-select>
      <md-table-cell md-label="Class Code" md-sort-by="code">{{ item.code }}</md-table-cell>
      <md-table-cell md-label="Class Name" md-sort-by="name">{{ item.name }}</md-table-cell>
      <md-table-cell md-label="Units" md-sort-by="units">{{ item.units }}</md-table-cell>
    </md-table-row>
  </md-table>

  <p>Total Units: {{selected}}</p>
  <label id="error" for="error" hidden=True> Error Label </label>

</div>
</template>

<script>
export default {
  name: 'ClassTable',

  data: () => ({
    selected: 0,
    classes: [{
        name: 'Data Structures and Algorithms',
        code: 'ECS 122A',
        units: 4,
      },
      {
        name: 'Data Structures and Algorithms',
        code: 'ECS 122A',
        units: 4,
      },
      {
        name: 'Data Structures and Algorithms',
        code: 'ECS 122A',
        units: 4,
      },
      {
        name: 'Data Structures and Algorithms',
        code: 'ECS 122A',
        units: 4,
      },
      {
        name: 'Data Structures and Algorithms',
        code: 'ECS 122A',
        units: 4,
      },
    ]
  }),
  methods: {
    onSelect(items) {
      var selected = 0
      for (var i = 0; i < items.length; i++) {
        selected = selected + items[i].units
      }
      this.selected = selected

    }
  }
}
</script>

<style scoped>
.md-table {
  margin-left: 10%;
  margin-right: 10%;
  margin-top: 16px;
}

.md-table-cell {
  text-align: left;
}

#error {
  color: red;
}
</style>
