<template>
 <div class=container>
   <app-header></app-header>
   <div class='content'>
     <search-bar></search-bar>
     <courses-searched></courses-searched>
     <courses-selected></courses-selected>

    </div>
   <app-footer></app-footer>
 </div>
</template>
 
<script>
import Header from './components/Header.vue';
import SearchBar from './components/SearchBar.vue'
import CoursesSearched from './components/CoursesSearched.vue'
import CoursesSelected from './components/CoursesSelected.vue'
import Footer from './components/Footer.vue';
 
export default {
 components: {
   'app-header': Header,
   'search-bar': SearchBar,
   'courses-searched': CoursesSearched,
   'courses-selected': CoursesSelected,
   'app-footer': Footer,
 }
}
</script>
 
<style>
.container{
  min-height: 100%;
  display: flex;
  flex-direction: column;

  font-size: 25px;
}

.content{
  flex: 1 0 auto;
}
</style>
