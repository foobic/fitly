<template>
  <v-container class="account-no-authorized">
    <v-layout text-xs-center wrap class="account-authorized">
      <v-alert v-model="err.visibility" dismissible type="error">
        {{ err.msg }}
      </v-alert>
      <div class="greeting">
        <span>
          You are logged in as
          <b>{{ user.username }}</b>
        </span>
      </div>

      <div class="links">
        <div class="link">
          <router-link tag="a" to="/">Home</router-link>
        </div>
        <div class="link">
          <router-link tag="a" to="/statistics">Statistics</router-link>
        </div>
      </div>
      <div class="logout-btn-wrapper">
        <v-btn class="center logout-btn" @click="logout">Logout</v-btn>
      </div>
    </v-layout>
  </v-container>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "Authorized",
  data() {
    return {
      err: { visibility: false, msg: "" },
      username: ""
    };
  },
  computed: {
    ...mapGetters(["user"])
  },
  methods: {
    async logout() {
      let loader = this.$loading.show();

      try {
        await this.$store.dispatch("logout");
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
.greeting {
  width: 100%;
  text-align: center;
  span {
    color: #1976d2;
    font-size: 2em;
  }
}

.logout-btn-wrapper {
  width: 100%;
  margin-top: 50px;
}
.logout-btn {
  background: #1976d2 !important;
  color: white !important;
}

.links {
  margin-top: 50px;
  width: 100%;
}
.link {
  margin: 10px 0;
  font-weight: bold;
  a {
    font-size: 2em;
    text-decoration: none;
    &:hover {
      text-decoration: underline;
    }
  }
}
</style>
