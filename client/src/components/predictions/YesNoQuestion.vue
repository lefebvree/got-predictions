<template>
  <div class="columns col-gapless">
    <div class="form-group">
      <label class="form-checkbox">
        <input type="checkbox">
        <i class="form-icon"></i> {{ this.text }}
      </label>
    </div>
  </div>
</template>

<script>
export default {
  name: "YesNoQuestion",
  props: {
    id: String,
    text: String,
    imgSrc: String
  },
  data: function() {
    return {
      status: "0"
    };
  }
};
</script>
