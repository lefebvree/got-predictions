<template>
  <tr :class="{ disabled: disabled }">
    <td class="col-1">
      <label class="form-checkbox float-right">
        <input type="checkbox" v-model="value" :id="id" :disabled="disabled">
        <i class="form-icon"></i>
      </label>
    </td>
    <td class="col-11">
      <label :for="id" :disabled="disabled">
        {{ this.text }}
      </label>
    </td>
  </tr>
</template>

<script>
export default {
  name: 'YesNoQuestion',
  props: {
    id: String,
    text: String,
    imgSrc: String,
    answer: Boolean
  },
  data: function () {
    return {
      value: false
    }
  },

  computed: {
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
        cat: 'yes_no_questions', id: this.id, ans: this.value
      })
    }
  },

  mounted () {
    if (this.disabled) {
      this.value = this.answer
    }

    this.saveAnswer()
  }
}
</script>
