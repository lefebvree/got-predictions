
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const API_URL = 'http://localhost:5000'

export default new Vuex.Store({
  state: {
    loading: false,
    all_questions: {}
  },
  mutations: {
    toggleLoading (state) {
      state.loading = !state.loading
    }
  },
  actions: {
    fetchQuestions ({ state, commit }) {
      commit('toggleLoading')
      fetch(`${API_URL}/questions`).then(res => {
        res.data.json(questions => {
          state.all_questions = questions
        })
      })
    }
  }
})
