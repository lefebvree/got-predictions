<template>
  <div id="app">
    <div>
      <div class="container grid-lg">
        <div class="columns">
          <div class="column">
            <div class="title hero hero-sm px-2">
              <div class="hero-body mx-2">
                <router-link to="/"><h1>Game of Thrones Predictions</h1></router-link>
<!--                <h5>Who dies, who survives, and who will site on the Iron Throne in the final season !?</h5>-->
              </div>
            </div>
          </div>
        </div>
        <div class="content">
          <router-view/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  methods: {
    checkRoom: function () {
      const roomName = this.$route.params.room
      if (roomName && this.$store.state.currentRoom.name !== roomName) {
        this.$store.dispatch('updateRoom', roomName).catch(_ => {
          this.$router.push({ name: 'home', params: { roomName } })
        })
      }
    }
  },
  mounted () {
    this.checkRoom()
  },
  updated () {
    this.checkRoom()
  },
  created () {
    this.$store.commit('loadRooms')
  }
}

</script>

<style lang="scss">

  body {
    background-image: url('/img/bg_pattern.png') !important;
    overflow-x: hidden;
  }

  h1, h2, h3 {
    font-family: 'Roboto Slab', serif;
  }

  .title, .title a {
    color: #eee !important;
    text-decoration: none !important;
  }

  .text {
    padding: 0 25px;
  }

  .panel-text {
    padding: 25px 50px;
  }

  .content h3 {
    padding: 35px 20px 25px;
    font-weight: bold;
  }

  .content .accordion .accordion-body, .content .accordion-body {
    overflow: visible;
  }

  .content .accordion input:not(:checked) ~ .accordion-body, .content .accordion[closed] .accordion-body {
    overflow: hidden;
  }

  .content .accordion input:checked ~ .accordion-body, .content .accordion[open] .accordion-body {
    max-height: none;
  }

  button .material-design-icon {
    transform: translateY(1px);
  }

</style>
