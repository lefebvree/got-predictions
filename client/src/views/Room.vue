
<template>
  <div>
    <h3>{{ this.roomName }} Predictions</h3>
  </div>
</template>

<script>

export default {
  name: 'room',
  computed: {
    roomName: function () {
      return this.$route.params.room
    }
  }
}
</script>
