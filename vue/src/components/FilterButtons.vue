<template>
  <div class="filterButtons btn-group btn-group-toggle container">
    <div class="row">
      <div class='col-3'>
        <button 
          v-for="n in 3"
          :key="n"
          id="button"
          class="btn btn-outline-success"
          :class = "{'btn-success': isSelected(distributions[n-1])}"
          @click = distChosen(distributions[n-1])>
            {{buttonsNames[n-1]}}
        </button>
      </div>
      <div class='col-3'>
        <button 
          v-for="n in 3"
          :key="n+3"
          id="button"
          class="btn btn-outline-success"
          :class = "{'btn-success': isSelected(distributions[n+3-1])}"
          @click = distChosen(distributions[n+3-1])>
            {{buttonsNames[n+3-1]}}
        </button>
      </div>
      <div class='col-3'>
        <button 
          v-for="n in 3"
          :key="n+6"
          id="button"
          class="btn btn-outline-success"
          :class = "{'btn-success': isSelected(distributions[n+6-1])}"
          @click = distChosen(distributions[n+6-1])>
            {{buttonsNames[n+6-1]}}
        </button>
      </div>
      <div class='col-3'>
        <button 
          v-for="n in 3"
          :key="n+9"
          id="button"
          class="btn btn-outline-success"
          :class = "{'btn-success': isSelected(distributions[n+9-1])}"
          @click = distChosen(distributions[n+9-1])>
            {{buttonsNames[n+9-1]}}
        </button>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  data(){
    return {
        // distribution:"Unclicked",
      distAdded: [],
      distributions: ["Writing WA", "Writing WP", "Writing WC", "U.S. Identities and Differences", "Internationalism", 
        "Humanities", "Social science", "Fine arts", "Natural science and mathematics","Quantitative Thinking Q1", 
        "Quantitative Thinking Q2", "Quantitative Thinking Q3"],
      buttonsNames: ["WA","WP","WC", "USID", "INTL", "HUM", "SS", "ARTS", "NS","Q1", "Q2", "Q3"]
    }
  },

  methods: {
    isSelected(distribution){
      let boolean = false
      this.distAdded.forEach(aDist =>{
        if(aDist == distribution){
          boolean = true
        }
      })
      return boolean
    },
    distChosen(distribution){
      if(!(this.distAdded.includes(distribution))){
        this.distAdded.push(distribution)
        this.$emit('distSelected', distribution);

      }
      else{
        var index = this.distAdded.indexOf(distribution)
        if (index > -1) {
          this.distAdded.splice(index, 1)                
        }
        this.$emit('distUnselected', this.distAdded);

      }


    }
  }
}
</script>

<style scoped>
  .green{
    background-color: green;
  }

  #button{
    border-radius: 24px;
    width: 7vw;
  }
</style>