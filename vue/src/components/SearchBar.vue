<template>
    <div>
        <input id='search-bar' type="text" v-model="input">
        <div>{{input}}</div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            input: ""
        }
    }
};
</script>

<style>
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
