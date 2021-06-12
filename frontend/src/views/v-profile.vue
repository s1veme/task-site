<template>
  <div class="v-profile">
    <div class="info" v-if="profile">
      {{ profile }}
    </div>

    <div>
      <template v-if="profile">
        <input
          ref="inputStatus"
          v-model="newStatus"
          @keyup.enter="changeStatus"
          v-if="isShowStatusInput"
        />
        <button type="text" v-if="changeStatus" @click="changeStatus">
          ИЗМЕНИТЬ
        </button>
      </template>
    </div>

    <div>
      <vTask v-for="task in tasksCompleted" :key="task.id" :task="task" />
      <h1></h1>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import vTask from "@/components/task/v-task";

export default {
  name: "v-profile",

  data() {
    return {
      isShowStatusInput: true,
      newStatus: "",
      profile: null,
    };
  },

  created() {
    this.loadingPrfile();
  },
  methods: {
    ...mapActions(["getProfile"]),
    onShowStatusInput() {
      this.isShowDescriptionInput = true;
      this.newStatus = this.profile.status;
    },

    onHideStatusInput() {
      this.isShowStatusInput = false;
    },

    async changeStatus() {
      if (this.profile.status === this.newStatus) {
        return;
      }

      this.$store.dispatch("updateProfile", { status: this.newStatus });
    },

    loadingPrfile() {
      if (this.$route.params.username) {
        this.getProfile(this.$route.params.username).then(
          (data) => (this.profile = data)
        );
        if (this.tasksCompleted) {
          return;
        }
        this.$store.dispatch("getTasksCompleted");
      }
    },
  },

  computed: {
    ...mapGetters(["tasksCompleted"]),
  },

  components: {
    vTask,
  },
};
</script>
