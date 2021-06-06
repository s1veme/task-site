import { createStore } from 'vuex'
import axios from 'axios'

let store = createStore({
    state() {
        return {
            user: {
                token: localStorage.getItem('token') || '',
            },

            leadersTable: []
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
        }
    },

    actions: {
        async createToken({ commit }, user) {
            const tokenData = await axios.post('api/user/token-create/', user)

            if (tokenData.data.token) {
                axios.defaults.headers[
                    "Authorization"
                ] = `Bearer ${tokenData.data.token}`;

                commit('setUser', tokenData.data.token)
            }
        },

        async createUser(_, user) {
            await axios.post("/auth/users/", user);
        },

        async getLeadersTable({ commit }) {
            const leadersTable = await axios.get('api/infomrmation/leaders/')

            commit('setLeadersTable', leadersTable.data)
        }
    },

    getters: {
        leadersTable: state => state.leadersTable
    }
})

export default store;