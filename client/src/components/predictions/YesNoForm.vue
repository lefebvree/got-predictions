<template>
  <div class="accordion">
    <input type="checkbox" id="yesno-questions" name="accordion-checkbox" hidden checked>
    <div class="accordion-header">
      <h3 class="hero hero-sm">
        <label for="yesno-questions">
          <i class="icon icon-arrow-right mr-2 "></i>
          Events
        </label>
      </h3>
    </div>
    <div class="accordion-body">
      <table class="table table-hover">
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
