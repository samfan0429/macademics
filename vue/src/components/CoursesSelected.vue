<template>
    <section id="courses-selected">
        <hr>
        <div 
        v-for="section in sectionsSelected" 
        :key="section" 
        v-if="section.show">
            {{section.numsection}} - {{section.name}} - {{section.days}} - {{section.time}}
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
    padding: 20px;
}
</style>