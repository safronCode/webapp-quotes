<script setup>
import { RouterLink, RouterView } from 'vue-router'
import BackgroundLayout from "@/components/BackgroundLayout.vue";
</script>


<template>
  <background-layout>
    <router-view />

    <nav class="mc-nav">
      <RouterLink to="/"   class="mc-btn">Hub</RouterLink>
      <RouterLink to="/top" class="mc-btn">Top</RouterLink>
    </nav>
  </background-layout>
</template>

<style scoped>
.mc-nav {
  position: fixed;
  bottom: 0px;
  left: 2%;
  transform: translateY(20%);
  display: flex;
  gap: 0.1rem;
}


.mc-btn {

  width: 200px;
  height: 40px;

  display: flex;
  align-items: center;
  justify-content: center;

  font-family: monospace;
  font-size: 14px;
  letter-spacing: .05em;
  text-transform: uppercase;

  color: #fff;
  text-decoration: none;
  cursor: pointer;

  background: url('@/assets/images/btn1.png') no-repeat center / contain;

  transition: transform .1s;
}
.mc-btn:hover,
.mc-btn.router-link-active {
  background-image: url('@/assets/images/btn2.png');
}
.mc-btn:active {
  transform: translateY(2px);
}
</style>