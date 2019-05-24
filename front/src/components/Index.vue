<template>
  <v-container class="index">
    <v-layout text-xs-center wrap>
      <v-flex>
        <div class="input-container">
          <input
            type="text"
            class="main-input"
            placeholder="Shorten your link"
          />
        </div>
        <div class="button-container">
          <button class="mybtn">Shorten</button>
        </div>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: "Index"
};
</script>

<style scoped lang="scss">
.index {
  margin: 100px auto;
}
.input-container {
  background: #1976d2;
  border-radius: 10px;
  padding: 20px 0;
}
.main-input {
  background: white;
  width: 70%;
  height: 62px;
  padding: 0 20px;
  border-radius: 10px;
  font-size: 1.4em;
  border: 1px solid #1976d2;
  &:focus {
    outline: 0;
    border: none;
  }
}
.button-container {
  margin-top: 65px;
}
.mybtn {
  background: #1976d2;
  color: white;
  padding: 20px 50px;
  border-radius: 10px;
  font-size: 2em;
  &:focus {
    outline: 0;
    border: none;
  }
}
</style>
