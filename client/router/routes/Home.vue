<template>
  <section class="hero is-black is-fullheight">
    <div class="hero-head">
      <nav class="navbar">
        <div class="container">
          <div class="navbar-brand">
            <a class="navbar-item" href="https://github.com/neetjn/grio-tech-challengen">
              <i class="ico ico-left ico-xl fi-social-github fi-2x"></i> <span class="logo-text">Fork</span>
            </a>
            <span class="navbar-burger burger" data-target="navbarMenuHeroA">
              <span></span>
              <span></span>
              <span></span>
            </span>
          </div>
          <div id="navbarMenuHeroA" class="navbar-menu">
            <div class="navbar-end">
              <a class="navbar-item" href="https://www.linkedin.com/in/john-nolette-69ba72132/" target="_blank">
                <i class="ico ico-left ico-xl fi-social-linkedin"></i> Linkedin
              </a>
              <a class="navbar-item" href="https://github.com/neetjn" target="_blank">
                <i class="ico ico-left ico-xl fi-social-github"></i> Github
              </a>
              <a class="navbar-item" href="https://twitter.com/neet_jn" target="_blank">
                <i class="ico ico-left ico-xl fi-social-twitter"></i> Twitter
              </a>
            </div>
          </div>
        </div>
      </nav>
    </div>

    <!-- Hero content: will be in the middle -->
    <div class="hero-body">
      <div class="container has-text-centered">
        <h1 class="title animated fadeInUp">
          Search <i class="ico fi-magnifying-glass animated flip"></i>
        </h1>
        <h2 class="subtitle">
          <SearchBar class="animated fadeInDown" />
        </h2>
      </div>
    </div>

    <!-- Hero footer: will stick at the bottom -->
    <div class="hero-foot has-text-centered">
      <span id="user-count" /> Records
      <h1>Web App by John Nolette</h1>
      <img id="vue-logo" src="../../assets/images/vue.svg" />
    </div>
  </section>
</template>

<script>
  import SearchBar from '@/components/SearchBar.vue'
  import anime from 'animejs'

  export default {
    name: 'Home',
    components: { SearchBar },
    mounted: function() {
      anime({
        targets: '#user-count',
        textContent: 1000,
        round: 1,
        easing: 'easeInOutExpo'
      })
    }
  }
</script>

<style lang="scss" scoped>
  .hero-body {
    padding-bottom: 12rem;
    & h1 {
      padding-bottom: 1.5rem;
    }
  }
  .hero-foot {
    padding-bottom: 2rem;
  }
  #vue-logo {
    width: 5rem;
    display: block;
    margin-left: auto;
    margin-right: auto;
  }
</style>
