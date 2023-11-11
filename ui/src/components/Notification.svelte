<script>
  // @ts-nocheck

  import { fly } from "svelte/transition";
  import { cubicOut } from "svelte/easing";

  export let direction = "top-right"; // default position
  export let type = "info"; // default type
  export let timeout = 3000; // default timeout (3 seconds)
  export let message = ""; // notification message

  let visible = true;

  const colors = {
    info: "bg-blue-500",
    warning: "bg-yellow-500",
    success: "bg-green-500",
    error: "bg-red-500",
    blue: "bg-blue-700",
    yellow: "bg-yellow-700",
    orange: "bg-orange-500",
  };

  let colorClass = colors[type];

  $: if (visible) {
    setTimeout(() => {
      visible = false;
    }, timeout);
  }

  $: colorClass = colors[type];

  const directions = {
    "top-left": { x: -100, y: -100 },
    "top-right": { x: 100, y: -100 },
    "bottom-left": { x: -100, y: 100 },
    "bottom-right": { x: 100, y: 100 },
    "top-center": { x: 0, y: -100 },
    "bottom-center": { x: 0, y: 100 },
  };

  let transitionDirection = directions[direction];

  $: transitionDirection = directions[direction];
</script>

{#if visible}
  <div
    class={`fixed p-4 rounded ${colorClass} text-white shadow-md z-50 ${
      direction === "top-left"
        ? "top-5 left-5"
        : direction === "top-right"
        ? "top-5 right-5"
        : direction === "bottom-left"
        ? "bottom-5 left-5"
        : direction === "bottom-right"
        ? "bottom-5 right-5"
        : direction === "top-center"
        ? "top-0 left-1/2 transform -translate-x-1/2"
        : "bottom-0 left-1/2 transform -translate-x-1/2"
    }`}
    transition:fly={{
      x: transitionDirection.x,
      y: transitionDirection.y,
      duration: 300,
      easing: cubicOut,
    }}
  >
    {message}
  </div>
{/if}
