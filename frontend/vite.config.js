import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'


export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
  ],

  server: {
      origin: 'http://localhost:5173'
    },

  base: "/static/",

  build: {
    outDir: "./static/qoutehub/",
    manifest: "manifest.json",
    rollupOptions: {
      input: './src/main.js',
    },
  },


  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
})
