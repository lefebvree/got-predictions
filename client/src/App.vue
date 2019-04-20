<template>
  <div id="app">
    <div class="container grid-lg">
       <div class="columns">
        <div class="column">
          <div class="title hero hero-sm px-2">
            <div class="hero-body mx-2">
              <router-link to="/"><h1>Game of Thrones Predictions</h1></router-link>
              <h5>Who dies, who survives, and who will site on the Iron Throne in the final season !?</h5>
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

  body {
    background-image: url('/img/bg_pattern.png') !important;
  }

  h1, h2, h3 {
    font-family: 'Roboto Slab', serif;
  }

  .container {
    padding: 35px 0;
  }

  .title, .title a {
    color: #eee !important;
    text-decoration: none !important;
  }

  .text {
    padding: 0 25px;
  }

  .panel-text {
    padding: 25px 50px;
  }

  .content h3 {
    padding: 35px 20px 25px;
    font-weight: bold;
  }

  .content .accordion .accordion-body, .content .accordion-body {
    overflow: visible;
  }

  .content .accordion input:not(:checked) ~ .accordion-body, .content .accordion[closed] .accordion-body {
    overflow: hidden;
  }

  .content .accordion input:checked ~ .accordion-body, .content .accordion[open] .accordion-body {
    max-height: none;
  }

</style>
