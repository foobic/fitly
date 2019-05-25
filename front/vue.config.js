module.exports = {
  devServer: {
    port: 8080,
    host: "0.0.0.0",
    public: "0.0.0.0:8080",
    watchOptions: {
      poll: true
    }
  },
  pwa: {
    name: "MyFavicon",
    iconPaths: {
      favicon32: "./public/favicon.ico",
      favicon16: "./public/favicon.ico",
      appleTouchIcon: "./public/favicon.ico",
      maskIcon: "./public/favicon.ico",
      msTileImage: "./public/favicon.ico"
    }
  }
};
