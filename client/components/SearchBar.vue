<template>
  <div class="field">
    <div class="control">
      <input v-on:keypress="search"
             class="input is-large has-text-centered"
             type="text"
             placeholder="Name, address, phone number..."
             autofocus />
    </div>
  </div>
</template>

<script>
  export default {
    name: 'SearchBar',
    data() {
      return {
        queue: []
      }
    },
    methods: {
      search(e) {
        const self = this
        if (e.target.value) {
          self.$parent.$emit('searching')
          // # cancel active searchs in queue
          self.$data.queue.forEach(cancel => cancel())
          var cancelToken = self.$http.CancelToken
          self.$http.get(`${this.$grio.v1.people}?query=${e.target.value}`, {
            cancelToken: new cancelToken(function executor(c) {
              // # push cancel callback to queue for active search
              self.$data.queue.push(c)
            })
          }).then(response => self.$parent.$emit('completed', response.data.people))
        }
      }
    }
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
