<script setup>
import {inject, computed, onMounted} from 'vue'
import StatsHub from '@/components/StatsHub.vue'
import {useQuoteStore} from "@/store/quoteStore.js";

const currentTheme = inject('currentTheme')

const wishText = computed(() => {
  switch (currentTheme?.value) {
    case 'morning': return 'Доброго утра'
    case 'day': return 'Доброго дня'
    case 'evening': return 'Доброго вечера'
    case 'night': return 'Доброй ночи'
    default: return 'Доброй ночи'
  }
})

const wishStyles = {
  morning: { "color": 'rgba(22, 22, 46, 1)', "text-shadow": '4px 4px 10px rgb(0, 0, 0)' },
  day: { "color": 'rgba(16, 61, 220, 1)', "text-shadow": '4px 4px 10px rgb(11, 36, 122)' },
  evening: { "color": 'rgba(255, 215, 0, 1)', "text-shadow": '4px 4px 10px rgba(255, 215, 0, 0.8)' },
  night: { "color": 'rgba(109,18,251,0.86)', "text-shadow": '4px 4px 10px rgba(134, 7, 209, 0.8)' },
}

const quoteStyles = {
  morning: { "color": 'rgba(6, 21, 74, 1)', "text-shadow": '4px 4px 10px rgb(0, 0, 0)' },
  day: { "color": 'rgba(9, 38, 136, 1)', "text-shadow": '4px 4px 10px rgb(4, 17, 57)' },
  evening: { "color": 'rgba(168, 142, 0, 1)', "text-shadow": '4px 4px 10px rgba(255, 215, 0, 0.8)' },
  night: { "color": 'rgba(103,18,152,0.86)', "text-shadow": '4px 4px 10px rgba(134, 7, 209, 0.8)' },
}

const sourceStyles = {
  morning: {"color": 'rgba(6, 21, 74, 1)', "text-shadow": '4px 4px 10px rgb(0, 0, 0)' },
  day: {"color": 'rgba(9, 38, 136, 1)', "text-shadow": '4px 4px 10px rgb(4, 17, 57)' },
  evening: {"color": 'rgba(168, 142, 0, 1)', "text-shadow": '4px 4px 10px rgba(255, 215, 0, 0.8)' },
  night: {"color": 'rgba(103,18,152,0.86)', "text-shadow": '4px 4px 10px rgba(134, 7, 209, 0.8)' },
}

const currentWishStyle = computed(() => wishStyles [currentTheme?.value])
const currentQuoteStyle = computed(() => quoteStyles [currentTheme?.value])
const currentSourceStyle = computed(() => sourceStyles [currentTheme?.value])


const backendData = JSON.parse(document.getElementById('initialData').textContent)

const quoteStore = useQuoteStore()

onMounted(() => {
  quoteStore.getUserActivity(backendData.quoteId)
  quoteStore.loadUserView(backendData.quoteId)
})

</script>

<template>
  <div class="quote-container">
    <span :style="{...currentWishStyle, 'font-size': '60px'}"> {{ wishText }}, интернет-путник! {{props}}</span>
    <p :style="currentQuoteStyle">{{backendData.text}}</p>
    <p :style="currentSourceStyle">~ {{backendData.source}}</p>
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

p {
  text-align: right;
  font-size: 25px;
}
</style>