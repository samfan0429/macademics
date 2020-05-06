<template>
  <div class="filterButtons">
    <button 
      v-for="n in 12"
      :key="n"
      id="button"
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
    distChosen(distribution){
      if(!(this.distAdded.includes(distribution))){
        this.distAdded.push(distribution)
      }
      else{
        var index = this.distAdded.indexOf(distribution)
        if (index > -1) {
          this.distAdded.splice(index, 1)                
        }
      }

      this.$emit('distClicked', this.distAdded);

    }
  }
}
</script>

<style scoped>
  #b1{
    position: absolute;
    color: whitesmoke;
    background-color: indigo;
    margin : 5px;
    width: 100px;
    height: 33px;
    top: 5%;
    left: 77%;
  }
  #b2{
    position: absolute;
    color: whitesmoke;
    background-color: indigo;
    margin : 5px;
    width: 100px;
    height: 33px;
    top: 5%;
    left: 82%;
  }
  #b3{
    position: absolute;
    color: whitesmoke;
    background-color: indigo;
    width: 100px;
    height: 33px;
    margin : 5px;
    top: 5%;
    left: 87%;
  }
  #b4{
    position: absolute;
    color: whitesmoke;
    background-color: indigo;
    margin : 5px;
    width: 100px;
    height: 33px;
    top: 5%;
    left: 92%;
  }
  #b5{
    position: absolute;
    color: whitesmoke;
    background-color: indigo;
    margin : 5px;
    width: 100px;
    height: 33px;
    top: 10%;
    left: 77%;
  }
  #b6{
    position: absolute;
    color: whitesmoke;
    background-color: indigo;
    margin : 5px;
    width: 100px;
    height: 33px;
    top: 10%;
    left: 82%;
  }
  #b7{
    position: absolute;
    color: whitesmoke;
    background-color: indigo;
    margin : 5px;
    width: 100px;
    height: 33px;
    top: 10%;
    left: 87%;
  }
  #b8{
    position: absolute;
    color: whitesmoke;
    background-color: indigo;
    margin : 5px;
    width: 100px;
    height: 33px;
    top: 10%;
    left: 92%;
  }
  #b9{
    position: absolute;
    color: whitesmoke;
    background-color: indigo;
    margin : 5px;
    width: 100px;
    height: 33px;
    top: 15%;
    left: 77%;
  }
  #b10{
    position: absolute;
    color: whitesmoke;
    background-color: indigo;
    margin : 5px;
    width: 100px;
    height: 33px;
    top: 15%;
    left: 82%;
  }
  #b11{
    position: absolute;
    color: whitesmoke;
    background-color: indigo;
    margin : 5px;
    width: 100px;
    height: 33px;
    top: 15%;
    left: 87%;
  }
  #b12{
    position: absolute;
    color: whitesmoke;
    background-color: indigo;
    margin : 5px;
    width: 100px;
    height: 33px;
    top: 15%;
    left: 92%;
  }
</style>