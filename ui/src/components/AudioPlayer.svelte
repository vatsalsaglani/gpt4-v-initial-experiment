<script>
  export let audioSrc = "";
</script>

{#if audioSrc}
  <div class="mt-4">
    <audio controls class="w-full" src={audioSrc} />
  </div>
{/if}
