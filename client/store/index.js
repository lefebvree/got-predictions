
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
    predictionAnswers: {
      'character_fates': {},
      'yes_no_questions': {},
      'character_choices': {}
    },
    characters: [],
    currentRoom: { name: null, users: [] },
    savedRooms: {}
  },
  mutations: {
    setRoomPassword (state, payload) {
      const roomName = payload.name.toLowerCase()
      state.savedRooms[roomName] = { 'password': payload.password }
    },

    setRoomName (state, payload) {
      const roomName = payload.name.toLowerCase()
      state.savedRooms[roomName]['userName'] = payload.userName
    },

    setCurrentRoom (state, room) {
      if (room) {
        state.currentRoom = room
      } else {
        state.currentRoom = { name: null }
      }
    },

    saveRooms (state) {
      const jsonRooms = JSON.stringify(state.savedRooms)
      if (jsonRooms) window.localStorage.setItem('saved_rooms', jsonRooms)
    },

    loadRooms (state) {
      const jsonRooms = window.localStorage.getItem('saved_rooms')
      if (jsonRooms) state.savedRooms = JSON.parse(jsonRooms)
    },

    setPredictionAnswer (state, payload) {
      state.predictionAnswers[payload.cat][payload.id] = payload.ans
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
      const password = context.state.savedRooms[name].password
      return context.state.api.getRoom(name, password)
    },

    submitPredictions (context, userName) {
      const predictionsJson = JSON.stringify(context.state.predictionAnswers)
      const password = context.state.savedRooms[context.state.currentRoom.name].password
      return context.state.api.submitPredictions(
        context.state.currentRoom.name, password, userName, predictionsJson
      )
    },

    fetchQuestions ({ state }) {
      Api.getAllQuestions().then(questions => {
        state.questions = questions
        state.characters = Object.entries(questions['character_fates']).map((c) => {
          return {
            'id': c[0],
            'name': c[1].text
          }
        })
      })
    }
  }
})
