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
    background-color: $color-dust;
    opacity: 0.1;
    &:focus {
      @include shadow(3);
      padding: 2.5rem;
      background-color: $color-ghost-white;
      opacity: 0.7;
    }
  }
</style>
