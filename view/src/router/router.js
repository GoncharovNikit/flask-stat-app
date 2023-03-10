import { createRouter, createWebHistory } from 'vue-router'
import MystatJson from '@/components/Main/Pages/MystatJson.vue'
import MystatTable from '@/components/Main/Pages/MystatTable.vue'
import ExpensesChart from '@/components/Main/Pages/ExpensesChart.vue'
import Login from '@/components/Main/Pages/Login.vue'

const routes = [
    {
        path: '/mystat/json',
        component: MystatJson
    },
    {
        path: '/mystat/table',
        component: MystatTable
    },
    {
        path: '/mystat/expenses/chart',
        component: ExpensesChart
    },
    {
        path: '/login',
        component: Login
    }
]

export default createRouter({ routes, history: createWebHistory() })
