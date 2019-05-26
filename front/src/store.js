import Vue from "vue";
import Vuex from "vuex";

import getters from "./store/getters";
import actions from "./store/actions";
import mutations from "./store/mutations";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    url: "",
    hashedUrl: "",
    user: { username: "", authorized: false },
    links: {},
    urlPrefix: `${process.env.VUE_APP_SERVER_URL}/l/`
  },
  mutations,
  actions,
  getters
});
