import { createRouter, createWebHashHistory, createWebHistory } from "vue-router";
import TrainView from "../views/TrainView.vue";
import AnalyticsView from "../views/AnalyticsView.vue";


const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "train",
      component: TrainView,
    },
    {
      path: "/analytics",
      name: "analytics",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: AnalyticsView,
    },
  ],
});

export default router;
