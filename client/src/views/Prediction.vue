<template>
  <div>
      <character-fates-form></character-fates-form>
      <yes-no-form></yes-no-form>
      <character-form></character-form>
  </div>
</template>

<script>
import CharacterFatesForm from '@/components/predictions/CharacterFatesForm.vue'
import YesNoForm from '@/components/predictions/YesNoForm.vue'
import CharacterForm from '@/components/predictions/CharacterForm.vue'
import { mapActions } from 'vuex'

export default {
  name: 'prediction',
  components: {
    CharacterFatesForm,
    YesNoForm,
    CharacterForm
  },

  methods: { ...mapActions(['fetchQuestions']) },

  mounted () {
    this.fetchQuestions()
  }
}
</script>
