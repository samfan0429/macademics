<template>
    <div>
        <input type="text" v-model="input">
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

</style>