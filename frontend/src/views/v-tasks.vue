<template>
  <div class="v-tasks">
    <vTask v-for="task in tasks" :key="task.id" :task="task" />
  </div>
</template>

<script>
import vTask from "@/components/task/v-task.vue";
import { mapGetters } from "vuex";

export default {
  name: "v-tasks",

  data() {
    return {};
  },

  components: {
    vTask,
  },

  computed: {
    ...mapGetters(["tasks"]),
  },

  mounted() {
    this.$store.dispatch("getTasks");
  },
};
</script>
