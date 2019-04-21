<template>
  <div class="accordion">
    <input type="checkbox" id="character-questions" name="accordion-checkbox" hidden checked>
    <form-header name="Character Questions" iptFor="character-questions" class="accordion-header"></form-header>
    <p class="text">
      <account-circle></account-circle>
      <b>+2</b> points when guessing correctly which character performs an action <br>
    </p>
    <div class="accordion-body">
      <table class="table">
        <tbody>
          <character-question v-for="(v, k) in choices"
            :key="k"
            :id="k"
            :text="v.text"
            :src="v.src"
            :answer="v.answer"
          ></character-question>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import CharacterQuestion from '@/components/predictions/CharacterQuestion.vue'
import FormHeader from '@/components/predictions/FormHeader.vue'

import AccountCircle from 'vue-material-design-icons/AccountCircle.vue'

export default {
  name: 'CharacterForm',
  computed: {
    choices () {
      return this.$store.state.questions['character_choices']
    }
  },
  components: {
    CharacterQuestion,
    FormHeader,
    AccountCircle
  }
}
</script>

<style>
  td label {
    display: inline-table !important;
  }
  td label i {
    position: inherit !important;
  }
</style>
