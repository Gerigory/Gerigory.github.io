---
layout: post
title: "【GDC 2021】Procedural Grass in Ghost of Tsushima"
date: 2026-05-09
img: GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_001.png # Add image post (optional)
fig-caption: # Add figcaption (optional)
tags: [GDC, 2021, Rendering, Vegetation]
description: 本文分享的是【GDC 2021】GDC2021 - Procedural Grass in Ghost of Tsushima相关的技术要点
---

> 来源：D:\迅雷下载\YTDown_YouTube_Procedural-Grass-in-Ghost-of-Tsushima_Media_Ibe1JBF5i5Y_001_1080p.mp4
> PDF：D:\迅雷下载\Graphics Materials\GDC 2021 - Procedural Grass in Ghost of Tsushima.pdf
> 提取时间：2026-05-09 22:06:41

---

以下是《对马岛之魂》中草叶渲染技术的总结，分点说明关键实现细节：

---

### **1. 草叶生成与数据流**
- **计算着色器生成数据**：通过计算着色器动态生成草叶的位置、方向、变换数据，避免预设大量模型数据，节省内存。
- **程序化资产放置**：使用"生长系统"将艺术家创作的资产（如蜘蛛百合、潘帕斯草）程序化放置在场景中，仅需输出位置、方向等基础数据，由GPU实例绘制系统渲染。
- **LOD优化**：根据距离相机的远近，动态加载最近的3x3图块数据，远距离图块数据被丢弃，减少资源占用。

---

### **2. 顶点处理与动画**
- **贝塞尔曲线建模**：草叶的形状由贝塞尔曲线定义，顶点法线通过曲线导数与风向交叉计算，实现自然弯曲。
- **风系统**：基于2D Perlin噪声模拟风力，风向和强度由用户参数控制，草叶的摆动通过正弦波实现，相位偏移由叶片哈希值和位置决定，确保每片草叶运动独立。
- **动态法线调整**：
  - **视觉优化**：法线略微向外倾斜，使草叶更自然圆润。
  - **远距离抗锯齿**：随着距离增加，法线逐渐调整为草丛的平均法线，减少镜面高光噪点，同时降低光泽度参数抑制过度反光。

---

### **3. 光照与材质**
- **延迟渲染输出**：草叶数据写入G缓冲区，提供材质信息（漫反射、光泽度、半透明度、环境光遮挡）。
  - **漫反射纹理**：沿草叶长度和宽度变化，底部变暗、尖端褪色。
  - **光泽度纹理**：一维纹理沿草叶宽度拉伸，重复使用。
  - **半透明度与AO**：根部半透明度低，尖端逐渐减小；AO值在根部较暗，尖端较浅。
- **艺术家控制**：颜色变化由草丛（团块）控制，而非单个叶片，确保整体一致性。

---

### **4. 阴影优化**
- **地形冒充者系统**：为节省性能，使用地形顶点高度匹配草叶高度，通过抖动深度偏移模拟阴影密度，结合阴影过滤实现近似效果。
- **屏幕空间阴影补充**：对超薄草叶，利用屏幕空间阴影弥补细节，尽管无法处理物体厚度，但草叶本身透明度低，效果可接受。

---

### **5. 特殊功能与挑战**
- **隐身草机制**：部分草叶标记为"隐形草"，返回固定高度，用于玩家藏身时的光线投射检测（如《幽灵》中的刺杀玩法）。
- **远处LOD处理**：远距离草叶不渲染完整模型，改用艺术家创作的纹理贴图（如红色蜘蛛百合田），成本低且视觉效果良好。
- **性能权衡**：放弃SSAO用于草叶阴影，因草叶动态摆动导致SSAO时间累积效果混乱，改用地形冒充者系统。

---

### **6. 技术亮点与未来方向**
- **高效数据流**：通过计算着色器和GPU实例绘制，实现大规模草叶渲染的低开销。
- **艺术家协作**：程序化系统与艺术家创作资产结合，平衡自动化与手动细节控制。
- **未来改进**：进一步优化远距离LOD，探索更精细的法线调整和阴影方案，提升视觉一致性。

---

以上技术方案在《对马岛之魂》中实现了大规模草场的高效渲染，兼顾性能与视觉效果，同时为后续项目（如《幽灵》）提供了可复用的解决方案。


---

## Slide 1 — Title

![Slide 1](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_001.png)

**📌 要点汇总**
- (Content too short, no key points)

> 。


---

## Slide 2 — Intro

![Slide 2](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_002.png)

**📌 要点汇总**
- (Content too short, no key points)

> 经过。


---

## Slide 3 — Speaker Introduction

![Slide 3](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_003.png)

**📌 要点汇总**
- Introduction of procedural grass system for art direction in *Ghost of Tsushima*
- Live Q&A participation for questions during the video's release

> 我叫 Eric Wallaby，是 Sucker Punch Productions 的一名图形程序员。这次演讲是关于我们在《对马岛之魂》中使用的程序草系统，以实现我们的艺术指导目标。
>
> 快速说明：除非出现某些不可预见的情况，否则我将在该视频发布时参与该视频的实时问答聊天。因此，请随时在演讲中提出任何问题，我会尽快回答。


---

## Slide 3b — Speaker Introduction (visual)

![Slide 3b](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_004.png)


---

## Slide 3c — Speaker Introduction (visual)

![Slide 3c](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_005.png)


---

## Slide 4 — In-Game Demonstration

![Slide 4](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_006.png)

**📌 要点汇总**
- Traditional grass blocks limited wind animation and performance, leading to a switch to Altera's procedural grass rendering for better scalability
- System rendered ~83,000 individual grass blades with per-blade wind animation, achieving ~2ms rendering time per frame for 1M+ blades in scenes
- Grass system enabled artist-configurable parameters for diverse environments (Pampas grass, burned fields, flower fields) while maintaining wind interaction for directional gameplay cues
- Wind system integration allowed grass to react to player/enemy movement, enhancing environmental feedback and navigation guidance
- Procedural approach solved density/performance tradeoffs while maintaining artistic control over natural landscape depiction

