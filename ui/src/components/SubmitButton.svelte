<script>
  import Spinner from "./Spinner.svelte";
  import { createEventDispatcher } from "svelte";
  export let text = "Submit";
  export let isLoading = false;
  const dispatch = createEventDispatcher();

  const onClick = () => {
    dispatch("click");
  };
</script>

<button
  class="flex mx-auto text-white bg-sky-400 border-0 py-2 px-8 focus:outline-none hover:bg-sky-700 rounded text-lg {isLoading
    ? 'disabled:opacity-50 disabled:cursor-not-allowed'
    : ''}"
  type="submit"
  on:click={onClick}
  disabled={isLoading}
>
  {#if isLoading}
    <Spinner />
  {:else}
    {text}
  {/if}
</button>
