<script setup>
import IconFilledDislike from "@/components/icons/IconFilledDislike.vue";
import IconEmptyDislike from "@/components/icons/IconEmptyDislike.vue";
import IconFilledLike from "@/components/icons/IconFilledLike.vue";
import IconEmptyLike from "@/components/icons/IconEmptyLike.vue";
import {computed} from "vue";
import {useQuoteStore} from "@/store/quoteStore.js";

const props = defineProps({
  type: {
    type: String,
    required: true,
  },
})

const typeIconMap = {
  dislike: {
    active: IconFilledDislike,
    inactive: IconEmptyDislike
  },
  like: {
    active: IconFilledLike,
    inactive: IconEmptyLike
  }
}

const quoteStore = useQuoteStore()
const quoteId = JSON.parse(document.getElementById('initialData').textContent).quoteId

const active = computed(() => {
  if (props.type === 'like') {
    return quoteStore.isQuoteLiked(quoteId)
  } else if (props.type === 'dislike') {
    return quoteStore.isQuoteDisliked(quoteId)
  } else {
    return false
  }
})

</script>

<template>
  <div style="display: flex; flex-direction: column">
    <button>
      <component
        style="cursor: pointer"
        :is="typeIconMap[props.type]?.[active ? 'active' : 'inactive']"
      />
    </button>
    <slot name="bottom-text"/>
  </div>
</template>

<style scoped>
button {
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  width: 128px;
  height: 128px;
  image-rendering: pixelated;
  transition: transform .1s;
}

button:active button {
  transform: translateY(10px);
}
</style>