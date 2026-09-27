# SnowMountain

An interactive, painterly 3D alpine world built with Three.js, featuring cinematic mountain flights, ambient audio, and free camera exploration.

## Run locally

Use Node.js 22.12+ (or a newer supported LTS release).

```sh
npm ci
npm run dev
```

Open http://127.0.0.1:5183 in your browser.

## Controls

- Drag to orbit and scroll to zoom.
- Use the flight controls or Space to start or pause the flight.
- Press Esc to return to free exploration.
- Press M to toggle audio, or use the sound controls to adjust the volume.

Audio starts after a user interaction.

## Production build

```sh
npm run build
npm run preview
```

The production website is generated in `dist/`. Deploy its contents to a static web host.

## Project files

- `src/`: scene rendering, camera controls, procedural audio, and styles.
- `public/models/snow_mountain_world.glb`: self-contained mountain model.
- `public/environment/painted-sky.png`: painted sky texture.

The website runs without the original Blender files, reference media, or authoring tools. Keep both public assets to preserve the complete scene.

## License

See [LICENSE](LICENSE).
