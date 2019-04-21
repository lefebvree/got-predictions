<template>
  <div>
    <div class="my-2 card panel-text">
      <h4><bookmark-plus-outline class="mr-1"></bookmark-plus-outline> Join a room or create one</h4>
      <p>
        You can create a room to invite your friends and post your predictions or join an existing one
      </p>
      <div class="input-group col-9 col-md-12">
        <input v-model="roomName" class="form-input input-lg" :class="{ 'is-success': validRoom }"
               type="text" placeholder="Room" minlength="4" maxlength="25" ref="roomInput"
               autocomplete="off" tabindex="1" v-on:input="roomName = $event.target.value" autofocus>
        <input v-model="roomPassword" class="form-input input-lg"
               :class="{ 'is-success': validPassword, 'is-error': roomExists && !validPassword }"
               type="text" placeholder="Password" minlength="1" maxlength="25" ref="roomPasswordInput"
               autocomplete="off" autocapitalize="none" tabindex="2" v-on:input="roomPassword = $event.target.value">
        <button class="btn input-group-btn btn-lg text-right" @click="createOrJoinRoom" :disabled="!validInput"
                :class="{ 'btn-success': validInput }"
                tabindex="3">
          <div class="room-status hide-sm">{{ roomStatus }}</div>
          <arrow-right-circle-outline v-if="roomExists" class="mx-1"></arrow-right-circle-outline>
          <plus-circle-outline v-else class="mx-1"></plus-circle-outline>
        </button>
      </div>
    </div>
    <div v-if="savedRooms.length > 0" class="my-2 card panel-text">
      <h4><bookmark-check class="mr-1"></bookmark-check> Your rooms</h4>
      <span>
        Connect back to previously joined rooms
      </span>
      <ul>
        <li v-for="room in savedRooms" :key="room">
          <router-link :to="'/' + room">{{ room }}</router-link>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>

import ArrowRightCircleOutline from 'vue-material-design-icons/ArrowRightCircleOutline.vue'
import PlusCircleOutline from 'vue-material-design-icons/PlusCircleOutline.vue'
import BookmarkPlusOutline from 'vue-material-design-icons/BookmarkPlusOutline.vue'
import BookmarkCheck from 'vue-material-design-icons/BookmarkCheck.vue'

export default {
  name: 'WelcomeScreen',
  data: function () {
    return {
      roomName: '',
      roomExists: false,
      validRoom: false,

      roomPassword: '',
      validPassword: false
    }
  },
  props: {
    initialRoomName: String
  },
  methods: {
    getRoom: function () {
      this.$store.state.api.getRoom(this.roomName, this.roomPassword)
        .then(room => {
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

    createOrJoinRoom: function () {
      if (this.roomExists) {
        this.joinRoom()
      } else {
        this.createRoom()
      }
    },

    joinRoom: function () {
      this.$store.commit('setRoomPassword', { 'name': this.roomName, 'password': this.roomPassword })
      this.$store.commit('saveRooms')
      this.$router.push(`/${this.roomName}`)
    },

    createRoom: function () {
      this.$store.state.api.createRoom(this.roomName, this.roomPassword)
        .then(room => {
          this.$store.commit('setRoomPassword', { 'name': room.name, 'password': this.roomPassword })
          this.$store.commit('saveRooms')
          this.$router.push(`/${room.name}`)
        })
        .catch(_ => {
          this.roomExists = false
        })
    }
  },
  watch: {
    roomName: function () {
      this.roomName = this.roomName.toLowerCase().replace(/[^a-z0-9+]+/gi, '')

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
    },
    savedRooms: function () {
      return Object.keys(this.$store.state.savedRooms)
    }
  },
  mounted () {
    if (this.initialRoomName) {
      this.roomName = this.initialRoomName
      this.validRoom = this.$refs.roomInput && this.$refs.roomInput.checkValidity()
      if (this.validRoom) this.getRoom()
    }
  },
  components: {
    ArrowRightCircleOutline,
    PlusCircleOutline,
    BookmarkPlusOutline,
    BookmarkCheck
  }
}
</script>

<style>
  .room-status {
    width: 3em;
    display: inline-block;
    text-align: center;
  }

  .panel-text ul {
    margin: 0 10px 0;
  }
</style>
