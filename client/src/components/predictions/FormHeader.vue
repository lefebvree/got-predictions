
<template>
  <div>
      <h3 class="hero hero-sm">
        <label :for="iptFor">
          <chevron-right class="hide-xs mr-2"></chevron-right>
          <span class="d-inline-block">
            {{ name }}
          </span>
        </label>
      </h3>
    </div>
</template>

<script>
import ChevronRight from 'vue-material-design-icons/ChevronRight.vue'

export default {
  name: 'FormHeader',
  props: {
    name: String,
    iptFor: String
  },
  components: {
    ChevronRight
  }
}
</script>

<style>

  .hero-sm {
    padding-bottom: 0;
  }

  label {
    cursor: pointer;
  }

</style>
