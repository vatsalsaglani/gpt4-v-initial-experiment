<script>
  import { browser } from "$app/environment";
  import { onMount, onDestroy } from "svelte";
  export let selected = "";
  export let options = [];
  export let placeholder = "";
  $: search = "";
  $: filteredOptions = options;
  $: showDropdown = false;

  const handleSearch = (event) => {
    search = event.target.value;
    filteredOptions = options.filter((opt) =>
      opt.toLowerCase().includes(search.toLowerCase())
    );
    showDropdown = true;
  };

  const selectOption = (option) => {
    selected = option;
    search = option;
    showDropdown = false;
  };

  const handleClickOutside = (event) => {
    if (!event.target.closest(".dropdown")) {
      showDropdown = false;
    }
  };

  const handleFocus = () => {
    filteredOptions = [...options];
    showDropdown = true;
  };
  onMount(() => {
    if (browser) {
      window.addEventListener("click", handleClickOutside);
    }
  });

  onDestroy(() => {
    if (browser) {
      window.removeEventListener("click", handleClickOutside);
    }
  });
</script>

<div class="dropdown relative mb-4">
  <input
    type="text"
    {placeholder}
    class="w-full bg-transparent text-white rounded-t border border-gray-300 focus:outline-none focus:border-sky-500 text-base px-4 py-2"
    on:input={handleSearch}
    on:focus={handleFocus}
    on:click={handleFocus}
    value={search}
  />
  {#if showDropdown}
    <div
      class="dropdown-menu absolute z-10 w-full bg-transparent rounded-b border border-gray-300 max-h-48 overflow-auto"
    >
      {#each filteredOptions as option}
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <!-- svelte-ignore a11y-no-static-element-interactions -->
        <div
          class="px-4 py-2 text-white cursor-pointer hover:bg-black"
          on:click={() => selectOption(option)}
        >
          {option}
        </div>
      {/each}
    </div>
  {/if}
  <!-- <input
    type="text"
    placeholder="Language..."
    class="w-full bg-gray-800 text-white rounded-b border border-gray-700 focus:outline-none focus:border-indigo-500 text-base px-4 py-2 mt-1"
    bind:value={selected}
  /> -->
</div>

<style>
  .dropdown:focus-within .dropdown-menu {
    display: block;
  }
</style>
