<template>
  <div class="modal modal-lg predictions" ref="modal">
    <a class="modal-overlay" aria-label="Close" @click="close"></a>
    <div class="modal-container">
      <div class="modal-header">
        <a class="btn btn-clear float-right" aria-label="Close" @click="close"></a>
        <div class="modal-title h3"><b>{{ userName }}</b>'s predictions in <b>{{ roomName }}</b></div>
        <div class="text-gray text-italic">{{ date }}</div>
      </div>
      <div class="modal-body">
        <div class="content">
          <div class="accordion">
            <input type="checkbox" id="character-fates" name="accordion-checkbox" hidden checked>
            <div class="accordion-header">
              <label for="character-fates">
                <h4 class="slab"><chevron-right class="mr-2"></chevron-right> Character Fates</h4>
              </label>
            </div>
            <div class="columns accordion-body">
              <div class="col-4 col-sm-12 my-2">
                <h5 class="slab text-bold c-alive"><emoticon class="mr-1"></emoticon> Alive</h5>
                <ul>
                  <li v-for="character in charactersAlive" :key="character" class="my-1">
                    <div class="d-inline-block">
                      {{ character }}
                    </div>
                  </li>
                </ul>
              </div>
              <div class="col-4 col-sm-12 my-2">
                <h5 class="slab text-bold c-dead"><emoticon-dead class="mr-1"></emoticon-dead> Dead</h5>
                <ul>
                  <li v-for="character in charactersDead" :key="character" class="my-1">
                    <div class="d-inline-block">
                      {{ character }}
                    </div>
                  </li>
                </ul>
              </div>
              <div class="col-4 col-sm-12 my-2">
                <h5 class="slab text-bold c-wight"><skull class="mr-1"></skull> Wight</h5>
                <ul>
                  <li v-for="character in charactersWight" :key="character" class="my-1">
                    <div class="d-inline-block">
                      {{ character }}
                    </div>
                  </li>
                </ul>
              </div>
            </div>
          </div>
          <div class="accordion">
            <input type="checkbox" id="events" name="accordion-checkbox" hidden checked>
            <div class="accordion-header">
              <label for="events">
                <h4 class="slab"><chevron-right class="mr-2"></chevron-right> Events</h4>
              </label>
            </div>
            <div class="accordion-body">
              <div v-for="event in events" :key="event[0]" class="my-2" :class="{'text-bold': event[1]}">
                <check v-if="event[1]"></check>
                <close v-else></close>
                <span class="ml-2">{{ event[0] }}</span>
              </div>
            </div>
          </div>
          <div class="accordion">
            <input type="checkbox" id="choices" name="accordion-checkbox" hidden checked>
            <div class="accordion-header">
              <label for="choices">
                <h4 class="slab"><chevron-right class="mr-2"></chevron-right> Character Choices</h4>
              </label>
            </div>
            <div class="accordion-body">
              <div v-for="choice in choices" :key="choice[0]" class="my-2">
                <div class="ml-2">
                  <span class="text-bold mr-1">{{ choice[1] === '0' ? 'Nobody' : getCharacterName(choice[1]) }}</span>
                  {{ choice[0] }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import Emoticon from 'vue-material-design-icons/Emoticon.vue'
import EmoticonDead from 'vue-material-design-icons/EmoticonDead.vue'
import Skull from 'vue-material-design-icons/Skull.vue'
import ChevronRight from 'vue-material-design-icons/ChevronRight.vue'
import Check from 'vue-material-design-icons/Check.vue'
import Close from 'vue-material-design-icons/Close.vue'

export default {
  name: 'PredictionView',
  props: {
    userName: String,
    roomName: String,
    predictionJson: String,
    date: String
  },
  methods: {
    getQuestionText (cat, id) {
      const category = this.$store.state.questions[cat]
      if (id in category) {
        return this.$store.state.questions[cat][id].text
      } else {
        return null
      }
    },

    close () {
      this.$refs.modal.classList.remove('active')
    },

    getCharactersByStatus (status) {
      const chars = Object.entries(this.predictions['character_fates']).filter(([c, v]) => v === status)
      return chars.map(c => this.getQuestionText('character_fates', c[0]))
    },

    getCharacterName (id) {
      return this.$store.state.questions['character_fates'][id].text
    }
  },
  computed: {
    predictions () {
      if (this.predictionJson) {
        return JSON.parse(this.predictionJson)
      } else {
        return null
      }
    },

    charactersAlive () {
      if (this.predictions) {
        return this.getCharactersByStatus(0)
      } else {
        return []
      }
    },

    charactersDead () {
      if (this.predictions) {
        return this.getCharactersByStatus(1)
      } else {
        return []
      }
    },

    charactersWight () {
      if (this.predictions) {
        return this.getCharactersByStatus(2)
      } else {
        return []
      }
    },

    events () {
      if (this.predictions) {
        const events = Object.entries(this.predictions['yes_no_questions'])
        return events.map(c => [this.getQuestionText('yes_no_questions', c[0]), c[1]]).filter(x => !!x[0])
      } else {
        return []
      }
    },

    choices () {
      if (this.predictions) {
        const choices = Object.entries(this.predictions['character_choices'])
        return choices.map(c => [this.getQuestionText('character_choices', c[0]), c[1]]).filter(x => !!x[0])
      } else {
        return []
      }
    }
  },
  components: {
    Emoticon,
    EmoticonDead,
    Skull,
    ChevronRight,
    Check,
    Close
  }
}
</script>

<style>

  .modal-body ul {
    margin: 0 0 0 8px;
  }

  .c-alive {
    color: #16a085;
  }

  .c-dead {
    color: #c0392b;
  }

  .c-wight {
    color: #2980b9;
  }

  label {
    cursor: pointer;
  }

  .predictions.modal-lg .modal-overlay {
    background: #000000cc !important;
  }

</style>
