<template>
    <section id="courses-summary">
        <hr>
        <h2>Your Courses</h2>
        <div 
        v-for="section in sectionsSelected" 
        :key="section">

            <div>
                {{section.numsection}} - {{section.name}} - {{section.days}} - {{section.start}} - {{section.end}} - {{section.instructor}}
            </div>
        </div>
    </section>
</template>

<script>
import {eventBus} from '../main'

export default {
    props: {
        sectionsSelected: Array
    },
    data() {
        return {
            
        }
    },

    created(){
        eventBus.$on('sectionClicked', (sectionsSelected)=>{
            this.sectionsSelected = sectionsSelected;
        });
    }
};
</script>

<style scoped>
div{
    padding: 2px;
}
</style>