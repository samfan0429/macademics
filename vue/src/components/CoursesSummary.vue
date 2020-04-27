<template>
    <section id="courses-summary">
        <hr>
        <div 
        v-for="section in sectionsSummary" 
        :key="section">
            {{section.numsection}} - {{section.name}} - {{section.days}} - {{section.start}} - {{section.end}}
        </div>
    </section>
</template>

<script>
import {eventBus} from '../main'

export default {
    props: {
        sectionsSummary: Array
    },
    data() {
        return {
            
        }
    },

    created(){
        eventBus.$on('sectionClicked', (sectionsSummary)=>{
            this.sectionsSummary = sectionsSummary;
        });
    }
};
</script>

<style scoped>
div{
    padding: 20px;
}
</style>