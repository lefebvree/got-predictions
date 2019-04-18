<template>
  <div class="columns col-gapless">
    <div class="column col-6">{{ this.text }}</div>
  </div>
</template>

<script>
export default {
  name: 'CharacterQuestion',
  props: {
    id: String,
    text: String,
    imgSrc: String
  },
  data: function () {
    return {
      status: '0'
    }
  }
}
</script>
