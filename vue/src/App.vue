<template>
  <div class="container">
    <app-header></app-header>
    <search-bar></search-bar>
    <hr>
    <course-display></course-display>
    <hr>
    <app-footer></app-footer>
  </div>
</template>

<script>
import Header from './components/Header.vue';
import SearchBar from './components/SearchBar.vue'
import CourseDisplay from './components/CourseDisplay.vue'
import Footer from './components/Footer.vue';

export default {
  
  components: {
    'app-header': Header,
    'search-bar': SearchBar,
    'course-display': CourseDisplay,
    'app-footer': Footer,
  }
  
}
</script>

<style>
.container{
  height: 100vh
}
</style>
