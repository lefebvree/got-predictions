<template>
  <tr>
    <td>
      <div class="form-checkbox float-right">
        <input type="checkbox" :id="id">
        <i class="form-icon"></i>
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
  name: 'YesNoQuestion',
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
