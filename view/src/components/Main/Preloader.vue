<template>
    <div class="main-preloader" v-if="isVisible">
        <span class="preloader-label">
            Loading...
        </span>
    </div>
</template>

<script>
export default {
    props: {
        isVisible: {
            type: Boolean,
            default: false
        }
    }
}
</script>

<style scoped>
.main-preloader {
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.2);
    z-index: 1000;

    position: absolute;
    top: 0;
    left: 0;

    display: flex;
    justify-content: center;
    align-items: center;
}

.preloader-label {
    font-size: 68px;
    color: aliceblue;
    padding-bottom: 130px;
}
</style>