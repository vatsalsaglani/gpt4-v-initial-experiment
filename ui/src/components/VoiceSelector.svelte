<script>
  export let selected = "";
  export let options = [
    "alloy",
    "echo",
    "fable",
    "onyx",
    "nova",
    "shimmer",
  ];
</script>

<div class="mb-4">
  <label>
    Select Voice
    <select
      bind:value={selected}
      class="w-full bg-gray-800 text-white rounded border border-gray-700 focus:outline-none focus:border-indigo-500 text-base px-4 py-2"
    >
      {#each options as option}
        <option value={option}>{option}</option>
      {/each}
    </select>
  </label>
</div>
