import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Account from "./views/Account.vue";
import Register from "./views/Register.vue";
import Statistics from "./views/Statistics.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/statistics",
      name: "statistics",
      component: Statistics
    },
    {
      path: "/register",
      name: "register",
      component: Register
    },
    {
      path: "/account",
      name: "account",
      component: Account
    },
    {
      path: "/",
      name: "home",
      component: Home
    }
  ]
});
