<template>
    <div>
        <button @click="show = !show">X</button>
        <div v-if="show">Blablabla</div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            show: true
        }
    }

};
</script>

<style>

</style>