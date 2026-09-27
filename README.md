# SNOWLINE · 雪线山间绘本

交互式 Three.js 雪山网页，支持自由环绕、缩放和约 52 秒的山脊飞行。

## 本地运行

需要 Node.js 20.19+（或 Vite 支持的新版本）。在仓库根目录执行：

```bash
npm ci
npm run dev
```

打开终端显示的本地地址。开始飞行后支持暂停、重播和返回自由观察。空格播放／暂停，Esc 返回，M 切换声音。

## 构建与部署

```bash
npm run build
npm run preview
```

将生成的 `dist/` 上传至静态网页托管服务即可。相对资源路径支持子目录部署；请通过 HTTP 服务访问，不要直接双击 HTML。

## 文件

- `src/`：场景、材质、镜头、音效、界面和样式。
- `public/models/snow_mountain_world.glb`：网页必需的优化模型，包含相机及飞行动画。
- `public/environment/`：网页必需的绘制天空及岩石纹理，由项目使用 AI 图像工具生成。
- `index.html`、`vite.config.js`、`package.json`、`package-lock.json`：网页入口与可复现构建配置。

运行依赖为 Three.js，构建工具为 Vite。模型的 Meshopt 解码器随 Three.js 打包；资源全部本地交付，不依赖 CDN。音效在浏览器内合成。

本分支仅保留网页交付内容，不包含 Blender 工程、制作脚本、参考视频、源贴图、截图报告或技能目录。
