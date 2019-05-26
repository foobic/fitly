export default {
  user: function(state) {
    return state.user;
  },
  url: function(state) {
    return state.url;
  },
  links: function(state) {
    return state.links;
  },
  hashedUrl: function(state) {
    return state.hashedUrl;
  },
  urlPrefix: function(state) {
    return state.urlPrefix;
  },
  shortUrl: function(state) {
    return state.urlPrefix + state.hashedUrl;
  }
};
