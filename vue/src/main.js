import Vue from 'vue'
import App from './App.vue'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

export const eventBus = new Vue({
  methods: {
      displaySection(sections, timesSelected, coursesSelected) {
          this.$emit('sectionClicked', sections, timesSelected, coursesSelected);
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
