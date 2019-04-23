<template>
  <div class="accordion">
    <input type="checkbox" id="yesno-questions" name="accordion-checkbox" hidden checked>
    <form-header name="Events" iptFor="yesno-questions" class="accordion-header"></form-header>
    <p class="text">
      <calendar-range></calendar-range>
      <b>+1</b> / <b>-1</b> points when guessing correctly that an event will happen or not.
    </p>
    <div class="accordion-body">
      <table class="table">
        <tbody>
          <yes-no-question v-for="(v, k) in characters"
            :key="k"
            :id="k"
            :text="v.text"
            :imgSrc="v.imgSrc"
            :answer="v.answer"
          ></yes-no-question>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import YesNoQuestion from '@/components/predictions/events/YesNoQuestion.vue'
import FormHeader from '@/components/predictions/FormHeader.vue'

import CalendarRange from 'vue-material-design-icons/CalendarRange.vue'

export default {
  name: 'YesNoForm',
  computed: {
    characters () {
      return this.$store.state.questions['yes_no_questions']
    }
  },
  components: {
    YesNoQuestion,
    FormHeader,
    CalendarRange
  }
}
</script>

<style>
  .form-checkbox {
    transform: translateY(-2px);
  }
</style>
