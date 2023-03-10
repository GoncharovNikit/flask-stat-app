<template>
    <nav>
        <div class="nav-item">
            <button id="mystat-json" @click="$router.push('/mystat/json')">Mystat Json</button>
        </div>
        <div class="nav-item">
            <button id="mystat-table" @click="$router.push('/mystat/expenses/chart')">Expenses Chart</button>
        </div>
        <div class="nav-item">
            <button id="expenses-chart" @click="$router.push('/mystat/table')">Mystat Table</button>
        </div>
    </nav>
</template>

<script>
export default {

}
</script>

<style scoped>
nav {
    height: 15vh;
    width: 100%;

    background-color: beige;
    border: 3px solid black;
    padding: 0 100px;

    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}
nav .nav-item {
    display: flex;
    flex-direction: column;
    row-gap: 2px;
    width: 260px;
}
.nav-item button {
    width: 100%;

    border: 3px solid black;
    border-radius: 4px;
    background-color: black;

    padding: 10px 14px;
    font-size: 22px;
    color: whitesmoke;

    cursor: pointer;
}
</style>
