<template>
  <tr :class="{ disabled: disabled }">
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
        <input type="radio" :name="id" v-model="status.alive" value="0" required :disabled="disabled">
        <i class="form-icon"></i>
      </label>
    </td>
    <td class="text-center ">
      <label class="form-radio form-inline" title="Dead">
        <input type="radio" :name="id" v-model="status.alive" value="1" required :disabled="disabled">
        <i class="form-icon"></i>
      </label>
    </td>
    <td class="text-center">
      <label class="form-checkbox form-inline" title="White Walker">
        <input type="checkbox" :name="'ww-' + id" v-model="status.ww" :disabled="disableWWCase" value="2">
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
    src: String,
    answer: Number
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
    },

    disabled () {
      return this.answer !== undefined
    },

    disableWWCase () {
      return this.disabled || this.status.alive !== '1'
    }
  },
  methods: {
    saveAnswer () {
      const formValue = (this.status.alive === '0') ? 0 : ((this.status.ww) ? 2 : 1)
      this.$store.commit('setPredictionAnswer', {
        cat: 'character_fates', id: this.id, ans: formValue
      })
    }
  },
  watch: {
    status: {
      handler (status) {
        if (status.alive === '0') status.ww = false
        this.saveAnswer()
      },
      deep: true
    }
  },
  mounted () {
    if (this.disabled) {
      this.status.alive = this.answer === 0 ? '0' : '1'
      this.status.ww = this.answer === 2
    } else {
      this.status.alive = '0'
    }

    this.saveAnswer()
  }
}
</script>
