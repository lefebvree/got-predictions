<template>
  <tr>
    <td>{{ this.name }}</td>
    <td class="text-center">
      <label class="form-radio form-inline">
        <input type="radio" :name="id" v-model="status" value="0" checked>
        <i class="form-icon"></i>
      </label>
    </td>
    <td class="text-center">
      <label class="form-radio form-inline">
        <input type="radio" :name="id" v-model="status" value="1" checked>
        <i class="form-icon"></i>
      </label>
    </td>
    <td class="text-center">
      <label class="form-radio form-inline">
        <input type="radio" :name="id" v-model="status" value="2" checked>
        <i class="form-icon"></i>
      </label>
    </td>
  </tr>
</template>

<script>
export default {
  name: 'CharacterFate',
  props: {
    id: String,
    name: String,
    imgSrc: String
  },
  data: function () {
    return {
      status: '0'
    }
  }
}
</script>
