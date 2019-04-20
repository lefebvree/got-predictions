<template>
  <tr>
    <td>
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
        <span class="d-inline-block">
          {{ this.name }}
        </span>
      </div>
    </td>
    <td class="text-center">
      <label class="form-radio form-inline" title="Alive">
        <input type="radio" :name="id" v-model="status.alive" value="0" required>
        <i class="form-icon"></i>
      </label>
    </td>
    <td class="text-center ">
      <label class="form-radio form-inline" title="Dead">
        <input type="radio" :name="id" v-model="status.alive" value="1" required>
        <i class="form-icon"></i>
      </label>
    </td>
    <td class="text-center">
      <label class="form-checkbox form-inline" title="White Walker">
        <input type="checkbox" :name="'ww-' + id" v-model="status.ww" :disabled="status.alive === '0'" value="2">
        <i class="form-icon"></i>
      </label>
    </td>
    <td> </td>
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
      status: {
        alive: '0',
        ww: false
      }
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
  },
  watch: {
    status: {
      handler (s) {
        if (s.alive === '0') {
          s.ww = false
        }
      },
      deep: true
    }
  }
}
</script>
