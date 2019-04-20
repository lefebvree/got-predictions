<template>
  <div id="app">
    <div class="container grid-lg">
       <div class="columns">
        <div class="column">
          <div class="title hero hero-sm px-2">
            <div class="hero-body mx-2">
              <h1>Game of Thrones Season 8 Predictions</h1>
              <h4>Who will site on the Iron Throne !?</h4>
              <!--<div id="nav">
                <router-link to="/">Home</router-link>
              </div>-->
            </div>
          </div>
        </div>
      </div>
      <div class="content">
        <router-view/>
      </div>
    </div>
  </div>
</template>

<style lang="scss">

  #app {
    background-image: url('/img/bg_pattern.png');
  }

  .title {
    color: #eee;
  }

  .container {
    padding: 35px 0;
  }

  .content h3 {
    padding: 35px 50px 25px;
    font-weight: bold;
  }

  .content .accordion input:checked ~ .accordion-body, .content .accordion[open] .accordion-body {
    max-height: none;
  }
</style>
