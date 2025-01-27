Vue.component("task", {
  template: `
    <tr>
      <td class="first-row">{{ task.description }}</td>
      <td class="last-row">
          <div class="form-check">
            <input type="checkbox" v-model="task.completed" />
            <label class="check-label">Complete</label>
          </div>  
          <button @click="deleteTask(task)">Delete</button>
      </td>
      </tr>
    `,
  props: ["task", "deleteTask"],
});

new Vue({
  el: "#app",
  data: {
    newTask: "",
    tasks: [{ description: "Task 1", completed: false }],
  },
  methods: {
    addTask: function () {
      if (this.newTask.trim("").length === 0) {
        alert("The field must not be empty!");
      } else {
        this.tasks.push({ description: this.newTask, completed: false });
      }

      this.newTask = "";
    },
    deleteTask: function (taskToDelete) {
      this.tasks = this.tasks.filter((task) => task !== taskToDelete);
    },
  },
  computed: {
    statusMessage: function () {
      const completedCount = this.tasks.filter((task) => task.completed).length;

      if (completedCount === this.tasks.length) {
        return "All task/s completed!";
      } else if (completedCount > 0) {
        return "Some task/s completed.";
      } else {
        return "No task/s completed yet.";
      }
    },
    totalTask: function () {
      return this.tasks.length;
    },
    completedTask: function () {
      return this.tasks.filter((task) => task.completed).length;
    },
  },
});
