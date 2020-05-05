import Vue from 'vue'
import App from './App.vue'

export const eventBus = new Vue({
  methods: {
      displaySection(sections, timesSelected) {
          this.$emit('sectionClicked', sections, timesSelected);
      },

      displayCourse(courses){
        this.$emit('courseAdded', courses);
      },
  }
});

new Vue({
  el: '#app',
  render: h => h(App)
})
