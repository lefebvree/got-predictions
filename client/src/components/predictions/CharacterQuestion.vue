<template>
  <tr>
    <td>
      <label :for="id">
        {{ this.text }}
      </label>
    </td>
    <td>
      <div class="form-group">
        <select :id="id" class="form-select">
          <option>...</option>
          <option v-for="character in characters" :key="character">{{ character }}</option>
        </select>
      </div>
    </td>
  </tr>
</template>

<script>
export default {
  name: 'CharacterQuestion',
  props: {
    id: String,
    text: String,
    imgSrc: String
  },
  computed: {
    characters () {
      return this.$store.state.characters
    }
  }
}
</script>
