<template>
  <div class="account">
    <Authorized v-if="user.authorized" />
    <NoAuthorized v-else />
  </div>
</template>
<script>
import { mapGetters } from "vuex";
import Authorized from "../components/account/Authorized";
import NoAuthorized from "../components/account/NoAuthorized";

export default {
  name: "account",
  components: { NoAuthorized, Authorized },
  data() {
    return {};
  },
  computed: {
    ...mapGetters(["user"])
  }
};
</script>

<style lang="scss" scoped></style>
