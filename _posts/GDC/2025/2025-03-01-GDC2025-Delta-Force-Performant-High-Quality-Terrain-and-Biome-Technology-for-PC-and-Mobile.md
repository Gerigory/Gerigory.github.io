---
layout: post
title: "【GDC 2025】'Delta Force' Performant High-Quality Terrain and Biome Technology for PC and Mobile"
date: 2025-03-01
img: GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_001.png # Add image post (optional)
fig-caption: # Add figcaption (optional)
tags: [GDC, 2025, Rendering, Terrain, Vegetation]
description: 本文分享的是【GDC 2025】GDC2025-'Delta Force' Performant High-Quality Terrain and Biome Technology for PC and Mobile相关的技术要点
---

> 来源：C:\Users\shaotang\Downloads\Draft\GDC2025-'Delta Force' Performant High-Quality Terrain and Biome Technology for PC and Mobile.pdf
> 提取时间：2026-05-15 19:31:39

---

## Slide 1

![Slide 1](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_001.png)

**📌 要点汇总**

- **腾讯游戏亮相GDC 2025**：代表腾讯游戏参与全球游戏开发者大会，展示技术成果。

> 大家好。我们非常荣幸站在这里 代表腾讯游戏参加GDC 2025
>
> 欢迎来到三角洲部队：高性能的高品质地形和 适用于 PC 和移动设备的 Biome 技术 在开始之前，有人告诉我要提醒大家， 将手机设置为静音并确保至少不会发出噪音 不管怎样，我真的很感激，也谢谢你的 合作

---

## Slide 2

![Slide 2](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_002.png)

> 项目X
>
> 信息分类： 一般
>
> 首先，请允许我简单介绍一下自己，并介绍一下 一些简短的背景信息。我叫王利川，加入游戏行业 从2005年开始。（至今已经过去了大约20年，很难 相信我）[CLICK]我曾经在育碧上海和蒙特利尔工作过 大约16年，我专注于AAA级冠军的拍摄 游戏，主要是《汤姆克兰西》系列，其中包括《幽灵》 《侦察兵》和《溢出细胞》，我相信你们中的一些人可能知道这些 IP 和 FarCry 特许经营权，从 FarCry 4 一直到 FarCry 6。
>
> 然后在2020年，我加入了腾讯游戏，特别是Team JADE， 作为支持多款游戏的工作室首席技术美工， 例如《穿越火线》手机版和《使命召唤》手机版 最近非常成功，我在三角洲部队项目上花了很多年，我专注于 主要是渲染、程序主义、管道、工具等等

---

## Slide 3

![Slide 3](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_003.png)

**📌 要点汇总**

- **PBR渲染技术**：采用基于物理的渲染实现超写实视觉效果，构建自然开放世界。  
- **跨平台开发**：需同时支持PC与移动设备，兼顾性能与资源限制下的高效开发。  
- **高性能需求**：确保游戏在多平台流畅运行，满足高帧率与复杂场景渲染要求。  
- **艺术与技术结合**：强调编程与视觉艺术

> 信息分类： 一般
>
> 首先，我想设定一些期望 今天。这不是一个简单的编程谈话，它是一种 f 编程与视觉艺术的结合/te 艺术管道 工具 好吧，让我们看看三角洲部队的目标和目标 今天。 Delta Force是一款超写实的FPS游戏，整体渲染 解决方案和艺术呈现基于PBR，因此您可以 将此视为纯粹基于物理的渲染项目。这也是创造自然开放世界的关键。 我们的技术框架应该为两个平台提供游戏 尽管时间和人力都非常有限，但仍然高效。最后，当然，游戏需要高性能。那 意味着它需要在PC和各种设备上流畅运行 移动设备。

---

## Slide 4

![Slide 4](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_004.png)

> 信息分类： 一般
>
> 好啦，先来说说我们今天的议程。首先，我们要简单介绍一下三角洲部队的情况，以防万一。 你们中的一些人对这个标题不熟悉。我将回顾一下两者的一些核心着色器技术 地形和生物群系，以获得您今天在这两个平台上看到的内容 然后，我将讨论我们如何使用程序工具来帮助 生物群落的生成和管理。从技术角度，我们将介绍这两个方面的解决方案 地形纹理和 具有极低消耗和最小化的地形几何形状 适合 PC 和移动设备的所有工件。接下来， 我们将深入研究各种性能优化技术 s。最后，我们将总结一些最终的想法和未来 我们已经在进行的工作。

---

## Slide 5

![Slide 5](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_005.png)

> 这里我们有一个几个月前刚刚发布的视频剪辑 我们觉得你们很多人还没有看过，也许你们中的一些人 有，我们很高兴今天在这里为您放映，应该给 您可以了解我们正在谈论的事情的一些背景，所以让我们 看看

---

## Slide 6

![Slide 6](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_006.png)

**📌 要点汇总**

- **跨平台性能目标**：支持PC及多端移动设备，PC达4K 144fps，旗舰移动设备达120fps  
- **昼夜循环兼容性**：开放世界需适配全天候光照变化，涵盖室内外复杂环境  
- **主世界规模**：核心地图面积达100平方公里，辅以多张小型地图补充场景内容

> 信息分类： 一般
>
> 好吧，让我们看看我们遇到的技术限制。三角洲特种部队可在多个平台上运行，其中包括 PC 跨越从低端到高端的多种移动设备我们的目标是在 PC 上实现高达 4K 144 fps 的速度，同时仍然运行 在旗舰移动设备上可达 120 fps。我们在开放世界中有一个完整的昼夜循环，其特点是 室内和室外环境。所以世界建筑包括生物群落、地形和 一切都需要与一天中的所有时间兼容
>
> 我们有一个100平方公里的主世界 还有几张相对较小的地图。

---

## Slide 7

![Slide 7](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_007.png)

> 信息分类： 一般
>
> 说到地图大小，我来详细说明一下游戏范围 简单地说。 我们有3种游戏模式， 抽取模式，就像我说的主世界， 位于 10 公里 x 10 公里的开放世界中。 这张巨大地图上的随机事件将让玩家 订婚,

---

## Slide 8

![Slide 8](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_008.png)

**📌 要点汇总**

- **大型PVP模式**：支持多地图（4x4/2x2）定制设计，适配不同游戏目标  
- **高并发性能**：64人同屏对战，保持高帧率流畅体验  
- **真实战场要素**：包含军用车辆、坦克、直升机

> 信息分类： 一般
>
> 大型PVP模式，包含多个4x4，和2x2 地图，每张地图的具体尺寸都是定制的 由关卡设计师根据游戏目的而设计。 此模式允许最多 64 名玩家同时在线 同时战场同时保持很高的帧 率。 并以真实的地形为特色，包括军用车辆， 大战中的坦克和直升机，我们还实施了 这场游戏中广泛的战争破坏和大规模破坏 模式。

---

## Slide 9

![Slide 9](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_009.png)

> 信息分类： 一般
>
> 最后是战役模式，非常典型的线性任务 游戏模式重启经典黑鹰坠落， 这也是发生在一张巨大的地图上。 本作的地形、环境以及游戏体验 模式将带你回到经典的三角洲部队IP 25年 前

---

## Slide 10

![Slide 10](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_010.png)

> 信息分类： 一般
>
> 好吧，所以在我们谈论其他事情之前，我们应该先谈谈 关于生物群落。在此，我将重点介绍一下跨平台的框架。

---

## Slide 11

![Slide 11](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_011.png)

**📌 要点汇总**

- **生物群落多样性**：通过多样的生态环境提升游戏世界真实感与沉浸感  
- **多地域环境适配**：支持全球不同气候、地形及战斗损毁效果的动态呈现  
- **跨平台资产复用**：系统化管理资源以实现双平台高效复用与性能优化  
- **着色技术应用**：核心解决方案聚焦于统一渲染管线与跨平台视觉一致性  
- **技术挑战主题**：探讨复杂环境

> 信息分类： 一般
>
> 该游戏具有各种生物群落，使整个三角洲 迫使世界更加真实可信。 虽然主要世界设定在摩洛哥，但其他游戏模式也会 发生在世界各地的不同地点 不同的气候、环境和战斗受损程度。 这些功能如何在两个巨大的 不同平台，系统化管理，甚至复用 资产尽可能多？这实际上是我们着色技术的主要主题 今天要讲的。

---

## Slide 12

![Slide 12](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_012.png)

**📌 要点汇总**

- **避免随机性/物质推导**：采用抽样纹理实现可控颜色变化，降低DrawCalls与管理复杂度  
- **10K纹理内存问题**：10

> 10 K 分辨率色调图
>
> 信息分类： 一般
>
> 对于植被种类，我们不想依赖 随机性，缺乏可信度。而且，也不是通过物质推导来实现这一点 会显着增加 DrawCalls 并使 管理和迭代更加困难。所以，一开始，我们尝试从大量样本中进行抽样 纹理以提供可控的颜色变化。
>
> 然而，对于 10x10 的开放世界，10k 纹理将 占用大约100Mb的内存，这对于 移动。所以，我们决定实现clipmap。

