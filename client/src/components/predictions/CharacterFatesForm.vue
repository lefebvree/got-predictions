<template>
  <div>
    <h3>Character Fates</h3>
    <table class="table table-hover">
      <thead>
        <tr>
          <th>Character</th>
          <th class="text-center" title="Still alive at the end of the season">Alive</th>
          <th class="text-center" title="Gone for good, no comeback">Dead</th>
          <th class="text-center" title="Even if if died again, this character turned a some point">White Walker</th>
        </tr>
      </thead>
      <tbody>
        <character-fate v-for="(v, k) in characters"
                        :key="k"
                        :id="k"
                        :name="v.text"
                        :imgSrc="v.imgSrc"
        ></character-fate>
      </tbody>
    </table>
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
