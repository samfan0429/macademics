<template>
    <section id="courses-selected" class="container">
        <div id="titles" class="row">
            <h3 class='col-5'><b>Courses of Interest</b></h3>
            <h3 class='col-7'><b>Available Sections</b></h3>
        </div>
        
        <div class="row" v-for="(course, index) in coursesAdded" :key="index">
            <div v-if="course.show" class= "course">
                <div class="col-5 course-title">
                    <button 
                    class="btn btn-danger"
                    id="x"
                    @click="deleteCourse(course)">
                        X
                    </button>
                    <div 
                        id="course-name"  
                        v-if="course.show">
                    <b>{{course.courseNum}}</b> - {{course.name}} 
                    </div>
                </div>
                <div class="section col-7 justify-content-center">
                    <button 
                    id="button-section"
                    class='col-4 btn'
                    v-for="(section, index) in course.sections" :key="index"
                    @click="sectionSelected(section)"
                    :class = "[{'btn-secondary': isConflicted(section)}, {'btn-warning': isSelected(section)}]">
                    <!-- listen to the emitted event and call isConflicted? -->
                        <b>{{section.days}} - {{section.start}}-{{section.end}}</b>
                    </button>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import db from '../firebaseinit.js'
import {eventBus} from '../main'

export default {
   props: {
        coursesAdded: Array
    },
   data() {
        return {
            sectionsSelected: [],
            timesSelected: [],
            coursesSelected: []
        }
    },

    methods: {
        deleteCourse(course){
            course.show = false
            var index = this.coursesAdded.indexOf(course)
            if (index > -1) {
                this.coursesAdded.splice(index, 1)
                
            }
        },
        sectionSelected(section){
            if(!(this.sectionsSelected.includes(section)) & 
            !(this.timesSelected.includes(""+ section.days + "-" + section.start + "-" + section.end))
            & !(this.coursesSelected.includes(section.name)))
            {
                this.sectionsSelected.push(section)
                this.coursesSelected.push(section.name)
                this.timesSelected.push(""+ section.days + "-" + section.start + "-" + section.end) 
                eventBus.displaySection(this.sectionsSelected, this.timesSelected, this.coursesSelected)

            }
            else if(this.coursesSelected.includes(section.name) 
            & !(this.sectionsSelected.includes(section))
            & !(this.timesSelected.includes(""+ section.days + "-" + section.start + "-" + section.end))){
                var oldSection = ''
                this.sectionsSelected.forEach(aSection => {
                    if(aSection.name == section.name){
                        oldSection = aSection
                    }
                })
                var index = this.sectionsSelected.indexOf(oldSection)
                if (index > -1) {
                    this.sectionsSelected.splice(index, 1)
                }

                index = this.timesSelected.indexOf(""+ oldSection.days + "-" + oldSection.start + "-" + oldSection.end)
                if (index > -1) {
                    this.timesSelected.splice(index, 1)
                }

                this.sectionsSelected.push(section)
                this.timesSelected.push(""+ section.days + "-" + section.start + "-" + section.end)
                eventBus.displaySection(this.sectionsSelected, this.timesSelected, this.coursesSelected)

            }
            
            // TODO: 
            // send a warning saying the time of the section the user is selecting conflict with 
            // a section already added to coursesSummary
            // if(this.timesSelected.includes(""+ section.days + "-" + section.start + "-" + section.end))){
            //    *send the warning*
            //}

            else if((this.sectionsSelected.includes(section)) & 
            (this.timesSelected.includes(""+ section.days + "-" + section.start + "-" + section.end))
            & (this.coursesSelected.includes(section.name))){
                var index = this.sectionsSelected.indexOf(section)
                if (index > -1) {
                    this.sectionsSelected.splice(index, 1)
                }

                var index = this.timesSelected.indexOf(""+ section.days + "-" + section.start + "-" + section.end)
                if (index > -1) {
                    this.timesSelected.splice(index, 1)
                }
            }
        },

        isConflicted(section){
            let boolean = false
            //WILL FIX THIS INTO ACTUALLY CHECKING FOR SCHEDULE CONFLICTS
            this.timesSelected.forEach(time => {
                if((""+ section.days + "-" + section.start + "-" + section.end) == time){
                    boolean = true
                }
            })
            return boolean
        },

        isSelected(section){
            let boolean = false

            this.sectionsSelected.forEach(aSection =>{
                if(aSection == section){
                    boolean = true
                }
            })
            return boolean
        }
    },
    computed: {
  
    },

    created(){
        eventBus.$on('courseAdded', (coursesAdded)=>{
            this.coursesAdded = coursesAdded;
        });
    }


}
</script>

<style>

#titles{
    display:flex;
    /* width: 100vw; */
    justify-content: center;
    justify-items: center;
    align-items: center;
}


h3{
    justify-self: center;
    align-self: center;
    text-align: center;
}

#button-section{
    background-color: #f8f9fa;
    border-color: #007bff;
    border-radius: 8px;
    padding: 5px;
    margin: 2px;
}



#button-section:hover{    
    transform: translateY(-0.8px);
    box-shadow: 0 7px 14px rgba(50, 50, 93, 0.1), 0 3px 6px rgba(0, 0, 0, 0.08);
}



.section{
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;

    align-content: center; 
     justify-items: center; 
     justify-content: center;
}

#x{
    font-weight: bold;
    border-radius: 50%;
    max-height: 3.5vh;
    max-width: 3.5vh;
    display: flex;
    align-items: center;
    justify-content: center;    

}
#x:hover{
    transform: translateY(-0.8px);
    box-shadow: 0 7px 14px rgba(50, 50, 93, 0.1), 0 3px 6px rgba(0, 0, 0, 0.08);
}

.course{
    width: 100%;
    display: flex;
    align-items: center;

}

.course-title{
    display: flex;

    align-items: center;

}
</style>