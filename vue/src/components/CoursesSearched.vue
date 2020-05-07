<template>
    <section id="search" class="container">
        <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet"/>
        <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css" rel="stylesheet"/>
        
        
        <div class='title-bar row'>    
                    <div class="p-1 bg-light rounded rounded-pill shadow-sm mb-4 input-group col-8" id="searchbar-portion">
                        <div class="input-group-append">
                            <button id="button-addon1" class="btn btn-link text-primary">
                                <i class="fa fa-search"></i>
                            </button>
                        </div>
                        
                        <input 
                            type="text" 
                            placeholder="Search here for courses!" 
                            aria-describedby="button-addon1" 
                            class="shadow-none form-control border-0 bg-light"
                            id='search-bar'
                            v-model="input" 
                            v-on:keyup.enter="searchTermEntered(input)">
                        
            </div>

            <filter-buttons class="col"
            @distSelected="distSelect($event)"
            @distUnselected="distUnselect($event)">
            </filter-buttons>
        </div>
        <div id="courses-searched" class='row'>
        <table class="table table-hover table-striped ">
            <tbody>
            <tr class="course" v-for="(course, index) in courses" :key="index" >
                
                <button
                    class="btn btn-success"
                    id="add"
                    @click="courseAdded(course)"> 
                Add
                </button>

                <div class= "course-name">
                    <div 
                        id="course-name"  
                    >
                    <b>{{course.courseNum}}</b> - {{course.name}} 
                    </div>
                </div>
            </tr>
            </tbody>
        </table>
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
            tempSearchCourses: [],
            tempFilterCourses: [],
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
            var newCourses = this.courses.filter(course =>
                course.distributions.includes(distribution)
            )     

            this.courses = []
            newCourses.forEach(course => {
                this.courses.push(course)
            })

            this.tempFilterCourses = []
            this.courses.forEach(course => {
                this.tempFilterCourses.push(course)
            })
        },

        distUnselect(distributionsSelected){
            this.courses = []
            if(distributionsSelected.length == 0){
                this.tempFilterCourses = []
                this.allCourses.forEach(course => {
                    this.tempFilterCourses.push(course)
                })
            }
            if(this.tempSearchCourses.length == 0){
                this.allCourses.forEach(course => {
                this.courses.push(course)
                })
                var i
                for (i=0; i < distributionsSelected.length; i++){
                    this.distSelect(distributionsSelected[i])
                }
            }
            else{
                this.tempSearchCourses.forEach(course => {
                this.courses.push(course)
                })
                var i
                for (i=0; i < distributionsSelected.length; i++){
                    this.distSelect(distributionsSelected[i])
                }
            }
            
        },

        searchTermEntered(input){
            this.courses = []
            if(this.tempFilterCourses.length==0){
                if(input.length == 0){
                    this.allCourses.forEach(course => {
                        this.courses.push(course)
                    })
                    this.tempSearchCourses = []
                }
                else{
                    this.allCourses.forEach(course => {
                        if((course.courseNum.includes(input.toUpperCase())) ||
                            (course.name.toLowerCase().includes(input.toLowerCase())) 
                            // || (course.sections.forEach(section => {
                            //     if(section.instructor.toLowerCase().includes(input.toLowerCase())){
                            //         console.log(section.instructor.toLowerCase())
                            //         return true

                            //     }
                            // }))
                        ){
                            this.courses.push(course)
                        }
                    })
                    this.tempSearchCourses = []
                    this.courses.forEach(course => {
                        this.tempSearchCourses.push(course)
                    })
                }

            }
            else{
                if(input.length == 0){
                    this.tempFilterCourses.forEach(course => {
                        this.courses.push(course)
                    })
                    this.tempSearchCourses = []
                }
                else{
                    this.tempFilterCourses.forEach(course => {
                        if((course.courseNum.includes(input.toUpperCase())) ||
                            (course.name.toLowerCase().includes(input.toLowerCase())) 
                            // || (course.sections.forEach(section => {
                            //     if(section.instructor.toLowerCase().includes(input.toLowerCase())){
                            //         console.log(section.instructor.toLowerCase())
                            //         return true

                            //     }
                            // }))
                        ){
                            this.courses.push(course)
                        }
                    })
                    this.tempSearchCourses = []
                    this.courses.forEach(course => {
                        this.tempSearchCourses.push(course)
                    })
                }

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
  @media screen and (max-width: 850px) {
    .title-bar {
        display: block;
    }
  }
.course{
    align-items: center;
    
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

#searchbar-portion{
    display: flex;
    height: 5vh;
    align-content: center;
    align-self: center;

}

#add{
    font-weight: bold;
}

#add:hover{
    transform: translateY(-0.8px);
    box-shadow: 0 7px 14px rgba(50, 50, 93, 0.1), 0 3px 6px rgba(0, 0, 0, 0.08);
}
</style>