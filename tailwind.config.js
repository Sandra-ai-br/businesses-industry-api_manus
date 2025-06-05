/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#1A5276',
        'primary-light': '#2874A6',
        'neutral-light': '#F2F3F4',
        'neutral-dark': '#566573',
        success: '#48C9B0',
        warning: '#F39C12',
      },
    },
  },
  plugins: [],
}
