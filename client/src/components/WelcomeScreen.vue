<template>
  <div>
    <div class="my-2">
      <h4>Join a room or Create one :</h4>
      <div class="input-group">
        <input v-model="roomName" class="form-input input-lg" type="text" placeholder="Room Name">
        <button class="btn btn-primary input-group-btn btn-lg">{{ roomStatus }}</button>
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

<style scoped lang="scss">
</style>
