<template>
  <div>
    <yes-no-question v-for="(v, k) in characters"
      :key="k"
      :id="k"
      :text="v.text"
      :imgSrc="v.imgSrc"
    ></yes-no-question>
  </div>
</template>

<script>
import YesNoQuestion from '@/components/predictions/YesNoQuestion.vue'

export default {
  name: 'YesNoForm',
  computed: {
    characters () {
      return this.$store.state.questions['yes_no_questions']
    }
  },
  components: {
    YesNoQuestion
  }
}
</script>
