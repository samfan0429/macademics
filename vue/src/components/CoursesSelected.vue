<template>
    <section id="courses-selected">
        <div id="titles">
            <h1 id="titleLeft">Courses Selected</h1>
            <h1 id="titleRight">Available Sections</h1>
        </div>
        
        <div class="course" v-for="(course, index) in coursesAdded" :key="index">
            <div v-if="course.show" class= "course">
                <button 
                @click="course.show=!course.show">
                    X
                </button>
                <div 
                    id="course-name"  
                    v-if="course.show">
                {{course.courseNum}} - {{course.name}} 
                </div>
            <!-- </div> -->
                <div class="section" v-for="(section, index) in course.sections" :key="index">
                    <button 
                    @click="sectionSelected(section)"
                    :class = "{gray: isConflicted(section)}">
                    <!-- listen to the emitted event and call isConflicted? -->
                        {{section.days}} - {{section.start}} - {{section.end}}
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
            // if(this.coursesSelected.includes(section.name)){
            //     this.sectionsSelected.push(section)
            //     this.timesSelected.push(""+ section.days + "-" + section.start + "-" + section.end)
            //     eventBus.displaySection(this.sectionsSelected, this.timesSelected, this.coursesSelected)

            // }
            
            // TODO: 
            // send a warning saying the time of the section the user is selecting conflict with 
            // a section already added to coursesSummary
            // if(this.timesSelected.includes(""+ section.days + "-" + section.start + "-" + section.end))){
            //    *send the warning*
            //}

            else{
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

            this.coursesSelected.forEach(courseSelected =>{
                if(courseSelected == section.name){
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
.course{
    display: flex;
    padding: 10px
}

#titles{
    display:flex;
    width: 100vw;

}

#titleLeft{
    width:40vw;
    text-align: left;
}

#titleRight{
    width: 40vw;
    text-align: right;
}
h1{
    padding-left: 10px;
    padding-right: 10px
}

.gray{
    color: gray;
}

#course-name{
    padding-left: 10px;
    padding-right: 10px;
}
</style>