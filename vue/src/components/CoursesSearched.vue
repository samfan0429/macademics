<template>
    <section id="search">
        <div class='title-bar'>
            <input 
                id='search-bar' type="text" 
                v-model="input" 
                v-on:keyup.enter="searchTermEntered(input)"
                >
            <filter-buttons
            @distSelected="distSelect($event)"
            @distUnselected="distUnselect($event)">
            </filter-buttons>
        </div>
        <div id="courses-searched">
            <div class="course" v-for="(course, index) in courses" :key="index" >
                <button
                    @click="courseAdded(course)"> 
                Add
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
import FilterButtons from './FilterButtons.vue'
import db from '../firebaseinit.js'
import {eventBus} from '../main'
import firebase from 'firebase'
import 'firebase/firestore'

export default {
    components: {
        'filter-buttons': FilterButtons,
    },

    data() {
        return {
            courses: [],
            allCourses: [],
            coursesAdded: [],
            input: ""
        }
    },

    methods: {
        courseAdded(course){
            if(!(this.coursesAdded.includes(course))){
                this.coursesAdded.push(course)
                course.show = true
                eventBus.displayCourse(this.coursesAdded)
            }
        },

        distSelect(distribution){
            // if (distributionsSelected.length > 0){
                // var i
                // for (i=0; i < distributionsSelected.length; i++){
                var newCourses = this.courses.filter(course =>
                    course.distributions.includes(distribution)
                )     
                    // }
                this.courses = []
                newCourses.forEach(course => {
                    this.courses.push(course)
                })
                console.log(this.courses.length)
                
            // }
            // else{
            //     this.courses = []
            //     this.allCourses.forEach(course => {
            //         this.courses.push(course)
            //     })
            // }   
        },

        distUnselect(distributionsSelected){
            // if (distributionsSelected.length > 0){
            this.courses = []
            this.allCourses.forEach(course => {
                this.courses.push(course)
            })
            var i
            for (i=0; i < distributionsSelected.length; i++){
                console.log(this.courses.length)
                console.log("AAA")

                this.distSelect(distributionsSelected[i])
            }
        
            // distSelect(distributionsSelected)                
            // if (distributionsSelected.length > 0){
            //     this.courses = []
            //     this.allCourses.forEach(course => {
            //         this.courses.push(course)
            //     })                
            //     var i
            //     var newCourses = []
            //     for (i=0; i < distributionsSelected.length; i++){
            //         var filterCourses = this.courses.filter(course =>
            //         course.distributions.includes(distributionsSelected[i])
            //         )
            //         filterCourses.forEach(course => {
            //             newCourses.push(course)
            //         })
            //     }
            //     this.courses = []
            //     newCourses.forEach(course => {
            //         this.courses.push(course)
            //     })  
            // }
            // else{
            //     this.courses = []
            //     this.allCourses.forEach(course => {
            //         this.courses.push(course)
            //     })
            // }
        },

        searchTermEntered(input){
            this.courses = []
            if(input.length == 0){
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
                            'distributions': course.data().distrbutions,
                            show: true,

                        }
                    this.courses.push(data)
            
                })
                })
            }
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
                            'distributions': course.data().distrbutions,
                            show: true,

                        }
                    this.courses.push(data)
            
                    })
                    })   
            } 
            else{
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
                            'distributions': course.data().distrbutions,
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
                    'distributions': course.data().distrbutions,
                    show: true,

                }
            this.courses.push(data)
            this.allCourses.push(data)
    
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

.title-bar{
    display:flex;
}

#search-bar{
    display: block;
    margin : 0% 0% 0% 0%;

    width: 50%;
    padding: 1%;
    border: 2px solid #dfe1e5;

    border-radius: 24px;
    outline: none;
}
</style>