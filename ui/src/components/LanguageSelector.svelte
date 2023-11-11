<script>
  export let selected = "";
  // Populate with actual language options
  export let options = [
    "English",
    "Mandarin Chinese",
    "Hindi",
    "Spanish",
    "French",
    "Modern Standard Arabic",
    "Bengali",
    "Portuguese",
    "Russian",
    "Urdu",
    "Indonesian",
    "Standard German",
    "Japanese",
    "Nigerian Pidgin",
    "Egyptian Arabic",
    "Marathi",
    "Telugu",
    "Turkish",
    "Tamil",
    "Yue Chinese",
    "Vietnamese",
    "Wu Chinese",
    "Tagalog",
    "Korean",
    "Iranian Persian",
    "Hausa",
    "Swahili",
    "Javanese",
    "Italian",
    "Western Punjabi",
    "Gujarati",
    "Thai",
    "Kannada",
    "Amharic",
    "Bhojpuri",
    "Eastern Punjabi",
    "Min Nan Chinese",
    "Jin Chinese",
    "Levantine Arabic",
    "Yoruba",
  ];
</script>

<div class="mb-4">
  <label>
    Select Language
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
