<template>
  <div>
    <character-question v-for="(v, k) in choices"
      :key="k"
      :id="k"
      :text="v.text"
      :imgSrc="v.imgSrc"
    ></character-question>
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
