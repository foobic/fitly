export default {
  changeUrl(state, payload) {
    state.url = payload.url;
  },
  changeHashedUrl(state, payload) {
    state.hashedUrl = payload.hashedUrl;
  },
  changeUser(state, payload) {
    state.user = { ...state.user, ...payload.user };
  },
  changeLinks(state, payload) {
    state.links = payload;
  },
  logout(state) {
    state.user = { authorized: false };
    state.links = [];
  }
};
