<template>
  <div>
    <div class="panel card">
      <h3 class="ml-2"> Make your predictions</h3>
      <p class="text">
        Be the first one in room <b>{{ room.name }}</b> to make your predictions and find out who is the Three-eyed raven capable of foreseeing every outcome of the season !
      </p>
    </div>
    <form>
      <character-fates-form class="panel card"></character-fates-form>
      <yes-no-form class="panel card"></yes-no-form>
      <character-form class="panel card"></character-form>
      <div class="panel card">
        <div class="panel-text">
          <p>
            Pick a name to to post your predictions :
          </p>
          <div class="columns">
            <div class="col-5">
              <div>
                <input class="form-input" type="text" placeholder="Name">
              </div>
            </div>
            <div class="col-12 text-center mt-2">
              <button class="btn btn-primary input-group-btn btn-lg">Submit <arrow-right-circle class="ml-2 mr-1"></arrow-right-circle> </button>
            </div>
          </div>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import CharacterFatesForm from '@/components/predictions/CharacterFatesForm.vue'
import YesNoForm from '@/components/predictions/YesNoForm.vue'
import CharacterForm from '@/components/predictions/CharacterForm.vue'

import ArrowRightCircle from 'vue-material-design-icons/ArrowRightCircle.vue'

import { mapActions } from 'vuex'

export default {
  name: 'prediction',
  components: {
    CharacterFatesForm,
    YesNoForm,
    CharacterForm,
    ArrowRightCircle
  },

  data () {
    return {
      room: {
        name: ''
      }
    }
  },

  methods: {
    ...mapActions(['fetchQuestions'])
  },

  mounted () {
    this.fetchQuestions()
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

  .popover .popover-container .card, .popover .popover-container img {
    height: fit-content;
    width: fit-content;
    border-radius: 5px;
  }

  .text .material-design-icon {
    margin-right: 10px;
  }

</style>
