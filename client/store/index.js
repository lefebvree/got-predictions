
import Vue from 'vue'
import Vuex from 'vuex'
import Api from '../api/service.js'

Vue.use(Vuex)

const API_URL = 'http://localhost/api'
Api.init(API_URL)

export default new Vuex.Store({
  state: {
    api: Api,
    questions: {
      'character_fates': {},
      'yes_no_questions': {},
      'character_choices': {}
    },
    characters: []
  },
  mutations: {
    toggleLoading (state) {
      state.loading = !state.loading
    }
  },
  actions: {
    fetchQuestions ({ state, commit }) {
      Api.getAllQuestions().then(questions => {
        state.questions = questions
        state.characters = Object.values(questions['character_fates']).map(q => q.text)
      })
    }
  }
})