---

## Slide 13

![Slide 13](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_013.png)

> 参考：https://notkyon.moe/vt/Clipmap.pdf
>
> 信息分类： 一般
>
> 简而言之，Clipmap，它是一种动态纹理表示 在有限的时间内有效地缓存任意大尺寸的纹理 用于实时渲染的物理内存量 [CLICK] 如您所见，纹理更新随相机滚动 移动，在摄像机范围内使用 mip0 并逐渐 随着距离的增加，mip 级别逐渐降低。这显着减少了内存，同时保持了近距离 提高精度。最终，内存从原来的100MB下降到2.5MB 大约，使移动成为可能。

---

## Slide 14

![Slide 14](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_014.png)

> 排除 湿度 泡沫速度 G 速度 R 树木健康 烧焦吸收 草健康
>
> 信息分类： 一般
>
> 与常规纹理采样相比，剪辑贴图更新 消耗更多的指令，所以我们决定不仅仅是 植被色调或颜色，我们想将更多信息打包到 我们可以尽可能多地使用这个单一的剪辑贴图。这包括植被季节状态、水数据、地形 湿气/湿气等都包含在这个纹理中。
>
> 它本质上包含了我们游戏的所有生物群系信息。 来自各种生物群落模块的着色器都对这种纹理进行采样 地图。该框架在 PC 和移动设备上是统一的，我将 接下来详细解释一下。

---

## Slide 15

![Slide 15](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_015.png)

**📌 要点汇总**

- **健康等级划分**：植被健康值0.1-0.85表示健康，0.9-1表示损伤，用于区分季节与战斗伤害。  
- **Clipmap通道编码**：树木健康（

> Clipmap R：树木健康 Clipmap R & B：烧焦 Clipmap B：草健康
>
> 0.1-0.85：健康 0.9-1：伤害
>
> 信息分类： 一般
>
> 首先，我们来谈谈植被。在 10x10 的开放世界中， 由于不同地区的植被健康状况不同 周围环境。而且在其他游戏模式中，地图也有不同的 另外还有季节性设置。我们想要一个单一的植被模型来显示各种 外观以最大化资产重用。所以我们引入了健康等级的概念，我们将树木和草的健康信息分别打包 在剪贴图中。此外，我们将战斗伤害视为生命值的一部分，因此我们 还将损坏信息编码到这两个通道中。值 0.1-0.85 存储季节信息，同时存储战斗伤害 信息被限制在 0.9-1 内

---

## Slide 16

![Slide 16](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_016.png)

**📌 要点汇总**

- **LUT与剪贴图结合**：通过剪贴图值采样独立LUT，实现植被颜色变化的可控随机性  
- **资产生命值系统**：个人资产已配置生命值与战斗伤害参数作为全局输入  
- **跨平台一致性**：该方法确保不同平台间视觉表现和数据逻辑的统一性  
- **独立LUT管理**：为每个植被模型单独创建颜色变化查找表以提升可控性

> 手机
>
> 信息分类： 一般
>
> 除了使用剪贴图作为健康水平的全局输入之外，个人 资产已准备好相应的生命值和战斗伤害 因此，我们为每个植被模型创建颜色变化并放置 它们位于独立的查找表 (LUT) 中。通过使用剪辑图中的值对 LUT 进行采样，我们 最终得到看似随机但可控的结果。而且，这种方法在两者之间保持一致 平台。

---

## Slide 17

![Slide 17](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_017.png)

> B：染色面膜
>
> 信息分类： 一般
>
> 资产方面，在PC上，我们使用打包到NormalMap中的蒙版作为 色调蒙版并使用线性插值与基色 它。

---

## Slide 18

![Slide 18](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_018.png)

> 剪辑B：健康
>
> 信息分类： 一般
>
> 在移动端，为了进一步优化性能，我们 放弃了基色，而是完全依赖于 灰度图我们称之为股线掩模，它被打包到 NormalMap 所以输入数据切掉了一张纹理，这是戏剧性的 减少纹理采样。实用又便宜，视觉上我们都很开心 与此。

---

## Slide 19

![Slide 19](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_019.png)

> 焦色
>
> 信息分类： 一般
>
> 当植物的健康水平转向极端时，事实证明 植物燃烧状态，由 0.9 到 1 的值定义。它允许平滑过渡，同时避免需要 额外的材料衍生。当然，由于性能限制，在移动端，它只能 显示为深色燃烧。在 PC 上，我们添加了更多着色细节和复杂性。

---

## Slide 20

![Slide 20](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_020.png)

**📌 要点汇总**

- **炸弹集成**：通过规则生成陨石坑与燃烧效果，增强场景真实感  
- **材质细节**：添加烧焦树叶、火花等元素，支持材质质量等级降级调整  
- **风格一致性**：通过材质降级保持视觉风格与效果的统一性

> 信息分类： 一般
>
> 为了营造更好的氛围和真实感，我们集成了炸弹 根据一定的规则产生陨石坑和燃烧效果。
>
> [点击]我们还添加了更多材质细节，例如烧焦的树叶 和燃烧的火花。所有这些元素都可以通过材料轻松降级 质量等级，以保持风格和效果的一致性 平台

---

## Slide 21

![Slide 21](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_021.png)

> ClipMap B：吸收 ClipMap RG：速度 剪辑贴图 A (0.6 -1)：泡沫
>
> 信息分类： 一般
>
> 我们还将与水相关的信息打包到此剪贴图中。在空间上，河流和陆地生物群落是相互排斥的。那 意味着大多数植物不会同时在水下生长并且 在陆地上，所以我们可以合而为一，而且它们不会发生冲突。关于全球河流数据，我们存储以下信息： RG 通道采用两个河流速度向量（通常 称为流量图），B 渠道包含河流吸收，其中 基本上是控制水的颜色，河泡沫投入 阿尔法通道。

---

## Slide 22

![Slide 22](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_022.png)

**📌 要点汇总**

- **多次采样**：增加采样周期可提升波浪运动的自然外观效果  
- **设备差异化策略**：PC用三次采样+余弦权重，高端移动设备用两次采样，低端设备用线性混合  
- **余弦权重优化**：用于混合层间采样以模拟尖锐小波浪  
- **性能优化**：低端移动设备采用线性循环混合以减少指令开

> 电脑 移动高中 移动低
>
> 信息分类： 一般
>
> 流图多次采样可以模拟水流 波浪运动。由于波在其周期内重复， 采样周期越多，外观越自然。对于 PC，我们对波法线进行三次采样，混合 使用余弦函数作为权重的层之间，以及 模拟更尖锐的小波浪。对于高端移动设备，我们将其减少到两个样本 每 1/2 个周期混合一次；对于较低规格的移动设备，我们直接使用简单的线性 循环混合以节省余弦指令开销

---

## Slide 23

![Slide 23](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_023.png)

> 吸水率 水分散
>
> 信息分类： 一般
>
> 关于颜色，我们使用剪辑贴图中的吸收掩模来 定义基本水浊度水平，绘制吸收图 LUT和散射LUT共同描述水彩和 分散颜色。这使我们能够处理天然水而无需额外抽取， 例如区分河流、湖泊以及其影响 沉积物被冲走。

---

## Slide 24

![Slide 24](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_024.png)

**📌 要点汇总**

- **手机半透明渲染**：手机流水采用半透明渲染，与PC通过切断散射获取数据不同，仅对吸收LUT进行采样。  
- **浊度模拟技术**：通过alpha通道映射LUT模拟水的浊度，浊度越高，透光率越低，水体越不透明。  
- **低规格优化**：针对手机低规格设备进行了更广泛的半透明渲染优化，以适应性能限制。

> 吸水率
>
> 剪辑贴图通道 B
>
> 水分散
>
> 信息分类： 一般
>
> 手机流水采用半透明渲染，与PC不同的是 通过切断散射来获取数据。因此它只对吸收 LUT 进行采样。它还映射 LUT alpha 通道模拟水的浊度。这个很容易理解——越浑浊越深 水，透光率越低，使其越不透明。关于半透明，我们实际上做了更广泛的工作 优化，以适应低规格手机。

---

## Slide 25

![Slide 25](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_025.png)

> 完整渲染 正常 镜面反射 影子 胃肠道正常 镜面反射 影子 胃肠道
>
> 信息分类： 一般
>
> 如前所述，大多数较深的水往往是 不透明，我们目前没有任何水下游戏 到目前为止。所以，我们做了不同程度的性能优化 用于标准地形渲染、半透明关节，以及 几乎不透明的深水区，大大降低了GPU 时钟。

---

## Slide 26

![Slide 26](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_026.png)

**📌 要点汇总**

