# 图像、色板与许可来源

- `painted-sky.png`：本项目使用内置 imagegen 生成，2026-09-26。用于远处绘本天空，不含地形。原始输出完整保留，网页仅投影其有效天空区域。无第三方摄影 HDRI。
- `Hero_*`、`Midground_*`、`Background_*` 颜色图：由制作脚本、雪岩画笔路径及下方生成的岩石源材质烘焙。mask 与 normal 是制作数据，分别用于雪岩分布和表面凹凸。
- 笔触为脚本辅助绘制，并非声称艺术家使用数位板逐笔绘制。用户可编辑画笔路径、颜色和源文件继续制作。
- 输入视频由用户提供，仅作为形态参考，不作为网页素材分发。

天空生成提示词：

> Seamless horizontally wrapping 2:1 equirectangular sky texture for a real-time alpine mountain world. Only painted sky, no mountains, land, silhouettes, objects, text, border. European graphic-novel / gouache illustration aesthetics. Muted dusty blue upper sky #718EA9, pale warm cream and lavender near horizon, restrained dry brush texture. Broad elongated ivory clouds with blue-violet underside, generous negative space. Lower half quiet pale blue gray #B8C5D6. Matching left/right edges. Not photographic, not anime, no black outlines, no sun disc.


## 2026-09-27 岩壁材质重做

`alpine-rock-painted.png`：使用内置 imagegen 模式生成的新绘制岩石材质，未使用第三方扫描素材。原始输出保持不变并复制入项目；Blender 使用三向投射后烘焙到地形 UV，进入标准 GLB Base Color 材质。不是把一张山体图片贴到屏幕上。

原始文件：`/Users/yuhng/.codex/generated_images/01a0dfe0-69ec-72a3-9dfe-cc90aeb3dbdd/exec-4fbd02b1-7ab9-4489-bd4a-ea6f2e5b5fec.png`。

生成提示词：

> Square seamless tileable albedo texture for a polished alpine exploration video game, not a scene or mountain image. A flat wall of fractured alpine slate and gneiss, dense irregular interlocking angular rock plates and long diagonal cracks, natural layered mineral grain. Premium hand-painted PBR base color, European graphic novel environmental painting, crisp shaped brushwork and convincing geological detail, restrained stylization. Medium cool gray stone, slate blue shadows in narrow cracks, subtle warm taupe mineral bands; mostly middle values, no pure black or pure white. Flat orthographic surface filling every pixel, approximately 4 meters of rock across. Flat diffuse uniform ambient light, no baked directional cast shadows, no specular highlights, no vignette. No snow, plants, sky, ground horizon, showcase ball, text, frame, grid, regular stripes, isolated boulders or repeating simple polygon shapes. Entire square opaque texture, edges designed to tile.
