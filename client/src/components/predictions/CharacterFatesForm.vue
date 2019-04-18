<template>
  <div>
    <character-fate v-for="(v, k) in characters"
      :key="k"
      :id="k"
      :name="v.text"
      :imgSrc="v.imgSrc"
    ></character-fate>
  </div>
</template>

<script>
import CharacterFate from '@/components/predictions/CharacterFate.vue'

export default {
  name: 'CharacterFatesForm',
  computed: {
    characters () {
      return this.$store.state.questions['character_fates']
    }
  },
  components: {
    CharacterFate
  }
}
</script>
