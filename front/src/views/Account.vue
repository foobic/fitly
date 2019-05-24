<template>
  <div class="account">
    <div v-if="user.username" class="account-authorized">Authorized</div>
    <div v-else class="account-no-authorized">
      <h1>This is an Account page.</h1>
    </div>
  </div>
</template>
<script>
import { mapGetters } from "vuex";

export default {
  name: "account",
  data() {
    return {};
  },
  computed: {
    ...mapGetters(["user"])
  }
};
</script>
