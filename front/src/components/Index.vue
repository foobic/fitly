<template>
  <v-container class="index">
    <v-layout text-xs-center wrap>
      <v-flex>
        <v-alert v-model="err.visibility" dismissible type="error">
          {{ err.msg }}
        </v-alert>
        <div class="input-container">
          <input
            v-model="url"
            type="text"
            class="main-input"
            placeholder="Shorten your link"
          />
        </div>
        <div class="result-container" v-if="result.visibility">
          <a :href="shortUrl">{{ shortUrl }}</a>
        </div>
        <div class="button-container">
          <button class="mybtn" @click="shortenUrl">Shorten</button>
        </div>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { setTimeout } from "timers";
import { mapGetters } from "vuex";
import { isUrlValid } from "@/helpers";

export default {
  name: "Index",
  data() {
    return {
      url: "http://google.com",
      err: { visibility: false, msg: "" },
      result: { visibility: false }
    };
  },
  computed: {
    ...mapGetters(["shortUrl", "hashedUrl"])
  },
  methods: {
    showErr(msg) {
      this.result.visibility = false;
      this.err.visibility = true;
      this.err.msg = msg;
      setTimeout(() => {
        this.err.visibility = false;
      }, 5000);
    },
    async shortenUrl() {
      const loader = this.$loading.show();
      try {
        if (
          // If protocol does not specified
          !(this.url.startsWith("http://") || this.url.startsWith("https://"))
        ) {
          this.url = `http://${this.url}`;
        }

        if (!isUrlValid(this.url)) return this.showErr("Url is not valid");

        this.$store.dispatch("changeUrl", { url: this.url });
        if (this.$store.getters.user.authorized) {
          await this.$store.dispatch("createHashedUrlAuthorized", {
            url: this.url
          });
        } else {
          await this.$store.dispatch("createHashedUrl", { url: this.url });
        }
        this.result.visibility = true;
      } catch (e) {
        this.showErr(e.response.data);
      } finally {
        loader.hide();
      }
    }
  }
};
</script>

<style scoped lang="scss">
.index {
  margin: 100px auto;
}
.input-container {
  background: #1976d2;
  border-radius: 10px;
  padding: 20px 0;
}
.main-input {
  background: white;
  width: 70%;
  height: 62px;
  padding: 0 20px;
  border-radius: 10px;
  font-size: 1.4em;
  border: 1px solid #1976d2;
  &:focus {
    outline: 0;
    border: none;
  }
}
.button-container {
  margin-top: 65px;
}
.mybtn {
  background: #1976d2;
  color: white;
  padding: 20px 50px;
  border-radius: 10px;
  font-size: 2em;
  &:focus {
    outline: 0;
    border: none;
  }
}
.result-container {
  height: 100px;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #4caf50bd;
  border-radius: 10px;
  margin: 30px 0;
  a {
    font-size: 2em;
    word-break: break-all;
    @media screen and (max-width: 400px) {
      font-size: 1.4em;
    }
    color: white;
    text-decoration: none;
    &:hover {
      text-decoration: underline;
    }
  }
}
</style>
