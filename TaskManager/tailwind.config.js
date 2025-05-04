/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./templates/**/*.html",          // Main templates folder
    "./**/templates/**/*.html",       // App-level templates
    "./static/**/*.js",    // Frontend HTML/JS
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

