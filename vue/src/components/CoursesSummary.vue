<template>
    <section id="courses-summary">
        <hr>
        <h2>Your Courses</h2>

            <div 
            v-for="section in sectionsSelected" 
            :key="section" class="sections">
                <button 
                @click="deleteSection(section)">
                X
                </button>            

                <div class="section-name">
                    {{section.numsection}} - {{section.name}} - {{section.days}} - {{section.start}} - {{section.end}} - {{section.instructor}}
                </div>
            </div>
    </section>
</template>

<script>
import {eventBus} from '../main'

export default {
    props: {
        sectionsSelected: Array,
        timesSelected: Array,
        coursesSelected: Array
    },
    data() {
        return {

        }
    },

    methods: {
        deleteSection(section){
            var index = this.sectionsSelected.indexOf(section)
            if (index > -1) {
                this.sectionsSelected.splice(index, 1)
            }

            var index = this.timesSelected.indexOf(""+ section.days + "-" + section.start + "-" + section.end)
            if (index > -1) {
                this.timesSelected.splice(index, 1)
            }

            var index = this.coursesSelected.indexOf(section.name)
            if (index > -1) {
                this.coursesSelected.splice(index, 1)
            }
        }
    },

    created(){
        eventBus.$on('sectionClicked', (sectionsSelected, timesSelected, coursesSelected)=>{
            this.sectionsSelected = sectionsSelected
            this.timesSelected = timesSelected
            this.coursesSelected = coursesSelected
        });
    }
};
</script>

<style scoped>
div{
    padding: 2px;
}

.sections{
    display: flex;
    padding: 10px;
}

.section-name{
    padding-left: 10px;
    padding-right: 10px;
}
</style>