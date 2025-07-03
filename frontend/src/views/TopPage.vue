<script setup>
import {onMounted, ref} from 'vue'
import IconFilledLike from "@/components/icons/IconFilledLike.vue";
import IconFilledDislike from "@/components/icons/IconFilledDislike.vue";
import IconViews from "@/components/icons/IconViews.vue";
import {useQuoteStore} from "@/store/quoteStore.js";
import {storeToRefs} from "pinia";

const quoteStore = useQuoteStore()

const {toggleLike, toggleDislike} = quoteStore

const {topQuotes} = storeToRefs(quoteStore)

const toggleLikeAndRequest = async (quoteId) => {
  await toggleLike(quoteId)
  await quoteStore.getTopQuotes(true)
}

const toggleDislikeAndRequest = async (quoteId) => {
  await toggleDislike(quoteId)
  await quoteStore.getTopQuotes(true)
}

onMounted(() => {
  quoteStore.getTopQuotes()
})
</script>

<template>
  <section class="tophub">
    <h1 class="page-title">Sorted by likes</h1>
    <article
      v-for="q in topQuotes"
      :key="q.id"
      class="quote-card"
    >
      <p class="quote-text">“{{ q.text }}”</p>

      <footer class="meta">
        <span class="author">— {{ q.source }}</span>

        <div class="stats">
          <button @click="toggleLikeAndRequest(q.id)" class="reaction-badge"><icon-filled-like class="button-image" />{{ q.like_cnt }}</button>
          <button @click="toggleDislikeAndRequest(q.id)" class="reaction-badge"><icon-filled-dislike class="button-image" />{{ q.dislike_cnt }}</button>
          <span class="reaction-badge"><icon-views class="button-image" />{{ q.view_cnt }}</span>
        </div>
      </footer>
    </article>
  </section>
</template>

<style scoped>
.button-image {
  width: 16px;
  height: 16px;
}

.reaction-badge {
  display: flex;
  flex-direction: row;
  gap: 4px;
}

button {
  font-family: 'EpilepsySans', sans-serif;
  font-size: 18px;
  outline: none;
  border: 0;
  background: transparent;
}

.tophub {
  max-width: 900px;
  margin: 0 auto;
  padding: 32px 16px;
  display: flex;
  flex-direction: column;

}

.page-title {
  font-size: 64px;
  text-align: center;
  margin-bottom: 24px;
  color: #ffffff;
  text-shadow: 4px 4px 10px rgba(87, 11, 168, 0.35);
}

.quote-card {
  border: 4px solid rgba(0, 0, 0, .35);
  padding: 24px;
  background: rgba(255, 255, 255, .15);
  backdrop-filter: blur(4px);
  image-rendering: pixelated;
}

.quote-text {
  font-size: 24px;
  margin-bottom: 16px;
}

.meta {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  font-size: 18px;
}

.stats {
  display: flex;
  gap: 24px;
}
</style>
