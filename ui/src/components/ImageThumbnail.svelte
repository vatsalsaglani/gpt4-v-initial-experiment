<script>
  export let files = [];
</script>

<div class="flex space-x-4 mb-4">
  {#each files as image}
    <img
      class="w-24 h-24 object-cover rounded"
      src={URL.createObjectURL(image)}
      alt="Thumbnail"
    />
  {/each}
</div>
