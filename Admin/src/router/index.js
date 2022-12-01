import { createRouter, createWebHistory } from "vue-router";
import TrainView from "../views/TrainView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "train",
      component: TrainView,
    },
    {
      path: "/manage",
      name: "manage",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/ManageView.vue"),
    },
  ],
});

export default router;
