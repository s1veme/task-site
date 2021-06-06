<template>
  <div class="v-table-leaders">
    <h1 v-for="item in leadersTable" :key="item">{{ item.username }}</h1>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "v-table-leaders",

  data() {
    return {};
  },

  computed: {
    ...mapGetters(["leadersTable"]),
  },

  methods: {
    ...mapActions(["getLeadersTable"]),
  },

  created() {
    this.getLeadersTable();
  },
};
</script>
