<template>
    <table v-if="mystatData.length" class="table">
        <thead>
            <tr>
                <th scope="col" v-for="fieldName in Object.keys(mystatData[0])">{{ fieldName }}</th>
            </tr>
        </thead>
        <tbody class="table-group-divider">
            <tr v-for="record in mystatData" :key="record.Date">
                <template v-for="(fieldValue, index) in Object.values(record)">
                    <th scope="row" v-if="index === 0">{{ fieldValue }}</th>
                    <td v-else>{{ fieldValue }}</td>
                </template>
            </tr>
        </tbody>
    </table>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            mystatData: []
        }
    },
    methods: {
        loadMystatData() {
            let isDataLoaded = false
            setTimeout(() => { if (!isDataLoaded) this.$emit('data-loading') }, 100)

            axios.get("http://127.0.0.1:5000/mystat/json?addSleepDuration=true")
                .then((response) => {
                    console.log(response.data);
                    window.mdata = response.data
                    this.mystatData = response.data
                    isDataLoaded = true
                    this.$emit('data-loaded')
                })
        }
    },
    mounted() {
        this.loadMystatData()
    },
    emits: ['data-loading', 'data-loaded']
}
</script>