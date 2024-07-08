import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import { createRouter, createWebHistory } from "vue-router";
import ReviewCard from "./components/ReviewCard.vue";
import ReviewList from "./components/ReviewList.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: ReviewCard,
  },
  {
    path: "/reviews",
    name: "reviews",
    component: ReviewList,
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  duplicateNavigationPolicy: "reload",
});

const app = createApp(App);
app.use(router);
app.mount("#app");
