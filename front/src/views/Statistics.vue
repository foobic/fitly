<template>
  <v-layout>
    <v-flex class="statistics-wrapper">
      <v-alert v-model="err.visibility" dismissible type="error">{{
        err.msg
      }}</v-alert>
      <div class="table" v-if="links.length">
        <div class="table-name">
          <span>Statistics</span>
        </div>
        <div class="table-data">
          <v-data-table
            :pagination.sync="table.pagination"
            :headers="table.headers"
            :items="links"
          >
            <template v-slot:items="props">
              <td>
                <a :href="urlPrefix + props.item.hashed_url">
                  {{ urlPrefix + props.item.hashed_url }}
                </a>
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
        <div class="fetch-btn-wrapper">
          <v-btn @click="fetchStat" class="center fetch-btn">Refresh</v-btn>
        </div>
      </div>
      <div v-else class="no-stat-wrapper">
        <span class="no-stat">No statistics yet</span>
      </div>
    </v-flex>
  </v-layout>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "Statistics",
  data() {
    return {
      err: { visibility: false, msg: "" },

      table: {
        pagination: {
          rowsPerPage: -1
        },
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
          { text: "Views", value: "views", align: "center", sortable: false }
        ]
      }
    };
  },
  computed: {
    ...mapGetters(["links", "urlPrefix"])
  },
  methods: {
    showErr(msg) {
      this.err.visibility = true;
      this.err.msg = msg;
      setTimeout(() => {
        this.err.visibility = false;
      }, 5000);
    },
    async fetchStat() {
      let loader = this.$loading.show();
      try {
        await this.$store.dispatch("fetchStat");
      } catch (e) {
        this.showErr(e.response.data.message);
      } finally {
        loader.hide();
      }
    }
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
.fetch-btn-wrapper {
  margin-top: 50px;
  display: flex;
  justify-content: center;
}
.fetch-btn {
  background: #1976d2 !important;
  color: white !important;
}
.table-data {
  tr,
  th,
  td {
    text-align: center !important;
  }
}
</style>