> 《对马岛之魂》以古代日本海岸附近的对马岛为背景，从一开始，主要目标之一就是描绘该岛的自然美景。这意味着大量的树叶、轻轻摇曳的树木的巨大森林、绵延不绝的草山，以及介于两者之间的一切。艺术指导还决定倾向于绘画的感觉，例如，我们选择大片单一类型的花朵，而不是混合多种花朵、灌木和蕨类植物的田野，就好像用巨大的笔触画在那里一样。
>
> 很早很早就，我们尝试了传统的草块。由于几个原因，这些最终并不符合我们的目标。首先，风是我们真正想要推动的东西，而将我们的动画绑定到整个草块是非常有限的。其次，性能对于我们希望在世界中拥有的树叶密度来说是有问题的。大约在这个时候，我们发现了一个优秀的块。Altera 发布的名为程序草渲染的帖子启发了我们很多方法。在演讲结束时我将提供他们的博客文章的链接，我绝对建议您查看一下。
>
> 这就是我们的想法。该场景考虑了超过 100 万片草叶，并渲染了大约 83000 个草叶，每个草叶都单独随风产生动画，从头到尾大约需要两半毫秒。草是高度艺术家可配置的。我们使用相同的草系统。对于我们巨大的潘帕斯草田、烧毁的田地和巨大的花田，草与我们的风系统相互作用，帮助给玩家一种方向感，以支持我们的引导风机制，风的方向告诉玩家要去哪里。
>
> 草也会对穿过草丛的玩家和敌人做出反应。


---

## Slide 5 — Overview

![Slide 5](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_007.png)

**📌 要点汇总**
- Compute shaders handle parallel data processing and generate complex geometry, requiring structured data interfaces for efficient pipeline communication
- Vertex shaders transform vertex attributes (position, normals) via matrix operations, directly impacting rendering precision and performance
- Material parameters (reflectance, roughness) are dynamically computed by pixel shaders, which execute final lighting models for visual fidelity
- Production engines require shader management systems with version control, cross-platform compatibility, and modular design for pipeline integration
- Key challenges include ensuring data consistency between shader stages and optimizing performance through parameterization and code modularity

> 这就是我希望如何组织这次演讲。我们将首先讨论计算着色器产生的内容，然后讨论该信息如何传递。接下来将探讨顶点着色器及其处理机制，随后分析材质数据与像素着色器的协作方式。最后一部分将聚焦于一些关键要素，这些要素能够帮助我们将整个系统整合到实际的生产引擎中。那么让我们开始吧。


---

## Slide 6 — Compute Shader: Terrain LOD (1/3)

![Slide 6](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_008.png)


---

## Slide 7 — Compute Shader: Terrain LOD (2/3)

![Slide 7](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_009.png)

**📌 要点汇总**
- 我们的第一步是将世界切成瓷砖。


---

## Slide 8 — Compute Shader: Terrain LOD (3/3)

![Slide 8](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_010.png)

**📌 要点汇总**
- Tiles include terrain height, material, and grass type/height for rendering
- Grass parameters (type, height) are critical for realistic vegetation placement
- Texture layers enable detailed terrain customization in 3D environments

> 这些图块包含一系列纹理，例如地形的高度、渲染地形的材质，以及为了我们这里的目的，在该位置放置什么类型的草以及它应该有多高。


---

## Slide 9 — Compute Shader: Tile Subdivision

![Slide 9](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_010.png)

**📌 要点汇总**
- 纹理尺寸为52×52，对应约39厘米间距，确保渲染时视觉连续性
- 高密度纹素设计避免因采样间隔过大导致的纹理模糊问题
- 父图块纹理信息分解到子图块，实现多缩放级别的视觉质量一致性
- 通过子图块细分提升细节表现，平衡渲染性能与视觉保真度

> 这些图块进一步细分为我们实际渲染的图块。它们从其父图块中的纹理的子部分中进行采样。纹理是52乘52，这意味着我们每39厘米左右就有一个纹素。
>
> 这种纹素密度设计确保了在渲染时能够保持视觉连续性，同时避免了因采样间隔过大导致的纹理模糊问题。通过将父图块的纹理信息分解到更细粒度的子图块中，系统可以在不同缩放级别下维持一致的视觉质量。


---

## Slide 10 — Compute Shader: Placing a Grass Blade

![Slide 10](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_011.png)

**📌 要点汇总**
- Compute shader processes each render tile, assigning grid positions with random offsets to select grass locations
- Distance and frustum culling applied before texture sampling to determine grass type and height
- Tiles with invalid grass data (null type/zero height) are discarded early in the pipeline
- Occlusion culling implemented but later found to have minimal impact in most camera scenarios
- Texture sampling for grass attributes is critical for determining which tiles proceed to rendering

> 对于每个渲染图块，我们运行一个计算着色器。计算着色器中的每个线程都会在图块内的网格上获得一个位置，并添加随机偏移来选择草片的位置。一旦我们知道它在哪里，我们就会进行距离剔除和视锥体剔除。
>
> 之后，我们从前面提到的纹理中进行采样，以确定草的类型以及草的高度。具有空草类型或高度为零的图块将被丢弃。现在我们相当确定我们有草叶，我们进行遮挡剔除。
>
> 在项目后期，我们发现这在大多数镜头中都是一个小玩笑。


---

## Slide 11 — Compute Shader: Grass Type (1/2)

![Slide 11](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_012.png)


---

## Slide 12 — Compute Shader: Grass Type (2/2)

![Slide 12](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_013.png)

