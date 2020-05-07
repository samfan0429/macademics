<template>
  <div class="filterButtons">
    <button 
      v-for="n in 12"
      :key="n"
      id="button"
      :class = "{green: isSelected(distributions[n-1])}"
      @click = distChosen(distributions[n-1])>
        {{buttonsNames[n-1]}}
    </button>
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
</style>