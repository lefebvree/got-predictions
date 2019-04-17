<template>
  <div>
    <character-fate v-for="c in characters"
      :key="c.name"
      :name="c.name"
      :imgSrc="c.imgSrc"
    ></character-fate>
  </div>
</template>

<script>
import CharacterFate from '@/components/predictions/CharacterFate.vue'

export default {
  name: 'CharacterFatesForm',
  props: {
    characters: String
  },
  data: function () {
    return {
      status: 0
    }
  },
  components: {
    CharacterFate
  }
}
</script>
