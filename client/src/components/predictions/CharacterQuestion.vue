<template>
  <tr>
    <td class="col-5">
      <div class="form-group">
        <select :id="id" class="form-select" required>
          <option disabled selected>Select a Character</option>
          <option value="NOBODY">Nobody</option>
          <option v-for="character in characters" :key="character" :value="character">{{ character }}</option>
        </select>
      </div>
    </td>
    <td>
      <label :for="id">
        {{ this.text }}
      </label>
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

<style>

  .form-group {
    margin-left: 10px;
  }

</style>
