<template>
  <div class="v-task">
    <router-link :to="{ name: 'task', params: { id: task.id } }">{{
      task.name_task
    }}</router-link>
    <hr />
    <p>{{ task.number_of_points }}</p>
  </div>
</template>

<script>
export default {
  name: "v-task",

  props: {
    task: Object,
  },

  data() {
    return {};
  },
};
</script>
