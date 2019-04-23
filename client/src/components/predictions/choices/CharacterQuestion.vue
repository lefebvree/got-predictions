<template>
  <tr>
    <td class="col-5">
      <div class="form-group">
        <select v-if="disabled" class="form-select" disabled>
           <option selected>{{ answer }}</option>
        </select>
        <select v-else v-model="value" :id="id" class="form-select" required>
          <option disabled selected value="">Select a Character</option>
          <option value="0">Nobody</option>
          <option v-for="character in characters" :key="character.id" :value="character.id">
            {{ character.name }}
          </option>
        </select>
      </div>
    </td>
    <td>
      <label :for="id">
        {{ this.text }}
      </label>
    </td>
  </tr>
</template>

<script>
export default {
  name: 'CharacterQuestion',
  props: {
    id: String,
    text: String,
    imgSrc: String,
    answer: String
  },
  data () {
    return {
      value: ''
    }
  },
  computed: {
    characters () {
      return this.$store.state.characters
    },

    disabled () {
      return this.answer !== undefined
    }
  },

  watch: {
    value () {
      this.saveAnswer()
    }
  },

  methods: {
    saveAnswer () {
      this.$store.commit('setPredictionAnswer', {
        cat: 'character_choices', id: this.id, ans: this.value
      })
    }
  }
}
</script>

<style>

  .form-group {
    margin-left: 10px;
  }

</style>