- **PC端水面倒影技术**：采用Screen Space反射与多IBL组合实现更真实效果  
- **移动端性能优化**：因性能限制仅使用IBL并手动调整参数提升视觉匹配度  
- **IBL手动调整策略**：基于捕获数据人工优化IBL参数以平衡视觉正确性与性能需求

> 信息分类： 一般
>
> 对于水面倒影，在 PC 上，我们使用了以下组合 Screen Space反射和多个IBL 在移动端，出于性能考虑，仅使用IBL 目前正在使用。但为了整体的相对正确性 视觉上，根据捕获的数据手动修改IBL以获得 更好的匹配。

---

## Slide 27

![Slide 27](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_027.png)

> 剪辑贴图 A (0.1 -0.5)：湿度
>
> 0.1-0.5：湿度
>
> 信息分类： 一般
>
> 最后，我们将湿度信息打包到剪贴图中 作为潮湿地形、潮湿岩石、水坑等的输入。

---

## Slide 28

![Slide 28](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_028.png)

> 黑暗面具
>
> 水坑水坑面膜
>
> 信息分类： 一般
>
> 剪辑贴图的精度仅为每米一个像素，但 地形，我们可以对高度层进行采样并将其与湿层混合 掩模阈值。然后夹住黑暗蒙版，给我们水坑区域。这个 实施湿润和水坑的方法可以节省额外的 绘制调用与使用贴花相比。

---

## Slide 29

![Slide 29](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_029.png)

> 信息分类： 一般
>
> 一旦这些潮湿区域被打包到剪贴图中，其他内容 可以利用它，比如我们的岩石，创造 与湿气和水坑的真实相互作用

---

## Slide 30

![Slide 30](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_030.png)

> 电脑 移动
>
> 信息分类： 一般
>
> 对于植物来说，全局光照会显着影响它们的生长 外观，其中AO是最重要的方面。在PC上，我们应用SSRTAO进行全局照明遮挡，而 从纹理中补充精细结构 AO。植物的预烘焙顶点 AO 仅影响地下 模拟多重散射遮挡
>
> 移动植物仅使用顶点 AO。对于草，可以得到AO 通过额外的 UV 坐标。另外，在移动端，AO也参与计算fake 阴影，这对于移动设备上的表示很重要

---

## Slide 31

![Slide 31](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_031.png)

**📌 要点汇总**

- **顶点/像素着色成本高**：处理顶点着色和像素着色在复杂场景中消耗大量资源。  
- **植物阴影优化挑战**：大量植物和阴影导致性能瓶颈，需通过LOD模型降低顶点数量。  
- **LOD模型质量缺陷**：使用低LOD模型投射阴影会导致阴影边缘粗糙、精度不足，影响视觉效果。

> 信息分类： 一般
>
> 处理顶点着色和像素着色时都非常昂贵 场景中有大量植物，有阴影 特别昂贵。对于树来说，我们不仅需要减少顶点数量， 还可以使用较低的 LOD 模型来投射阴影。
>
> 【CLICK】但这会导致阴影质量低得令人无法接受 - 你可以看到到处都是低精度和粗糙的边缘 树冠，真是可怕

---

## Slide 32

![Slide 32](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_032.png)

> 信息分类： 一般
>
> 所以我们应用顶点AO来直接光着色来近似 阴影以获得更平滑的过渡，同时降低成本 同时阴影采样通过调整假阴影，我们还可以近似模拟 多重透射效果，防止阴影过暗 和场景中的像素

---

## Slide 33

![Slide 33](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_033.png)

> 信息分类： 一般
>
> 最终你可以看到一个更稳定、更流畅、更统一的 结果。最重要的是它的价格便宜 性能的

---

## Slide 34

![Slide 34](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_034.png)

**📌 要点汇总**

- **草渲染阴影处理**：草因渲染复杂度高，不投射也不接收阴影，通过随机值与AO混合模拟类似树的阴影效果  
- **假

> 信息分类： 一般
>
> 草渲染比树重得多，所以它既不投射也不投射 接收阴影。我们使用每个实例的随机值与 AO 混合作为假值 阴影，类似于树。稍微复杂的部分是假阴影衰减 基于观看距离和角度，防止出现刺眼的黑色 从远处观看或向下看时的过渡。

---

## Slide 35

![Slide 35](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_035.png)

**📌 要点汇总**

- **

> 信息分类： 一般
>
> 此外，由于草的数量较多，因此不会投射阴影。我们将草地位置信息烘焙到地形剪贴图中 采样，添加额外的直接光和镜面遮挡 地形，这有效地改善了地形和草地之间的融合 当它们实际上没有被阴影覆盖时。

---

## Slide 36

![Slide 36](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_036.png)

> 信息分类： 一般
>
> All right, so let‘s talk about the distant foliage To get good performance and visuals across all platforms, the vegetation distance rendering differs significantly between PC and mobile, so we prepared three different approaches.
>
> 首先是impostor，仅在PC上使用并服务 作为植被网格的最终LOD级别 然后，是Billboard，专门用于 手机上的远距离模型最后，我们称之为装配卡，这是一个真实的背景，以及 它完全用于地图边界和区域 通过游戏无法到达。这个两个平台都用。

---

## Slide 37

![Slide 37](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_037.png)

> 参考：Billboard Clouds for Extreme Model Simplification (2003) 用于森林渲染的Extreme Model Simplification for Forest Rendering (2005) 《战神》中的风与植被互动（2019）
>
> 信息分类： 一般
>
> 首先，我们来看看冒名顶替者，我们使用的是相当常见的技术，已经介绍过 在之前的许多演讲和论文中——这实际上是一种方法 基于网格卡。它的概念很简单，它捕获来自 不同角度，主张最佳角度，然后重复 对模型的其余部分进行处理，直到 什么都没有剩下。

---

## Slide 38

![Slide 38](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_038.png)

> 信息分类： 一般
>
> 但这样，我们注意到它产生了良好的结果 丛生的树冠。然而，如果我们一味地套用卡片生成和纹理捕捉 对于所有树或某些特殊类型的整棵树，我们最终会 卡片过度使用和纹理像素浪费。我们有多个不同地区的地图；植被 类型多样且差异明显。为了挤更多 性能，我们得到了不同的东西

---

## Slide 39

![Slide 39](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_039.png)

**📌 要点汇总**

- **分离处理**：独立分离树冠与树干，通过少量卡片（如3张）高效捕捉纹理并拟合模型。  
- **差异化处理**：树冠侧重集群与体积表现，树干采用不同策略，提升整体建模精度。  
- **合并

> + =
>
> 信息分类： 一般
>
> 我们将树冠和树干独立分离，然后 使用尽可能少的卡片来捕捉纹理，同时效果更好 拟合树模型。例如，通常只需3张牌即可获得 一辆非常满意的卡车。
>
> 分别生成这两部分的另一个优点是 我们可以以不同的方式对待他们。例如，树冠 需要更多地强调集群和体积，而树干和 最后，我们将两部分合二为一

---

## Slide 40

![Slide 40](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_040.png)

> 组合（躯干+皇冠）
>
> 信息分类： 一般
>
> 我们在整个树上实现了抖动时间 AA 以获得 平滑过渡。我们使用顶点颜色来区分零件，从而允许 分别为每个参数设置不同的参数。这种方法减少了树干的卡片状外观 同时保持较高的树冠密度

---

## Slide 41

![Slide 41](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_041.png)

> 信息分类： 一般
>
> 与PC冒名顶替者相比，广告牌在以下方面的应用更为广泛： 较低性能的平台。在移动设备上，我们使用这种方式来处理远处的植被。 根据不同的树，我们的方法 处理广告牌的方式各不相同。我们一般有三种做法：第一种是单平面广告牌，这是最常见的。 常见类型的广告牌。我们用这个来实现最对称的效果 我们游戏中的植被。
>
> [点击] 非常简单，我们 选择合适的拍摄视角，并且无论 玩家在世界上的位置，广告牌总是面向 玩家。

---

## Slide 42

![Slide 42](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_042.png)

**📌 要点汇总**

- **双平面广告牌**：用于植物，解决单平面不对称问题  
- **双角度纹理捕捉**：从两个相差90度的视角获取纹理  
- **平行平面应用**：双平面广告牌始终面向玩家

> 信息分类： 一般
>
> 但难免有不少不对称的地方 植物，使用单平面广告牌显然不合适。因此，对于此类植被，我们使用双平面广告牌。
>
> [CLICK]这涉及从两个角度捕捉纹理 形状差异显着，相差 90 度。这些纹理应用于两个平行平面，并且 就像单平面广告牌一样，它们总是面向玩家。

---

## Slide 43

![Slide 43](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_043.png)

**📌 要点汇总**

