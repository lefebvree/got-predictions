<template>
  <div>
    <div class="panel card">
      <h3 class="ml-2"> Make your predictions</h3>
      <p class="text">
        <span v-if="nbUsers === 0">Be the first one </span>
        <span v-else>Join {{ nbUsers }} viewer{{ nbUsers === 1 ? '' : 's' }}  </span>
        in room <b>{{ room.name }}</b> to make your predictions and find out who is the Three-eyed raven capable of foreseeing every outcome of the season !
      </p>
      <p class="text">
        Some questions have been answered already and are disabled, you can't gain or loose any points with them.
      </p>
    </div>
    <form @submit="checkForm" ref="form">
      <character-fates-form class="panel card"></character-fates-form>
      <yes-no-form class="panel card"></yes-no-form>
      <character-form class="panel card"></character-form>
      <div class="panel card">
        <div class="panel-text">
          <div class="columns">
            <div class="col-3 col-lg-5 col-md-7 col-sm-12 mb-2">
              <div class="form-group">
                <label class="form-label" for="user-name">User Name</label>
                <input v-model="userName" class="form-input" type="text" placeholder="Name" minlength="3" maxlength="25" ref="nameInput"
                       autocomplete="off" tabindex="1" v-on:input="userName = $event.target.value" id="user-name">
              </div>
            </div>
            <div class="col-7 col-sm-12 m-2">
              <span>
                Post your predictions
              </span><br>
              <button class="btn input-group-btn mt-1" tabindex="2" :disabled="!validName">
                Submit <arrow-right-circle class="ml-2 mr-1"></arrow-right-circle>
              </button>
            </div>
          </div>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import CharacterFatesForm from '@/components/predictions/fates/CharacterFatesForm.vue'
import YesNoForm from '@/components/predictions/events/YesNoForm.vue'
import CharacterForm from '@/components/predictions/choices/CharacterForm.vue'

import ArrowRightCircle from 'vue-material-design-icons/ArrowRightCircle.vue'

export default {
  name: 'prediction',

  data: function () {
    return {
      userName: '',
      validName: false
    }
  },

  computed: {
    room: function () {
      return this.$store.state.currentRoom
    },
    nbUsers () {
      return Object.keys(this.room.users).length
    }
  },

  watch: {
    userName: function () {
      if (this.$refs.nameInput && this.$refs.nameInput.checkValidity()) {
        this.validName = !Object.values(this.room.users).map(u => u.name).includes(this.userName)
      } else {
        this.validName = false
      }
    }
  },

  methods: {
    checkForm: function (e) {
      e.preventDefault()
      if (this.$refs.form && this.$refs.form.reportValidity()) {
        this.post()
      }
    },

    post: function () {
      this.$store.dispatch('submitPredictions', this.userName)
        .then(answer => {
          this.$store.commit('setRoomName', { 'name': this.room.name, 'userName': answer.name })
          this.$store.commit('saveRooms')
          this.$router.push(`/${this.room.name}`)
        })
    }
  },

  components: {
    CharacterFatesForm,
    YesNoForm,
    CharacterForm,
    ArrowRightCircle
  }
}
</script>

<style>

  .panel {
    margin-bottom: 25px;
  }

  figure.avatar {
    margin: 0 20px;
    background: none;
    box-shadow: #00000040 0px 0px 10px 0px;
  }

  td.popover {
    display: table-cell;
  }

  tr.disabled {
    background-color: #dadada;
    opacity: 0.5;
  }

  .popover .popover-container .card, .popover .popover-container img {
    height: fit-content;
    width: fit-content;
    border-radius: 5px;
  }

  .text .material-design-icon {
    margin-right: 10px;
  }

</style>
