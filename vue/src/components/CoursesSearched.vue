<template>
    <section id="search">
        <input id='search-bar' type="text" v-model="input" v-on:keyup.enter="searchTermEntered(input)">

        <div id="courses-searched">
            <div class="course" v-for="(course, index) in courses" :key="index" >
                <button
                    @click="courseAdded(course)"> 
                +
                </button>

                <div class= "course-name">
                    <div 
                        id="course-name"  
                    >
                    {{course.courseNum}} - {{course.name}} 
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import db from '../firebaseinit.js'
import {eventBus} from '../main'
import firebase from 'firebase'
import 'firebase/firestore'

export default {

    data() {
        return {
            courses: [],
            coursesAdded: [],
            input: ""
        }
    },

    methods: {
        courseAdded(course){
            if(!(this.coursesAdded.includes(course))){
                this.coursesAdded.push(course)
                eventBus.displayCourse(this.coursesAdded)
            }
        },

        searchTermEntered(input){
            console.log(this.input)
            this.courses = []
            if(input.length <= 4){
                db.collection('fall20').where("dept", "==",input.toUpperCase())
                .get().then
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
            } 
            else{
                console.log("NAME OF COURSE ENTERED")
                db.collection('fall20').where(firebase.firestore.FieldPath.documentId(), "==",input.toUpperCase())
                .get().then
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
            }


            

        }

    },

    created() { 
    // get data from database and save it temporarily in Vue. 
    // This includes all data (courses and their sections)
        
        // .where("dept", "==", "LING") before .get
        db.collection('fall20')
        .get().then
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

#courses-searched{
    overflow-y: auto;
    max-height: 40vh;
}

#search-bar{
    display: block;
    margin : 0% 0% 0% 5%;

    width: 50%;
    padding: 1%;
    border: 2px solid #dfe1e5;

    border-radius: 24px;
    outline: none;
}
</style>