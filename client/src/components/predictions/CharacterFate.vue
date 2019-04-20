<template>
  <tr>
    <td class="col-8">
      <div>
        <div class="popover popover-right">
          <figure class="avatar">
            <img :src="image" :alt="name">
          </figure>
          <div class="popover-container">
            <div class="card">
              <img :src="image" :alt="name">
            </div>
          </div>
        </div>
        {{ this.name }}
      </div>
    </td>
    <td class="text-center col-1">
      <label class="form-radio form-inline">
        <input type="radio" :name="id" v-model="status" value="0">
        <i class="form-icon"></i>
      </label>
    </td>
    <td class="text-center col-1">
      <label class="form-radio form-inline">
        <input type="radio" :name="id" v-model="status" value="1">
        <i class="form-icon"></i>
      </label>
    </td>
    <td class="text-center col-1">
      <label class="form-radio form-inline">
        <input type="radio" :name="id" v-model="status" value="2">
        <i class="form-icon"></i>
      </label>
    </td>
    <td class="col-1">
      <samp
      >
        <small>1 point</small>
      </samp>
    </td>
  </tr>
</template>

<script>
export default {
  name: 'CharacterFate',
  props: {
    id: String,
    name: String,
    src: String
  },
  data: function () {
    return {
      status: ''
    }
  },
  computed: {
    image () {
      try {
        return require('@/assets/img/' + this.src)
      } catch (e) {
        return ''
      }
    }
  }
}
</script>
