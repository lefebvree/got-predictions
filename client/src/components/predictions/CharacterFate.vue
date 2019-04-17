<template>
  <div class="columns col-gapless">
    <div class="column col-6">{{ this.name }} {{this.status}}</div>
    <div class="column col-6">
      <div class="form-group">
        <label class="form-radio form-inline">
          <input type="radio" name="status" v-model="status" value="0">
          <i class="form-icon"></i> Alive
        </label>
        <label class="form-radio form-inline">
          <input type="radio" name="status" v-model="status" value="1">
          <i class="form-icon"></i> Dead
        </label>
        <label class="form-radio form-inline">
          <input type="radio" name="status" v-model="status" value="2">
          <i class="form-icon"></i> White Walker
        </label>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CharacterFate',
  props: {
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
