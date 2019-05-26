import axios from "axios";
export default {
  changeUrl(ctx, payload) {
    ctx.commit("changeUrl", payload);
  },
  async refreshToken(ctx) {
    const res = await axios.post(
      `${process.env.VUE_APP_API_URL}/users/token/refresh`,
      {},
      {
        headers: {
          Authorization: `Bearer ${ctx.state.user.refresh_token}`
        }
      }
    );
    ctx.commit("changeUser", { user: { access_token: res.data.access_token } });
  },
  async loginUser(ctx, payload) {
    const user = {
      username: payload.username,
      password: payload.password
    };
    const res = await axios.post(
      `${process.env.VUE_APP_API_URL}/users/login`,
      user
    );

    ctx.commit("changeUser", {
      user: { ...user, ...res.data, authorized: true }
    });
    ctx.dispatch("fetchStat");
  },
  async createUser(ctx, payload) {
    const user = {
      username: payload.username,
      password: payload.password
    };
    const res = await axios.post(`${process.env.VUE_APP_API_URL}/users`, user);

    ctx.commit("changeUser", {
      user: { ...user, ...res.data, authorized: true }
    });
  },
  async createHashedUrlAuthorized(ctx, payload) {
    await ctx.dispatch("revokeAccessToken");
    await ctx.dispatch("refreshToken");

    const res = await axios.post(
      `${process.env.VUE_APP_API_URL}/links/authorized`,
      {
        url: payload.url
      },
      {
        headers: {
          Authorization: `Bearer ${ctx.state.user.access_token}`
        }
      }
    );

    ctx.commit("changeHashedUrl", { hashedUrl: res.data.hashed_url });
    ctx.dispatch("fetchStat");
  },
  async createHashedUrl(ctx, payload) {
    const res = await axios.post(`${process.env.VUE_APP_API_URL}/links`, {
      url: payload.url
    });

    ctx.commit("changeHashedUrl", { hashedUrl: res.data.hashed_url });
  },
  async revokeAccessToken(ctx) {
    await axios.post(
      `${process.env.VUE_APP_API_URL}/users/logout/access`,
      {},
      {
        headers: {
          Authorization: `Bearer ${ctx.state.user.access_token}`
        }
      }
    );
  },
  async revokeRefreshToken(ctx) {
    await axios.post(
      `${process.env.VUE_APP_API_URL}/users/logout/refresh`,
      {},
      {
        headers: {
          Authorization: `Bearer ${ctx.state.user.refresh_token}`
        }
      }
    );
  },
  async logout(ctx) {
    await ctx.dispatch("revokeRefreshToken");
    await ctx.dispatch("revokeAccessToken");
    ctx.commit("logout");
  },
  async fetchStat(ctx) {
    await ctx.dispatch("revokeAccessToken");
    await ctx.dispatch("refreshToken");
    let { data: links } = await axios.post(
      `${process.env.VUE_APP_API_URL}/links/fetch`,
      {},
      {
        headers: {
          Authorization: `Bearer ${ctx.state.user.access_token}`
        }
      }
    );

    links = links.sort((a, b) =>
      a.hashed_url > b.hashed_url ? 1 : b.hashed_url > a.hashed_url ? -1 : 0
    );

    ctx.commit("changeLinks", links);
  }
};
