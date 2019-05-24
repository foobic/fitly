import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    url: "",
    shorten_url: "",
    user: { username: "" },
    links: {}
  },
  mutations: {},
  actions: {},
  getters: {
    user: function(state) {
      return state.user;
    }
  }
});
