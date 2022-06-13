<template>
  <NavBar class="h-10"/>
  <div class="h-90 main-container container-fluid">
    <div class="row h-100">
      <LeftBlock class="col-3"/>
      <RightBlock class="col-9"/>
    </div>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'
import LeftBlock from './components/LeftBlock.vue'
import RightBlock from './components/RightBlock.vue'

export default {
  name: 'App',
  components: {
    NavBar,
    LeftBlock,
    RightBlock
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-size: 16px;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100vh;
  background: linear-gradient(225.44deg, #96C1EE -8.16%, #F7F2E4 97.55%);
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}
.h-10{
  height:5%
}
.h-90{
  height:95%
}
</style>