**📌 要点汇总**
- Each grass blade type uses specific artist-defined parameters stored in a 512x512 texture with 8-bit indices per tile
- Bilinear sampling fails due to meaningless interpolation between 4 distinct grass type indices
- Point sampling reveals visible pixelation in control texture due to discrete index mapping
- Custom solution uses weighted random selection based on proximity to 4 texture pixel centers for smoother transitions
- Weighted random approach reduces visible artifacts from low-resolution texture-driven grass type transitions

> 每个草叶都有一个特定的类型，这决定了它使用的艺术家创作的参数。每个图块都包含一个 512 x 512 纹理，该纹理将每个图块位置映射到对应的草地类型，并将对应的草地参数索引以 8 位格式存储到草地参数数组中。
>
> 我们无法对这些数据进行双线性采样，因为在最多四个不同索引之间进行插值是没有意义的。如果我们采用简单的点采样方法，会发现控制草类型的纹理中每个像素都清晰可见。
>
> 因此我们采取了另一种方案：首先收集所有可能的草类型，然后随机选择一种类型，并根据该位置相对于四个纹理像素中心的位置进行加权计算。与单纯的点采样相比，这种方法能实现更平滑的抖动过渡，这对于降低低分辨率纹理驱动草类型所造成的视觉明显度具有重要意义。


---

## Slide 13 — Compute Shader: Generating a Grass Blade

![Slide 13](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_014.png)

**📌 要点汇总**
- Each active channel stores 16 floats per blade: 3 for position, 2 for orientation (direction vector determining grass direction), and wind strength as an animation parameter.
- Position-based hash drives blade attributes (animation, grass type, art asset selection) and includes artist parameters, cluster info, and shape controls.
- Blade parameters are influenced by hash, cluster, wind, terrain slope, interacting objects, and camera position, with artist parameters dictating interaction rules per grass type.
- Artist parameters vary by grass type to control how blades respond to environmental factors and maintain visual consistency across different grass variants.

> 现在，对于仍处于活动状态的每个通道，我们为每个刀片实例填充16个浮点数数据：其中三个浮点数表示位置，两个浮点数表示刀片的朝向。这个方向向量决定了草叶指向的方向。我们将风的强度作为叶片位置的参数，这会驱动动画效果。
>
> 我们在每个刀片上放置一个基于位置的哈希值，用于驱动刀片上的各种属性，包括动画效果、草的类型（这决定了使用哪组美术资源）。除了这些，还包含艺术家参数、丛集信息（我将在此处详细介绍），以及用于控制刀片形状的各类参数。
>
> 这些参数受到多重因素影响：每个刀片的哈希值、所属的丛集、风力强度、底层地形的坡度、穿过草地并将其推开的物体，以及相机的位置等。刀片与这些因素的交互方式均由艺术家参数驱动，且这些参数的配置会根据草的类型产生差异。


---

## Slide 14 — Compute Shader: Clump Motivation

![Slide 14](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_015.png)

**📌 要点汇总**
- Pre-cluster code resulted in uniform, artificial grass fields lacking natural variation
- Randomness alone failed to replicate real-world factors like shade or soil nutrient differences
- Clustering enabled grouping of grass blades based on environmental parameters (e.g., nitrogen levels)
- Cluster membership influenced multiple parameters to create more realistic terrain variation
- Key lesson: Natural variation requires structured clustering, not pure randomness

> 我想提请注意我在上一张幻灯片中提到的簇值。在添加簇集代码之前，我们所有的场地看起来都像你想要打高尔夫球的草地。您可以增加每个草片的随机性，使其看起来更混乱，但它看起来并不更像自然场地。它看起来只是随机的。
>
> 实际场地有所不同。也许这个地区早上处于阴影中，草长得较少。也许这个地区土壤中的氮含量多一些，草长得更高。为了尝试并模仿这一点，我们决定将草组织成簇，并使用草片属于哪个簇来影响其他参数。


---

## Slide 15 — Compute Shader: Voronoi Algorithm (1/6)

![Slide 15](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_016.png)


---

## Slide 16 — Compute Shader: Voronoi Algorithm (2/6)

![Slide 16](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_017.png)


---

## Slide 17 — Compute Shader: Voronoi Algorithm (3/6)

![Slide 17](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_018.png)


---

## Slide 18 — Compute Shader: Voronoi Algorithm (4/6)

![Slide 18](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_019.png)


---

## Slide 19 — Compute Shader: Voronoi Algorithm (5/6)

![Slide 19](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_020.png)

**📌 要点汇总**
- 使用过程性 Voronoi 算法，通过网格上最近九个点的哈希抖动生成随机分布特征
- 基于距离信息映射草参数，实现视觉规律性与自然随机变化的平衡
- 适用于大规模植被生成，有效解决性能与视觉效果的矛盾
- 哈希抖动机制确保每个网格点分布特征的独立性与可控性
- 距离参数直接影响草丛密度、高度等属性，增强场景真实感

> 我们通过使用过程性 Voronoi 算法实现了这一点。对于 2D 空间中的任何给定位置，我们都会查看网格上最近的九个点。每个点都会根据哈希值进行抖动以赋予其变化。然后我们将此 2D 样本点分配给最近的点的簇。通过这个共享的簇和我们到它的距离，我们可以影响各种草参数。


---

## Slide 20 — Compute Shader: Voronoi Algorithm (6/6) — Clump Adjustments

![Slide 20](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_021.png)

**📌 要点汇总**
- Adjusting height and cluster alignment allows blades to be positioned closer to the cluster point for optimized performance
- Blades can be oriented either facing toward or away from the cluster point, depending on system requirements
- Combining directional alignment with positional adjustments offers flexibility in configuration and performance tuning

> 我们可以调整高度。我们可以让所有的簇都指向同一个方向。我们可以将刀片拉近聚集点。
>
> 我们可以使刀片全部背向聚集点，或者将所有这些事情组合起来。


---

## Slide 21 — Data Pipeline: Overview

![Slide 21](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_022.png)

