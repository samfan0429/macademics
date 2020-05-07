<template>
    <section id="courses-summary">
        <hr>
        <h3><b>Your Courses</b></h3>

            <div 
            v-for="(section, index) in sectionsSelected" 
            :key="index" class="sections">
                 
                <button 
                    class="btn btn-danger"
                    id="x"
                    @click="deleteSection(section)">
                X
                </button>         

                <div class="section-name justify-content-center">
                    <b>{{section.numsection}} - {{section.name}} 
                    - <br>{{section.days}} - {{section.start}} - {{section.end}} - {{section.instructor}}</b>
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

            index = this.timesSelected.indexOf(""+ section.days + "-" + section.start + "-" + section.end)
            if (index > -1) {
                this.timesSelected.splice(index, 1)
            }

            index = this.coursesSelected.indexOf(section.name)
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
#courses-summary{
    justify-items: center;
    justify-content: center;
    text-align: center;
    align-items: center;
    align-content: center;
}
.sections{
    display: flex;
    padding: 10px;
    justify-items: center;
    /* justify-content: center; */
    text-align: center;
    align-items: center;
    align-content: center;
    min-width: 80%;
    justify-self: start;
    /* width: 80vw; */
}

.section-name{
    padding-left: 10px;
    padding-right: 10px;
    /* align-self: left ; */
    /* display: flex; */
    /* justify-items: center; */
    /* justify-content: center; */
    /* text-align: center; */
    /* align-items: center; */
    /* align-content: center; */
}
</style>