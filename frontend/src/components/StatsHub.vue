<script setup>
import { ref } from 'vue'
import IconEmptyLike     from '@/components/icons/IconEmptyLike.vue'
import IconFilledLike    from '@/components/icons/IconFilledLike.vue'
import IconEmptyDislike  from '@/components/icons/IconEmptyDislike.vue'
import IconFilledDislike from '@/components/icons/IconFilledDislike.vue'
import IconViews from "@/components/icons/IconViews.vue";

/* счётчики; в реальном проекте придут с бэкенда  */
const likes     = ref(1)
const dislikes  = ref(0)

/* реакция текущего пользователя: null | 'like' | 'dislike'  */
const myVote = ref(null)

/* --- обработчики ---------------------------------------------------- */
function toggleLike () {
  if (myVote.value === 'like') {          // снимаем лайк
    likes.value--
    myVote.value = null
  } else {
    if (myVote.value === 'dislike') {     // был диз — убираем
      dislikes.value--
    }
    likes.value++
    myVote.value = 'like'
  }
  //  здесь можно сделать axios.post('/views/quote/123/vote', {like:myVote.value})
}

function toggleDislike () {
  if (myVote.value === 'dislike') {
    dislikes.value--
    myVote.value = null
  } else {
    if (myVote.value === 'like') {
      likes.value--
    }
    dislikes.value++
    myVote.value = 'dislike'
  }
}
</script>

<template>
  <!-- ряд иконок -->
  <div class="hearts">
    <button class="heart-btn" @click="toggleLike">
      <component
          :is="myVote==='like' ? IconFilledLike : IconEmptyLike"
          class="heart"
      />
    </button>

    <button class="heart-btn" @click="toggleDislike">
      <component
        :is="myVote==='dislike' ? IconFilledDislike : IconEmptyDislike"
        class="heart"
      />
    </button>

   <icon-views style="width:130px; height:130px" />



  </div>

  <!-- ряд счётчиков -->
  <div class="counters">
    <span class="counter" @click="toggleLike">likes: {{ likes }}</span>
    <span class="counter" @click="toggleDislike">disliked: {{ dislikes }}</span>
    <span class="counter">views: {{ likes }}</span>
  </div>
</template>

<style scoped>
/* --- расположение --------------------------------------------------- */
.hearts {
  display: flex;
  justify-content: center;
  gap: 115px;           /* чтобы цифры встали ровно под иконками */
  margin-top: 24px;
}
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

/* --- сами иконки ---------------------------------------------------- */
.heart-btn {
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
}
.heart {
  width: 128px;
  height: 128px;
  image-rendering: pixelated;
  transition: transform .1s;
}
.heart-btn:active .heart {
  transform: translateY(10px);            /* лёгкий «нажим» */
}

/* цифры тоже кликабельные */
.counter {
  cursor: pointer;
  user-select: none;
}
</style>
