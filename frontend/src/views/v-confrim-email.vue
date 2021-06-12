<template>
  <div class="v-confrim-email">
    <h1>ОКЕЙ, ВСЁ УСПЕШНО!!!</h1>
  </div>
</template>

<script>
export default {
  name: "v-confrim-email",

  async created() {
    let uid = this.$route.query.user_code.split("___")[1];
    let token = this.$route.query.user_code.split("___")[2];

    if (!token || !uid) {
      await this.$router.push("/");
      return;
    }

    this.$store.dispatch("getConfrimEmail", { uid, token });
  },
};
</script>
