<template>
  <div class="accordion">
    <input type="checkbox" id="character-questions" name="accordion-checkbox" hidden checked>
    <div class="accordion-header">
      <h3 class="hero hero-sm">
        <label for="character-questions">
          <i class="icon icon-arrow-right mr-2 "></i>
          Character Choices
        </label>
      </h3>
    </div>
    <div class="accordion-body">
      <table class="table table-hover">
        <tbody>
          <character-question v-for="(v, k) in choices"
            :key="k"
            :id="k"
            :text="v.text"
            :src="v.src"
          ></character-question>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import CharacterQuestion from '@/components/predictions/CharacterQuestion.vue'

export default {
  name: 'CharacterForm',
  computed: {
    choices () {
      return this.$store.state.questions['character_choices']
    }
  },
  components: {
    CharacterQuestion
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
