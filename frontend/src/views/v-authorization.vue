<template>
  <div class="v-authorization">
    <vLogin />
    <vRegistration />
  </div>
</template>

<script>
import vLogin from "@/components/v-login";
import vRegistration from "@/components/v-registration";

export default {
  name: "v-authorization",

  data() {
    return {};
  },

  components: {
    vLogin,
    vRegistration,
  },
};
</script>
