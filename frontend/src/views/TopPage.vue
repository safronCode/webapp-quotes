<script setup>
import { ref } from 'vue'
import IconFilledLike from "@/components/icons/IconFilledLike.vue";
import IconFilledDislike from "@/components/icons/IconFilledDislike.vue";
import IconViews from "@/components/icons/IconViews.vue";

const quotes = ref(
  Array.from({ length: 10 }, (_, i) => ({
    id: i + 1,
    text: 'If you live to be a hundred I want to live to be a hundred minus one day so I never have to live without you.',
    author: 'A. A. Milne',
    likes: 42,
    dislikes: 3,
    views: 128,
  }))
)
</script>

<template>
  <section class="tophub">
    <h1 class="page-title">Sorted by likes</h1>ccd

    <article
      v-for="q in quotes"
      :key="q.id"
      class="quote-card"
    >
      <p class="quote-text">“{{ q.text }}”</p>

      <footer class="meta">
        <span class="author">— {{ q.author }}</span>

        <div class="stats">
          <span> <icon-filled-like style="width:16px; height:16px" /> {{ q.likes }}</span>
          <span> <icon-filled-dislike style="width:16px; height:16px" /> {{ q.dislikes }}</span>
          <span> <icon-views style="width:16px; height:16px" /> {{ q.views }}</span>
        </div>
      </footer>
    </article>
  </section>
</template>

<style scoped>
.tophub {
  max-width: 900px;
  margin: 0 auto;
  padding: 32px 16px;
  display: flex;
  flex-direction: column;

}

.page-title {
  font-family: 'EpilepsySans', monospace;
  font-size: 64px;
  text-align: center;
  margin-bottom: 24px;
  color: #000;
  text-shadow: 4px 4px 10px rgba(0, 0, 0, .35);
}

.quote-card {
  border: 4px solid rgba(0, 0, 0, .35);
  padding: 24px;
  background: rgba(255, 255, 255, .15);
  backdrop-filter: blur(4px);
  image-rendering: pixelated;
}

.quote-text {
  font-family: 'EpilepsySans', monospace;
  font-size: 24px;
  margin-bottom: 16px;
}

.meta {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  font-family: 'EpilepsySans', monospace;
  font-size: 18px;
}

.stats {
  display: flex;
  gap: 24px;
}
</style>
