<template>
  <div>
      <character-fates-form :characters="[{name: 'test', imgSrc: 'test1'}]"></character-fates-form>
  </div>
</template>

<script>
import CharacterFatesForm from '@/components/predictions/CharacterFatesForm.vue'

export default {
  name: 'prediction',
  components: {
    CharacterFatesForm
  }
}
</script>
