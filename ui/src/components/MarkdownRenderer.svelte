<script>
  import { marked } from "marked";

  export let markdown_content = ``;
</script>

<div class="prose prose-invert">
  {@html marked(markdown_content)}
</div>
