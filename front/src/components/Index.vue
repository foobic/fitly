<template>
  <v-container class="index">
    <v-layout text-xs-center wrap>
      <v-flex>
        <v-alert v-model="errAlert" dismissible type="error">
          Unable to shorten that link. It is not a valid url. Make sure that you
          dont forget about http/https part of url
        </v-alert>
        <div class="input-container">
          <input
            v-model="url"
            @input="inputChanged"
            type="text"
            class="main-input"
            placeholder="Shorten your link"
          />
        </div>
        <div class="result-container" v-if="showResult">
          <a :href="shortenUrl">{{ shortenUrl }}</a>
        </div>
        <div class="button-container">
          <button class="mybtn" @click="shorten">Shorten</button>
        </div>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { setTimeout } from "timers";
function isUrlValid(url) {
  const pattern = new RegExp(
    "(https?:\\/\\/)" + // protocol
    "((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|" + // domain name
    "((\\d{1,3}\\.){3}\\d{1,3}))" + // OR ip (v4) address
    "(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*" + // port and path
    "(\\?[;&a-z\\d%_.~+=-]*)?" + // query string
      "(\\#[-a-z\\d_]*)?$",
    "i"
  );
  return !!pattern.test(url);
}

export default {
  name: "Index",
  data() {
    return {
      url: "",
      errAlert: false,
      showResult: false,
      urlPrefix: `${process.env.VUE_APP_SERVER_URL}/l/`
    };
  },
  computed: {
    shortenUrl: {
      get() {
        return this.urlPrefix + this.$store.getters.hashedUrl;
      }
    }
  },
  methods: {
    inputChanged() {
      this.$store.dispatch("changeUrl", { url: this.url });
    },
    async shorten() {
      const url = this.$store.getters.url;
      let loader = this.$loading.show({
        container: this.fullPage ? null : this.$refs.formContainer
      });
      if (isUrlValid(url)) {
        await this.$store.dispatch("createHashedUrl", { url });
        this.showResult = true;
      } else {
        this.errAlert = true;
        setTimeout(() => {
          this.errAlert = false;
        }, 5000);
      }
      loader.hide();
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
    color: white;
    text-decoration: none;
    &:hover {
      text-decoration: underline;
    }
  }
}
</style>
