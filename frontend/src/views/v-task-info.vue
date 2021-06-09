<template>
  <div class="v-task-info">
    <div class="mx-auto">
      <h1 class="text-2xl">{{ taskData.name_task }}</h1>
      <hr />
      <p class="text-xl">{{ taskData.task_text }}</p>
      <p>{{ taskData.number_of_points }}</p>

      <input type="text" />

      <form
        @submit.prevent="
          $store.dispatch('sendAnswer', {
            answer: answer,
            task_id: taskData.id,
          })
        "
      >
        <label>Введите ответ:</label>
        <input type="text" v-model="answer" required />
        <button type="submit">ОТПРАВИТЬ</button>
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "v-task-info",

  data() {
    return {
      taskData: {},
      answer: "",
    };
  },

  created() {
    this.loadingTask();
  },
  watch: {
    $route: "loadingTask",
  },

  methods: {
    ...mapActions(["getTask"]),
    loadingTask() {
      if (this.$route.params.id) {
        this.getTask(this.$route.params.id).then(
          (data) => (this.taskData = data)
        );
      }
    },
  },
};
</script>
