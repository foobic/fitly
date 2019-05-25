import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    url: "",
    hashedUrl: "",
    user: { username: "" },
    links: {}
  },
  mutations: {
    changeUrl(state, payload) {
      state.url = payload.url;
    },
    changeHashedUrl(state, payload) {
      state.hashedUrl = payload.hashedUrl;
    }
  },
  actions: {
    changeUrl(ctx, payload) {
      ctx.commit("changeUrl", payload);
    },
    async createHashedUrl(ctx, payload) {
      const res = await axios.post(`${process.env.VUE_APP_API_URL}/links`, {
        url: payload.url
      });
      ctx.commit("changeHashedUrl", { hashedUrl: res.data.hashed_url });
    }
  },
  getters: {
    user: function(state) {
      return state.user;
    },
    url: function(state) {
      return state.url;
    },
    hashedUrl: function(state) {
      return state.hashedUrl;
    }
  }
});
