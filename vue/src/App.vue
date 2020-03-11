<template>
  <div class="container">
    <app-header></app-header>
    <hr>
    <search-bar></search-bar>
    <courses-searched></courses-searched>

    <app-footer></app-footer>
  </div>
</template>

<script>
import Header from './components/Header.vue';
import SearchBar from './components/SearchBar.vue'
import CoursesSearched from './components/CoursesSearched.vue'
import Footer from './components/Footer.vue';

export default {
  components: {
    'app-header': Header,
    'search-bar': SearchBar,
    'courses-searched': CoursesSearched,
    'app-footer': Footer,
  }
}
</script>

<style>
.container{
  min-height: 100%;
  font-size: 25px
}
</style>