- **双平面广告牌**：通过两个平行平面实现视觉过渡，提升渲染效果  
- **抖动技术**：用于平滑角度变化时的视觉过渡，减少锯齿感  
- **动态间距调整**：根据相机距离实时优化平面间距，避免Z-fight现象

> 网格 双平面广告牌
>
> 信息分类： 一般
>
> 然后，我们使用抖动技术来创建平滑的效果 观察时两个平行平面之间的过渡 角度变化。 [CLICK]最后，我们动态调整间距 基于相机距离的两个平面，以防止 z-fight 时 从远处观看。

---

## Slide 44

![Slide 44](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_044.png)

> 信息分类： 一般
>
> 另一种类型的广告牌我们称为倾斜平面广告牌。这通常用于非常倾斜、高度的树木 轮廓不对称，例如手掌。
>
> [CLICK]我们从最对称的位置捕捉纹理 角度作为原始纹理，然后我们在着色器中倾斜它

---

## Slide 45

![Slide 45](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_045.png)

**📌 要点汇总**

- **树干树冠分离处理**：在着色器中将树干与树冠分开，分别应用不同的变形操作（偏移、旋转、扭曲等）。  
- **躯干参数调整**：通过弯曲曲率和枢轴偏移量调整树干形态，主观驱动以匹配实际模型。  
- **Lerp函数应用**：利用Lerp函数

> 网格 倾斜平面广告牌
>
> 信息分类： 一般
>
> 在着色器中，我们将树干和树冠部分分开， 在顶部应用偏移、旋转甚至扭曲。对于躯干，我们调整弯曲曲率和枢轴偏移量这实际上是一个非常主观驱动的操作，力求 将形状与实际模型对齐。
>
> 通过Lerp函数，我们最终恢复了轮廓 在一个平面上倾斜的树。

---

## Slide 46

![Slide 46](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_046.png)

> 缩放卡（在着色器中）
>
> 信息分类： 一般
>
> 我想指出的另一个技巧是，无论 广告牌的类型，我们最初标准化了平面的尺寸， 无论树木的实际大小。然后，我们调整阴影的大小以符合实际情况，即 在移动设备上支持批处理，并显着减少 渲染成本

---

## Slide 47

![Slide 47](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_047.png)

> 装配卡
>
> 信息分类： 一般
>
> 对于人迹罕至的森林地区，我们做了更进一步的事情。这实际上是广告牌技术的延伸，其中 艺术家手动放置各种比例随机的广告牌 形成组件。然后将其捕获为原始纹理并 将其应用于条形平面，并创建我们所说的装配卡。不同类型的集结卡的组合， 然后在遥远和难以到达的地区建造森林 三角洲特种部队的世界。

---

## Slide 48

![Slide 48](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_048.png)

> 信息分类： 一般
>
> 好吧，让我们继续进行植入 程序主义
>
> 关于程序世界生成，已经有很多了 业界成熟的解决方案

---

## Slide 49

![Slide 49](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_049.png)

> 参考：《幽灵行动：荒野》地形工具和技术 (2017) 《孤岛惊魂 5》程序世界生成 (2018) CLIPMAP
>
> 信息分类： 一般
>
> 是的，我们使用基于Houdini的工作流程，生成过程 离线我们获取地形信息，根据地形信息生成点云 具体规则，将它们返回给引擎，并实例化生物群落 由于这种方法很常见，我想你们大多数人都知道 就这个，今天就不展开了。相反，我将更多地关注讨论我们如何进行跨平台 实施。当然首先就是我们刚才讲的Clipmap。 其中存储的大部分数据是由PCG生成和修改的。

---

## Slide 50

![Slide 50](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_050.png)

> 信息分类： 一般
>
> 在我们的游戏中，几乎所有的地形和生物群系都是相连的 一起并根据食谱，我们提供画笔工具 预设给艺术家和内容创作者。 [单击]预设包括地形、植被资源、贴花和 视觉特效（如落叶、浮尘、烟雾、雾气等）。 艺术家只需选择相应的预设即可在其中进行绘画 他们想要的世界，无需做任何额外的步骤或 设置

---

## Slide 51

![Slide 51](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_051.png)

**📌 要点汇总**

- **预设工具组**：使用预设工具组进行编辑，但食谱与平台解耦，导致跨平台HDA文件差异  
- **跨平台HDA差异**：PC与移动设备因平台限制和性能需求，需独立HDA文件实现不同结果  
- **性能优化目标**：通过解耦设计解决平台兼容性问题，优先保障移动设备运行效率

> 电脑硬盘驱动器 移动HDA
>
> 信息分类： 一般
>
> 这让我们可以在编辑器中使用一组预设工具，但是 我们的食谱是完全解耦的，这意味着相同的 Recipe对于每个平台都有单独的HDA文件最后，我们在PC和移动设备上得到不同的结果，主要是为了 解决平台限制和性能问题。

---

## Slide 52

![Slide 52](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_052.png)

**📌 要点汇总**

- **跨平台一致性**：PC与移动端共享生物群系类型，需保持外观相似性  
- **继承机制**：通过Houd

> 信息分类： 一般
>
> 虽然PC端和移动端是两个独立的管道，但由于 他们共享相同的生物群系类型，我们仍然希望他们拥有 相似的外观。当然，在创建和迭代过程中，我们 不想做两次事情。所以，我们寻找两者之间的继承关系 版本并在Houdini中进行降级操作。我们的方法 就是锁定菜谱中高优先级的元素并继承 他们到移动版本，同时获得不太重要的装备 诸如矮树、小灌木丛和装饰物等元素 对象。这导致了一个简化的移动版本，保留了 整体看起来相似。

---

## Slide 53

![Slide 53](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_053.png)

> 信息分类： 一般
>
> 而且，如果我们仍然存在一些性能热点，需要减少 仅凭配方复杂性无法满足要求，我们还设计和创建专门的配方以获得更多 积极降低某些地区的密度和类别 您可以将其视为仅限移动设备或移动专用工具 仅影响移动版本。

---

## Slide 54

![Slide 54](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_054.png)

**📌 要点汇总**

- **生物群系设计**：基于预设并满足特定

> 信息分类： 一般
>
> 我们尝试使生物群系尽可能基于预设，但 满足非常具体的游戏需求，我们还提供了灵活性 手工放置树木和大灌木丛，[点击]但是周围的装扮需要考虑到程序 处理最后，细节将生成得非常好 集成的。

---

## Slide 55

![Slide 55](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_055.png)

**📌 要点汇总**

- **体素化检测相交**：通过3D数组总和判断模型是否交叉，值≥2表示相交  
- **自动修正流程**：反复调整模型方向并验证，直至消除植被重叠问题  
- **跨平台一致性**：在PC与移动设备同步执行修正，确保植被布局整齐  
- **棕榈树案例**：以棕榈树为例验证算法有效性，解决植被交叉核心问题

> 网格转换为 3D 体素
>
> 信息分类： 一般
>
> 我们实施了自动更正来处理 大块植被的重叠和交叉。喜欢 棕榈树始终是最好的例子首先，我们应该找到一种方法来验证它们是否相交
>
> [CLICK]所以我们对几何体进行了体素化，3D 体素是 相当于值为 1 的 3D 数组。如果最大值 多个 3D 数组的总和等于 2 或更大，则 意味着模型相交。 [CLICK]接下来，我们自动更改任一方向 模型 然后我们再次进行验证和修正 一遍又一遍地重复这个过程，直到什么都没有 这样交叉，我们在PC和移动设备上都这样做，以确保所有树 摆放整齐。

---

## Slide 56

![Slide 56](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_056.png)

> 信息分类： 一般
>
> 草漂浮是一个普遍的问题，尤其是在移动设备上。的 移动设备上草簇模型的边界框通常是 由于预算和性能限制，我们要做的，[点击]首先，射线将投影投射到地形上，测量草模型的枢轴与地形本身之间的距离，如果结果超过阈值，则将漂浮的草拉下来 稍加验证，去除浮草，或者在性能允许的情况下更换较小的

---

## Slide 57

![Slide 57](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_057.png)

**📌 要点汇总**

- **PCG控制**：通过调整密度和替换模型类型，灵活优化渲染效率。  
- **Drawcall优化**：动态减少Drawcall次数，实现性能与视觉效果的平衡。  
- **跨平台平衡**：PC与移动版在感知体验上趋同，同时满足各自性能需求。  
- **质量适配**：针对不同平台调整模型复杂度，确保视觉质量与性能的最优匹配。

> 信息分类： 一般
>
> 因为一切都是由PCG控制的，所以我们可以调整 密度以减少三角形，或替换某些类型的模型 灵活减少drawcall次数，达到最优 每个质量级别的视觉和性能之间的平衡。最后我们得到了PC版和移动版 感知上相似，同时满足质量和性能 两个平台的根本需求。

---

## Slide 58

![Slide 58](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_058.png)

**📌 要点汇总**

- **性能优化

