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

  getRoom (name) {
    return new Promise((resolve, reject) => {
      fetch(`${this.baseURL}/room/${name}`).then(response => {
        if (response.status !== 200) {
          reject(Error('Room not Found'))
        } else {
          response.json().then(room => { resolve(room) })
        }
      })
    })
  }
}

export default Api
