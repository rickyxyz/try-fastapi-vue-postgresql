<!-- This file is not supposed to be seen by end user, so making this pretty is not a priority 🙂 -->

<script setup>
import { ref, onMounted } from 'vue'
import axios from '../axios'
import Loading from './Loading.vue'

const reviews = ref([])
const loading = ref(false)

const fetchReviews = async () => {
    try {
        loading.value = true
        const response = await axios.get('/reviews/')
        reviews.value = response.data
    } catch (error) {
        console.error('Error fetching reviews:', error)
        alert("Failed to fetch review data")
    } finally {
        loading.value = false
    }
}

const formatCreatedAt = (createdAt) => {
    const date = new Date(createdAt)
    return `${date.toLocaleDateString()} ${date.toLocaleTimeString()}`
}

onMounted(() => {
    fetchReviews()
})
</script>

<template>
    <div class="reviews-table">
        <h2>Review Data</h2>
        <Loading :loading="loading" />
        <table v-if="!loading">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Rating</th>
                    <th>Created At</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="review in reviews" :key="review.id">
                    <td>{{ review.id }}</td>
                    <td>{{ review.rating }}</td>
                    <td>{{ formatCreatedAt(review.created_at) }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<style scoped>
.reviews-table {
    margin-top: 20px;
    background-color: #ffffff;
    padding: 2rem;
    border-radius: 1rem;
    box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);

}

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 10px;
}

th,
td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}

th {
    background-color: #f2f2f2;
}
</style>
