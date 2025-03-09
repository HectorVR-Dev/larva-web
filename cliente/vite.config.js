import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import fs from 'fs';
import path from 'path';

import tailwindcss from '@tailwindcss/vite'


export default defineConfig({
  plugins: [react(),
    tailwindcss(),
  ],
  // server: {
  //   https: {
  //     key: fs.readFileSync(path.resolve(__dirname, 'certs/key.pem')),
  //     cert: fs.readFileSync(path.resolve(__dirname, 'certs/cert.pem')),
  //   },
  //   host: '0.0.0.0', // Permite acceso desde LAN
  //   port: 5173,      // Puerto de tu servidor
  // },
})
