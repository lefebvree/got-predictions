<template>
  <div>
    <h3>?</h3>
    <table class="table table-hover">
      <thead>
        <tr>
          <th></th>
          <th>Question</th>
        </tr>
      </thead>
      <tbody>
        <yes-no-question v-for="(v, k) in characters"
          :key="k"
          :id="k"
          :text="v.text"
          :imgSrc="v.imgSrc"
        ></yes-no-question>
      </tbody>
    </table>
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
