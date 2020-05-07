<template>
 <div class='container vertical-center'>
   <app-header></app-header>
   <div class='content'>
     <hr>
     <courses-searched></courses-searched>
     <hr>
     <courses-selected></courses-selected>
     <courses-summary></courses-summary>

    </div>
   <!-- <app-footer></app-footer> -->
 </div>
</template>

<script>
import Header from './components/Header.vue'
import CoursesSearched from './components/CoursesSearched.vue'
import CoursesSelected from './components/CoursesSelected.vue'
import CoursesSummary from './components/CoursesSummary.vue'
// import Footer from './components/Footer.vue'

export default {
 components: {
   'app-header': Header,
   'courses-searched': CoursesSearched,
   'courses-selected': CoursesSelected,
   'courses-summary': CoursesSummary,
  //  'app-footer': Footer,
 }
}
</script>

<style>
.container{
  margin-left: 10px;
  margin-right: 10px;
  max-width: 100vw;
  /* min-height: 100%;
  display: flex;
  flex-direction: column;

  font-size: 20px; */
}

.content{
  flex: 1 0 auto;
}

body, html {
  padding: 0;
  margin: 0;
  width: 100%;
  min-height: 100vh;
}
body {
  /* background-color: rgb(178, 184, 189); */
  background-color: white
}
</style>
