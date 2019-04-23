<template>
  <div class="accordion">
    <input type="checkbox" id="character-fates" name="accordion-checkbox" hidden checked>
    <form-header name="Character Fates" iptFor="character-fates" class="accordion-header"></form-header>
    <p class="text">
      <b>+1</b> point if the character status (dead or alive) is guessed correctly. <br>
      <b>+3</b> / <b>-2</b> bonus points when
      predicting that he will turn into a White Walker.
    </p>
    <p class="text">
      <emoticon></emoticon>
      <b>Alive</b> : Still alive by season's end. <br>
      <emoticon-dead></emoticon-dead>
      <b>Dead</b> : Dead at the end of the season. <br><br>
      <skull></skull>
      <b>Whight</b> : Turned into a undead Whight (White Walkers army) during the season.
    </p>
    <div class="accordion-body">
      <table class="table table-scroll">
        <thead>
          <tr>
            <th class="col-8 col-sm-9">Character</th>
            <th class="text-center col-1" title="Still alive at the end of the season">
              <span class="hide-sm">Alive</span>
              <emoticon class="show-sm text-justify"></emoticon>
            </th>
            <th class="text-center col-1" title="Gone for good, no comeback">
              <span class="hide-sm">Dead</span>
              <emoticon-dead class="show-sm text-justify"></emoticon-dead>
            </th>
            <th class="text-center col-1" title="Even if he died again, this character turned a some point">
              <span class="hide-sm">Whight</span>
              <skull class="show-sm text-justify"></skull>
            </th>
            <th class="col-1 col-sm-0"></th>
          </tr>
        </thead>
        <tbody>
        <character-fate v-for="(v, k) in characters"
                        :key="k"
                        :id="k"
                        :name="v.text"
                        :src="v.src"
                        :answer="v.answer"
        ></character-fate>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>

import FormHeader from '@/components/predictions/FormHeader.vue'
import CharacterFate from '@/components/predictions/fates/CharacterFate.vue'

import Emoticon from 'vue-material-design-icons/Emoticon.vue'
import EmoticonDead from 'vue-material-design-icons/EmoticonDead.vue'
import Skull from 'vue-material-design-icons/Skull.vue'

export default {
  name: 'CharacterFatesForm',
  computed: {
    characters () {
      return this.$store.state.questions['character_fates']
    }
  },
  components: {
    CharacterFate,
    FormHeader,
    Emoticon,
    EmoticonDead,
    Skull
  }
}
</script>
