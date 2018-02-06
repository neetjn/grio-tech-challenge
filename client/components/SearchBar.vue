<template>
  <div class="field">
    <div class="control">
      <input class="input is-large has-text-centered"
             type="text"
             placeholder="Name, address, phone number..."
             autofocus />
    </div>
  </div>
</template>

<script>
  export default {
    name: 'SearchBar'
  }
</script>

<style lang="scss" scoped>
  input[type="text"] {
    @include shadow(2);
    max-width: 50rem;
    display: block;
    margin-left: auto;
    margin-right: auto;
    background-color: $color-dust;
    opacity: 0.1;
    &:focus {
      @include shadow(3);
      background-color: $color-ghost-white;
      color: black;
      opacity: 0.7;
    }
  }
</style>
