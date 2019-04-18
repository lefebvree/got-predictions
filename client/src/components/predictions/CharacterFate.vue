<template>
  <div class="columns col-gapless">
    <div class="column col-3">{{ this.name }}</div>
    <div class="column col-6">
      <div class="form-group">
        <label class="form-radio form-inline" title="Still alive at the end of the season">
          <input type="radio" :name="id" v-model="status" value="0" checked>
          <i class="form-icon"></i> Alive
        </label>
        <label class="form-radio form-inline" title="Gone for good, no comeback">
          <input type="radio" :name="id" v-model="status" value="1">
          <i class="form-icon"></i> Dead
        </label>
        <label class="form-radio form-inline" title="Even if if died again, this character turned a some point">
          <input type="radio" :name="'status-' + id" v-model="status" value="2">
          <i class="form-icon"></i> White Walker
        </label>
      </div>
    </div>
    <hr>
  </div>
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
