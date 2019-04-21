
<template>
  <div>
    <div class="my-2 card panel-text">
      <h3>{{ room.name }}</h3>

      <h4><pencil-plus-outline></pencil-plus-outline> Post your Predictions to {{ room.name }}</h4>
      <router-link :to="'/' + room.name + '/prediction'" class="text mb-2">
        <button class="btn btn-success">New Predictions</button>
      </router-link>
    </div>
    <div class="my-2 card panel-text">
      <h4><account-multiple-outline class="mr-1"></account-multiple-outline> Users</h4>
      <ul>
        <li v-for="user in room.users" :key="user.name">
          {{ user.name }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>

import AccountMultipleOutline from 'vue-material-design-icons/AccountMultipleOutline.vue'
import PencilPlusOutline from 'vue-material-design-icons/PencilPlusOutline.vue'

export default {
  name: 'room',

  data () {
    return {
      refreshInterval: null
    }
  },

  computed: {
    room () {
      return this.$store.state.currentRoom
    }
  },

  methods: {
    update () {
      const roomName = this.room.name
      this.$store.dispatch('updateRoom', roomName)
    }
  },

  beforeMount () {
    this.update()
    this.refreshInterval = window.setInterval(this.update, 1000)
  },

  beforeDestroy () {
    clearInterval(this.refreshInterval)
  },

  components: {
    AccountMultipleOutline,
    PencilPlusOutline
  }
}
</script>
