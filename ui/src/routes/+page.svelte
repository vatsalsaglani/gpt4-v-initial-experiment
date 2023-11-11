<script>
  // @ts-nocheck

  import TextInput from "../components/TextInput.svelte";
  import FileUpload from "../components/FileUpload.svelte";
  import LanguageSelector from "../components/LanguageSelector.svelte";
  import SubmitButton from "../components/SubmitButton.svelte";
  import ImageThumbnail from "../components/ImageThumbnail.svelte";
  import AudioPlayer from "../components/AudioPlayer.svelte";
  import LoadingSpinner from "../components/LoadingSpinner.svelte";
  import VoiceSelector from "../components/VoiceSelector.svelte";
  import SearchableDropdown from "../components/SearchableDropdown.svelte";
  import MarkdownRenderer from "../components/MarkdownRenderer.svelte";
  import Notification from "../components/Notification.svelte";

  $: toast = { visible: false, header: "", message: "" };
  $: showNotification = false;
  $: notificationTimeout = 3000;
  $: notificationMessage = "";
  $: notificationType = "";
  $: notificationPosition = "bottom-center";

  let inputText = "";
  let selectedLanguage = "English";
  let selectedVoice = "alloy";
  let audioSrc = "";
  let isLoading = false;
  const languageOptions = [
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
  const voiceOptions = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"];
  $: files = [];
  $: textResponse = ``;

  const triggerNotification = (type, message, position) => {
    notificationMessage = message;
    notificationPosition = position;
    notificationType = type;

    showNotification = true;

    setTimeout(() => {
      showNotification = false;
    }, notificationTimeout + 300);
  };

  const handleSubmit = async () => {
    textResponse = ``;
    audioSrc = "";

    if (!files.length > 0 || !inputText.trim().length > 3) {
      triggerNotification(
        "error",
        "Inputs Unavailable. Need at least one file and some text",
        "bottom-right"
      );
      return;
    }

    isLoading = true;
    const imageBase64 = await Promise.all(
      Array.from(files).map(
        (file) =>
          new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.readAsDataURL(file);
            reader.onload = () => resolve(reader.result);
            reader.onerror = (error) => reject(error);
          })
      )
    );
    const user_message_content = imageBase64.map((img64) => {
      return {
        type: "image_url",
        image_url: img64,
      };
    });
    user_message_content.push({ type: "text", text: inputText });
    const messages = [
      {
        role: "user",
        content: user_message_content,
      },
    ];
    try {
      const response = await fetch("http://localhost:5010/api/chat", {
        method: "POST",
        body: JSON.stringify({
          messages: messages,
          language: selectedLanguage,
          voice: selectedVoice,
        }),
        headers: {
          "Content-Type": "application/json",
        },
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      audioSrc = `data:audio/mpeg;base64,${data.voice_result}`;
      textResponse = data.text_result;
      //   const blob = await response.blob();
      //   audioSrc = URL.createObjectURL(blob);
    } catch (error) {
      console.error("Request Failed: ", error);
    } finally {
      isLoading = false;
    }
  };
</script>

<svelte:head>
  <title>Image2Text2Speech</title>
</svelte:head>

<div
  class="bg-darkBlack min-h-screen text-white p-4 items-center justify-center flex flex-col"
>
  <div class="container max-w-xl min-w-xl flex flex-col space-y-2">
    <div class="text-3xl font-bold mb-6">Image-to-Text-to-Speech</div>
    <div class="relative">
      <TextInput bind:value={inputText} />
      <div class="absolute bottom-6 right-0">
        <FileUpload bind:files />
      </div>
    </div>
    {#if files.length > 0}
      <ImageThumbnail {files} />
    {/if}
    <div class="flex justify-between space-x-2">
      <!-- svelte-ignore a11y-label-has-associated-control -->
      <label>
        Select Language
        <SearchableDropdown
          bind:selected={selectedLanguage}
          options={languageOptions}
          placeholder={"Search Language"}
        />
      </label>
      <!-- svelte-ignore a11y-label-has-associated-control -->
      <label>
        Select Voice
        <SearchableDropdown
          bind:selected={selectedVoice}
          options={voiceOptions}
          placeholder={"Search Voice"}
        />
      </label>
      <!-- <LanguageSelector bind:selected={selectedLanguage} /> -->
      <!-- <VoiceSelector bind:selected={selectedVoice} /> -->
    </div>
    <SubmitButton text="Submit" on:click={handleSubmit} {isLoading} />
    {#if audioSrc}
      <div class="grid grid-cols-2 gap-2">
        <MarkdownRenderer markdown_content={textResponse} />
        <AudioPlayer {audioSrc} />
      </div>
    {/if}
  </div>
</div>

{#if showNotification}
  <Notification
    message={notificationMessage}
    direction={notificationPosition}
    timeout={notificationTimeout}
    type={notificationType}
  />
{/if}
