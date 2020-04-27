<template>
    <section id="courses-selected">
        <div class="course" v-for="(course, index) in coursesAdded" :key="index" >
            <button 
                @click="course.show=!course.show">
            X
            </button>

            <div v-if="course.show" class= "course-name">
                <div 
                    id="course-name"  
                    v-if="course.show">
                {{course.courseNum}} - {{course.name}} 
                </div>
            </div>
            <div class="section" v-for="(section, index) in course.sections" :key="index">
                <button 
                @click="sectionSelected(section)"
                :class = "{gray: isConflicted(section)}"
                >
                    {{section.days}} - {{section.start}} - {{section.end}}
                </button>
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
        }
    },

    methods: {
        sectionSelected(section){
            if(!(this.sectionsSelected.includes(section))){
                this.sectionsSelected.push(section)
                eventBus.displaySection(this.sectionsSelected)
            }

            this.timesSelected.push(""+ section.days + "-" + section.start + "-" + section.end) 
            //WILL FIX THIS INTO ACTUALLY CHECKING FOR SCHEDULE CONFLICTS
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

.gray{
    color: gray;
}

#course-name{
    padding-left: 10px;
    padding-right: 10px;
}
</style>