> 最后，道路也是地形的一部分，所以让我 详细说明我们在一些低配手机上出于性能原因所做的一些优化 由于限制，我们不支持VT（虚拟纹理）。并且 此外，我们的地形精度已从 1m/grid 降低 至2m/格。正如你所看到的，道路和地形几乎到处都有重叠， 而且 z-fight 非常严重。
>
> 因此，即使使用相同的数据输入，每个方法 需要改变。

---

## Slide 59

![Slide 59](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_059.png)

**📌 要点汇总**

- **拓扑调整**：为低规格设备生成2米精度道路模型，但导致三角形数量激增  
- **LOD优化**：通过多边形缩减技术对远处道路进行

> 信息分类： 一般
>
> 在程序处理中，我们生成额外的道路 专门针对低规格设备的模型，其中拓扑 需要改为2米以匹配地形网格 精确地[CLICK]所以从视觉上看它看起来是正确的，但是，这会导致 另一个问题是三角形的极度增加 对于这种低规格的设备来说，这也是负担不起的
>
> [CLICK]所以我们将远处的道路作为 LOD 进行多边形缩减 模型。 [CLICK]为了避免再次重叠，此外，在 顶点着色器，我们逐渐向上拉顶点以避免它 从远处看[点击]最后看起来一切都很好。
>
> 好吧，现在我要把它交给我们的领导者引擎 程序员，焦航。他会带你了解核心 技术特点

---

## Slide 60

![Slide 60](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_060.png)

> 项目X
>
> 信息分类： 一般
>
> 大家好，我是焦航，Jade Studio 引擎团队负责人。你可以叫我杰西。我从事手机游戏工作已有 10 年， 曾开发过多款成功的游戏，包括《穿越火线》 和COD Mobile，它们都使用Unity引擎。
>
> 今天我将重点讨论地形和技术方面 生物群落渲染，在游戏 Delta Force 中，使用了 Unreal 发动机 4.24（四点二四）。

---

## Slide 61

