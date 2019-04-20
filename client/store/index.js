
import Vue from 'vue'
import Vuex from 'vuex'
import Api from '../api/service.js'

Vue.use(Vuex)

const API_URL = '/api'
Api.init(API_URL)

export default new Vuex.Store({
  state: {
    api: Api,
    questions: {
      'character_fates': {},
      'yes_no_questions': {},
      'character_choices': {}
    },
    characters: [],
    currentRoom: { name: null }
  },
  mutations: {
    setRoomPassword (state, payload) {
      window.localStorage.setItem(payload.name, payload.password)
    },
    setCurrentRoom (state, room) {
      if (room) {
        state.currentRoom = room
      } else {
        state.currentRoom = { name: null }
      }
    }
  },
  actions: {
    updateRoom (context, name) {
      return new Promise((resolve, reject) => {
        context.dispatch('getRoom', name).then(room => {
          context.commit('setCurrentRoom', room)
          resolve()
        }).catch(_ => {
          reject(Error('Can\'t connect to room'))
        })
      })
    },
    getRoom (context, name) {
      let password = context.getters['getRoomPassword'](name)
      return context.state.api.getRoom(name, password)
    },
    fetchQuestions ({ state }) {
      Api.getAllQuestions().then(questions => {
        state.questions = questions
        state.characters = Object.values(questions['character_fates']).map(q => q.text)
      })
    }
  },
  getters: {
    getRoomPassword: (state) => (roomName) => {
      return window.localStorage.getItem(roomName)
    }
  }
})
