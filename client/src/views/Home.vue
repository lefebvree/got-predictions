<template>
  <div>
    <WelcomeScreen :initial-room-name="prefilledRoomName"/>
  </div>
</template>

<script>
// @ is an alias to /src
import WelcomeScreen from '@/components/WelcomeScreen.vue'

export default {
  name: 'home',
  components: {
    WelcomeScreen
  },
  computed: {
    prefilledRoomName () {
      return this.$route.params.roomName || ''
    }
  }
}
</script>