![Slide 61](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_061.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 信息分类： 一般
>
> 首先，让我们了解地形纹理。

---

## Slide 62

![Slide 62](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_062.png)

**📌 要点汇总**

- **虚拟纹理**：通过纹理缓存算法节省带宽，提升地形渲染效率  
- **贴花功能**：支持在地形表面添加细节贴图，增强视觉表现  
- **跨平台兼容**：实现PC与移动设备高质量地形渲染的统一方案  
- **自适应VT**：虚幻引擎中动态调整纹理精度以优化性能的技术实现

> 信息分类： 一般
>
> 就像前面利川说的，我们使用虚拟纹理来渲染地形 纹理。 VT基本上是一种纹理缓存算法，它节省了 带宽。此外，它还允许在地形上贴花。这使我们能够在 PC 和移动设备上渲染高质量的地形。我们在虚幻引擎中使用自适应VT。

---

## Slide 63

![Slide 63](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_063.png)

**📌 要点汇总**

- **运行时压缩必要性**：未压缩纹理会导致高带宽占用与发热，需通过ASTC 4*4/6*6压缩降低影响  
- **ASTC格式特性**：采用仅支持双端点模式的简化算法，省略分区处理以提升效率  
- **跨设备兼容方案**：通过像素着色器实现统一压缩流程，输出128位unsigned int4

> 信息分类： 一般
>
> 要在移动设备上使用 VT，我们需要进行运行时压缩 纹理，然后写入 VT。如果未压缩，这意味着每帧需要大量带宽， 并带来热量。 [CLICK] 因此，我们将它们压缩为 ASTC 4*4（四乘四）_ 或 6*6（六 六）。我们使用非常简单的算法，仅支持两个端点 模式，ASTC 中没有分区。 [CLICK] 对于兼容性问题，我们使用像素着色器来执行 所有移动设备上的压缩。首先，我们从像素着色器输出到 unsigned int 4 纹理， 其中每个像素是 128 位，适合表示中的块 美国技术委员会。然后将纹理复制到缓冲区，然后再传输到 压缩纹理。

---

## Slide 64

![Slide 64](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_064.png)

**📌 要点汇总**

- **带宽效率

> 信息分类： 一般
>
> 这是结果。 [点击]在带宽方面，每帧是四分之一或九分之一。 [CLICK] PSNR 为 40 至 50，我们的艺术家对此感到满意 由此产生的外观。 [CLICK] 我们可以将 VT 页面压缩为 0.2 左右（第二点） 毫秒。

---

## Slide 65

![Slide 65](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_065.png)

> 信息分类： 一般
>
> 接下来，我们来谈谈地形纹理的基础——splat 贴图。我们在两个平台上使用基本相同的方法进行 splat 地图。这为手机游戏提供了非常高质量的地形。 [CLICK] 我们将 PBR 纹理的通道打包成更少的纹理 移动。有 2 个纹理数组，一个用于反照率和高度图， 其他用于正常、粗糙度和环境光遮挡。

---

## Slide 66

![Slide 66](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_066.png)

**📌 要点汇总**

- **多层需求**：艺术家要求至少32层以增强视觉表现力  
- **ID映射与权重混合**：需结合高度混合及可控权重实现自然过渡  
- **低带宽限制**：纹理采样受限，需优化资源使用效率  
- **现有方法不足**：传统ID地图

> 我们来看看要求。 [CLICK] 我们的艺术家想要更多层，至少 32 层， 让世界变得多姿多彩。 [CLICK] 好的，我们需要以某种方式使用 ID 映射。 [CLICK] 我们需要基于高度的混合，并且可控 重量。这允许在大面积上混合两层， 使过渡看起来更自然。 [CLICK] 好的，我们需要为每个点的每一层分配一个权重 地形。 [CLICK] 而且我们需要低带宽，这意味着我们无法使用 纹理样本太多。 [CLICK] 但是，嘿，每层权重方法，就像虚幻一样 默认情况下，不支持这么多层。您需要对所有样本进行采样 可能的层数以获得最终结果。 [CLICK] 而且，ID 地图方法，就像《Far Cry》和《Ghost Reckon》所做的那样， 不支持权重混合。他们只能拥有一个ID 点。我们能做什么？

---

## Slide 67

![Slide 67](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_067.png)

**📌 要点汇总**

- **图层顺序**：明确图层从下到上的覆盖顺序以简化问题  
- **双层ID存储**：每个地形点存储底部和顶层ID，禁用三层结构  
- **权重固定**：底层权重固定为1，仅需存储顶层权重值  
- **ID

> 5位 5位 3位底部ID 顶部 ID 混合 重量 顶部
>
> 信息分类： 一般
>
> 因此，让我们从一种简单的方法开始，以简化问题。 [CLICK] 首先我们可以给图层一个明确的顺序，使它们 从下到上互相覆盖。 [CLICK] 对于地形上的每个点，我们存储 2 个图层 ID，一个底部 层和顶层。我们不允许同一点有 3 层。所以我们可以假设底层总是有一个权重值 为1，因此我们只需要存储顶层的权重。我们使用ID映射来存储这些信息，并有一个分辨率 每米 1 点。

---

## Slide 68

![Slide 68](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_068.png)

> 信息分类： 一般
>
> 为了获得 ID 贴图，我们的艺术家为每一层绘制权重 通常在编辑器中。 [CLICK] 在地形的每个点上，我们只保留 2 层 最大重量。

---

## Slide 69

![Slide 69](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_069.png)

> ID6 ID7 ID4 ID5
>
> 信息分类： 一般
>
> 因此对于地形上的每个像素，我们需要获取周围 4 个点 并在它们之间进行插值。 [CLICK]我们需要采样4个ID地图点，然后采样8个图层， 这意味着移动设备上有 20 个样本。 [点击] 这太多了，需要减少。

---

## Slide 70

![Slide 70](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_070.png)

**📌 要点汇总**

- **ID限制优化**：将Texels的ID限制从6降至3，减少采样层数。  
- **层数减少方法**：通过插值调整，将图层从8层减少至6层，再进一步优化至3层。  
- **功能验证结果**：测试表明

> Sample 3 Texels Get 6 IDs Limit down to 3
>
> 信息分类： 一般
>
> 首先给大家介绍一个小技巧。 [CLICK] 我们可以在三角形内部进行插值，而不是在三角形内部插值 square around it. [CLICK] 这将层数从 8 层减少到 6 层。它可能会给地面带来一些三角形的外观，但是 适当的图层混合，几乎察觉不到。但仍然有6层，而大多数时候，艺术家 不会在同一个地方画那么多层。 [CLICK] 如果我们使用此信息并限制不同的 ID 会怎样 from 6 down to 3?这样我们就得到了6个ID号，但是我们只需要采样 3 层。 [CLICK]我们测试了这个方法，发现3是一个 保持功能转换的最小值，并且足以 代表复杂的地形。

---

## Slide 71

![Slide 71](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_071.png)

> 信息分类： 一般
>
> 那么我们如何从 6 个 ID 中获得 3 个不同的层 triangle?我们离线进行 ID 修复通行证。当艺术家在编辑器中为每个三角形绘制权重时， we get 6 layer numbers. 3 bottom, and 3 top IDs. [点击] 在我们开始之前，创建一个空集，大小为 3。 [点击] 首先，我们将所有 3 个底部 ID 添加到该集合中。 [CLICK] 如果未满，我们将继续将顶级 ID 逐一添加到集合中。 [CLICK]请注意，我们首先添加权重最大的。 [CLICK] 如果已满，我们通过将顶部 ID 设置为 与底层相同的ID。

---

## Slide 72

![Slide 72](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_072.png)

**📌 要点汇总**

- **ID删除影响**：删除ID不会破坏相邻三角形结构，仅处理当前ID关联。  
- **层级顺序规则**：各层ID有明确顺序，顶部ID始终大于底部ID。  
- **ID提取目标**：从6个数字中提取最小、中间和最大ID用于后续处理。

> 最小Idx 中号 最大Idx
>
> 信息分类： 一般
>
> 由于我们只是删除 ID，因此处理相邻的 ID triangles won’t break the current one.
>
> 现在我们在 6 个号码中只有 3 个不同的 ID。并且 请记住，我们为各层定义了明确的顺序，因此 顶部 ID 始终大于底部 ID。 [CLICK]接下来，我们需要从shader中的6个数字中获取3个ID， 即最小、中间和最大 ID。

---

## Slide 73

![Slide 73](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_073.png)

> 最小Idx 中号 最大Idx
>
> 信息分类： 一般
>
> 在着色器中，对于每个要着色的像素，首先我们需要解码 3个ID图样本，得到6个ID号和3个权重。 [CLICK]然后我们可以从这6个数字中得到最小、中间和最大ID， 与这里的代码。

---

## Slide 74

![Slide 74](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_074.png)

> 信息分类： 一般
>
> 最后，我们可以获得每个三角形上每一层的权重 点，并在它们之间进行混合。这些幻灯片随后将在 GDC Vault 上提供。所以我会 继续。

---

## Slide 75

![Slide 75](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_075.png)

> 这是一个总结。 [点击] 与传统的每层权重方法相比，我们的方法 允许更多层。 [点击] 与《Far Cry》或《Ghost Reckon》中的 ID-map 方法相比， 我们的方法允许权重混合。 如果你想在ID-map方法中进行转换，你必须做一个 混合两层的附加层，消耗更多 记忆。 在我们的方法中，我们可以混合任意两层， 没有内存成本。 [点击] 此外，两层的混合可以产生类似的效果 正常的叠加和阻尼，就像他们在《巫师 3 Wild》中所做的那样 狩猎。

---

## Slide 76

![Slide 76](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_076.png)

> 信息分类： 一般
>
> 以及悬崖渲染。在 VT 上，UV 通常从 XY 世界位置投影。这个 导致悬崖上的外观拉伸。 [CLICK] 因此，一种方法是使用三平面，这需要对 再纹理 2 次，从 XZ 和 YZ 投射 UV，然后混合 他们之间。这是每帧的额外成本。还有其他方法来优化三平面，通常 仍然涉及在基础通道中采样额外的纹理。

---

## Slide 77

![Slide 77](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_077.png)

**📌 要点汇总**

- **XY投影局限性**：XY投影在平坦地形显示良好，但悬崖等地形会导致UV拉伸变形  
- **三平面渲染挑战**：直接渲染三平面至VT存在技术障碍，需考虑投影方式适配性  
- **地形复杂性影响**：不同地形特征（如悬崖）对UV映射效果产生显著影响，需优化处理方案

> 信息分类： 一般
>
> 那么为什么不直接将三平面渲染到 VT 中呢？让我解释一下。 [点击]我们通过 XY 投影看到，这是自上而下的视图 地形，只有在平坦的地形上才好看。 [CLICK] 在悬崖上，如果我们仍然用 XY 投影，UV 看起来会很 伸展。

---

## Slide 78

![Slide 78](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_078.png)

**📌 要点汇总**

- **UV视觉错觉**：VT页面显示拉伸但

> 信息分类： 一般
>
> 如果我们将 XZ 或 YZ 投影到悬崖上，UV 看起来就不会如此 伸展。请注意，它在 VT 页面中可能看起来被拉伸，但实际上并非如此 在网格本身上。 [CLICK] 因此，获得正确 UV 的一个简单方法是：对于 VT 通道中的每个像素，我们检查法线方向。基于此，我们决定使用 XY、XZ 或 YZ 作为最佳选择 投影平面。并使用该 UV 来绘制该像素。

---

## Slide 79

![Slide 79](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_079.png)

**📌 要点汇总**

- **Z轴位置与地形网格**：需提供实际地形网格而非简单四边

> 修复网格 CDLOD网格
>
> 接缝呢？
>
> 信息分类： 一般
>
> 为了实现这一点，我们需要 Z 轴位置。我们需要将实际的地形网格提供给 VT 管道，而不是 原始的简单四边形。 [CLICK] 请记住使用 SampleGrad，因为我们正在更改 UV 每个像素，我们需要手动指定正确的 mipmap。 [点击]这就是结果。你可以看到，UV不再被拉伸，但是有一个 清晰的接缝。 [点击]接缝怎么样？

---

## Slide 80

![Slide 80](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_080.png)

> 信息分类： 一般
>
> 为了修复接缝，我们使用随机方法，灵感来自《孤岛惊魂》。 [CLICK] 令我们惊讶的是，这在 VT 中看起来很好很自然。帧之间是一致的，因为我们并不总是 刷新 VT 缓冲区。由于它具有 mipmap，因此不会出现锯齿问题。

---

## Slide 81

![Slide 81](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_081.png)

**📌 要点汇总**

- **成本效益**：采用随机方法以最低成本实现Tri-planar类似效果，优于双平面方法  
- **方法选择**：随机方法因混合效果足够且成本可控，被选为游戏发布方案  
- **分辨率限制**：直接绘制悬崖至VT存在分辨率下降问题，但被判定为可接受结果  
- **样品对比**：1样品有接缝/2样品无接缝，验证了无接缝方案的可行性  
- **

> 过渡
>
> 1 个样品，有接缝 2个样品，无接缝 1 个样品，无接缝
>
> 信息分类： 一般
>
> 因此，我们以最小的成本实现了与Tri-planar类似的效果。我们还尝试了双平面方法，它具有更好的混合效果， 增加了成本。随机方法看起来足够好，这就是我们使用的方法 游戏中发货。 [CLICK] 将悬崖直接绘制到 VT 中有一个限制，即最大 仔细观察时，分辨率会降低。我们认为这是一个可以接受的结果。

---

## Slide 82

![Slide 82](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_082.png)

**📌 要点汇总**

- **高LOD mips块状问题**：远处使用

> 信息分类： 一般
>
> 还有其他技巧可以提高视觉质量。使用高度混合时，在相机附近看起来不错，但是 远处呈块状。由于在距离上，混合使用高 LOD mips，这 精度不够，导致看起来块状。除了使用远平铺因子之外，我们还引入了另一个技巧。 [CLICK] 我们在距离上逐渐切换到线性混合。它看起来更柔和，解决了块状问题。

---

## Slide 83

![Slide 83](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_083.png)

**📌 要点汇总**

- **地形细节丢失**：运行时移动设备显示的地形缺乏编辑器中的沟壑和侵蚀细节，显得平坦。  
- **性能优化限制**：为平衡渲染性能与视觉效果，远处地形细节被简化以降低计算负载。  
- **编辑器与运行时差异**：艺术家在

> 信息分类： 一般
>
> 运行时还会出现另一个问题。我们的艺术家在编辑器中绘制地形，看起来很详细 无处不在。但在运行时，尤其是在移动设备上，地形看起来很平坦 距离。沟壑和侵蚀被消除。

---

## Slide 84

![Slide 84](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_084.png)

**📌 要点汇总**

- **地形网格优化**：编辑器中地形包含38万faces，运行时版本优化至8万faces以提升性能。  
- **运行时网格密度降低**：通过减少远处网格密度显著降低计算负载。  
- **几何细节损失**：顶点法线中的几何细节因网格简化而减少。

> 信息分类： 一般
>
> 原因是在编辑器中，地形有380k（38万） faces，而运行时版本只有80k（8万）。我们大大降低了远处网格的密度，对于 性能。 [CLICK] 因此，反映在顶点法线中的几何细节是 也减少了。

---

## Slide 85

![Slide 85](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_085.png)

**📌 要点汇总**

- **Streaming Virtual纹理（SVT）**：通过烘焙顶点距离数据为纹理，解决网格存储空间不足问题  
- **SVT与RVT共享物理纹理**：无需额外内存成本，直接加载SVT数据至物理纹理  
- **mipmap烘焙与页面请求处理**：下部mipmap烘焙至SVT格式，页面请求时优先加载SVT数据而非RVT渲染

> 信息分类： 一般
>
> 为了恢复细节，我们引入了 Streaming Virtual 纹理来解决问题。由于网格中没有足够的空间来存储顶点 距离正常，我们可以将其烘焙为纹理。
>
> 整个地形的下部 mipmap 被烘焙到 SVT 中 格式。 [CLICK] 在 VT pass 中，当我们收到页面请求时，我们检查是否 有 SVT 数据。如果是这样，我们直接将其加载到物理纹理中，而不是 通过RVT方法渲染它。
>
> SVT 和 RVT 共享相同的物理纹理，因此不存在 额外的内存成本。

---

## Slide 86

![Slide 86](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_086.png)

> 全场景顶点法线 地图米级精度 = 80,000-face + 米级精度顶点法线10K地图的SVT
>
> 信息分类： 一般
>
> 所以我们将顶点法线烘焙到SVT中，并忽略顶点 渲染到屏幕时地形网格上的法线。正常信息现在完全在 SVT 中。但是当SVT在相机附近与RVT混合时，我们必须使用 同样的方法可以避免接缝。也就是说，我们还将顶点法线渲染到 RVT 中。这个 要求我们使用实际的地形网格来渲染VT，只需 就像我们对悬崖所做的那样。 [CLICK] 结果看起来不错，没有丢失任何细节 距离。我们的艺术家甚至可以通过以下方式定制远处的外观 一方面，通过改变离线SVT。

---

## Slide 87

![Slide 87](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_087.png)

**📌 要点汇总**

- **FOV变化影响**：快速FOV变化导致VT重绘精度提升，地形突现干扰敌人  
- **解决方案**：引入偏差保持mip级别，提升游戏流畅度  
- **权衡代价**：瞄准镜开启时地形呈现模糊效果

> 信息分类： 一般
>
> 此外，我们的游戏中有很多精美的曲调。例如，由于我们的游戏是快节奏的FPS游戏，当 我们使用枪的瞄准镜，相机FOV变化非常快， 这会导致 VT 重绘到更高的精度。这是非常明显的，因为我们可以看到这里的地形突然出现 在那里，干扰寻找敌人。 [CLICK] 因此，我们在打开范围时引入了额外的偏差，以 当 FOV 改变时，保持请求的 mip 级别。这使得游戏玩起来更加流畅，但代价是 打开瞄准镜时，地形看起来有点模糊。

---

## Slide 88

![Slide 88](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_088.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 信息分类： 一般
>
> 接下来，我们将讨论地形几何。

---

## Slide 89

![Slide 89](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_089.png)

> 景观代理 顶点纹理获取+高度图集+CDLOD
>
> 信息分类： 一般
>
> 使用虚幻中的默认解决方案，地形的每个图块都有 一个单独的绘制调用，这需要多次绘制调用 渲染整个地形。这对于移动设备来说是一笔很大的成本。 [CLICK] 所以我们引入了 CDLOD，它代表 Continuous 与距离相关的细节级别，用于渲染我们的地形 网格。它使用绘制实例来渲染图块的所有不同 LOD。
>
> 一个实例是一个网格，它靠近相机较小，并且 距离较大。所有实例都具有相同的顶点数，因此它们更密集 离我们较近，较远则稀疏。
>
> 这样我们只需要1~2次Draw Calls就可以绘制整个 地形。

---

## Slide 90

![Slide 90](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_090.png)

**📌 要点汇总**

- **LOD细分优化**：通过细分更高LOD图块减少实例数量，通常生成4个实例。  
- **顶点着色器剪切**：在顶点着色器中剪切低LOD部分，合并顶点位置以简化网格。  
- **实例数量减少**：剪切后仅需绘制2个实例，顶点数相同但减少绘制次数。

> 信息分类： 一般
>
> 此外，我们使用一个小技巧来减少实例数量。当我们请求地形图块具有更高的 LOD 时，通常我们 将其细分为四个更高 LOD 的图块，使其成为 4 个实例 渲染。 [CLICK]但是我们也可以把低LOD对应的部分剪掉 网格，然后细分所需的部分。剪切是在顶点着色器中完成的，设置位置 在一起。这样，我们只绘制了2个实例。每个实例都有相同的顶点数，因此我们用更少的数量进行绘制 顶点。

---

## Slide 91

![Slide 91](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_091.png)

**📌 要点汇总**

- **硬件镶嵌问题**：存在性能差、三角形图案不理想及移动端不适用等缺陷  
- **软曲面细分方案**：作为CDLOD的自然扩展，通过引入LOD -1/-2实现优化  
- **高度图采样**：对VT高度图进行采样并修改几何图形以提升地形精度  
- **LOD层级扩展**：通过多级LOD（-1/-2）增强地形补丁的细节表现与性能平衡  
- **技术改进方向**：从硬件转向软件方案，解决传统镶嵌技术的局限性

> 信息分类： 一般
>
> 并用于镶嵌。 硬件镶嵌存在很多问题。 它有性能问题，而且三角形图案不理想， 这可能会带来更多的错误。 而且不适合移动端。 [点击] 因此，我们实现了软曲面细分。 这是 CDLOD 的自然扩展，通过引入 LOD -1, -2, 对于地形补丁等，它对 VT 中的高度图进行采样 修改几何图形。

---

## Slide 92

![Slide 92](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_092.png)

**📌 要点汇总**

- **

> 信息分类： 一般
>
> 对于软镶嵌，我们需要非常高的几何密度 附近。我们希望密度随着距离的增加而迅速减小。但CDLOD需要相邻之间的LOD级别差异 补丁合而为一。这个限制带来了很多补丁的浪费。正如您所看到的，我们削减了额外的补丁来满足此限制。 [CLICK] 我们放宽了这一限制，允许将 LOD 划分为多个 次，并保留剪切剔除方法。 [CLICK] 传统的方法是2乘2细分，我们尝试了4乘4 和 8 x 8。您可以看到，通过我们之前介绍的剪切技巧， 实例数更小，网格密度下降得更快 这边。 [CLICK] 我们选择 4 x 4，因为它在 错误率和实例数。

---

## Slide 93

![Slide 93](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_093.png)

> Soft-Tess 错误图 Hard-Tess 错误图
>
> GPU(ms) 软件曲面细分 0.15 ms 硬件曲面细分 3080 上的性能为 0.62 毫秒
>
> 信息分类： 一般
>
> 与硬件曲面细分相比，该方法具有更好的 性能，并且具有更好的三角形图案，带来更少的 错误。我们已经在 PC 上发布了它。 [CLICK] 这应该也适用于移动设备，但我们没有足够的 是时候将其运送到最终游戏中了。在高中档设备上值得一试。

---

## Slide 94

![Slide 94](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_094.png)

> 信息分类： 一般
>
> 而且我们还有很多性能优化，其中优化 为了时间和内存，更重要的是，为了手机的热量。

---

## Slide 95

![Slide 95](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_095.png)

**📌 要点汇总**

- **纹理数量级优化**：将纹理数量从10K级降至640x5级，内存占用减少至1%  
- **剪贴贴图内存优化**：剪贴贴图内存从133.3MB压缩至1.95MB，节省98.5%空间  
- **clipmap技术应用**：通过动态加载高精度纹理，按相机视角保留细节以节省内存  
- **多场景

> 减少到 10K 纹理数量级 → 640x5 纹理阵列数量级为 1%！ 剪贴贴图 133.3MB →1.95MB
>
> 信息分类： 一般
>
> 正如利川之前所说，我们在很多地方都使用了clipmap。这是一种仅加载高精度纹理的有用技术 相机周围的细节较少，具体取决于 您想保留细节的程度。它可以节省大量内存。

---

## Slide 96

![Slide 96](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_096.png)

**📌 要点汇总**

- **splat ID贴图转换**：将splat ID贴图转为剪贴贴图，仅保留局部高精度数据  
- **场景渲染器替代VT渲染器**

> Splat ID 贴图剪辑贴图纹理
>
> 信息分类： 一般
>
> 我们还将 splat ID 贴图变成了剪贴贴图，因为我们只 需要我们附近的高精度数据。 [CLICK] 我们没有为每个图块使用一个 VT 渲染器，而是使用一整套 场景渲染器，用于管理剪辑贴图流。演员数量减少，口吃现象减少。

---

## Slide 97

![Slide 97](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_097.png)

**📌 要点汇总**

- **动态纹理数组**：仅在需要时加载纹理并填充到数组空位，减少内存消耗  
- **mipmap优化**：中距离渲染使用较小mipmap，控制全分辨率图层数量  
- **分层加载策略**：近处地形使用部分32层，远处使用完整32层实现性能平衡

> 信息分类： 一般
>
> 如果我们将所有 32 层的纹理加载到一个纹理数组中， 会消耗太多内存。当渲染我们附近的地形时，我们只会使用一部分 32层。所以我们实现了动态纹理数组，仅加载纹理 当需要时，并将它们填充到纹理数组中的孔中。
>
> 渲染中距离地形时，我们使用完整的32层 纹理数组，具有较小的 mipmap。这控制了加载所需的全分辨率图层的数量。

---

## Slide 98

![Slide 98](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_098.png)

> 信息分类： 一般
>
> 我们监控自动使用的层数，并执行 可视化图层检查。在 POI 之间的过渡区域，内存压力较低， 这样我们就可以放宽限制以获得更好的质量。

---

## Slide 99

![Slide 99](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_099.png)

**📌 要点汇总**

- **优化混合层数**：减少像素混合层数（草/泥土多用单层），多数区域不超过2层  
- **着色器排列策略**：根据页面实际使用层数（1-3层）动态选择着色器排列方式  
- **低内存数据采集**：离线统计LOD页面使用层数，内存成本极低  
- **LOD切换优化**：高精度LOD VT页面频繁切换物理纹理需适配

> 信息分类： 一般
>
> 还有另一个优化机会。我们允许 3 个不同的层来混合每个像素，但是很多图块 不要使用那么多层。有大面积使用单层，如草和泥土。 大部分区域混合的层数不超过 2 层。请注意，我们经常绘制高精度 LOD VT 页面，它们 不断地在物理纹理中切换。 [CLICK] 因此，我们对着色器进行 3 种排列，然后选择 根据页面使用的层数进行排列 即将渲染。这些数字是离线收集的，内存成本极低。

---

## Slide 100

![Slide 100](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_100.png)

> 对于移动设备，我们可以优化 VT pass 中使用的渲染目标。我们想在 VT 中使用 2 个纹理，将通道堵塞在一起， 在基本通道中保存样本计数。 [CLICK] 但由于我们有用于贴花的 alpha 混合，我们仍然需要 渲染 VT 页面时将不透明度作为 Alpha 通道。 [CLICK] 之后，我们使用子通道或帧缓冲区获取来 将通道重新排列成理想的形式。由于这利用了移动设备上的片上内存，因此不会 解析回主存。 [CLICK]然后，我们可以对ASTC进行压缩。为了进一步优化，如果我们发现特定图块不包含 alpha 混合，我们简单地绘制到具有理想通道的 RT 安排。这些信息也是离线烘焙的。

---

## Slide 101

![Slide 101](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_101.png)

> 至于跨设备扩展，我们有很多参数需要调整 切换。我们可以在不同的设备上有不同的最大分辨率， 关闭此选项意味着 VT 脏页更少。 [CLICK] 我们可以设置 VT mip 偏差以及纹理数组 MIP 偏差。它可以在低端节省一些内存。 [CLICK] 我们的地形网格高度图精度为 1 米 在高端，而在低端则回退至 2 米精度 设备。这意味着需要着色的顶点更少。 [CLICK] 地形网格 LOD 距离标量为我们提供了另一种方法 通过减少远处网格的密度来减少顶点数 更快。 [CLICK] 我们可以限制一帧中填充的页面数量， 以减少口吃的机会。 [CLICK] 此外，异向纹理采样可以设置为不同的 由质量水平控制的值。

---

## Slide 102

![Slide 102](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_102.png)

> 信息分类： 一般
>
> 在非常低端的移动设备上，我们有一个特殊的路线 地形渲染。这主要是为了兼容性问题。一些低端设备 VT 有问题。我们必须寻找另一条不使用 VT 的路线。 [CLICK] 我们直接在基础通道中渲染 splat 贴图。由于没有良好的动态纹理数组支持，我们使用 完整的 32 层纹理阵列，但分辨率较小。 [CLICK] 我们将 splat 贴图减少为每个顶点单层， 这实际上回退到 ID 映射方法。 [点击]我们删除法线贴图。 [CLICK] 由于没有贴花支持，道路需要 渲染为单独的网格。

---

## Slide 103

![Slide 103](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_103.png)

**📌 要点汇总**

- **参数微调**：在不同设备上调整参数以确保流畅运行和良好外观  
- **设备性能优化

> 信息分类： 一般
>
> 我们在许多不同的设备上微调了每个参数， 确保每台设备运行流畅且外观良好 尽其所能。这是不同级别设备上的最终内存占用量。

---

## Slide 104

![Slide 104](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_104.png)

> 信息分类： 一般
>
> 这是一些性能结果数据

---

## Slide 105

![Slide 105](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_105.png)

**📌 要点汇总**

- **4层权重法**：与移动设备广泛使用的4层权重法进行性能对比测试  
- **骁龙855测试**：所有数据基于骁龙855芯片，仅针对地形渲染性能测试  
- **性能优势**：在帧速率、功耗、带宽及GPU时间等指标全面优于对比方法  
- **32层支持**：方法可扩展支持32层地形及大量贴花，提升渲染复杂度

> 我们测试了地形渲染性能，比较了我们的 方法为4层的每层权重法，其中 在移动设备上被广泛使用。所有数据均来自骁龙855，仅测试 地形渲染。我们可以看到，无论高调还是低调， 我们的方法在帧速率、功耗方面获胜， 带宽和 GPU 时间。更好的是，我们可以支持 32 层，并带有大量贴花。

---

## Slide 106

![Slide 106](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_106.png)

> 信息分类： 一般
>
> 这是今天的要点。
>
> 对于生物群落和地形渲染，我们限制了复杂性，并且 同时适应PC端和移动端。我们整合程序方法，使迭代更快 更好。我们引入了独特的地形纹理方法和 几何，以及我们的性能和可扩展性方式。
>
> 对于未来的工作，我们可以制作更好的天气系统 实施，并探索水下功能。我们可以对地形法向阻尼进行更多测试，以改善 视觉效果。

---

## Slide 107

![Slide 107](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_107.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 信息分类： 一般
>
> 非常感谢我们伟大的同事，他们是真正的英雄。我们要感谢整个三角洲部队团队。感谢 GDC 委员会。感谢大家参加我们的演讲。

---

## Slide 108

![Slide 108](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_108.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 108 信息分类：一般
>
> 如果您有疑问，我们会在那里，我们可以使用 总结室。谢谢你！

---

## Slide 109

![Slide 109](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_109.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 信息分类： 一般

---

## Slide 110

![Slide 110](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_110.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 110 信息分类：一般

---

## Slide 111

![Slide 111](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_111.png)

**📌 要点汇总**

- **平方插值**：相比三角形插值，平方插值生成8个ID但需保留3个，需特殊处理。  
- **ID选择策略**：优先添加底部ID（0-2），再补充顶部ID，确保集合容量为3。  
- **动态调整规则**：若集合已满，优先保留权重高的ID，替换冗余的顶部ID。  
- **最终验证步骤**：检查底部ID 3与顶部ID 3是否在集合

> 信息分类： 一般
>
> 如果您发现三角形插值对您来说不够好， 你可以尝试平方插值。不过 ID 修复可能会略有不同。我将提供它 参考。
>
> 通过平方插值，我们得到 8 个 ID，我们仍然想要 保留这 8 个号码中的 3 个 ID。那么我们如何从 8 个数字中获得 3 个不同的层呢？对于每个方格，我们得到 8 个层数。 4 个底部 ID 和 4 个顶部 ID。 [点击] 在我们开始之前，创建一个空集，大小为 3。 [点击] 首先，我们将 0、1 和 2 个底部 ID 添加到该集。 [CLICK]如果未满，我们继续将0、1、2个top ID添加到 设置，一一设置。 [CLICK][CLICK]请注意，我们仍然添加最多的那些 首先称重，如果已满，则去除多余的顶部 ID。 [点击]现在我们来到了最后一个角落。首先我们添加底部 ID 3 和顶部 ID 3 按顺序添加到该组。
>
> 然后我们检查底部 ID 3 和顶部 ID 3 是否确实在集合中：
>
> 1. 他们在场，我们很好。
>
> 2.它们都不在集合中，我们将它们都更改为底部ID 1
>
> 或 2
>
> 3. 部分在集合中，丢弃不在集合中的，并设置它
>
> 到另一个的号码。

---

## Slide 112

![Slide 112](https://gerigory.github.io/assets/img/GDC/2025/GDC2025-Delta-Force-Performant-High-Quality-Terrain-and-Biome-Technology-for-PC-and-Mobile/slide_112.png)

> 信息分类： 一般
>
> 我们仅删除 0、1 和 2 的层，可能会更改 3 与原始 ID 不同。 [CLICK] 所以在处理当前的方块时，我们不会破坏 绿色方块，但可能会破坏红色方块 颜色。所以我们需要按顺序处理方块，以确保 整个过程结束后，每个方格最多有3个不同的ID。

---
