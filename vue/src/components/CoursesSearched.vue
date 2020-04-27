<template>
    <section id="courses-searched">
        <div class="course" v-for="(course, index) in courses.slice(0,10)" :key="index" >
            <button
                @click="courseAdded(course)"> 
            +
            </button>

            <div v-if="course.show" class= "course-name">
                <div 
                    id="course-name"  
                    v-if="course.show">
                {{course.courseNum}} - {{course.name}} 
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import db from '../firebaseinit.js'
import {eventBus} from '../main'

export default {
    data() {
        return {
            courses: [],
            coursesAdded: []
        }
    },

    methods: {
        courseAdded(course){
            if(!(this.coursesAdded.includes(course))){
                this.coursesAdded.push(course)
                console.log("IN COURSES SEARCHED")
                eventBus.displayCourse(this.coursesAdded)

            }
        }

    },

    created() { 
    // get data from database and save it temporarily in Vue. 
    // This includes all data (courses and their sections)
        
        // 
        db.collection('fall20').get().then
        (querySnapshot => {
            querySnapshot.forEach(course => {
                const sections = []
                course.data().sections.forEach(section => {
                    const aSection = {
                        'name': course.data().name,
                        'numsection': section.numsection,
                        'days': section.days,
                        'start': section.start,
                        'end': section.end,
                        'instructor': section.instructor,
                    }
                    sections.push(aSection)
                    }        
                )
                const data = {
                    'courseNum': course.id, 
                    'name': course.data().name,
                    'sections': sections,
                    show: true,

                }
            this.courses.push(data)
    
            })
            })        
    },
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