**📌 要点汇总**
- Two compute shaders handle instance data accumulation and indirect draw parameter setup, with the second shader running quickly in a single stage
- Double-buffering strategy processes four grass blocks at a time using eight-block buffer, preventing memory overuse while maintaining GPU utilization
- Vertex shader uses instanced index draw calls with no vertex streams, generating output based on index and instance ID for low/high LOD grass (15/7 vertices per blade)
- Curvature distribution issues in grass blades are mitigated by artist-configurable vertex position adjustment parameters along blade length
- LOD differentiation impacts vertex count (high LOD: 15 vertices per blade, low LOD: 7 vertices) and rendering complexity

> 下面概述了我们的着色器流程的整体情况。我们的第一个计算着色器填充我们的实例数据并累积我们的刀片数量。第二个计算着色器在第一个计算着色器完成后运行，将刀片计数移动到该图块绘制调用的间接绘制参数。第二个计算着色器仅运行一个阶段，几乎不需要时间。一旦完成并且间接绘制参数准备就绪，顶点着色器将启动并根据实例数据进行渲染。最后，像素着色器只需执行着色即可。
>
> 不过，我们不会同时处理所有图块，因为内存成本会非常高。相反，我们的实例数据缓冲区可以容纳八个方块的草地数据。我们首先通过他们的计算着色器运行四个图块。然后，当他们的顶点和像素着色器运行时，我们通过他们的计算着色器运行接下来的四个图块。这种双缓冲策略使GPU保持忙碌，并且不会耗尽我们的内存预算。


---

## Slide 22 — Data Pipeline: Double Buffering

![Slide 22](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_023.png)


---

## Slide 23 — Vertex Shader: LOD Overview

![Slide 23](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_024.png)

**📌 要点汇总**
- Vertex shader uses instanced index draw calls with no vertex streams, generating output based on index and instance ID
- High LOD: 15 vertices per blade, Low LOD: 7 vertices per blade
- Curvature distribution issues in grass blades are mitigated by artist-configurable vertex position adjustment parameters

> 现在我们开始详细说明顶点着色器的实现细节。顶点着色器是使用实例化索引绘制调用绘制的，没有顶点流。它们仅根据索引和实例ID生成输出数据。每个图块都是一个绘制调用，并且是低LOD或高LOD。高LOD草的每个叶片有15个顶点，而低LOD有7个顶点。
>
> 对于每个顶点，我们需要知道它沿叶片长度的位置以及它是在左侧还是右侧的0到1值。此时值得注意的是，我们的草叶片的曲率分布不是很好，因此我们可能也不希望顶点均匀分布。为了帮助解决这个问题，我们有一个艺术家可配置的参数，可以让他们重新调整顶点沿着刀片的位置。


---

## Slide 24 — Vertex Shader: LOD Transition

![Slide 24](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_025.png)

**📌 要点汇总**
- High curvature in grass models causes visible popping when switching to lower LODs due to sudden vertex count reduction
- Dynamic vertex weight blending between LODs reduces visual discontinuity by gradually transitioning high-detail geometry to low-detail
- Distance-based weighting ensures smooth morphing at LOD boundaries while maintaining performance optimization tradeoffs
- This approach prevents abrupt geometry changes that would otherwise disrupt visual continuity in rendering pipelines

> 在两个 LOD 之间实现无缝过渡存在一定挑战，因为我们的草模型可能具有非常高的曲率。当切换到顶点数量较少的 LOD 时，可能会出现明显的弹跳现象。这种现象会导致视觉上的不连贯，影响整体渲染效果。
>
> 为了解决这一问题，高 LOD 会在接近低 LOD 时通过混合技术进行过渡。具体来说，当模型处于两个 LOD 的交界区域时，系统会根据距离动态调整顶点权重，使高精度模型逐渐向低精度模型过渡。这种渐变过程可以有效减少突变带来的视觉干扰，同时保持性能优化的平衡。


---

## Slide 25 — Vertex Shader: LOD Transition (continued)

![Slide 25](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_026.png)


---

## Slide 26 — Vertex Shader: Low LOD Split Blades

![Slide 26](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_027.png)

**📌 要点汇总**
- Low LOD tiles use twice the size of high LOD tiles with same grass blade count, requiring blades to spread twice as far
- High LOD tiles remove 3/4 blades when transitioning to low LOD to maintain density, using vertex folding for short grass (Altera technique)
- Odd vertex count in blades creates an asymmetrical triangle on one side due to split blade handling
- Low LOD blades omit tips to avoid polygon visibility, using cubic Bezier curves for efficient shape control and animation

> 还值得一提的是，低地块瓷砖的尺寸是高地块瓷砖的两倍，但草叶数量相同。这意味着它们的草叶展开的距离是原来的两倍。为了做到这一点，高地块瓷砖在过渡到低地块瓷砖之前，会抽出每四个草叶中的三个。通常，我们所有的顶点都花在单个刀片上，但如果草足够短，我们会将顶点折叠起来形成两个刀片。这是我们从 Altera 得到的伟大想法之一，它确实有助于使短草区域更密集。因此，除了沿着刀片的放置之外，在刀片的左侧或右侧，还有一个我们根据顶点 ID 确定的"我是两个刀片中的哪一个"变量。由于草叶中的顶点数是奇数，因此其中一个草叶的顶点数会比另一个草叶少一个。这导致我们的一侧有一个奇怪的三角形。
>
> 对于低 LOD、较低顶点数的叶片，我们没有尖端。因为在制作动画时，即使在远处，它的多边形数量也非常明显。


---

## Slide 27 — Vertex Shader: Cubic Bezier Curve

![Slide 27](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_028.png)

**📌 要点汇总**
- Each grass blade shape is a cubic Bezier curve — position and derivative are easy to calculate
- Moving control points changes blade shape — useful for animation and varying grass appearance
- Derivative calculation enables easy normal determination for accurate lighting

