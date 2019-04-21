<template>
  <div class="modal modal-lg">
    <a href="#close" class="modal-overlay" aria-label="Close"></a>
    <div class="modal-container">
      <div class="modal-header">
        <a href="#close" class="btn btn-clear float-right" aria-label="Close"></a>
        <div class="modal-title h5"><b>{{ userName }}</b> predictions in <b>{{ roomName }}</b></div>
      </div>
      <div class="modal-body">
        <div class="content">
          <h4>Character Fates</h4>
          <p v-for="char in predictions.character_fates" :key="char.id">
            {{ char }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import Emoticon from 'vue-material-design-icons/Emoticon.vue'
import EmoticonDead from 'vue-material-design-icons/EmoticonDead.vue'
import Skull from 'vue-material-design-icons/Skull.vue'

export default {
  name: 'PredictionView',
  data: function () {
    return {
      predictions: {}
    }
  },
  props: {
    userName: String,
    roomName: String,
    predictionJson: String
  },
  methods: {
  },
  watch: {
    predictionJson () {
      if (this.predictionJson) {
        return JSON.parse(this.predictionJson)
      } else {
        return {}
      }
    }
  },
  components: {
    Emoticon,
    EmoticonDead,
    Skull
  }
}
</script>
