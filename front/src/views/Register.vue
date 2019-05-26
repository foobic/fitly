<template>
  <v-container class="register" v-if="!user.username">
    <span>
      <v-layout class="justify-center">
        <v-flex xs12 md4>
          <div class="text">
            <span>Registration</span>
          </div>
          <v-alert v-model="err.visibility" dismissible type="error">
            {{ err.msg }}
          </v-alert>
          <div class="form justify-center">
            <v-form v-model="valid">
              <v-text-field
                v-model="username"
                :rules="usernameRules"
                :counter="15"
                label="Username"
                required
              ></v-text-field>
              <v-text-field
                v-model="password"
                :rules="passwordRules"
                :type="'password'"
                :counter="15"
                label="Password"
                required
              ></v-text-field>
              <v-text-field
                v-model="password2"
                :rules="password2Rules"
                :type="'password'"
                :counter="15"
                label="Password"
                required
              ></v-text-field>
              <div class="submit-wrapper">
                <v-btn @click="submit" class="center submit-btn">submit</v-btn>
              </div>
            </v-form>
          </div>
          <div class="login-wrapper">
            <router-link tag="a" to="/account">Login</router-link>
          </div>
        </v-flex>
      </v-layout>
    </span>
  </v-container>
  <v-container class="register text" v-else
    >You are already registered and authorized</v-container
  >
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Register",
  data() {
    return {
      err: { visibility: false, msg: "" },
      valid: false,
      username: "",
      usernameRules: [
        v => !!v || "Name is required",
        v => v.length >= 6 || "Name should contain at least 6 characters",
        v => v.length <= 15 || "Name must be less than 15 characters"
      ],
      password: "",
      passwordRules: [
        v => !!v || "Password is required",
        v => v.length >= 6 || "Password should contain at least 6 characters",
        v =>
          v.length <= 15 || "Password should contain no more then 15 characters"
      ],
      password2: "",
      password2Rules: [
        v => !!v || "Password is required",
        v => v == this.password || "Passwords should be equal"
      ]
    };
  },

  computed: {
    ...mapGetters(["user"])
  },
  methods: {
    showErr(msg) {
      this.err.visibility = true;
      this.err.msg = msg;
      setTimeout(() => {
        this.err.visibility = false;
      }, 5000);
    },
    async submit() {
      if (!this.valid) return;
      let loader = this.$loading.show();

      try {
        await this.$store.dispatch("createUser", {
          username: this.username,
          password: this.password
        });
        this.$router.push("/");
      } catch (e) {
        this.showErr(e.response.data.message);
      } finally {
        loader.hide();
      }
    }
  }
};
</script>

<style lang="scss" scoped>
.text {
  font-size: 2em;
}
</style>

<style lang="scss" scoped>
.text {
  font-size: 1.5em;
  font-weight: bold;
  text-align: center;
}

.submit-wrapper {
  display: flex;
  justify-content: center;
}
.login-wrapper {
  text-align: center;
  margin-top: 20px;
}

.submit-btn {
  background: #1976d2 !important;
  color: white !important;
}
</style>