> 现在我们知道我们是什么类型的草叶以及顶点的相关细节，我们必须决定我们的顶点在世界空间中的位置。每个草叶的形状都是三次贝塞尔曲线。这有很多有用的属性。沿叶片的顶点位置计算起来很简单。导数计算起来也很简单，这使得我们的法线很容易确定。控制点使我们能够对刀片的形状进行大量控制，因此可以轻松为草设置动画，并且还有许多不同形状的草。


---

## Slide 28 — Vertex Shader: Tilt and Bend Control Points

![Slide 28](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_029.png)

**📌 要点汇总**
- Blade tip position determined by tilt parameter and facing direction
- Midpoint defined by bend parameter — zero bend places midpoint on base-to-tip line
- Greater bend values push midpoint away from the line
- Split blades maintain same overall shape but separate for coverage

> 但是我们在哪里放置贝塞尔曲线控制点呢？首先，我们确定尖端相对于底座的位置。这是由之前的倾斜参数以及朝向控制的。接下来，我们定义中点。它由弯曲参数控制。如果弯曲为零，则中点位于基部和尖端之间的线上。大于零的值会将其向上推离该线。对于分体刀片，我们保持相同的总体形状，但将两个刀片分开。这使它们保持相同的总体方向，同时仍然增加覆盖范围。


---

## Slide 29 — Vertex Shader: Bezier Evaluation

![Slide 29](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_030.png)

**📌 要点汇总**
- Vertex world position: evaluate Bezier curve at 0-1 parameter along blade
- Get normal orthogonal to facing direction (swap and negate x,y)
- Step vertex in width direction, scaled by blade width tapering toward tip
- Normal = Bezier derivative crossed with orthogonal normal

> 既然我们知道了控制点在哪里，就可以直接确定顶点的世界空间位置。我们采用零到一的值。确定我们沿着刀片的位置并将其输入到我们的贝塞尔曲线函数中。接下来，我们采用我们的面向方向，翻转 x 和 y，然后求反以找到与我们的面向正交的法线。我们将顶点在法线方向上移动一段距离，具体取决于刀片的宽度，该宽度在计算着色器中计算并根据我们沿刀片的位置进行缩放。当我们到达尖端时，我们想要逐渐变细。
>
> 接下来，为了找到顶点法线，我们找到贝塞尔曲线在我们位置的导数，并将其与我们刚刚找到的法线交叉。


---

## Slide 30 — Vertex Shader: Wind System

![Slide 30](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_031.png)


---

## Slide 31 — Vertex Shader: Single Blade Wind Animation

![Slide 31](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_032.png)

**📌 要点汇总**
- Wind system uses 2D Perlin noise shaped by user parameters, combined with 2D wind vectors for unified CPU/GPU sampling with low overhead
- Grass motion employs sine wave displacement with phase shifts based on blade-specific hashing and position along the blade for varied swaying
- Additional Perlin noise layers added for grass and particle systems to achieve more complex motion patterns
- Bezier curve arc length calculation is challenging but manageable if animation remains relatively constrained during blade movement
- Compute shaders handle wind influence on grass orientation, simplifying animation to basic vertical oscillation after initial wind application

> 但我们如何让它动起来呢？关于我们的风系统：我们很早就决定要拥有一个统一的风系统，可以在 CPU 和 GPU 上进行采样，并且开销相对较小。为此，我们力求简单。风实际上是由用户参数塑造的 2D Perlin 噪声，并沿风吹的方向滚动。Perlin 噪声为我们提供了某个位置的单个风推力值，我们将其与 2D 风向矢量结合起来，用作对风做出反应的各种系统的输入。对于草和一些粒子系统，我们添加了一层 Perlin 噪声以获得更复杂的运动。如果您想更多地了解我们的风，请查看我的同事 Bill Rockenbeck 的演讲"从西边吹来"。
>
> 那么，回到我们的草叶。我们的朝向已经受到计算着色器中风的影响，所以现在我们只做一些简单的上下摆动。这种摆动是一个简单的正弦波，其中相位偏移受到每个叶片散列以及沿草叶的位置的影响，从而使运动具有摇摆的外观。每个叶片的散列偏移量确保每个叶片的运动都是不同的。
>
> 此时需要注意的是，贝塞尔曲线的弧长不太容易计算且难以控制。当叶片运动时，弧长肯定会发生变化。然而，如果动画保持相对约束，这一点并不明显。


---

## Slide 32 — Vertex Shader: Rounded Normals

![Slide 32](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_033.png)

**📌 要点汇总**
- Adjusting grass blade normals outward creates a more natural, rounded appearance without increasing polygon count
- This technique is computationally cheaper than adding additional vertices for similar visual results
- Demonstrates an efficient R&D approach to balancing visual quality with performance in 3D modeling

> 这就是它如何组合在一起的高级要点。但还有一些作品有助于推动该领域的发展。首先，我们将草叶的法线稍微向外倾斜。这有助于使草叶看起来更自然、更圆润，并且比添加更多顶点便宜得多。


---

## Slide 33 — Vertex Shader: Glancing Angle Adjustment (1/2)

![Slide 33](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_034.png)


---

## Slide 34 — Vertex Shader: Glancing Angle Adjustment (2/2)

![Slide 34](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_035.png)

**📌 要点汇总**
- 通过调整视图空间中草叶顶点位置，利用法线与视图向量正交时的微小位移，实现视觉厚度增强，减少薄三角形光栅化开销
- 中远距离渲染中，草叶法线在屏幕空间的剧烈变化导致镜面高光噪点，动画加剧闪烁效果，尤其在雨天场景中显著
- 采用基于距离的法线调整方案，随相机距离增加逐步过渡至草丛平均法线，平衡形状保真与噪点抑制
- 降低像素着色器中光泽度参数，通过将光泽度与法线方差关联，自然抑制高光过度表现，符合物理渲染逻辑

