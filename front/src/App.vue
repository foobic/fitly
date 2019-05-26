<template>
  <v-app>
    <v-toolbar color="primary">
      <v-btn icon @click="redirectToHome">
        <v-icon color="white" class="logo">trip_origin</v-icon>
      </v-btn>

      <v-toolbar-title>
        <router-link to="/" class="toolbar-title toolbar-link" value="Fitly"
          >Fitly</router-link
        >
      </v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon @click="redirectToStat" v-if="user.authorized">
        <v-icon color="white">equalizer</v-icon>
      </v-btn>
      <v-btn icon @click="redirectToAccount">
        <v-icon color="white">account_circle</v-icon>
      </v-btn>
    </v-toolbar>
    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "App",
  data() {
    return {};
  },
  computed: {
    ...mapGetters(["user"])
  },
  methods: {
    redirectToAccount() {
      this.$router.push("/account");
    },
    redirectToHome() {
      this.$router.push("/");
    },
    redirectToStat() {
      this.$router.push("/statistics");
    }
  }
};
</script>

<style lang="scss" scoped>
.v-toolbar__title {
  color: white;
  font-size: 30px;
  font-weight: bold;
}
.toolbar-link {
  color: white;
  text-decoration: none;
  font-size: 30px;
}
.logo {
  font-size: 35px !important;
}
</style>
