
<template>
  <div>
    <h3>{{ this.room.name }} Predictions</h3>
  </div>
</template>

<script>

export default {
  name: 'room',

  computed: {
    room () {
      return this.$store.state.currentRoom
    }
  }
}
</script>
