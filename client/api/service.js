const Api = {
  baseURL: null,
  init (url) {
    this.baseURL = url
  },

  getAllQuestions () {
    return new Promise((resolve, reject) => {
      fetch(`${this.baseURL}/questions`).then(response => {
        response.json().then(questions => {
          resolve(questions)
        })
      })
    })
  },

  getRoom (name, password) {
    return new Promise((resolve, reject) => {
      let formData = new URLSearchParams()
      formData.append('password', password)
      fetch(`${this.baseURL}/room/${name}`, {
        method: 'POST',
        body: formData,
        headers: { 'Content-type': 'application/x-www-form-urlencoded' }
      }).then(response => {
        if (response.status !== 200) {
          reject(response.status)
        } else {
          response.json().then(room => { resolve(room) })
        }
      })
    })
  },

  createRoom (name, password) {
    name = name.trim()
    let formData = new URLSearchParams()
    formData.append('name', name)
    formData.append('password', password)

    return new Promise((resolve, reject) => {
      fetch(`${this.baseURL}/room/add`, {
        method: 'POST',
        body: formData,
        headers: { 'Content-type': 'application/x-www-form-urlencoded' }
      }).then(response => {
        if (response.status !== 201) {
          reject(Error('Room already exists'))
        } else {
          response.json().then(room => { resolve(room) })
        }
      })
    })
  },

  submitPredictions (room, roomPassword, userName, predictions) {
    room = room.trim()
    userName = userName.trim()
    let formData = new URLSearchParams()
    formData.append('password', roomPassword)
    formData.append('name', userName)
    formData.append('predictions', predictions)

    return new Promise((resolve, reject) => {
      fetch(`${this.baseURL}/room/${room}/user/add`, {
        method: 'POST',
        body: formData,
        headers: { 'Content-type': 'application/x-www-form-urlencoded' }
      }).then(response => {
        if (response.status !== 201) {
          reject(Error('Error sending predictions'))
        } else {
          response.json().then(room => { resolve(room) })
        }
      })
    })
  }
}

export default Api
