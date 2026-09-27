# SNOWLINE · An Illustrated Alpine Journey

An interactive Three.js mountain landscape with free orbit, zoom, and a 52-second flight along the ridgeline.

## Run locally

Requires Node.js 20.19+ or a newer version supported by Vite. From the repository root:

```bash
npm ci
npm run dev
```

Open the local address printed in the terminal. Flight controls include pause, replay, and return to free roam. Press Space to play or pause, Esc to return, and M to toggle sound.

## Build and deploy

```bash
npm run build
npm run preview
```

Upload the generated `dist/` directory to a static web host. Relative asset paths support deployment under a subdirectory. Serve the site over HTTP rather than opening the HTML file directly.

## Files

- `src/`: scene, materials, camera, audio, interface, and styles.
- `public/models/snow_mountain_world.glb`: optimized runtime model, including cameras and flight animation.
- `public/environment/`: required painted sky and rock textures, generated for this project with AI image tools.
- `index.html`, `vite.config.js`, `package.json`, and `package-lock.json`: entry point and reproducible build configuration.

Three.js is the runtime dependency and Vite is the build tool. The Meshopt decoder is bundled with Three.js. All runtime assets are included locally; no CDN is required. Audio is synthesized in the browser.

This branch contains only the web application. Blender projects, authoring scripts, reference videos, source textures, screenshot reports, and skill directories are excluded.
