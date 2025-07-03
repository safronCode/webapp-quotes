import { defineStore } from "pinia";
import axios from "axios";
import {ref} from "vue";

export const useQuoteStore = defineStore('quoteStore', () => {
  const addLike = async (quoteId) => {
    return await axios.post('/api/like_add/', {quote_id: quoteId})
  }
  const removeLike = async (quoteId) => {
    return await axios.post('/api/like_remove/', {quote_id: quoteId})
  }
  const addDislike = async (quoteId) => {
    return await axios.post('/api/dislike_add/', {quote_id: quoteId})
  }
  const removeDislike = async (quoteId) => {
    return await axios.post('/api/dislike_remove/', {quote_id: quoteId})
  }

  const toggleLike = async (quoteId) => {
    try {
      if (await isQuoteLiked(quoteId)) {
        await removeLike(quoteId)
      } else {
        await addLike(quoteId)
      }
      await loadUserActivity(quoteId)
    }
    catch {
      // aaa
    }
  }

  const toggleDislike = async (quoteId) => {
    try {
      if (await isQuoteDisliked(quoteId)) {
        await removeDislike(quoteId)
      } else {
        await addDislike(quoteId)
      }
      await loadUserActivity(quoteId)
    }
    catch {
      // aaa
    }
  }

  const userActivity = ref(null)

  const loadUserActivity = async (quoteId) => {
    const {data} = await axios.get("/api/user_activity/", {params: {quote_id: quoteId}})
    userActivity.value = data
    return userActivity.value
  }

  const getUserActivity = async (quoteId, forceResponse=false) => {
    if (userActivity.value && !forceResponse) return userActivity.value
    return await loadUserActivity(quoteId)
  }

  const isQuoteLiked = async (quoteId) => {
    await loadUserActivity(quoteId)
    return userActivity.value.isLiked || false
  }

  const isQuoteDisliked = async (quoteId) => {
    await loadUserActivity(quoteId)
    return userActivity.value.isDisliked || false
  }

  const topQuotes = ref(null)

  const loadTopQuotes = async () => {
    const {data} = await axios.get("/api/quote_list/")

    topQuotes.value = data
    return topQuotes.value
  }

  const getTopQuotes = async (forceResponse=false) => {
    if (topQuotes.value && !forceResponse) return topQuotes.value
    return await loadTopQuotes()
  }

  const loadUserView = async (quoteId) => {
    return await axios.post("/api/view_add/", {quote_id: quoteId})
  }

  const getQuote = async (quoteId) => {
    const {data} = await axios.get("/api/get_quote/", {params: {quote_id: quoteId}})
    return data
  }

  return {
    loadUserView,
    getUserActivity,
    getTopQuotes,
    getQuote,
    isQuoteLiked,
    isQuoteDisliked,
    toggleLike,
    toggleDislike,
    userActivity,
    topQuotes,
  }
})