<template>
  <div>
    <div class="my-2 card panel-text">
      <h4>Join a room or create one</h4>
      <p>
        You can create a room to invite your friends and post your predictions or join an existing one
      </p>
      <div class="input-group col-9 col-md-12">
        <input v-model="roomName" class="form-input input-lg" :class="{ 'is-success': validRoom }"
               type="text" placeholder="Room" minlength="4" maxlength="25" ref="roomInput">
        <input v-model="roomPassword" class="form-input input-lg" :class="{ 'is-success': validPassword, 'is-error': roomExists && !validPassword }"
               type="text" placeholder="Password" minlength="1" maxlength="25" ref="roomPasswordInput">
        <button class="btn input-group-btn btn-lg text-right" @click="createRoom" :disabled="!validInput"
                :class="{ 'btn-success': validInput }">
          <div class="room-status hide-sm">{{ roomStatus }}</div>
          <arrow-right-circle-outline v-if="roomExists" class="mx-1"></arrow-right-circle-outline>
          <plus-circle-outline v-else class="mx-1"></plus-circle-outline>
        </button>
      </div>
    </div>
  </div>
</template>

<script>

import ArrowRightCircleOutline from 'vue-material-design-icons/ArrowRightCircleOutline.vue'
import PlusCircleOutline from 'vue-material-design-icons/PlusCircleOutline.vue'

export default {
  name: 'WelcomeScreen',
  data: function () {
    return {
      roomExists: false,
      validRoom: false,

      roomPassword: '',
      validPassword: false
    }
  },
  props: {
    roomName: String
  },
  methods: {
    getRoom: function () {
      this.$store.state.api.getRoom(this.roomName, this.roomPassword)
        .then(room => {
          this.roomName = room.name
          this.roomExists = true
          this.validPassword = true
        })
        .catch(returnCode => {
          if (returnCode === 404) {
            this.roomExists = false
          } else if (returnCode === 401) {
            this.roomExists = true
            this.validPassword = false
          }
        })
    },

    createRoom: function () {
      this.$store.state.api.createRoom(this.roomName, this.roomPassword)
        .then(room => {
          this.$store.commit('setRoomPassword', { 'name': room.name, 'password': this.roomPassword })
          this.$store.commit('setCurrentRoom', room)

          this.$router.push(`/${room.name}`)
        })
        .catch(_ => {
          this.roomExists = false
        })
    }
  },
  watch: {
    roomName: function () {
      this.roomName = this.roomName.replace(/[^a-z0-9+]+/gi, '')

      if (this.roomName) {
        this.validRoom = this.$refs.roomInput && this.$refs.roomInput.checkValidity()
      } else {
        this.validRoom = false
        this.roomExists = false
      }

      if (this.validRoom) this.getRoom()
    },

    roomPassword: function () {
      const validInput = this.$refs.roomPasswordInput && this.$refs.roomPasswordInput.checkValidity()
      if (!this.roomExists) this.validPassword = validInput
      if (this.roomExists && validInput) this.getRoom()
    }
  },
  computed: {
    roomStatus: function () {
      return this.roomExists ? 'Join' : 'Create'
    },
    validInput: function () {
      return this.validRoom && this.validPassword
    }
  },
  mounted () {
    if (this.roomName) {
      this.validRoom = this.$refs.roomInput && this.$refs.roomInput.checkValidity()
      if (this.validRoom) this.getRoom()
    }
  },
  components: {
    ArrowRightCircleOutline,
    PlusCircleOutline
  }
}
</script>

<style>
  .room-status {
    width: 3em;
    display: inline-block;
    text-align: center;
  }
</style>
