<template>
  <div>
    <div class="my-2 card panel-text">
      <h4>Join a room or Create one :</h4>
      <div class="columns">
        <div class="input-group col-6">
          <input v-model="roomName" class="form-input input-lg" type="text" placeholder="Room Name">
          <button class="btn btn-primary input-group-btn btn-lg">{{ roomStatus }}</button>
        </div>
      </div>
      <div class="col-6">
        You can create a room to invite your friends
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'WelcomeScreen',
  data: function () {
    return {
      roomName: '',
      roomExists: false
    }
  },
  methods: {
    getRoom: function () {
      this.$store.state.api.getRoom(this.roomName)
        .then(room => {
          this.roomExists = true
        })
        .catch(_ => {
          this.roomExists = false
        })
    }
  },
  watch: {
    roomName: function () {
      this.getRoom(this.roomName)
    }
  },
  computed: {
    roomStatus: function () {
      return this.roomExists ? 'Join' : 'Create'
    }
  }
}
</script>
