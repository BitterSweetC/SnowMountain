# 材质源与烘焙（第二版）

- `alpine-rock-painted.png`：imagegen 绘制的岩壁源图，完整保留；来源与提示词见 provenance.md。按世界空间三向投射到岩壁，减少陡坡拉伸，再烘焙到标准 UV 贴图。
- `paint-layout.json`：米制雪槽、雪坡、雪帽、裸岩窗路径，控制分布与边界。
- `*_color.png`：sRGB Base Color。当前远景 512²、中景 1024²、三个 Hero 地块 2048²。合成岩壁绘制源、大色块、雪岩遮罩和固定笔触，不包含实时主光投影。
- `*_normal.png`：九个核心地块的 Non-Color 切线空间法线，标准材质强度 .32。导出携带 TANGENT，不依赖浏览器临时猜测切线。
- `*_snowmask.png`：Non-Color 分布数据，供继续修改；已合成入运行材质。
- 标准 Roughness .94、Metallic 0；轮廓与大沟槽来自几何，法线只提供表面细节。
- `painted-sky.png`：保留完整 imagegen 原图及 alpha。网页只选择有效天空区域，不用于山体几何。

源图 PNG 保留；优化版 GLB 的颜色图使用 WebP quality 90，法线使用无损 WebP，纹理尺寸不变。WebP 减少传输文件体积，不等于降低解码后的显存占用。边界采用 ClampToEdge，笔触固定在 UV，未使用屏幕空间绘画滤镜。制作过程中旧尺寸资源可能仍保留，运行资产以最终 GLB 的内嵌贴图为准。
