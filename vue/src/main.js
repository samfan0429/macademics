import Vue from 'vue'
import App from './App.vue'

export const eventBus = new Vue({
  methods: {
      displaySection(section) {
          this.$emit('sectionClicked', section);
      }
  }
});

new Vue({
  el: '#app',
  render: h => h(App)
})