> 我们还遇到了让场景看起来足够饱满的困难。添加更多草叶当然是一种选择，但成本相当高昂。相反，当草叶的法线与视图向量正交时，我们会在视图空间中略微移动草叶顶点。从用户视角来看，这种处理巧妙地加厚了草叶，既减少了光栅化非常薄三角形所需的时间，也让场景看起来更加完整。
>
> 在中远距离的渲染中，我们遇到了非常锯齿状的镜面高光问题，尤其是在雨天场景中。远处草叶的法线在屏幕空间中会发生显著变化，由于草叶表面非常光滑，导致高光区域出现大量噪点。随着草叶动画的进行，这种噪点会进一步加剧，形成不自然的闪烁效果。


---

## Slide 35 — Vertex Shader: Specular Anti-Aliasing (1/2)

![Slide 35](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_036.png)


---

## Slide 36 — Vertex Shader: Specular Anti-Aliasing (2/2)

![Slide 36](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_037.png)

**📌 要点汇总**
- 随距离增加，将法线调整为草丛平均法线，降低镜面高光噪点
- 降低光泽度参数与法线方差关联，自然抑制高光过度表现

> 为了解决这个问题，我们设计了一种基于距离的法线调整方案。随着与相机距离的增加，会逐渐将输出的法线调整为草丛的平均法线。这种处理既保持了场景的整体形状，又有效降低了噪点。同时我们还减少了像素着色器中的光泽度参数，这种调整在技术上是合理的——如果将光泽度视为表面法线在子像素细节上的变化程度，那么随着法线方差的增加，降低光泽度能够自然地抑制高光的过度表现。


---

## Slide 37 — Pixel Shader: Material Output

![Slide 37](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_038.png)

**📌 要点汇总**
- 草叶材质数据通过G缓冲区输出，使用1D光泽纹理沿宽度拉伸并沿长度重复
- 漫反射使用双纹理：1D纹理提供长度/宽度变化，2D纹理的v维度控制颜色渐变（底部深色→顶部浅色）
- 2D纹理u维度由草丛控制而非单个叶片，实现艺术家可控的全局颜色变化
- 实践中草丛间颜色差异较小以保持绘画风格，未来可探索更复杂方案
- 半透明度和AO值随草叶长度变化：根部透明度低、尖端高；AO在根部暗、尖端浅

> 这样我们就有了草叶和它们的顶点。现在我们只需给这些三角形着色即可。我们的草输出到延迟渲染器的 G 缓冲区，因此我们所要做的就是提供材质数据。光泽是一种简单的一维纹理，我们在草叶的宽度上拉伸并沿着长度重复。
>
> 对于漫反射，我们有两种纹理。第一个的工作原理与光泽相同，并提供沿着草叶延伸的纹理以及宽度上的一些变化。第二个是包含实际颜色信息的 2D 纹理。纹理的 v 维度给出了颜色，因为它随着草叶的长度而变化。例如，这使得草叶的底部变暗，并在较高处褪色为浅色。纹理的 u 维度由草叶所属的丛控制，而不是每个单独的叶片都有自己的随机颜色。这让我们可以在整个领域中产生可以由艺术家偏好控制的变化。
>
> 在实践中，团块之间的颜色差异通常非常小，以保持我们的绘画外观。但在未来，我认为这值得更多的尝试。对于半透明度和环境光遮挡，我们输出随草叶长度变化的恒定值。草叶最厚的根部的半透明度相当低，并向尖端逐渐减小。 AO 的功能相同，在基部附近颜色较暗，那里的光线可能会被其他草叶遮挡，而在尖端附近颜色较浅。


---

## Slide 38 — Velocity Buffer Issues

![Slide 38](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_039.png)

**📌 要点汇总**
- 草叶无状态特性导致无法直接写入速度缓冲区
- 需缓存风数据和位移缓冲区追踪顶点位置变化，但性能和内存限制使其不切实际
- 草叶动态摆动导致SSAO时间累积效果混乱，不适合作为AO方案

> 好的，您可能有的问题是，为什么我们要输出 AO 值，而不是仅仅依赖 SSAO？好吧，我们的草不会将速度写入速度缓冲区。草叶的无状态特性使其有点困难，但也是可行的。为了找到前一帧顶点的位置，我们需要缓存最后一帧的风数据，因为风速和风向可能会发生变化。我们还需要有上一帧的位移缓冲区，以防玩家在上面行走。并且由于大量的风和位移信息是在计算着色器中处理的，因此我们需要存储每个叶片的处理数据以供顶点着色器使用。这一切都是有可能的，但性能和内存限制使其不切实际。也就是说，如果我们确实生成了供时间累积的 SSAO 消耗的速度数据，那么草的工作方式使其成为时间累积效果的不良目标。草叶不断地来回摆动。不间断地包含和去除遮挡，因此即使我们确实花费了 perf 来获得正确的速度，我们的 AO 最终也会变成一片斑点和闪闪发光的混乱。


---

## Slide 39 — Fields: Proxy Instances (1/2)

![Slide 39](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_040.png)


---

## Slide 40 — Fields: Proxy Instances (2/2)

![Slide 40](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_041.png)

**📌 要点汇总**
- 使用GPU实例绘制系统程序化放置艺术家创作的资产（蜘蛛百合、潘帕斯草等）
- 生长系统仅输出最小数据流——位置、方向和调用信息
- 加载图块时运行计算着色器为程序草地资产生成数据流
- 保留距离相机最近的3x3图块数据，远距离图块被丢弃

