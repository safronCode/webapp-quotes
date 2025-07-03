<script setup>
import { ref, onMounted, onUnmounted, provide, computed } from 'vue'
import { useRoute } from 'vue-router'

const currentTheme = ref('')

const THEMES = [
  { start: 5, end: 12, name: 'morning' },
  { start: 12, end: 18, name: 'day' },
  { start: 18, end: 22, name: 'evening' },
  { start: 22, end: 24, name: 'night' },
  { start: 0, end: 5, name: 'night' },
]

const calculateCurrentTheme = () => {
  const hour = new Date().getHours()
  currentTheme.value =
    THEMES.find(({ start, end }) => hour >= start && hour < end)?.name ?? 'night'
}

let intervalId

onMounted(() => {
  calculateCurrentTheme()
  intervalId = setInterval(calculateCurrentTheme, 60_000)
})

onUnmounted(() => clearInterval(intervalId))

provide('currentTheme', currentTheme)

const themeSeparate = {
  light: ['day', 'morning'],
  dark: ['evening', 'night'],
}

const route = useRoute()
const pageTitle = computed(() => route.meta?.title ?? '')
</script>

<template>
  <div :class="['page-wrapper', `page-wrapper--${currentTheme}`]">
    <span
      class="page-title"
      :style="{color: themeSeparate.light.includes(currentTheme) ? 'rgba(0, 0, 0, 0.86)' : 'rgba(255, 255, 255, 0.86)'}"
    >
      {{pageTitle}}
    </span>
    <a href="/accounts/login/" class="login-link">LogIn</a>
    <slot />
  </div>
</template>

<style scoped>
.page-wrapper {
  position: relative;
  min-height: 100vh;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-attachment: fixed;

  padding-top: 2.5%;
  text-align: center;
}

.login-link {
  position: absolute;
  right: 60px;
  font-size: 72px;
  text-decoration: none;
}

.page-wrapper--morning {
    background-image: url('@/assets/images/bg_morning.png');
    color: #16162e;
    text-shadow: 4px 4px 10px rgb(0, 0, 0);
}

.page-wrapper--day     {
    background-image: url('@/assets/images/bg_day.png');
    color: #092688;
    text-shadow: 4px 4px 10px rgb(4, 17, 57);
}

.page-wrapper--evening {
    background-image: url('@/assets/images/bg_evening.png');
    color: rgba(168, 142, 0, 0.86);
    text-shadow: 4px 4px 10px rgba(255, 215, 0, 0.8);
}

.page-wrapper--night   {
    background-image: url('@/assets/images/bg_night.png');
    color: rgba(100, 0, 168, 0.86);
    text-shadow: 4px 4px 10px rgba(134, 7, 209, 0.8);
}


.page-title {
  text-align: center;
  font-weight: bold;
  font-size: 72px;
  letter-spacing: .15em;
  text-shadow: 4px 4px 10px rgba(211, 165, 239, 0.8);
}
</style>
