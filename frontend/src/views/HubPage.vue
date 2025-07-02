<script setup>
import { inject, computed } from 'vue'
import StatsHub from '@/components/StatsHub.vue'

const currentTheme = inject('currentTheme')

const wishText = computed(() => {
  switch (currentTheme?.value) {
    case 'morning':  return 'Доброго утра'
    case 'day':      return 'Доброго дня'
    case 'evening':  return 'Доброго вечера'
    case 'night':
    default:         return 'Доброй ночи'
  }
})

const wishStyles = {
  morning: { "font-family": 'EpilepsySans, sans-serif', "font-size": '60px',
             "color": 'rgba(22, 22, 46, 1)',             "text-shadow": '4px 4px 10px rgb(0, 0, 0)' },
  day    : { "font-family": 'EpilepsySans, sans-serif', "font-size": '60px',
             "color": 'rgba(16, 61, 220, 1)',            "text-shadow": '4px 4px 10px rgb(11, 36, 122)' },
  evening: { "font-family": 'EpilepsySans, sans-serif', "font-size": '60px',
             "color": 'rgba(255, 215, 0, 1)',            "text-shadow": '4px 4px 10px rgba(255, 215, 0, 0.8)' },
  night  : { "font-family": 'EpilepsySans, sans-serif', "font-size": '60px',
             "color": 'rgba(109,18,251,0.86)',           "text-shadow": '4px 4px 10px rgba(134, 7, 209, 0.8)' },
}

const quoteStyles = {
  morning: { "text-align": 'left',  "font-family": 'EpilepsySans, sans-serif', "font-size": '25px',
             "color": 'rgba(6, 21, 74, 1)',            "text-shadow": '4px 4px 10px rgb(0, 0, 0)' },
  day    : { "text-align": 'left',  "font-family": 'EpilepsySans, sans-serif', "font-size": '25px',
             "color": 'rgba(9, 38, 136, 1)',           "text-shadow": '4px 4px 10px rgb(4, 17, 57)' },
  evening: { "text-align": 'left',  "font-family": 'EpilepsySans, sans-serif', "font-size": '25px',
             "color": 'rgba(168, 142, 0, 1)',          "text-shadow": '4px 4px 10px rgba(255, 215, 0, 0.8)' },
  night  : { "text-align": 'left',  "font-family": 'EpilepsySans, sans-serif', "font-size": '25px',
             "color": 'rgba(103,18,152,0.86)',         "text-shadow": '4px 4px 10px rgba(134, 7, 209, 0.8)' },
}

const sourceStyles = {
  morning: { "text-align": 'right', "font-family": 'EpilepsySans, sans-serif', "font-size": '20px',
             "color": 'rgba(6, 21, 74, 1)',            "text-shadow": '4px 4px 10px rgb(0, 0, 0)' },
  day    : { "text-align": 'right', "font-family": 'EpilepsySans, sans-serif', "font-size": '20px',
             "color": 'rgba(9, 38, 136, 1)',           "text-shadow": '4px 4px 10px rgb(4, 17, 57)' },
  evening: { "text-align": 'right', "font-family": 'EpilepsySans, sans-serif', "font-size": '20px',
             "color": 'rgba(168, 142, 0, 1)',          "text-shadow": '4px 4px 10px rgba(255, 215, 0, 0.8)' },
  night  : { "text-align": 'right', "font-family": 'EpilepsySans, sans-serif', "font-size": '20px',
             "color": 'rgba(103,18,152,0.86)',         "text-shadow": '4px 4px 10px rgba(134, 7, 209, 0.8)' },
}

const currentWishStyle   = computed(() => wishStyles   [currentTheme?.value])
const currentQuoteStyle  = computed(() => quoteStyles  [currentTheme?.value])
const currentSourceStyle = computed(() => sourceStyles [currentTheme?.value])

</script>

<template>
  <div class="quote-container">
    <span :style="currentWishStyle"> {{ wishText }}, интернет-путник! {{props}}</span>
    <p :style="currentQuoteStyle"> If you live to be a hundred I want to live to be a hundred minus one day so I never have to live without you. They're right to think that about me because I'm the person most likely to sleep with my female fans I genuinely love other women. And I think they know that. If you live to be a hundred I want to live to be a hundred minus one day so I never have to live without you. They're right to think that about me because I'm the person most likely to sleep with my female fans I genuinely love other women. And I think they know that.</p>
    <p :style="currentSourceStyle"> ~ 65465 </p>
    <stats-hub/>
  </div>
</template>

<style scoped>
.quote-container {
  position: absolute;
  top: 25%;
  left: 40%;
  max-width: 800px;
}
</style>