> 所以我们有很多足够令人信服的草叶，但田野大多数时候不仅仅是无尽的草叶。为了完成外观，我们还在程序上将完整的艺术家创作的资产放置在整个字段中。这让我们可以轻松添加蜘蛛百合、小花或最常见的潘帕斯草等东西。我们的成长系统使用 GPU 实例绘制系统，而不是创建完整的游戏对象。增长系统有效地输出最少的数据流——只有位置、方向和呼叫信息——然后从中提取大量资产。有关我们的生长系统的更多信息，请查看我的同事 Matt Pullman 的演讲"Samurai Landscapes：在 PS4 上构建和渲染对马岛"。
>
> 当我们加载图块时，我们运行一个计算着色器，为生长系统使用的程序草地资产生成相同的数据流。我们将距离相机最近的三乘三块保留在内存中，并从中删除任何内容，这样我们就不会因为保留远处的资产而消耗太多资源。放置算法的工作原理与草叶类似。它在图块中选择一个位置，随机生成它，然后检查该位置的草类型是否与其类型相匹配。如果是这样，它会将程序变换数据添加到稍后渲染的流中。我最初只是加入了随机抖动，然后回来尝试做一些更复杂的事情，但当我有时间这样做时，艺术家已经使用该系统来放置这些水稻作物，效果非常好，所以我就保持原样。


---

## Slide 41 — Far LOD (1/2)

![Slide 41](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_042.png)


---

## Slide 42 — Far LOD (2/2)

![Slide 42](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_043.png)

**📌 要点汇总**
- 远距离草叶不渲染完整模型，改用艺术家创作的纹理贴图渲染在地形上
- 大片鲜红的蜘蛛百合田等场景通过纹理替代实现，成本低且效果良好
- 依赖团块法线驱动远景的方案因成本过高且不支持艺术家资产而放弃

> 我们在草方面遇到的最大困难之一是如何处理很远的 LOD。对马岛有玩家可以到达的位置，让他们可以立即看到几乎整个岛屿，而渲染那么远的草叶显然是不切实际的。我尝试了一些依赖于视图的方法来渲染由丛信息驱动的地形。毕竟，如果团块驱动法线，它们应该能够控制法线占主导地位的远景。不幸的是，这最终变得昂贵得不切实际。此外，一旦我们后来添加了我之前提到的艺术家创作的资产，这种方法就行不通了。大片鲜红的蜘蛛百合田地已经长成了绿草。因此，我们选择在地形中的该位置渲染艺术家创作的纹理，而不是底层材质。这种方法成本低廉且效果良好，但仍有改进的空间。


---

## Slide 43 — Stealth Grass Physics

![Slide 43](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_044.png)

**📌 要点汇总**
- 计算着色器将GPU纹理数据复制到CPU友好格式，生成物理网格用于光线投射检测
- 草类型分为隐形草和装饰草，返回恒定高度确保一致性
- 真正的隐秘性来自于草本身

> 在《幽灵》中，玩家可以躲在草丛中偷偷摸摸地刺杀蒙古人。由于我们所有的草数据都存储在 GPU 友好的纹理上，不方便在 CPU 上访问，因此每当我们加载图块时，我们都会运行一个计算着色器，该着色器从快速 GPU 纹理中复制一些信息到更 CPU 友好的纹理。根据这个高度信息，我们生成 phis 网格，游戏可以通过光线投射来确定玩家是否可见。我们最初返回未修改的草的高度，但发现这可能非常不一致。相反，每种类型的草要么被标记为隐形草，要么被标记为装饰草，并根据该高度返回恒定的高度。出于一致性原因，请原谅。出于一致性原因，每种隐形草类型中都有潘帕斯花。但是真正的隐秘性来自于草本身。


---

## Slide 44 — Shadows: Terrain Impostor

![Slide 44](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_045.png)

**📌 要点汇总**
- 使用地形冒充者系统替代完整阴影计算，通过调整顶点高度并抖动深度偏移实现草地阴影密度匹配
- 代理网格的离散性质可能导致硬边问题
- 完整的阴影计算管道（compute + vertex/pixel shader）非常昂贵，仅极少数情况使用

> 我们还必须对阴影进行一些特殊的优化。我们确实支持为阴影投射灯光运行完整的计算和顶点/像素着色器管道，但考虑到它必须为每个灯光至少运行一次，它非常昂贵。尽管我们在极少数情况下会这样做，但我们通常依赖于使用底层地形的冒充者系统。
>
> 实际上，我们升高地形的顶点以匹配该位置的草地高度，然后以抖动模式偏移我们写入阴影贴图的深度。当我们将其与阴影过滤结合起来时，我们最终得到的结果大致匹配草地的阴影密度。不过，这并非没有问题。代理网格的离散性质可能会导致难以解析的硬边。


---

## Slide 45 — Shadows: Screen Space Shadows (1/2)

![Slide 45](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_046.png)


---

## Slide 46 — Shadows: Screen Space Shadows (2/2)

![Slide 46](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_047.png)

**📌 要点汇总**
- 屏幕空间阴影弥补冒充者系统的细节不足
- 草叶超薄特性规避了屏幕空间阴影无法处理厚度计算的限制
- 仅限于短距离和屏幕空间，但草在屏幕空间中通常很小
- 冒充几何体与屏幕空间阴影结合，在保证性能预算前提下实现高质量阴影

> 但在游戏的大部分场景中，结果都不错，性能也很棒。为了获得更精细的细节，我们依靠屏幕空间阴影来弥补差异。屏幕空间阴影无法理解物体的厚度，但我们的草无论如何都是超薄的。它们仅限于短距离和屏幕空间，但我们的草在大多数情况下在屏幕空间中都非常小。
>
> 它们没有考虑屏幕外的几何形状，但同样，由于我们的草很小，屏幕外的任何东西都不会对屏幕上的内容产生巨大的影响。因此，在我们的冒充几何体和屏幕空间阴影之间，我们最终得到了质量不错的阴影，并且不会超出我们的性能预算。


---

## Slide 47 — Future Work: Arbitrary Surfaces

![Slide 47](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_048.png)

**📌 要点汇总**
- 当前草叶放置仅限地形表面，艺术家资产与地形交叉处出现可见边缘
- 提议将艺术家几何体标记为"草表面"，允许程序化生长实现无缝过渡

