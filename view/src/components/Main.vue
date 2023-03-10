<template>
    <main>
        <Preloader :isVisible="preloaderVisible" />
        <router-view 
            @data-loading="preloaderVisible=true" 
            @data-loaded="preloaderVisible=false">
        </router-view>
    </main>
</template>

<script>
import Preloader from './Main/Preloader.vue'

export default {
    components: {
        Preloader
    },
    data() {
        return {
            preloaderVisible: false,
        }
    },
}
</script>

<style scoped>
main {
    width: 100%;
    border: 3px solid black;
    height: 85vh;
    overflow-y: auto;
    padding: 45px;
    font-size: 18px;
}
</style>