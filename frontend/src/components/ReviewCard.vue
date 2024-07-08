<script setup>
import { ref } from 'vue'
import axios from '../axios'
import Loading from './Loading.vue'

const selectedRating = ref(0)
const hoveredRating = ref(0)
const loading = ref(false)
const showThankYou = ref(false)
const errorMessage = ref('')

const setRating = (rating) => {
  selectedRating.value = rating
}

const handleMouseOver = (rating) => {
  hoveredRating.value = rating
}

const handleMouseLeave = () => {
  hoveredRating.value = 0
}

const submitRating = async () => {
  try {
    loading.value = true
    const response = await axios.post('/reviews/', { rating: selectedRating.value })
    if (response.status === 200) {
      showThankYou.value = true
    } else {
      errorMessage.value = `Server responded with ${response.status}`
    }
  } catch (error) {
    console.error('Error submitting rating:', error)
    if (error.response) {
      // Technically speaking, error code 400 should be handled separately, but this application is simple enough that I think it is fine to just lump 400 and 500 together.
      if (error.response.status >= 500 || error.response.status >= 400) {
        errorMessage.value = "Oops, something went wrong on our end, don't worry nothing is wrong on your end. Please try again later."
      }
    } else {
      errorMessage.value = "You don't seem to be connected to the internet. Please check your internet connection."
    }
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="card">
    <p>How would you rate your satisfaction<br>with our product?</p>
    <div class="stars">
      <ul class="stars__list">
        <li v-for="star in 5" :key="star">
          <i class="star" :class="{ active: star <= selectedRating, hovered: star <= hoveredRating }"
            @click="setRating(star)" @mouseover="handleMouseOver(star)" @mouseleave="handleMouseLeave"></i>
          <span class="star-number">{{ star }}</span>
        </li>
      </ul>
      <div class="star__labels">
        <span>Very Dissatisfied</span>
        <span>Very Satisfied</span>
      </div>
    </div>
    <button @click="submitRating" v-if="!showThankYou">Submit Rating</button>
    <Loading :loading="loading" />

    <div v-if="showThankYou" class="thank-you-message">
      Thank you for your feedback!<br>
      <a href="/" class="reload-link">Click here to rate again</a>
    </div>

    <div v-if="errorMessage" class="error-message">
      {{ errorMessage }}
    </div>
  </div>
</template>

<style scoped>
.card {
  background-color: #ffffff;
  padding: 1.2rem 2rem;
  border-radius: 1rem;

  display: flex;
  flex-direction: column;
  gap: 1.5rem;

  box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);
}

.card>p {
  text-align: center;
  font-weight: 700;
}

.stars {
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}

.stars__list {
  display: flex;
  justify-content: space-evenly;
  padding: 0;
  list-style: none;
  gap: 1rem;
}

.stars__list li {
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
}

.stars__list li span {
  font-size: 12px;
}

.star {
  position: relative;
  display: inline-block;
  width: 0;
  height: 0;
  margin: 0 0.5em 1em;
  border-right: 0.3em solid transparent;
  border-bottom: 0.7em solid #ccc;
  border-left: 0.3em solid transparent;
  cursor: pointer;
  transition: border-bottom-color 0.3s;
  font-size: 20px;
}

.star:before,
.star:after {
  content: '';
  display: block;
  width: 0;
  height: 0;
  position: absolute;
  top: 0.6em;
  left: -1em;
  border-right: 1em solid transparent;
  border-bottom: 0.7em solid #ccc;
  border-left: 1em solid transparent;
  transform: rotate(-35deg);
  transition: border-bottom-color 0.3s;
}

.star:after {
  transform: rotate(35deg);
}

.star.active,
.star.active:before,
.star.active:after,
.star.hovered,
.star.hovered:before,
.star.hovered:after {
  border-bottom-color: #FC0;
}

.star__labels {
  display: flex;
  justify-content: space-between;
}

.star__labels span {
  font-size: 0.7rem;
}

button:hover {
  border-color: #646cff;
}

button:focus,
button:focus-visible {
  outline: 4px auto -webkit-focus-ring-color;
}

button {
  background-color: #007BFF;
  color: white;
  border: none;

  border-radius: 4px;
  border: 1px solid transparent;
  padding: 0.5em 0.9em;
  font-size: 1rem;
  font-weight: 500;
  font-family: inherit;
  cursor: pointer;
  transition: border-color 0.25s;
}

button:hover {
  background-color: #0056b3;
}

.reload-link {
  color: #007BFF;
  text-decoration: underline;
  cursor: pointer;
  margin-top: 0.5rem;
  display: inline-block;
}

.error-message {
  color: #c23232;
  width: 100%;
  max-width: calc(350px - 4.2rem);
  text-align: center;
}
</style>
