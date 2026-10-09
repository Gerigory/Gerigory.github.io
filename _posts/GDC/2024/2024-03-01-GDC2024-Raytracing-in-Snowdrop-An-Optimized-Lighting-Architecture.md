---
layout: post
title: "【GDC 2024】Raytracing in Snowdrop - An Optimized Lighting Architecture"
date: 2024-03-01
img: GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_001.png # Add image post (optional)
fig-caption: # Add figcaption (optional)
tags: [GDC, 2024, Lighting, Rendering]
description: 本文分享的是【GDC 2024】GDC2024 - Raytracing in Snowdrop - An Optimized Lighting Architecture相关的技术要点
---

> 来源：D:\迅雷下载\Graphics Materials\GDC 2024 - Raytracing in Snowdrop - An Optimized Lighting Architecture.pdf
> 提取时间：2026-05-15 12:24:34

---

## Slide 1

![Slide 1](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_001.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 大家早上好， 我是 Quentin Kuenlin，Massive Entertainment 的高级渲染程序员 今天，我将向您展示我们的光线追踪管道，因为它被用于每个 《阿凡达：潘多拉边境》的控制台和质量设置

---

## Slide 2

![Slide 2](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_002.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 2

---

## Slide 3

![Slide 3](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_003.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 让我们首先快速浏览一下我们管道的主要构建模块

---

## Slide 4

![Slide 4](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_004.png)

**📌 要点汇总**

- **LOD设置**：光线追踪世界对象使用低LOD（LOD1/LOD2），降低细节复杂度  
- **材质简化**：网格仅采用无纹理的单一材质，未涉及复杂材质表现  
- **Alpha对象处理**：树叶等Alpha测试对象通过基于Alpha值的抖动纹理

> 让我们从光线追踪世界开始。 > rt 世界中的对象使用比栅格化世界更低的 LOD，通常是 LOD1 或 2. > 我们每个网格只有一种简单的材质，没有纹理 > Alpha 测试对象，例如树叶，使用基于 Alpha 的简单抖动 纹理覆盖。 > 地形是单独进行光线行进的并且可以使用纹理，因此您可以看到 示例图像上的纹理 > 我不会详细介绍这一点，请参阅 Oleksandr Koshlo 的演示 本周晚些时候

---

## Slide 5

![Slide 5](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_005.png)

> 漫射照明示例 5
>
> 我们拥有的第一个光线追踪功能是光线追踪全局照明 > 我们使用每像素光线追踪，使用四分之一/半/全分辨率，具体取决于 质量设置。 > rt gi 的整体管道由初始屏幕空间跟踪组成， > 如果屏幕空间失败，则进行“世界”空间跟踪， > 最后，如果世界空间跟踪失败，我们有一个轻量级缓存回退

---

## Slide 6

![Slide 6](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_006.png)

**📌 要点汇总**

- **光线追踪反射**：支持每像素追踪，分辨率根据质量设置调整（四分之一/半/全）。  
- **可变混合分辨率**：图像不同区域可采用不同分辨率进行光线追踪。  
- **反射层数限制**：最多支持两层反射，结合屏幕空间与世界空间追踪。  
- **分阶段追踪流程**：初始屏幕空间追踪→世界空间追踪→轻缓存后备方案。

> 镜面照明示例 6
>
> 我们拥有的第二个光线追踪功能是光线追踪反射 > 我们还使用每像素光线追踪，使用四分之一/半/全分辨率，具体取决于 关于质量设置。 > 此外，rt 反射使用可变混合分辨率，这意味着不同的 图像的一部分可以以不同的分辨率进行追踪 > 我们还支持最多两个反射层 > 与 rtgi 类似，我们有一个初始屏幕空间跟踪， > 随后进行世界空间追踪， > 最后是轻缓存的后备方案

---

## Slide 7

![Slide 7](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_007.png)

**📌 要点汇总**

- **级联结构**：采用4级联（32x32x8）存储多类型光照信息  
- **数据存储**：包含余弦加权辐照度、粗糙光缓存、平均灯光及采样深度  
- **可视化示例**：通过视频展示探针系统在潘多拉世界的渲染效果

> 探针光缓存示例 7
>
> 最后，我们有一个用于各种目的的光线追踪探针系统 > 我们使用 4 个级联，每个级联 32x32x8 我们在其中存储不同的信息，包括 > 余弦加权辐照度 > 更粗糙的光缓存 > 完全平均的灯光 > 用于探头采样的深度 在详细介绍这一切之前，我准备了一个小视频来展示 美丽的潘多拉世界

---

## Slide 8

![Slide 8](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_008.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 8

---

## Slide 9

![Slide 9](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_009.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 现在让我们更详细地了解探针系统的工作原理

---

## Slide 10

![Slide 10](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_010.png)

**📌 要点汇总**

- **灯光缓存**：作为光线追踪后备，缩短光线射出时间  
- **平均光存储**：用于雾效果，提升场景渲染效率  
- **延迟照明技术**：优化探针光照计算流程  
- **Gbuffer缓存**：实现探针跟踪与独立点亮分离  
- **RTXGI扩展**：基于GDC 2019技术，新增功能增强渲染性能

> 我们的探针系统基于 GDC 2019 演示文稿“Dynamic Diffuse Global Morgan McGuire 的《Illumination》，最常被称为 RTXGI 除了该演示文稿中描述的内容之外，我们还添加了一些功能： + 首先，我们添加了一个灯光缓存，用作光线追踪的后备，使我们能够 射出相对较短的光线 + 其次，我们存储每个探头的平均光，主要用于 雾 + 我们对探头使用延迟照明 + 我们将探针跟踪结果缓存到探针 Gbuffer 中，这样我们就可以跟踪和 独立点亮探头

---

## Slide 11

![Slide 11](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_011.png)

> 以下是探针更新管道的快速概述。我将详细介绍每个步骤 详细信息，除了最后一项。 探头重新定位是一种将探头稍微移动以将其推离的选项。 物体表面，或将它们从物体中取出。它并没有带来任何显着的好处 阿凡达所以没有被使用。有关更多详细信息，请查看 Nvidia 的 RTXGI

---

## Slide 12

![Slide 12](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_012.png)

**📌 要点汇总**

- **级联位置独立更新**：每个级联位置使用独立参数进行更新，确保灵活性。  
- **初始基于相机位置**：级联位置的初始设置依赖于相机的当前位置。  
- **向前对齐选项**：允许级联位置向前移动以优化布局。  
- **地形限制功能**：可选限制级联范围以包含地形，减少探测

> 管道的第一步是更新 cpu 上的级联位置 > 每个级联位置都用自己的参数独立更新 > 级联位置最初基于相机位置 > 然后可以使用向前对齐选项向前移动。 > 可选地，级联可以被限制为包括地形 > 在第二个级联中，三分之一被“浪费”在地形下，所以我们可以强制 级联向上移动，以免浪费地形下方的探测器

---

## Slide 13

![Slide 13](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_013.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 13

---

## Slide 14

![Slide 14](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_014.png)

> 现在我们知道级联在哪里，我们可以选择要更新的探针 我们每帧的更新预算是 1024 个探针 >如果级联移动，将选择新的探头进行更新 >各种事情都会触发一些探测器失效，例如物体移动 场景或一天中的时间发生变化。如果我们有任何无效的探测器，我们将 在新探测之后优先更新那些。 >如果还有预算，现有探头将被动更新 当我们缓存跟踪结果时，可以独立地跟踪和点亮探针 不同的框架 一些探头完全回溯并点亮（〜15％〜162个探头，如果有完整的预算） 其余探头仅重新点燃（~85%~862 个探头）

---

## Slide 15

![Slide 15](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_015.png)

> 对于每个探针，我们在其周围均匀发送 400 条光线 > 迹线范围设置为下一个级联的探头间距的 2 倍，因此这意味着 Cascade 3 中的探测器将发射 16m 射线 >如果我们击中某物，我们会记录击中点的距离、法线和材质 >然后我们检查级联阴影贴图以查看命中点是否在阴影中。如果是的话 不，我们将追踪一条朝向太阳的光线。 >最后，所有这些数据都保存到探针gbuffer中

---

## Slide 16

![Slide 16](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_016.png)

**📌 要点汇总**

- **探针追踪**：一次追踪后可随时进行光照计算，提升后续帧效率  
- **光线追踪处理**：未命中采样天空纹理或轻缓存体积，命中则使用探针gbuffer信息点亮  
- **简化BSDF计算**：排除复杂材质（如头发、布料），仅计算直射光与分析光  
- **BVH加速照明**：通过BVH快速获取世界任意位置灯光信息，优化计算性能  
- **间接照明**：最终使用另一探针对命中点进行间接光照计算，增强画面真实感

> 一旦探针被追踪一次，我们就可以随时进行光照计算 后续帧 > 如果光线追踪未命中，> 我们将采样天空纹理以获取更大的纹理 级联，> 或对较小级联的轻缓存体积进行采样 >如果我们命中，>我们将使用探针 gbuffer 信息点亮命中点。 >我们使用简化的 bsdf 进行所有照明计算，因此没有诸如 如头发、布料、清漆…… >我们计算来自太阳的直射光，>加上分析光。我们正在使用 BVH 可快速获取世界任何地方的相关灯光。 > 最后，我们使用另一个探针间接照亮生命点。

---

## Slide 17

![Slide 17](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_017.png)

**📌 要点汇总**

- **RTGI卷**：平均400条光线结果，用于间接照明与前向渲染  
- **Light Cache**：非平均RTGI版本，作为光线追踪回退缓存  
- **八面体映射

> 我们没有直接使用 400 条光线的照明结果，但我们正在平均 这些结果分为不同的卷。 RTGI 卷与 RTXGI 演示和存储中描述的类似 余弦加权辐照度。主要用于照明间接命中时，以及 前向渲染对象。 Light Cache是RTGI体积不太平均的版本，主要用作缓存 追踪光线时的回退。 深度用于检查探头采样时的可见性。 平均+有效体积主要用于雾和云渲染。 RTGI、Light Cache 和 Depth 使用八面体映射进行存储。

---

## Slide 18

![Slide 18](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_018.png)

**📌 要点汇总**

- **采样探针流程**：采样过程类似RTXGI演示，需参考其细节实现  
- **周围8探针定位**：确定采样点周围8个探针位置并循环处理  
- **权重计算参数**：基于距离、角度、可见度三要素计算探针权重  
- **切比雪夫不等式应用**：用于估计采样误差范围及不确定性分析

> 现在我们有了探针，我们可以对它们进行采样。 采样探针的过程与 RTXGI 演示类似，因此我建议您参考该演示 细节。 找出采样位置周围有哪 8 个探头 循环它们并根据距离、角度、可见度计算权重 切比雪夫不等式

---

## Slide 19

![Slide 19](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_019.png)

**📌 要点汇总**

- **平均体积存储**：使用3D纹理存储简化版本，但无效探测器会导致暗光泄漏  
- **无效探测器问题**：内部或地形下探测器标记为无效，灯光全黑引发采样误差  
- **有效性纹理采样**：通过1/0值区分有效/无效探测器，避免无效数据干扰计算  
- **除法优化方案**：平均值与有效性纹理结合，直接输出有效探头的平均光照结果

> 对于平均体积，我们可以使用更简单的版本，因为它存储在 3D 中 纹理。 但是，位于物体内部或地形下方的探测器被标记为无效 他们的灯光将是全黑的。如果我们这样做，这可能会导致暗光泄漏 仅对平均 3D 纹理进行采样。 为了解决这个问题，我们还对有效性纹理进行采样，如果探测器有效，则存储 1，或者 如果无效则为 0。 平均/有效性除法返回平均光，无需无效探头

---

## Slide 20

![Slide 20](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_020.png)

> 以下是我们在《阿凡达》中使用的一些值。

---

## Slide 21

![Slide 21](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_021.png)

> 这是直接在 gbuffer 上使用时 RTGI 卷的调试视图。

---

## Slide 22

![Slide 22](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_022.png)

> 如果我们只使用探针而不是每个探针，这就是最终渲染的图像 像素光线追踪。

---

## Slide 23

![Slide 23](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_023.png)

> 现在我们已经有了一个可以工作的探针系统，我们可以讨论每像素光线追踪 地理标志

---

## Slide 24

![Slide 24](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_024.png)

> 我们的实现最初基于 GDC 2019 演示文稿“探索射线 《地铁：离去》中追踪未来”。 > 根据质量，每像素 gi 以四分之一、一半或全分辨率进行追踪 设置。对于《阿凡达》，控制台使用的是四分之一分辨率。 整体流程如下： > 我们从初始屏幕空间追踪开始 > 如果屏幕空间追踪失败，我们继续进行世界空间追踪 > 如果后者失败，我们将使用探针缓存 > 光结果被编码为球谐函数 > 然后使用循环模糊方法进行去噪 > 最后，如果以四分之一或一半分辨率渲染，结果会放大

---

## Slide 25

![Slide 25](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_025.png)

**📌 要点汇总**

- **余弦加权半球采样**：用于光线追踪GI的光线生成，提高采样效率  
- **非完全不透明表面处理**：通过随机翻转光线方向模拟透射效果  
- **射线范围计算**：根据探针间距和级联信息确定射线最大范围

> 光线追踪 GI 的光线生成非常简单，我们只需使用余弦加权半球对随机方向进行采样 分布。 > 如果表面不是完全不透明，则随机将光线翻转到另一个 表面的一侧。 > 射线范围基于可用的最高级联中的探头间距，其中 我们启动射线。 因此，如果光线从最细级联开始，则光线范围将为 2x2m=4m。

---

## Slide 26

![Slide 26](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_026.png)

> 现在我们有了光线，我们可以开始屏幕空间追踪。 > 如果追踪距离大于光线范围，我们就会错过，所以我们将 能够在点亮时对探针缓存进行采样，有效地绕过任何“真实” 光线追踪。 > 如果光线被阻挡或离开屏幕空间，我们会检查有多少光线 它已经追踪到的范围，>如果它大于某个阈值，我们也认为射线 作为未命中，将直接对探针缓存进行采样。 > 如果不是，我们将该像素添加到 进行光线追踪 > 如果命中，我们将对 Gbuffer 进行采样以获取所有材质数据。 > 如果我们击中的像素是自发光的，我们会检查其自发光亮度。 > 如果大于 某个阈值，我们可能不想直接使用它，而是检查什么发射 我们在 rt 世界中拥有的价值并使用它。提醒一下 rt 世界使用 平均材料，因此物体上的明亮发射点 qets 在整个物体上平均 网格代替。 > 如果命中不够发光或不够暗淡，我们将按原样使用它 照明。

---

## Slide 27

![Slide 27](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_027.png)

**📌 要点汇总**

- **屏幕空间与直接跟踪结合**：ss跟踪命中发射材质时，继续跟踪以获取rt世界材质数据。  
- **未命中条件判断**：ss未命中且距离<0.01时重置射线，否则从屏幕空间断

> 光线跟踪是间接调度屏幕空间跟踪结果的。 > 如果 ss 跟踪导致发射命中，我们将跟踪该命中以获得 rt 生命值的世界材质。 > 如果ss未命中距离小于0.01，我们从头开始射线 > 否则，我们从屏幕空间停止的地方开始光线。 > 如果发生命中，如果 ss 命中是发射性的且 rt 命中不使用 ss 命中。 > 否则使用 rt hit 结果。 > 如果我们错过了，我们将在照明时简单地回退到灯光缓存。

---

## Slide 28

![Slide 28](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_028.png)

> 说到照明，它分两次完成。第一个会错过 照明，第二个将处理击中。我们分两次完成，因为击球 部分比未命中部分复杂得多，因此单独进行意味着我们得到 更好地利用 GPU 线程。 > 因此，如果我们有一个未命中的情况，我们首先检查射线的终点是否在任何级联中。 > 如果是，我们使用射线方向作为采样方向对探针缓存进行采样。 > 如果不在级联范围内，我们只需对天空盒进行采样。 > 然后将最终的照明结果编码为球谐函数，并且所有数据 去噪所需的信息也被写入必要的纹理中。 > 在击中的 cade 中，我们只需将该像素转发到光击着色器。

---

## Slide 29

![Slide 29](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_029.png)

**📌 要点汇总**

- **重新投影采样**：将击中点投影到前一帧，采样历史照明以降低计算成本。  
- **光照处理逻辑**：根据投影结果区分使用太阳光+CSM阴影或探针+点光源的间接照明方案。  
- **简化BSDF计算**：探针照明采用简化的BSDF模型以提高效率。  
- **萤火虫抑制**：通过限制发射亮度减少光击中产生的噪点（萤火虫）。  
- **输出去噪数据**：最终输出光照结果

> 对于光击中着色器，我们要做的第一件事是将击中点重新投影到前一个 框架。 > 如果投影点对应于前一帧的像素，我们可以简单地 对之前的框架照明进行采样，这将以更低的成本提供更好的照明 而不是在这里重新计算。 > 否则，我们将用太阳照亮命中点，使用 CSM 获得阴影 信息。 > 然后对探针进行采样以获得间接照明， > 然后使用 点光源。至于探针照明，这里的所有计算都是用简化的 BSDF。 > 最后，我们尝试通过限制发射来减少发射命中产生的萤火虫 每个着色器波内的亮度。 > 然后输出光结果和所有必要的数据以进行去噪。

---

## Slide 30

![Slide 30](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_030.png)

**📌 要点汇总**

- **球谐编码**：光线追踪GI采用球谐编码技术处理光照信息  
- **纹理格式**：将数据转换为64位RG_Uint32纹理以提升存储效率  
- **编码实现**：通过特定函数实现光结果的球谐编码转换逻辑

> 如前所述，光线追踪 gi 使用球谐编码。我们正在打包 将它们转换成 64 位的 RG_Uint32 纹理。您可以参考下面的函数 看看我们如何编码光结果。

---

## Slide 31

![Slide 31](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_031.png)

**📌 要点汇总**

- **光线追踪GI原理**：通过屏幕空间追踪与探针回退技术实现全局光照效果  
- **屏幕空间局限性**：在屏幕空间追踪失效区域可能出现过暗的渲染结果  
- **技术示例场景**：以具体场景演示光线追踪GI的实现过程与潜在

> 你并不知道光线追踪 GI 是如何工作的，让我们看一些例子。 我们就从这个场景开始吧。这里我们只使用屏幕空间追踪， 探针的回退。 >在这里我们可以看到，在屏幕空间失败的地方，我们可以得到一些过暗的东西 结果。

---

## Slide 32

![Slide 32](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_032.png)

**📌 要点汇总**

- **自交集问题**：RT世界中悬崖LOD生成大量自交集，影响视觉效果  
- **微小物体缺失**：地表细节（如草）在RT世界中未呈现，导致细节丢失  
- **轨迹局限性**：仅依赖世界空间轨迹无法解决复杂场景的几何问题

> 然而，在仅使用世界空间轨迹的情况下，我们可以看到一些更大的 由于自交集导致的问题。 >这里，RT世界中使用的悬崖LOD创建了很多自交集。 >另一个问题是地面上的微小物体，例如草，不存在于 RT 世界，所以我们失去了所有这些细节。

---

## Slide 33

![Slide 33](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_033.png)

> 当同时使用屏幕和世界空间追踪时，我们可以获得所有漂亮的细节 屏幕空间，而且我们还从世界空间获得正确的照明。 但更重要的是，同时使用屏幕空间跟踪和回退 对于探测器来说，我们能够大量减少实际光线追踪的数量。 对于这个特定的场景，只有 29% 的光线需要光线追踪，这意味着我们 每 14 个像素追踪一条光线 – 这取决于场景，某些场景需要更多 或更少的硬件射线

---

## Slide 34

![Slide 34](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_034.png)

> 我们简单说一下去噪。 在 Snowdrop 中，我们有 4 种不同的漫反射降噪器可用。 >TWD是最便宜的，但质量较差。在许多简单的情况下效果很好，例如 与外部一样，但在更复杂的场景中留下了很多噪音 >MSD 是最新的一款，并且是随 Avatar 一起提供的。基于循环模糊， 几乎与 TWD 一样快，但噪音降低更多，但代价是更多 模糊。 >我们还拥有 NRD 的 ReBLUR 和 >ReLAX，它们在 质量好，但也比较贵。

---

## Slide 35

![Slide 35](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_035.png)

> 这是在控制台质量设置下去噪之前光线追踪 GI 的示例

---

## Slide 36

![Slide 36](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_036.png)

> 这是使用 MSD 去噪后的结果

---

## Slide 37

![Slide 37](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_037.png)

> 现在我们有了最终的去噪光线追踪 gi，我们可以将其应用到最终图像。 >我们没有直接应用它，而是使用球形 谐波创建一个光源，用于我们拥有的完整 BSDF。 >可以使用以下方法提取光发射颜色和强度及其方向 公式在这里。

---

## Slide 38

![Slide 38](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_038.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 38

---

## Slide 39

![Slide 39](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_039.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 39

---

## Slide 40

![Slide 40](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_040.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 现在我们来谈谈光线追踪反射。

---

## Slide 41

![Slide 41](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_041.png)

**📌 要点汇总**

- **重要性采样**：使用GGX重要性采样替代余弦加权半球采样。  
- **混合分辨率跟踪**：屏幕不同区域采用差异化的输入分辨率进行光线追踪。  
- **射线长度控制**：基于材质粗糙度而非固定探头间距计算射线长度。  
- **反射层级限制**：最多支持两层反射（Gbuffer与水/清漆材质分离）。  
- **照明解调流程**：在去噪处理前对照明结果进行解调处理。

> 光线追踪反射管道与光线追踪 gi 几乎完全相同。它是 根据设置，还可以使用四分之一/一半或全分辨率。再次，控制台 使用四分之一分辨率。我不会再讲完整的流程，只讲关键的部分 差异。 > 显然我们使用的是 GGX 重要性采样而不是余弦加权 半球一 > 我们在“输入”分辨率之上使用混合变量分辨率跟踪。 这意味着屏幕的不同部分使用不同的分辨率进行追踪。 > 射线长度基于粗糙度而不是仅基于探头间距 > 我们最多可以有两个反射层，一个用于从 Gbuffer 反射，一个用于反射 第二个来自水和/或清漆。 > 我们在去噪之前解调照明结果。

---

## Slide 42

![Slide 42](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_042.png)

> 光线的生成又非常简单： > 我们使用 GGX 分布对光线方向进行采样 > 光线范围基于粗糙度；我们在这里使用一点噪音来 没有相同粗糙度值的直线切割。这里的值被校准为 对于粗糙度为 0.1 的范围为 50 米，对于粗糙度为 0.7 的范围为 5m

---

## Slide 43

![Slide 43](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_043.png)

**📌 要点汇总**

- **优化光线追踪效率**：通过调整权重减少低贡献光线的追踪时间  
- **权重影响

> 并非所有反射表面对最终图像都有相同的贡献，所以我们想要 花更少的时间追踪贡献较低的光线 这确实取决于内容，因此需要进行大量调整才能获得最佳结果 以及质量和性能之间的权衡。 但对于《阿凡达》，我们使用了不同权重的混合，基于 Ø亮度 Ø着色器组内的光照差异 Ø 打击距离 Ø 粗糙度 Ø 表面镜面反射率 Ø我们还根据表面法线计算方向值，该值用于决定半分辨率应为哪个方向

---

## Slide 44

![Slide 44](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_044.png)

**📌 要点汇总**

- **像素质量计算**：通过单个像素质量推导整个瓷砖的理想质量  
- **质量混合策略**：结合个体质量最大值与平均值，提升前帧质量稳定性  
- **质量传递机制**：当前帧计算的新质量将作为下一帧的输入参数

> 一旦计算出单个像素的质量，我们就可以计算出什么是理想的质量 整个瓷砖。 在这里，我们还得到了所有个体质量的最大值和平均值的混合 作为前一帧的质量以获得暂时稳定的结果。 新的质量将在下一帧中使用

---

## Slide 45

![Slide 45](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_045.png)

**📌 要点汇总**

- **混合分辨率**：不同颜色代表不同分辨率层级（全、半、四分之一、1/16）。  
- **追踪质量差异**：浅灰色与蓝色同为四分之一分辨率，但浅灰色迹线质量较低。  
- **方向特性**：绿色半分辨率分垂直和水平两种方向。  
- **颜色与精度**：红色全分辨率精度最高，深灰色1/16分辨率精度最低。  
- **可视化示例**：通过颜色区分分辨率层级，直观展示追踪效果差异。

> 这是混合分辨率分布的示例。 红色瓷砖将以全分辨率追踪，在这里我们可以看到水主要是红色的。 绿色是一半分辨率，具有两个方向：垂直或水平一半。 蓝色是四分之一分辨率 浅灰色也是四分之一分辨率，但迹线质量较低。 深灰色为 1/16 分辨率

---

## Slide 46

![Slide 46](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_046.png)

**📌 要点汇总**

- **解调与降噪对象**：光线追踪反射结果在去噪前解调，以降噪到达物体表面的光，

> 光线追踪反射结果在去噪之前被解调，因为我们想要 对到达物体表面的光进行降噪，而不是对物体表面的光进行降噪 反射向相机。 有关这方面的更多信息，我建议您参阅“光线追踪宝石”一章 32，以及 Eric 的“Sampling the GGX Distribution of Visible Normals”论文 海茨。

---

## Slide 47

![Slide 47](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_047.png)

**📌 要点汇总**

- **屏幕空间跟踪失效**：在对象后方时无法正确追踪，导致不连续性或错误结果  
- **薄物体误判问题**：屏幕空间跟踪可能将薄物体错误识别为撞击对象  
- **局限性**：屏幕空间方法无法有效处理遮挡和复杂反射场景

> 最后，这是光线追踪反射的一些示例。 让我们首先查看仅跟踪屏幕空间的结果。 > 在这里我们可以看到，屏幕空间跟踪在对象后面时会失败 并可能导致明显的不连续性或错误的结果 > 您还可以看到屏幕空间跟踪将考虑传递到后面的问题 较薄的物体作为撞击。

---

## Slide 48

![Slide 48](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_048.png)

> 当仅追踪世界空间时， > 你显然可以看到低 rt 世界质量 然而，光线正确地穿过薄物体后面，并且没有明显的不连续性 是可见的

---

## Slide 49

![Slide 49](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_049.png)

**📌 要点汇总**

- **SS与WS结合**：SS提供细节但薄物体追踪无效，WS结果存在不连续性  
- **光线追踪效率**：仅需

> 当同时使用 ss 和 ws 跟踪时，我们从 ss 获得所有不错的细节，但也没有 对薄物体的打击无效。 然而，我们仍然可以得到 ss 结果和 ws 结果之间的一些不连续性
>
> 在这个场景中，只有大约 35% 的像素需要光线追踪，这可以给我们带来很大的帮助。 性能改进。

---

## Slide 50

![Slide 50](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_050.png)

> 我之前提到过 2 层反射，所以这里是一个示例 喜欢。 这里有第一层，位于 GBuffer 中

---

## Slide 51

![Slide 51](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_051.png)

**📌 要点汇总**

- **分层结构**：第二层含水与透明涂层，分层处理提升效果  
- **成本

> 这里有第二层，每层都有水，再加上透明涂层。 这两层分别进行追踪和去噪，有效地使成本增加了一倍 rt 反射。因此，这仅适用于 PC 上的最高质量设置。

---

## Slide 52

![Slide 52](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_052.png)

**📌 要点汇总**

- **漫反射降噪器**：Snowdrop引擎提供多种降噪器用于漫

> 至于漫反射，我们在 Snowdrop 中有几种可用的降噪器。除了 4 已经提到，我们还有 AMD Fidelity FX Specular Denoiser。就而言 质量/速度，它位于 TWD 和 MSD 之间。

---

## Slide 53

![Slide 53](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_053.png)

**📌 要点汇总**

- **去噪前rt反射示例**：展示左上角存在混合创建的方形工件  
- **分辨率范围**：从1/

> 这是去噪之前的 rt 反射的示例。 您可以在左上角清楚地看到一些由混合创建的方形工件 分辨率从 1/16 分辨率到全分辨率

---

## Slide 54

![Slide 54](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_054.png)

> 并且去噪后

---

## Slide 55

![Slide 55](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_055.png)

**📌 要点汇总**

- **高粗糙度处理**：粗糙度≥0.9时采用光线追踪GI SH替代rt反射  
- **粗糙度阈值**：粗糙度＞0.7时对rt反射与rt GI结果进行lerp混合  
- **解调重应用**：需重新应用解调过程以实现rt反射在最终图像中的呈现

> 要将 rt 反射应用于最终图像，我们需要重新应用解调。 对于粗糙度为 0.9 或更高的表面，我们使用光线追踪 GI SH 代替，并且 粗糙度高于 0.7 时，我们会在 rt 反射和 rt gi 结果之间进行 lerp。

---

## Slide 56

![Slide 56](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_056.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 56

---

## Slide 57

![Slide 57](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_057.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 57

---

## Slide 58

![Slide 58](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_058.png)

> 因此，了解光线追踪管道的工作原理固然很好，但我们真的可以在所有情况下使用它吗？ 控制台？我们来谈谈性能

---

## Slide 59

![Slide 59](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_059.png)

> 首先，这是探针更新的 GPU 时序。 探针更新是在计算队列上异步完成的，因此它的一些成本 是隐藏的，但这里是不同部分的原始时间。 您可以看到两个 Xbox 都有类似的成本重新分配，花费了一半的时间 在光线追踪上。另一方面，RTX 4080 具有更多的光线追踪功能 表演，大部分时间都花在灯光上。

---

## Slide 60

![Slide 60](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_060.png)

**📌 要点汇总**

- **四分之一分辨率追踪**：通过降低追踪分辨率，节省约34%追踪时间，减少计算负载。  
- **屏幕空间跟踪优化**：添加屏幕空间跟踪技术，

> 上面讲了一些优化，但是一些优化的实际影响是什么？ 那些？ 我们来看看。在这里我们可以看到追踪、照明和去噪的时间 Xbox Series X 上 1440p 的 gi 和反射。基线数无 任何优化；无需使用任何探头、屏幕即可追踪无限长度的光线 空间追踪，……唯一的优化是我们以四分之一分辨率进行追踪。 > 将屏幕空间跟踪添加到管道中，我们可以看到我们节省了大约 34% 以及 27% 的追踪时间 Ø向探针缓存添加回退，从而大大减少光线长度，我们将跟踪时间减少一半，并且还减少了照明通道 位，因为更多的光线将回落到探测器上。 Ø接下来，分两次进行照明可以减少大约 10% 的部分 Ø最后，添加镜面反射的混合分辨率，我们又全面节省了 28%。 有了所有这些，我们将漫反射和镜面反射的时间减少了一半，从 15 毫秒降至 7 毫秒

---

## Slide 61

![Slide 61](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_061.png)

**📌 要点汇总**

- **Xbox Series S性能优势**：XSS因有限光线追踪和简化照明，在特定场景下超越其他系列  
- **光线追踪发射检查限制**：XSS仅执行少量WS光线追踪，减少计算需求  
- **照明简化优化**：XSS未使用点光源，避免二次照明计算，提升效率

> 以下是 Xbox 和 RTX 4080 的一些性能数据，在 潘多拉星球上的各种不同位置。 在这里，您可以看到 Xbox 系列 S 奇怪地超越了 WS 中的其他两个系列 追踪。这仅仅是因为对于XSS，我们只做WS 用于前面讨论的发射检查的光线追踪，因此只有少量的 WS 需要射线。 XSS 的照明也得到了简化，因为它不使用任何点光源；这意味着 不需要分两次进行照明。

---

## Slide 62

![Slide 62](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_062.png)

> 最后，这里有一些 rt 反射的数字。 这里 XSS 还有一些额外的限制：我们只进行 WS 跟踪 对于发射检查和水面，混合分辨率仅限于 分辨率的一半为最大值。

---

## Slide 63

![Slide 63](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_063.png)

> 我向您展示的所有内容都是我们随《阿凡达》一起提供的。对于那场比赛来说， 在 95% 的情况下效果很好，但仍然存在一些局限性。

---

## Slide 64

![Slide 64](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_064.png)

> 不连续性示例 屏幕空间和之间 光线追踪
>
> 第一个是明显的低分辨率 RT 世界。虽然这不会造成任何 rt gi 的问题，因为我们不需要高频细节，这是低频的问题 粗糙度反射，例如镜子和静水。 根据视角的不同，我们可以清楚地看到两者之间的不连续性 屏幕空间和RT世界 因此，艺术家需要避免此类反射表面。

---

## Slide 65

![Slide 65](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_065.png)

> 走廊不的例子 与探头对齐（顶部） 以及（下）
>
> 其他一些问题来自探针系统，其形式如下： 对关卡设计师的限制。 Ø第一个是封闭间距不能小于探头间距 Ø第二个是长走廊需要与探头对齐，要么完全轴线对齐，要么成45度。 Ø第三个是关于壁厚。这些需要足够厚，以免由于解决切比雪夫不等式的精度低而导致任何泄漏 能见度。 最后一点是室内空间不能太大，尤其是垂直方向。事实上，大的内部空间可能会导致我们不得不使用低密度的级联，这可能会导致泄漏。

---

## Slide 66

![Slide 66](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_066.png)

> 这是一个内部太高最终需要采样的示例 上升时级联1。

---

## Slide 67

![Slide 67](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_067.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 那么，我们下一步该做什么？这里我不会讲太多细节，只是概述一下 我们正在调查

---

## Slide 68

![Slide 68](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_068.png)

**📌 要点汇总**

- **八叉树方法**：替代级联方式，优化探针布局策略  
- **探头集中探测**：聚焦关键区域，避免冗余部署  
- **适应不同关卡布局**：八叉树结构兼容多类型场景规模  
- **避免不重要区域**：智能筛选有效探测范围  
- **提升探测效率**：动态调整

> 自适应探头示例 探头间距：4m 外部，0.25m 探头 里面
>
> 首先，我们一直在寻找更好的放置探针的方法，旨在解决 我刚才谈到的大部分问题。 我们最终尝试了八叉树方法来代替级联。 有了它，我们可以>避免将探针放置在不重要的地方，并将探针集中在 探测附近的物体。 Ø八叉树更适合任何类型的关卡布局和大小

---

## Slide 69

![Slide 69](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_069.png)

**📌 要点汇总**

- **启发式删除策略**：通过距离相机、视

> 以下是八叉树更新管道的概述。这替换了更新的部分 在CPU上完成级联，但实际的探针更新没有改变。 Ø我们首先删除不再有用的单元格，这是通过一些不同的启发式方法完成的，例如到相机的距离，是否在视口中，...... Ø然后我们删除不再使用的探针，因为不再与细胞相关联 Ø然后我们选择要细分的新单元格。我们有不同的方法来做到这一点。一种方法是查看深度缓冲区并确定我们应该使用哪个八叉树深度 有。另一种是根据要求。在照明过程中，当光线 对探针进行采样，如果那些期望八叉树位于某个深度，但它是 不是，他们可以请求为下一帧细分相关单元 Ø最后我们选择要更新的探针。对于级联，新探针优先。然后其余的都是随机选择的

---

## Slide 70

![Slide 70](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_070.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 70

---

## Slide 71

![Slide 71](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_071.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 71

---

## Slide 72

![Slide 72](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_072.png)

**📌 要点汇总**

- **泄漏问题**：薄壁导致室内外光线泄漏，需通过过滤探头限制采样范围  
- **过滤探头**：新增机制仅采样与光线实际位置对应的区域，避免无效计算  
- **门户BVH**：引入轻量级BVH结构，追踪光线是否从室内出发，判断是否离开房间  
- **成本优化**：新BVH结构计算开销极低，对性能影响可忽略

> >正如我们所见，室内和室外之间可能会发生泄漏，特别是因为 薄壁。 >所以我们增加了一种在室外和室内之间过滤探头的方式，只采样 对应于光线所在位置的那个 >如果房间有门或窗，我们需要知道光线是否离开了房间 房间。为此，我们添加了一个新的门户 BVH，我们可以跟踪每条光线 开始室内。这是一个相当轻的 BVH，因此成本可以忽略不计。

---

## Slide 73

![Slide 73](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_073.png)

**📌 要点汇总**

-

> 顶部：不完整结果的示例 由于均匀光线 分布 底部：已解决不完整的结果 具有自适应光线分布
>
> 因为我们为每个探头均匀地发送光线， >由于某些探针捕捉到微小的发射物体，我们可能会得到不完整的结果问题 而其他人可能不会。 >因此，为了解决这个问题，我们正在尝试更巧妙地将光线发送到重要的地方。 这似乎解决了斑点问题，但也产生了更多的对比度。

---

## Slide 74

![Slide 74](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_074.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 74

---

## Slide 75

![Slide 75](https://gerigory.github.io/assets/img/GDC/2024/GDC2024-Raytracing-in-Snowdrop-An-Optimized-Lighting-Architecture/slide_075.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 75

---
