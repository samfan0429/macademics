<template>
    <section id="courses-searched">
        <!-- <div id="course" v-for="(course, index) in courses.slice(0,10)" :key="index" v-if="course.show"> -->
        <div  
        v-for="i in 10" :key="i"  >
            <div 
            class="course" 
            v-if="courses[i].name != courses[i-1].name">
                <button 
                    v-if="courses[i].show"
                    @click="courses[i].show=!courses[i].show">
                X
                </button>

                <div 
                    id="course-name"  
                    v-if="courses[i].show">
                {{courses[i].numsection}} - {{courses[i].name}} 
                </div>

                <button>{{courses[i].days}} - {{courses[i].time}}</button>
            </div>
            
            <!-- <button v-else>{{courses[i].days}} - {{courses[i].time}}</button> -->
        </div>
        <div 
            class="sections">
                <button
                    v-for="i in 10" 
                    :key="i"
                    v-if="courses[i].name == courses[i-1].name">
                {{courses[i].days}} - {{courses[i].time}}</button>
        </div>

    </section>
</template>

<script>
import db from './firebaseinit.js'
export default {
    data() {
        return {
            courses: []
        }
    },
    created() {
        db.collection('spring20').get().then
        (querySnapshot => {
            querySnapshot.forEach(document => {
                const data = {
                    'numsection': document.data().numsection.slice(0,-3),
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
.course, .sections{
    display: flex;
    padding: 10px
}

#course-name{
    padding-left: 10px;
    padding-right: 10px;
}
</style>