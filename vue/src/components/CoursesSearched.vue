<template>
    <section id="courses-searched">
        <div id="course" v-for="(course, index) in courses.slice(0,4)" :key="index">
            <button @click="course.show=!course.show">X</button>

            <div id="course-name" v-if="course.show" >{{course.numsection}} - {{course.name}} </div>
            <button v-if="course.show">{{course.days}} - {{course.time}}</button>
        </div>
    </section>
</template>

<script>
import db from '/home/ngonhat352/CodingProjects/macademics/vue/src/firebaseinit.js'
export default {
    data() {
        return {
            courses: []
        }
    },

    created() {
        db.collection('spring20').orderBy('numsection').get().then
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

#course{
    display: flex;
    padding: 10px
}

#course-name{
    padding-left: 10px;
    padding-right: 10px;
}
</style>