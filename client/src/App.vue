<template>
  <div id="app">
    <div class="columns">
      <div class="column">
        <div class="hero bg-dark hero-sm px-2">
          <div class="hero-body mx-2">
            <h1>Game of Thrones Season 8 Predictions</h1>
            <p>Who will site on the Iron Throne !?</p>
            <!--<div id="nav">
              <router-link to="/">Home</router-link>
            </div>-->
          </div>
        </div>
      </div>
    </div>
    <div class="container grid-lg">
      <div class="content">
        <router-view/>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
  .content {
    margin: 50px 0;
  }
</style>
