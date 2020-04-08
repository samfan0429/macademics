<template>
    <section id="courses-searched">
        <div class="course" v-for="(course, index) in courses.slice(0,10)" :key="index" >
            <button 
                @click="course.show=!course.show">
            X
            </button>

            <div v-if="course.show" class= "course">
                <div 
                    id="course-name"  
                    v-if="course.show">
                {{course.numsection.slice(0,-3)}} - {{course.name}} 
                </div>

                <button @click="sectionSelected(course)">{{course.days}} - {{course.time}}</button>
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
            sectionsSelected: []
        }
    },

    methods: {
        sectionSelected(course){
            if(!(this.sectionsSelected.includes(course))){
                this.sectionsSelected.push(course);
                eventBus.displaySection(this.sectionsSelected);
            }
        }
    },
    created() {
        db.collection('spring20').get().then
        (querySnapshot => {
            querySnapshot.forEach(document => {
                const data = {
                    'numsection': document.data().numsection,
                    'name': document.data().name,
                    'days': document.data().days,
                    'time': document.data().time,
                    show: true
                }
                this.courses.push(data)
            });
        })
    }
};
</script>

<style>
.course{
    display: flex;
    padding: 10px
}

#course-name{
    padding-left: 10px;
    padding-right: 10px;
}
</style>