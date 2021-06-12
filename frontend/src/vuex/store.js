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
        },

        setProfile(state, profileData) {
            if (state.user.profile) {
                state.user.profile = { ...state.user.profile, ...profileData };
            } else {
                state.user.profile = profileData;
            }

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
            const tasks = await axios.get('api/tasks/no-completed/')

            commit('setTasks', tasks.data)
        },

        async getTask(_, id) {
            const task = await axios.get(`api/tasks/${id}/`)
            return task.data
        },

        async getTasksCompleted({ commit }) {
            const tasksCompleted = await axios.get('/api/tasks/completed/')

            commit('setProfile', { tasksCompleted: tasksCompleted.data })

            return tasksCompleted.data
        },

        async sendAnswer(_, answerData) {
            await axios.patch('/api/user/task_in_user_update/', answerData)
        },

        async getProfile(_, username) {
            const profile = await axios.get(`/api/user/${username}`)

            return profile.data
        },

        async updateProfile({ commit }, payload) {
            const data = await axios.patch(`/api/user/${this.state.user.profile.username}/`, payload)

            commit('setProfile', data.data);
        },

        async getMyProfile({ commit }) {
            const profile = await axios.get(`/api/user/profile/`)

            commit('setUser', { profile: profile.data })
        },

        async getConfrimEmail(_, payload) {
            console.log(payload)
            await axios.post('/auth/users/activation/', { uid: payload.uid, token: payload.token })
        }
    },

    getters: {
        leadersTable: state => state.leadersTable,
        tasks: state => state.tasks,
        profile: state => state.user.profile,
        tasksCompleted: state => state.user.profile.tasksCompleted
    }
})

export default store;