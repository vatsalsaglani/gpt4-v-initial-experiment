/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{html,js,svelte,ts}"],
  theme: {
    extend: {
      colors: {
        darkBlack: "#09090B",
      }
    },
  },
  plugins: [require("@tailwindcss/typography")],
};
