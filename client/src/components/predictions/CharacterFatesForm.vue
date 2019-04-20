<template>
  <div class="accordion">
    <input type="checkbox" id="character-fates" name="accordion-checkbox" hidden checked>
    <div class="accordion-header">
      <h3 class="hero hero-sm">
        <label for="character-fates">
          <i class="icon icon-arrow-right mr-2 "></i>
          Character Fates
        </label>
      </h3>
    </div>
    <div class="accordion-body">
      <table class="table table-hover">
        <thead>
        <tr>
          <th class="col-8">Character</th>
          <th class="text-center col-1" title="Still alive at the end of the season">Alive</th>
          <th class="text-center col-1" title="Gone for good, no comeback">Dead</th>
          <th class="text-center col-1" title="Even if if died again, this character turned a some point">White Walker</th>
          <th class="col-1"></th>
        </tr>
        </thead>
        <tbody>
        <character-fate v-for="(v, k) in characters"
                        :key="k"
                        :id="k"
                        :name="v.text"
                        :src="v.src"
        ></character-fate>
        </tbody>
      </table>
    </div>
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
