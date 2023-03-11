<template>
    <form @submit.prevent>
        <span class="error-message" v-if="error">{{ error }}</span>
        <br><br>
        <label for="email">Email: </label>
        <input type="text" name="email" id="email" v-model="email" />
        <br /><br />
        <label for="password">Password: </label>
        <input type="text" name="password" id="password" v-model="password" />
        <br>
        <button type="button" @click="sendLoginRequest">Submit</button>
    </form>
</template>

<script>
import axios from "axios"

export default {
    data() {
        return {
            email: "fawef",
            password: "fawe",
            error: ""
        }
    },
    methods: {
        sendLoginRequest() {
            console.log(this.email, this.password);
            axios.post("http://127.0.0.1:5000/auth/register", {
                email: this.email.toLowerCase(),
                password: this.password
            }, {
                headers: {
                    "Access-Control-Allow-Origin": "*"
                },
                withCredentials: false
            }).then((resp) => {
                console.log(resp)
                
            }).catch((error) => {
                const resp = error.response.data
                if (resp.error) {
                    this.error = resp.message
                    setTimeout(() => { this.error = "" }, 1000)
                }
            })
        },
    },
}
</script>

<style scoped>
.error-message {
    border: 1px solid darkred;
    padding: 4px 7px;
    color: darkred;
    font-size: 18px;
}
</style>