> 这是游戏中的结果。展望未来，我想对系统进行一些改进。首先，在制作过程中很多时候，艺术家会放置他们想要在其上长草的资源，但我们严格限制在地形上的草上。资源可以选择在与地面相交时对地形材质进行采样，并将其材质与地形材质混合，以实现从高度图控制的地形到艺术家创作的资源的平滑过渡。但由于无法将草放置在这些资源上，因此通常会出现尴尬的边缘，或者更糟糕的是，草从资源下方伸出。将来，我认为将艺术家创作的几何体标记为草地表面是值得的，我们可以通过程序从中生长刀片。这样资产和地形之间的过渡就可以真正实现无缝。


---

## Slide 48 — Future Work: Artist-Authored Vertices

![Slide 48](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_049.png)

**📌 要点汇总**
- 立方贝塞尔曲线顶点灵活快速，但难以程序化生成蕨类、银杏叶、小岩石等
- 艺术家驱动资源与任意表面生长结合可能非常强大
- 可能用于高细节动物的毛皮卡片

> 我们现在生成的立方贝塞尔曲线顶点非常灵活和快速，但是我们可以通过程序放置许多其他类型的茂密树叶。蕨类植物、银杏叶，甚至小岩石可能与我们当前的草具有非常相似的顶点数，但更难以通过程序生成。艺术家驱动的资源支持，尤其是与能够在任意表面上增长它相结合时，可能会非常强大。
>
> 也许我们可以为高细节动物制作毛皮卡片。我不确定，但这是我将来想尝试的事情。


---

## Slide 49 — Future Work: LOD Tile Size Decoupling

![Slide 49](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_050.png)

**📌 要点汇总**
- 每个渲染图块尺寸为前者的两倍，切换时丢失75%草叶，导致暴露距离固定
- 统一草叶数量实现视觉均匀性，但暴露距离与图块尺寸强耦合，限制独立调整
- 未来计划解耦暴露程度与图块尺寸，通过独立参数控制可见范围

> 第三，因为每个渲染的图块都是前一个图块大小的两倍，所以当我们切换到下一个图块尺寸时，我们已经丢失了四分之三的草叶。每块图块都有相同数量的草叶，既美观又简单。然而，这意味着我们必须在不容易改变的距离处外露四分之三的草叶。
>
> 这种设计在视觉上保持了均匀性，但带来了距离控制的局限性。当前方案将草的外露程度与图块尺寸直接绑定，导致调整可见距离时需要同步修改图块参数。这种耦合关系限制了灵活性，特别是在需要独立调整草的可见范围时。
>
> 未来我们希望将外露程度与图块尺寸解耦，通过独立参数控制草的可见距离。这种分离将允许更精细的调整，例如在保持图块尺寸不变的情况下，单独延长或缩短草的可见范围，从而实现更自然的视觉过渡和更高效的性能优化。


---

## Slide 50 — Conclusion

![Slide 50](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_051.png)

**📌 要点汇总**
- 使用计算着色器生成可配置的草刀片实例数据，实现艺术家对细节的控制
- 通过间接绘制调用渲染近100,000条贝塞尔曲线，优化草叶分布性能
- 程序化放置艺术家资源补充基础草叶，提升视觉表现层次
- 采用极简替代者技术实现阴影与火光效果，平衡性能与视觉质量

> 这就是我们如何在帧预算内渲染大片草地并实现艺术指导目标。我们使用计算着色器生成高度可由艺术家配置的每根草刀片实例数据。通过间接绘制调用在屏幕上渲染出近100,000条贝塞尔曲线，实现了高效的草叶分布。
>
> 为增强视觉表现，我们用程序化放置的艺术家资源补充这些基础草叶。同时采用极简的替代者技术制作阴影和火光效果，这种方案在保持性能的同时实现了视觉质量的平衡。


---

## Slide 51 — Questions

![Slide 51](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_052.png)

**📌 要点汇总**
- 联系方式：Twitter @ericwoh

> 如果您对我们做了什么或如何做有任何疑问，请随时在 Twitter 上与我联系。我很乐意回答您的任何问题。


---

## Slide 52 — Acknowledgements

![Slide 52](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_053.png)

**📌 要点汇总**
- Jasmin Patry：最初原型开发
- Bill Rockenbeck：浮点精度问题修复
- Adrian Bentley：系统设计
- Matt Pohlmann：艺术家可用性
- Tom Lowe：阴影系统
- Dave Elder：离线地形AO烘焙
- Joanna Wang：草叶顶点参数调整

> 我还要感谢一群和我一起在 Sushi Mo 制作《草与鬼》的人：Jasmine Patry 为最初的原型做了所有艰苦的工作，然后让我让事情摇摆了几年； Bill Rockenbeck 帮助我解决了无数浮点精度问题；阿德里安·本特利（Adrian Bentley）让我破门而入，并用问题斥责他；马特·普尔曼（Matt Pullman）制作了整个东西。实际上，对于艺术家来说是有用的。 Tom Lowe 出色的阴影工作，Dave Elder 出色的离线地形 AO 烘焙，Joanna Wang 不断调整两个评分参数，使老鼠的巢状顶点看起来像真正的草。


---

## Slide 53 — We Are Hiring

![Slide 53](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_054.png)

**📌 要点汇总**
- Sucker Punch 正在招聘图形和游戏程序员

> 最后一点，我想指出我们正在招聘。我们有图形和游戏程序员职位，正在寻找人才。因此，如果您对我们正在开展的工作感兴趣，请联系我们。非常感谢您观看我的演讲，希望您有美好的一天。


---

## Slide 54 — References

![Slide 54](https://gerigory.github.io/assets/img/GDC/2021/GDC2021-Procedural-Grass-in-Ghost-of-Tsushima/slide_055.png)

**📌 要点汇总**
- Outerra 2012 博客文章：Procedural Grass Rendering — https://outerra.blogspot.com/2012/05/procedural-grass-rendering.html

> 这是我之前承诺的 Altera 博客文章。你绝对应该检查一下。


---

## Slide 55 — End

*(最后一页无内容)*
