<script setup>
import IconViews from "@/components/icons/IconViews.vue";
import ActionButton from "@/components/ActionButton.vue";
import {useQuoteStore} from "@/store/quoteStore.js";
import {computed, onMounted, ref} from "vue";


const quoteStore = useQuoteStore()
const backendData = JSON.parse(document.getElementById('initialData').textContent)

const quoteId = backendData.quoteId
const quoteInfo = ref(null)

const likes = computed(() => {
  return quoteInfo.value?.like_cnt || 0
})

const dislikes = computed(() => {
  return quoteInfo.value?.dislike_cnt || 0
})

const views = computed(() => {
  return quoteInfo.value?.view_cnt || 0
})

const toggleLikeAndResponse = async (quoteId) => {
  await quoteStore.toggleLike(quoteId)
  quoteInfo.value = await quoteStore.getQuote(quoteId)
}

const toggleDislikeAndResponse = async (quoteId) => {
  await quoteStore.toggleDislike(quoteId)
  quoteInfo.value = await quoteStore.getQuote(quoteId)
}

onMounted(async () => {
  quoteInfo.value = await quoteStore.getQuote(quoteId)
})

</script>

<template>
  <div style="display: flex; flex-direction: row; align-items: center; justify-content: space-between">
    <action-button @click="toggleLikeAndResponse(quoteId)" type="like">
      <template #bottom-text>
        <span class="counter">likes: {{ likes }}</span>
      </template>
    </action-button>
    <action-button @click="toggleDislikeAndResponse(quoteId)" type="dislike">
      <template #bottom-text>
        <span class="counter">disliked: {{ dislikes }}</span>
      </template>
    </action-button>
    <div style="display: flex; flex-direction: column; justify-content: center">
      <icon-views style="width:130px; height:130px" />
      <span class="counter">views: {{ views }}</span>
    </div>
  </div>
</template>

<style scoped>
.counters {
  display: flex;
  justify-content: center;
  gap: 140px;
  font-family: 'EpilepsySans', monospace;
  font-size: 32px;
  text-decoration: underline;
  margin-top: 8px;
  color: #ffffff;
  text-shadow: 2px 2px 6px rgba(0,0,0,.35);
}

.counter {
  user-select: none;
  text-align: center;
}
</style>
