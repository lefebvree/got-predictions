<template>
  <div>
    <div class="panel card">
      <h3>Make your predictions</h3>
      <div class="info">
        <p>
          Be the first one in room <b>{{ room }}</b> to make your predictions and find out who is the Three-eyed raven capable of foreseeing every outcome of the season !
        </p>
      </div>
    </div>
    <character-fates-form class="panel card"></character-fates-form>
    <yes-no-form class="panel card"></yes-no-form>
    <character-form class="panel card"></character-form>
  </div>
</template>

<script>
import CharacterFatesForm from '@/components/predictions/CharacterFatesForm.vue'
import YesNoForm from '@/components/predictions/YesNoForm.vue'
import CharacterForm from '@/components/predictions/CharacterForm.vue'
import { mapActions } from 'vuex'

export default {
  name: 'prediction',
  components: {
    CharacterFatesForm,
    YesNoForm,
    CharacterForm
  },

  methods: { ...mapActions(['fetchQuestions']) },

  mounted () {
    this.fetchQuestions()
  },

  computed: {
    room () {
      return this.$route.params.room
    }
  }
}
</script>

<style>

  .info {
    padding: 0 50px;
  }

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

</style>
