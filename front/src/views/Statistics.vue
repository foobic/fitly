<template>
  <v-layout>
    <v-flex class="statistics-wrapper">
      <div class="table" v-if="table.data.length">
        <div class="table-name">
          <span>Statistics</span>
        </div>
        <div class="table-data">
          <v-data-table :headers="table.headers" :items="table.data">
            <template v-slot:items="props">
              <td>
                <a :href="props.item.hashed_url">{{ props.item.hashed_url }}</a>
              </td>
              <td>
                <a :href="props.item.original_url">{{
                  props.item.original_url
                }}</a>
              </td>
              <td>{{ props.item.views }}</td>
            </template>
          </v-data-table>
        </div>
      </div>
      <div v-else class="no-stat-wrapper">
        <span class="no-stat">No statistics yet</span>
      </div>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  name: "Statistics",
  data() {
    return {
      table: {
        headers: [
          {
            text: "Short Link",
            value: "hashed_url",
            align: "center",
            sortable: false
          },
          {
            text: "Original Link",
            value: "original_url",
            align: "center",
            sortable: false
          },
          { text: "Views", value: "views", align: "center" }
        ],
        data: [
          {
            hashed_url: "http://foobic.fitly.tk/l/asdf",
            original_url: "http://google.com",
            views: 2
          }
        ]
      }
    };
  }
};
</script>

<style lang="scss" scoped>
.statistics-wrapper {
  max-width: 80%;
  margin: 50px auto;
}
.table-name {
  text-align: center;
  color: #1976d2;
  font-size: 3em;
  font-weight: bold;
}
.table-data {
  margin-top: 20px;
}

.no-stat-wrapper {
  color: #1976d2;
  text-align: center;
}
.no-stat {
  font-size: 3em;
  font-weight: bold;
}

.table-data {
  tr,
  th,
  td {
    text-align: center !important;
  }
}
</style>
