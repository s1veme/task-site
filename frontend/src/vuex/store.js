import { createStore } from 'vuex'
import axios from 'axios'

let store = createStore({
    state() {
        return {
            user: {
                token: localStorage.getItem('token') || '',
            },

            leadersTable: [],

            tasks: []
        }
    },

    mutations: {
        setUser(state, userData) {
            if (state.user) {
                state.user = { ...state.user, ...userData }
            } else {
                state.user = userData
            }
        },

        setLeadersTable(state, table) {
            if (state.leadersTable !== table) {
                state.leadersTable = table
            }
        },

        setTasks(state, tasks) {
            state.tasks = tasks
        }
    },

    actions: {
        async createToken({ commit }, user) {
            const tokenData = await axios.post('api/user/token-create/', user)

            if (tokenData.data.token) {
                axios.defaults.headers[
                    "Authorization"
                ] = `Bearer ${tokenData.data.token}`;
                localStorage.setItem('token', tokenData.data.token)

                commit('setUser', tokenData.data.token)
            }
        },

        async createUser(_, user) {
            await axios.post("/auth/users/", user);
        },

        async getLeadersTable({ commit }) {
            const leadersTable = await axios.get('api/infomrmation/leaders/')

            commit('setLeadersTable', leadersTable.data)
        },

        async getTasks({ commit }) {
            const tasks = await axios.get('api/task/tasks/')

            commit('setTasks', tasks.data)
        },

        async getTask(_, id) {
            const task = await axios.get(`api/task/tasks/${id}/`)
            return task.data
        },

        async sendAnswer(_, answerData) {
            await axios.patch('/api/user/task_in_user_update/', answerData)
        }
    },

    getters: {
        leadersTable: state => state.leadersTable,
        tasks: state => state.tasks
    }
})

export default store;