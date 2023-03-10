<template>
    <pre>
{{ jsonContent }}
    </pre>
</template>

<script>
import axios from "axios"

export default {
    data() {
        return {
            jsonContent: "",
        }
    },
    methods: {
        loadJson() {
            let isDataLoaded = false
            setTimeout(() => { if (!isDataLoaded) this.$emit('data-loading') }, 100)

            axios.get("http://127.0.0.1:5000/mystat/json")
                .then((response) => {
                    console.log(response);
                    this.jsonContent = JSON.stringify(response, undefined, 4)
                    isDataLoaded = true
                    this.$emit('data-loaded')
                })
        },
    },
    mounted() {
        this.loadJson()
    },
}
</script>
