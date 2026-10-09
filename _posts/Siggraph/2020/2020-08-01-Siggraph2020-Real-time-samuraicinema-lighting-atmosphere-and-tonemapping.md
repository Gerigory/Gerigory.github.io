---
layout: post
title: "【Siggraph 2020】Siggraph2020 - Real-time samuraicinema lighting atmosphere and tonemapping"
date: 2020-08-01
img: Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_001.png # Add image post (optional)
fig-caption: # Add figcaption (optional)
tags: [Siggraph, 2020, Lighting, Rendering]
description: 本文分享的是【Siggraph 2020】Siggraph2020 - Real-time samuraicinema lighting atmosphere and tonemapping相关的技术要点
---

> 来源：D:\迅雷下载\Graphics Materials\已摘录\【已摘录】Siggraph 2020 - Real-time samuraicinema lighting atmosphere and tonemapping.pdf
> 提取时间：2026-05-16 08:20:10

---

## Slide 1

![Slide 1](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_001.png)

> 你好！我叫 Jasmin Patry，在 Sucker Punch Productions 担任首席渲染工程师。我很荣幸也很兴奋能与您谈论 我们在《对马岛之魂》中用于创建实时“武士影院”体验的一些技术。

---

## Slide 2

![Slide 2](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_002.png)

> 如果您不熟悉 Sucker Punch，我们自 2011 年起就成为索尼互动娱乐公司的一部分，位于华盛顿州贝尔维尤，靠近 西雅图。 [下一页] 在《Ghost》的开发过程中，我们工作室的人数达到了160人的顶峰， [下一页] 我们之前的游戏包括 [下一页] 狡猾的库珀系列， [下一页] 以及臭名昭著的系列游戏。

---

## Slide 3

![Slide 3](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_003.png)

**📌 要点汇总**

- **PlayStation 4版发布**：去年夏天推出《对马岛之魂》PS4版本  
- **免费合作多人扩展

> 去年夏天，我们发布了 PlayStation 4 版《对马岛之魂》。 [下一页] 秋季推出了免费合作多人游戏扩展包， [下一页] 在向后兼容模式下在 PS5 上玩游戏时还支持 60 FPS。

---

## Slide 4

![Slide 4](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_004.png)

> 《幽灵》是一款以 13 世纪封建日本为背景的开放世界动作冒险游戏……

---

## Slide 5

![Slide 5](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_005.png)

> ...您在其中扮演武士Jin Sakai的角色...

---

## Slide 6

![Slide 6](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_006.png)

> ...蒙古入侵对马岛的唯一幸存者...

---

## Slide 7

![Slide 7](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_007.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> ...当他为解放家园而奋斗时。

---

## Slide 8

![Slide 8](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_008.png)

> 在开始我的材料之前，我想插入一些可能与你们中的一些人相关的其他演讲。 [下一页] 在去年的 SIGGRAPH 上，作为基于物理的着色课程的一部分，我做了一次演讲，内容涉及我们为 Ghost 所做的一些着色研究。 [下一页] 今年的 GDC 上有过几次演讲； Eric Wohllaib 做了关于程序草的演讲； [下一页] 马修·波尔曼 (Matthew Pohlmann) 发表了一场讨论世界构建和渲染的演讲； [下一页] 比尔·罗肯贝克（Bill Rockenbeck）谈到了风和布料； [下一页] Adrian Bentley 讨论了我们如何让游戏加载得如此之快等。

---

## Slide 9

![Slide 9](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_009.png)

**📌 要点汇总**

- **开放世界设计**：打造比以往更大的动态开放世界，重现1274年对马岛的沉浸式体验  
- **动态环境系统**：引入前所未有的动态天气与连续时间系统，增强世界真实感  
- **电影化视觉风格**：通过戏剧灯光、风效与天空氛围，复刻经典武士电影美学（含黑泽模式）  
- **历史沉浸感**：以“时间机器”概念构建历史场景，让玩家深度体验古代对马岛文化  
- **技术突破**：通过环境动态系统与视觉风格创新，实现游戏世界的“生命力”与情感共鸣

> 我们在《Ghost》中的目标包括所谓的“时间机器”：我们希望让玩家沉浸在 1274 年我们版本的对马岛中。 [下一页] 这意味着创建一个巨大的、动态的开放世界——比我们之前的游戏大得多—— [下一页] 那真是美得令人窒息，而且感觉还活着。 [下一页] 它还意味着创建一个动态的天气和连续的时间系统，这是我们以前没有做过的。 [下一页] 我们还想重现经典武士电影的风格—— [下一页] 《幽灵》甚至有一个“黑泽模式”来纪念这位传奇电影制作人—— [下一页] 这意味着我们需要戏剧性的灯光、刺骨的风以及富有表现力的天空和氛围。

---

## Slide 10

![Slide 10](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_010.png)

> 现在我来谈谈《Ghost》中的灯光；我们的艺术方向要求“风格化的现实主义”——所以我们在这个项目上的目标并不是照片写实主义。 [下一页] 然而，我们的光照模型是基于物理的；它们是节能的，使用具有可选各向异性的 GGX 镜面 NDF；他们用史密斯 可见度函数和 Schlick Fresnel 近似。漫射照明是朗伯照明，具有可选的节能半透明和模糊模型。 灯光是使用物理单位编写的，我们支持节能区域灯光。 [下一页] 我们的材料是使用物理上合理的参数和一些摄影测量来编写的。这使得我们的材料能够以一致的方式响应光 方式。 [下一页] 我们的间接照明由动态更新的球谐函数和反射探针组成，基于当前的天空和定向光，加上局部 光传输数据。 [下一页] 说到天空，我们对所有大气照明（包括云、雾霾和大气照明）使用基于物理的多散射大气散射模型。 颗粒。 [下一页] 我们的场景采用 HDR 进行渲染，并使用一组自定义技术进行色调映射，这些技术是实现我们想要的外观所必需的。 [下一页] 由于我们的目标不是照片写实主义，因此我们确实允许艺术家在照明阶段偏离物理正确性，使用一组旋钮，使他们能够 全局调整各种照明参数（例如环境漫反射和镜面平衡、天空亮度等）。这通常是在粒度上完成的 我们的天气系统中的天气和时间状态。 [下一页] 在本次演讲中，我将详细阐述此处强调的三个主题。

---

## Slide 11

![Slide 11](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_011.png)

**📌 要点汇总**

- **间接照明技术**：涵盖漫射照明与间接镜面照明，提升场景真实感。  
- **大气体积照明**：用于渲染天空

> 本次演讲将分为三个部分： [下一页] 首先，我将讨论我们的间接照明技术， [下一页] 首先关于漫射照明， [下一页] 接下来是间接镜面照明。 [下一页] 然后我将讨论我们的大气体积照明方法， [下一页] 它被用来照亮我们的天空、云彩， [下一页] 体积雾度， [下一页] 和颗粒。 [下一页] 最后我将介绍我们的色调映射技术， [下一页] 包括我们本地的色调映射操作员， [下一页] 我们的颜色分级方法使用白平衡和自定义色调映射颜色空间， [下一页] 以及我们对人类视觉系统的低光行为的模拟，以帮助渲染令人信服的夜间场景。

---

## Slide 12

![Slide 12](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_012.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 现在，我们来谈谈间接照明。

---

## Slide 13

![Slide 13](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_013.png)

> 我们将从漫射照明开始。在《臭名昭著：次子》中，我们使用以四面体网格排列的二次辐照度探头来提供间接 整个世界的漫射照明。 [下一页] 您可以参阅 Adrian Bentley 的 GDC 2014 演讲了解更多详细信息。

---

## Slide 14

![Slide 14](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_014.png)

> 这非常适合我们的要求，即一天中的静态时间和天气，变化仅发生在负载之后。

---

## Slide 15

![Slide 15](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_015.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 这是没有本地 SH 探测器的相同场景。

---

## Slide 16

![Slide 16](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_016.png)

**📌 要点汇总**

- **动态时间与天气处理**：首次需处理动态时间与天气变化，调整原有方法以适应新需求  
- **规则探测器网格布局**：采用规则网格覆盖整个岛屿，确保探测范围全面性  
- **三维高度分层布置**：探测器沿地面间隔12.5m布置，分1.5m、10m

> 在《幽灵》中，我们必须照亮一个更大的世界，并且我们必须第一次处理一天中的动态时间和天气，因此我们必须做出一些改变 我们的方法。 [下一页] 为了覆盖整个岛屿，我们使用规则的探测器网格， [下一页] 沿地面间隔12.5m布置，高程为距地面1.5、10、30m。

---

## Slide 17

![Slide 17](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_017.png)

> 这是一天中 24 小时的周期，显示了整个岛屿 9 个 SH 波段的绝对值。快速的变化发生在日出时 和日落。

---

## Slide 18

![Slide 18](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_018.png)

**📌 要点汇总**

- **四面体网格**：用于解决探头间距过粗

> 例如，探头的间距太粗，无法准确照亮内部，因此我们使用四面体网格（或“四面体网格”） [下一页] 在城镇、村庄、农庄等地方。 [下一页] 这些作为单独的单元进行流式传输，因此四面体网格也与它们一起进行流式传输。 [下一页] 加载后，四面体网格会覆盖网格，并且它们在边界处混合。

---

## Slide 19

![Slide 19](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_019.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 前景是游戏中的金庙地点......

---

## Slide 20

![Slide 20](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_020.png)

> ...在这里您可以看到它的一些四面体网格。

---

## Slide 21

![Slide 21](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_021.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 该缓冲区显示漫反射间接照明...

---

## Slide 22

![Slide 22](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_022.png)

> ...正如您所看到的，常规网格照明和四面体网格照明之间存在平滑过渡。

---

## Slide 23

![Slide 23](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_023.png)

> 由于游戏的动态时间周期和动态天气，我们需要在运行时更新辐照度探测器。 [下一页] 离线，而不是捕获 [下一页] 辐照度...

---

## Slide 24

![Slide 24](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_024.png)

**📌 要点汇总**

- **SH表示**：使用球谐函数（SH）捕获天空能见度信息  
- **运行时投影**：动态计算天空的SH投影以适应实时变化  
- **探测器更新**：通过亮度与可见度相乘更新探测器数据  
- **卷积处理**：与余弦波瓣卷积模拟传统辐照度探头效果  
- **照明

> [下一页] ...我们捕获天空能见度的 SH 表示， [下一页] 在运行时， [下一页] 我们计算天空的 SH 投影， [下一页] 然后通过将天空亮度乘以天空可见度来更新探测器， [下一页] 并将结果与余弦波瓣进行卷积，就像使用传统的辐照度探头一样。结果就像普通辐照度探头一样使用 照明的目的。

---

## Slide 25

![Slide 25](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_025.png)

**📌 要点汇总**

- **直接照明局限**：原方法仅提供直接天空光，无法模拟环境反射光  
- **SH函数近似**：通过天空可见性SH函数，用均匀白光近似捕获反射光  
- **

> 这种方法有效，但它只能提供直接的天空照明—— [下一页] 也就是说，没有来自环境的反射光。 [下一页] 在《臭名昭著》中，我们尝试了辐射传输矩阵，它适用于小世界， [下一页] 但由于它们需要至少九倍的存储空间，因此它们会占用太多内存， [下一页] 并且花了太长时间才捕捉到。 [下一页] 因此，如果天空光在半球上近似恒定，我们选择的近似值是有效的： [下一页] 我们使用天空可见性 SH 函数，通过均匀的白色天空有效地照亮世界来捕获反射光。 [下一页] 然后，我们将这种辐射度投射到 SH 以捕获反射的天空可见度。 [下一页] 在运行时，我们将反射的天空可见度乘以平均天空颜色，并将其添加到之前的结果中。

---

## Slide 26

![Slide 26](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_026.png)

**📌 要点汇总**

- **SH表示**：使用球谐函数（SH）仅基于天空信息构建明亮场景表示  
- **排除可见性**：未引入天空可见性信息，仅依赖天空光照数据进行场景建模  
- **场景特性**：示例展示SH在复杂光照条件下的高效表示能力与局限性  
- **技术对比**：通过对比传统方法，凸显SH在简化计算中的优势与潜在偏差  
- **应用限制**：强调仅使用天空信息可能导致的环境细节丢失问题

> 好吧，让我们看一些例子。这里我们有一个仅使用天空的 SH 表示的明亮场景，即不使用天空可见性信息。

---

## Slide 27

![Slide 27](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_027.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 这就是直接天空能见度数据的样子......

---

## Slide 28

![Slide 28](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_028.png)

> ...反弹的天空能见度数据如下所示。黄色来自寺庙周围树木明亮的黄色叶子， 落叶落在地上。

---

## Slide 29

![Slide 29](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_029.png)

> 这又是没有使用天空可见性数据的场景......

---

## Slide 30

![Slide 30](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_030.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> ...这就是我们使用直接天空可见度时得到的结果。

---

## Slide 31

![Slide 31](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_031.png)

> 添加反射天空可见性会添加一些黄色反射光。

---

## Slide 32

![Slide 32](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_032.png)

**📌 要点汇总**

- **关键词**：引入太阳光模型补充反射照明  
- **关键词**：利用反弹天空可见性避免数据冗余

> 然而，反射天空照明本身还远远不够。在晴朗的天气中，就像前面的例子一样，大部分反射光来自太阳，所以 我们需要一种方法将其添加到我们的模型中。 [下一页] 我们希望避免存储额外的数据，因此我们问自己是否可以利用反弹的天空可见性数据。 [下一页] 我们的想法是考虑一组固定的弹跳方向；与假设反射光均匀分布在整个表面相比，这给出了更好的结果 球体。 [下一页] 通过将这些反射方向的 SH 表示乘以反射的天空能见度 SH，然后乘以太阳或月亮辐照度，我们得到 SH 反射光的表示。 [下一页] 这使得一个相当大的假设，即由弹跳天空能见度捕获的表面的余弦加权平均天空能见度是一个很好的 估计他们的阴影。 [下一页] 在很多情况下情况并非如此，但事实证明它对于我们的目的来说是一个足够好的近似值。

---

## Slide 33

![Slide 33](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_033.png)

**📌 要点汇总**

- **反射方向**：主要来自水平（地平面）和垂直（墙

> 好的，那么我们使用了哪些反弹方向？我们观察到，实际上大多数反射光来自水平或垂直表面，因此我们使用 想象的 [下一页] 地平面 [下一页] 和墙平面。我们在这些平面上反射光；事实证明，这些向量 r_g 和 r_w 指向完全相反的方向。 [下一页] 我们将（否定的）反射光方向投影到 SH 中； [下一页] 这就是它的样子（在去环以确保它们到处都是积极的之后）。 [下一页] 然后，我们按光颜色对其进行缩放（应用云阴影后，云阴影是动态的，因此不会被天空可见性捕获）， [下一页] 并将其乘以反弹的天空 SH 表示，并将其添加到之前的结果中。

---

## Slide 34

![Slide 34](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_034.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 这是一个没有阳光反射的场景......

---

## Slide 35

![Slide 35](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_035.png)

**📌 要点汇总**

- **阳光反射**：添加阳光反射显著改变了场景视觉效果  
- **场景差异**：反射效果使同一场景呈现明显不同特征  
- **视觉影响**：光照反射对场景真实感和细节表现有重要影响

> 这是添加了阳光反射的同一场景。正如您所看到的，它产生了相当大的差异。

---

## Slide 36

![Slide 36](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_036.png)

> 这是另一个例子，这次是在寺庙内。这里我们没有使用天空可见度，因此照明非常平坦。

---

## Slide 37

![Slide 37](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_037.png)

> 这是直接天空能见度......

---

## Slide 38

![Slide 38](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_038.png)

> 以及反弹的天空能见度。

---

## Slide 39

![Slide 39](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_039.png)

> 这又是没有使用天空能见度数据的寺庙......

---

## Slide 40

![Slide 40](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_040.png)

**📌 要点汇总**

- **直接天空可见度**：使用该方法得出结果，但未明确具体表现  
- **结果分析**：未提供量化数据或对比信息  
- **应用局限

> ...这就是我们使用直接天空可见度时得到的结果。

---

## Slide 41

![Slide 41](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_041.png)

> 添加反射的天空光会使物体变亮一点（相对于外部）......

---

## Slide 42

![Slide 42](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_042.png)

> ...同时添加反射阳光可以很好地加热它。

---

## Slide 43

![Slide 43](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_043.png)

**📌 要点汇总**

- **二次SH局限性**：二次SH乘积截断至2阶，导致高频数据丢失，灯光效果平淡  
- **启发式优化方法**：对delta函数进行线性SH投影，计算成本低且效果提升  
- **分项处理策略**：分别对辐照度探头的直接光与反射光部分独立应用SH投影  
- **混合系数应用**：最终采用25% lerp系数平衡不同处理结果的权重

> 如果您使用过 SH，您就会知道二次 SH 不能很好地表示高频数据。我们将二次 SH 函数相乘， 这给出了 4 阶 SH 结果，但为了保持数据大小合理，我们截断了高阶项并仅存储到 2 阶。 [下一页] 因此，我们的灯光看起来有点平淡。 [下一页] 我们采用另一种启发式方法来改进这一点：我们在线性 SH 最大值方向上对 delta 函数进行 SH 投影， [下一页] 计算成本低廉。 [下一页] 我们分别对辐照度探头的直接部分和反射部分进行了此操作。 [下一页] 最终，我们在整个游戏中使用了 25% 的 lerp 系数。

---

## Slide 44

![Slide 44](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_044.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 这是一个没有应用方向性增强的场景......

---

## Slide 45

![Slide 45](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_045.png)

**📌 要点汇总**

- **性能提升**：场景优化实现25%性能提升，增强渲染效率  
-

> ...这是相同的场景，但提升了 25%。正如您所看到的，它有助于为法线贴图提供更多定义。

---

## Slide 46

![Slide 46](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_046.png)

**📌 要点汇总**

- **负瓣问题与去振铃**：通过修改

> 如果您使用过 SH，您可能_也_知道负瓣是一个问题。在这种情况下，去振铃是修改SH的过程 代表性，以确保到处都是积极的。 [下一页] 最初，我们尝试对天空可见度应用额外的固定去振铃因子，但这降低了探头的方向性和保真度。 [下一页] 相反，我们在 GPU 上运行时对天空亮度和最终辐照度进行探测， [下一页] 使用 Peter-Pike Sloan 在本文中描述的方法。 [下一页] 在实践中，我们发现单个牛顿步足以找到 SH 最小值， [下一页] 我们使用深度为 3 的二叉搜索树来找到确保 SH 处处为正所需的最小去振铃因子。

---

## Slide 47

![Slide 47](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_047.png)

> 本文提出了一种新的窗口函数，它比 Inknown 中使用的旧窗口函数提供了更清晰的结果，正如您在此处看到的， 我们对 delta 函数的 SH 表示进行加窗。红色曲线使用旧的窗口函数，而蓝色曲线使用新的窗口函数 一。 （图表链接：https://www.desmos.com/calculator/bopiih3uka）

---

## Slide 48

![Slide 48](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_048.png)

> 这是一个在窗户附近呈现负瓣的场景......

---

## Slide 49

![Slide 49](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_049.png)

**📌 要点汇总**

- **运行时去振铃修复**：通过实时处理消除振铃效应，不改变场景整体照明  
- **独立探头测量**：对每个探头单独测量以确保场景其余部分的照明保持不变  
- **照明隔离技术**：独立处理探头数据避免修复过程影响全局光照效果

> ...这是通过运行时去振铃修复的。请注意，场景其余部分的照明不会改变，因为我们独立地对每个探头进行了测量。

---

## Slide 50

![Slide 50](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_050.png)

**📌 要点汇总**

- **SH投影耗时**：

> 以下是 SH 更新的一些性能数据。将天空亮度投影到 SH 大约需要 60 微秒，包括去振铃步骤。 此步骤使用了 4096 个样本，每个线程一个样本，因此这不会使 GPU 饱和（我们在异步计算中并行运行所有 SH 更新） 使用我们的仅深度通道）。我们每帧更新一个四面体网格，平均网格约为 5000 个探针（这也不会让 GPU 饱和）。对于 常规网格，我们每帧更新 8x8 个图块，加上每帧最接近相机的 3x3 个图块。这足以使基础 PS4 GPU 饱和 （尽管不是 PS4 Pro）。请注意，常规网格数据交错直接系数和反弹系数，因此消除更新中的反弹对整体影响很小 性能（因为缓存压力相同）。

---

## Slide 51

![Slide 51](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_051.png)

**📌 要点汇总**

- **漏光问题**：辐照度探头穿透障碍物导致不自然照明，影响渲染效果  
- **Inknown解决方案**：厚墙加探头有效，但《幽灵》因薄墙和复杂内部空间难以应用  
- **尝试方法**：圆锥体、遮挡平面、低分辨率阴影贴图均未达预期效果且性能损耗高

> 当明亮的辐照度探头“泄漏”墙壁或屋顶等障碍物时，就会出现漏光，导致另一方出现不自然的明亮照明 边。这是我们在 Inknown 中设法解决的一个问题， [下一页] 主要是因为我们没有太多的内部空间，有问题的情况可以通过在厚墙上放置额外的探头来解决。 [下一页] 然而，在《幽灵》中，有很多内部空间，而且由于当时的建筑风格，它们的墙壁都很薄。 [下一页] 我们尝试了多种解决方案来解决这个问题： [下一页] 我们向每个探头添加了圆锥体，以指示哪些相邻探头被遮挡（因此不应采样）， [下一页] 我们尝试向探针添加遮挡平面来代表墙壁和其他障碍物， [下一页] 我们尝试了低分辨率阴影贴图， [下一页] 但这些方法都没有让我们满意地解决问题，而且它们的性能开销也非常高。

---

## Slide 52

![Slide 52](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_052.png)

**📌 要点汇总**

- **探测器分类**：将探测器划分为内部与外部两类，作为后续处理的基础。  
- **内部掩模值创建**：通过几何属性、顶点颜色或延迟贴花为表面分配默认值w=0.5。  
- **权重调整策略**：内部探针使用w权重，外部探针使用1-w权重，影响重心坐标计算。  
- **辐照度混合逻辑**：重新规范化调整后的重心坐标，按权重混合辐照度；若权重全零则回退至原始重心。

> 我们最终找到了一个在运行时开销和额外创作负担方面可行的解决方案。首先，我们将探测器分类为_内部_ 或_外部_。 [下一页] 然后我们为所有表面分配一个_内部掩模_值w，默认为0.5。该值可以使用以下任一方式创建 [下一页] 几何体或着色器的属性， [下一页] 顶点颜色通道， [下一页] 或作为延迟贴花单独应用。 [下一页] 为了执行照明，我们像平常一样计算四面体重心坐标，然后将每个坐标乘以 [下一页] w 如果坐标属于内部探针， [下一页] 如果属于外部探头，则增加 1-w。 [下一页] 然后，我们重新规范化重心并像往常一样计算加权辐照度混合。 （如果所有权重都为零，我们就回落到 原始重心。）

---

## Slide 53

![Slide 53](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_053.png)

**📌 要点汇总**

-

> 这是在不使用内部遮罩权重的情况下照明的内部场景。

---

## Slide 54

![Slide 54](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_054.png)

> 由于漏光，后墙比应有的更亮。

---

## Slide 55

![Slide 55](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_055.png)

> 应用内部掩模解决了漏光问题。

---

## Slide 56

![Slide 56](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_056.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

---

## Slide 57

![Slide 57](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_057.png)

> 这显示了场景内部遮罩的价值。

---

## Slide 58

![Slide 58](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_058.png)

**📌 要点汇总**

- **（无内容）

> 这是另一个例子，首先没有内部面罩......

---

## Slide 59

![Slide 59](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_059.png)

> ...这里应用了面具。注意后墙上部的漏光是如何修复的。

---

## Slide 60

![Slide 60](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_060.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

---

## Slide 61

![Slide 61](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_061.png)

**📌 要点汇总**

- **探针优化**：通过添加生物群落默认探针和实例化内部探测器，减少探针数量需求  
- **数据挑战**：重新点亮需额外数据（1.5倍压缩点亮探针大小），改用

> 好的，让我们继续讨论间接镜面照明。臭名昭著：二子使用了230个静态反射探头， [下一页] 从记忆角度来说，这已经在推动它了。 [下一页] 我们最终在对马岛使用了235， [下一页] 但由于重新点亮需要额外的数据（是压缩点亮探针大小的 1.5 倍）， [下一页] 我们改用点播方式播放它们。 [下一页] 我们能够通过添加每个生物群落的默认探针来减少所需的探针数量， [下一页] 以及实例化许多内部探测器（例如，对于许多较小的房屋）。 [下一页] 我们还添加了对一级嵌套的支持（由于游戏中有许多内部结构）； [下一页] 我们总共可同时支持多达 128 个重新点燃探头。

---

## Slide 62

![Slide 62](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_062.png)

**📌 要点汇总**

- **数据捕获**：使用BC1压缩的反照率立方体贴图和BC6H压缩的法线+深度立方体贴图  
- **通道分配**：红色和绿色通道存储八面体法线，蓝色通道存储双曲深度  
- **统一规格**：所有立方体贴图尺寸均为256，

> 我们捕获以下数据以进行重新照明： [下一页] 压缩为 BC1 的反照率立方体贴图， [下一页] 以及用 BC6H 压缩的法线 + 深度立方体贴图。 [下一页] 我们使用红色和绿色通道来存储八面体法线， [下一页] 我们将双曲深度存储在蓝色通道中。 [下一页] 顺便说一下，我们所有的立方体贴图的大小都是 256。

---

## Slide 63

![Slide 63](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_063.png)

**📌 要点汇总**

- **异步更新探测器**：每帧选择探测器并异步计算更新，提升性能。  
- **阴影贴图优化**：使用远阴影贴图集（128x128/200m块）覆盖非级联区域。  
- **SH样本与亮度归一化**：单SH样本

> 为了重新启动我们的探测器，我们每帧选择一个探测器并在异步计算中更新它。 [下一页] 由于探针体积不一定被我们的级联阴影贴图覆盖，因此我们使用远阴影贴图集， [下一页] 每 200m 块有一个 128x128 阴影贴图。 [下一页] 为了提高性能，我们使用单个 SH 样本进行间接照明； [下一页] 我们还使用此示例（转换为亮度）进行反射探针亮度归一化。这确保了在其捕获位置使用的探针将 具有预期的亮度，并且避免将探头投射到 SH。 [下一页] 我们使用 GGX NDF 的过滤重要性采样来预过滤探针， [下一页] 并使用 Krzysztof Narkowicz 优秀的开源压缩器将它们压缩为 BC6H。 [下一页] 这对于减少内存占用非常有帮助，并防止在水等具有高光泽度和高度的表面上发生缓存抖动。 不同的法线贴图。

---

## Slide 64

![Slide 64](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_064.png)

> 我们遇到的一个问题是我们的内部探头没有正确遮挡， [下一页] 因为我们的远阴影贴图无法胜任这项任务，部分原因是它们的分辨率低，部分原因是许多建筑物在渲染到远距离时的 LODing 阴影贴图。 [下一页] 我们意识到我们的立方体贴图包含大量遮挡信息，因为它们存储深度，所以我们将其用于阴影。 [下一页] 重新点亮纹理像素时， [下一页] 我们追踪光线以找到与立方体贴图体积的交点， [下一页] 并在该交点处对立方体贴图的深度进行采样。 [下一页] 我们将任何足够小的值视为未被遮挡（我们使用 1-z 深度缓冲区）， [下一页] 为了帮助柔化阴影，我们在 4x4 封装中进行采样并应用 PCF 滤波。

---

## Slide 65

![Slide 65](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_065.png)

> 这种技术相当粗糙，我们可以通过沿光线采集多个深度样本来提高精度，但这个版本对于 我们的目的。让我们逐步浏览一些示例光线。 [下一页] 这是我们的第一束光线， [下一页] 它击中了某物， [下一页] 这样 texel 就被遮蔽了。 [下一页] 我们的下一条射线 [下一页] 没有击中任何东西，因此 texel 没有阴影。 [下一页] 通过这条光线，我们可以看到这种方法的一些问题，因为它显然应该被遮蔽， [下一页] 但根据其深度样本，事实并非如此。 [下一页] 最后，这条射线 [下一页] 认为它撞到了什么东西， [下一页] 所以它被遮蔽了，尽管如果我们继续超越本书的界限，我们可能会发现它没有被遮蔽。

---

## Slide 66

![Slide 66](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_066.png)

> 这是一个探测器没有使用立方体贴图阴影追踪的场景......

---

## Slide 67

![Slide 67](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_067.png)

**📌 要点汇总**

- **发光抑制**：新版本有效减少场景中“发光”现象，提升视觉清晰度  
- **场景优化**：改进地板与墙壁渲染，消除冗余细节  
- **倒影匹配**：倒影效果与场景元素高度贴合，增强真实感

> ...这是启用它的同一场景。正如您所看到的，它阻止了先前版本中可见的大部分“发光”，以及新版本中的地板和墙壁。 倒影与场景非常吻合。

---

## Slide 68

![Slide 68](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_068.png)

> 当用我们的反射探针照明时，我们的艺术家抱怨法线贴图凹凸的背面看起来太亮，因为反射光应该 被宏观几何形状部分遮挡。因此，我们开发了所谓的“水平线遮挡”术语来解释法线贴图的倾斜 法线 n_m 相对于顶点法线 n_v。 [下一页] 该问题的输入空间是四维的：一维表示表面粗糙度，一维表示法线贴图法线相对于法线的倾斜度。 顶点法线，两个用于视图向量方向。我们想要快速同时给出合理结果的东西，所以我们开发了这个 近似值。 [下一页] 首先，我们使用以下关系用圆锥体近似反射光线：对于 GGX 粗糙度 alpha，圆锥体半角 theta_c 包含 能量的分数 u_e 由该方程给出。我们对 u_e 使用 0.95 的值，并拟合一条曲线来降低计算锥角的成本。

---

## Slide 69

![Slide 69](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_069.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 简单来说就是问题...

---

## Slide 70

![Slide 70](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_070.png)

> ...我们首先将法线贴图法线 n_m 投影到由反射向量和顶点法线形成的平面中；我们将其称为投影法线 n_p。

---

## Slide 71

![Slide 71](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_071.png)

> 然后，我们让 theta_p 为投影法线与顶点法线之间的角度，theta_r 为反射矢量的倾斜度。

---

## Slide 72

![Slide 72](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_072.png)

> 我们将 theta_o 定义为圆锥体低于表面的角度...

---

## Slide 73

![Slide 73](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_073.png)

**📌 要点汇总**

- **BRDF遮挡处理**：theta_p为零时已考虑遮挡，限制其两倍以避免重复计算  
- **近似公式约束**：遮挡量计算不超出u_e（能量分数上限，如95%）  
- **角度变化关系**：theta_p每变化1度，theta_r变化2度，影响遮挡计算范围

> 我们计算如下。由于当 theta_p 为零时 BRDF 已经考虑了遮挡，并且由于 theta_p 的 1 度变化会导致 theta_r 发生两度变化，我们将其限制为 theta_p 的两倍，这样我们就只计算额外的遮挡。 [下一页] 然后，我们使用以下近似公式计算最终的遮挡量。请注意，我们永远不会超过 u_e，它是能量的分数 在圆锥体中（在我们的例子中为 95%）。

---

## Slide 74

![Slide 74](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_074.png)

> 这是使用视差遮挡贴图渲染但没有地平线遮挡的河床......

---

## Slide 75

![Slide 75](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_075.png)

> 这是启用了地平线遮挡的情况；请注意岩石的背面如何不再不切实际地“发光”。

---

## Slide 76

![Slide 76](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_076.png)

**📌 要点汇总**

- **视差校正**：通过边界框建模反射环境，计算反射向量与框的交集以确定立方

> 我们对反射探头应用视差校正；也就是说，我们使用编写的边界框对反射环境进行建模，并计算 反射向量与该框的交集，这为我们提供了立方体贴图样本位置。在右图中，立方体贴图是从红色摄像机的角度捕获的，而当前视图由蓝眼表示。 假设眼睛距样本位置 d_e 单位，而相机距样本位置 d_c 单位。我们可以重用之前看到的相关公式 对于给定的能量分数，锥角与粗糙度的正切值。将两个视图的表达式分开可以消除除粗糙度之外的所有内容 右边的项（即 alpha_e 优于 alpha_c）。然后我们观察到这大约等于距离之比， [下一页] 所以我们在对立方体贴图进行采样时通过这个因子来调整粗糙度。

---

## Slide 77

![Slide 77](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_077.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 这是没有视差补偿的场景......

---

## Slide 78

![Slide 78](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_078.png)

> 障子屏幕在略显粗糙的镀铬球体中的反射比应有的更加模糊。

---

## Slide 79

![Slide 79](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_079.png)

> 应用视差补偿可以解决这个问题。

---

## Slide 80

![Slide 80](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_080.png)

> 所有反射探针重新点亮步骤都是在异步计算中与我们的仅深度通道并行执行的。我们每帧重新点燃一个探针。

---

## Slide 81

![Slide 81](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_081.png)

**📌 要点汇总**

- **（无内容

> 现在我将讨论一些我们用来照亮天空、云、薄雾和雾的技术。

---

## Slide 82

![Slide 82](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_082.png)

> 正如当今很常见的那样，我们使用预先计算的 3D 查找表来照亮我们的天空。然而，我们也用它们来照亮其他大气 游戏中的现象——即云、体积雾和雾粒子。 [下一页] 用于天空存储的瑞利和米氏散射（按各自的相位函数划分）的 LUT，按高度、定向光极坐标索引 角度和视角极角。 [下一页] LUT 包括多次散射反射， [下一页] 基于 Bruneton、Elek 和 Yusov 的论文。 [下一页] 由于 3D LUT 不考虑方位角，因此我们在运行时应用了分析地球阴影项。 [下一页] 当我们尝试使用此 LUT 照亮云、薄雾和雾时，我们遇到了精度问题，尤其是在地平线处， [下一页] 因此我们添加了并行 LUT（以相同方式索引），用于存储每个点的散射瑞利光和米氏光。这些是*之前*的值 乘以局部密度，然后除以之前的相位函数。 [下一页] 它的单位是勒克斯，可以被认为是每个点的平均辐照度。

---

## Slide 83

![Slide 83](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_083.png)

**📌 要点汇总**

- **米氏/瑞利处理差异**：米氏散射应用阴影，瑞利散射应用AO，因前者前向性强，后者分布均匀  
- **体积雾度优化**：通过采样天空可见度计算AO，结合雨影贴图避免室内雾气过亮  
- **云渲染纹理结构**：抛物面Rgb11f纹理中，红/绿/蓝通道分别存储米氏散射、瑞利散射和透射率数据  
- **LUT应用方式**：米氏/瑞利辐照度分别与对应通道数据相乘，实现光照效果合成  
- **数据格式特性**

> 当使用这些辐照度 LUT 进行照明时，我们对米氏辐照度应用阴影，对瑞利辐照度应用 AO。 [下一页] 这是因为米氏散射是强烈的前向散射， [下一页] 而瑞利散射则更加均匀。 [下一页] 体积雾度从间接照明数据中采样平均天空可见度，并将其用于 AO， [下一页] 辅以雨影贴图，防止室内出现过亮的雾气。 [下一页] 云渲染为抛物面纹理， [下一页] Rgb11f 格式， [下一页] 其中红色通道存储米氏散射，然后将其乘以来自 LUT 的米氏辐照度； [下一页] 绿色通道存储瑞利散射，然后乘以来自 LUT 的瑞利辐照度； [下一页] 蓝色通道存储透射率。

---

## Slide 84

![Slide 84](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_084.png)

> 这是云图对应的场景， [下一页] 在这里，我放大了场景中心可见的云图部分。

---

## Slide 85

![Slide 85](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_085.png)

> 使用 LUT 进行照明的好处是，它允许我们在云、雾和雾照明中包含多重散射。这是一个没有多个的场景 散射...

---

## Slide 86

![Slide 86](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_086.png)

> 这是包含多次散射后的同一场景；正如你所看到的，它对场景的外观有很大的影响，尤其是在日出和日落时。

---

## Slide 87

![Slide 87](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_087.png)

**📌 要点汇总**

- **动态采样**：每帧根据太阳和月亮角度将3D LUT重新采样为2D，提升环境适应性。  
- **三次上采样**：采用三次插值方法，避免日出日落时的混叠伪影。  
- **性能优化**：2D化LUT降低查找计算量，提升实时渲染效率。

> 现在介绍一些实现细节：每一帧，我们使用当前的太阳和月亮角度将 3D LUT 重新采样为 2D。 [下一页] 我们使用三次上采样，这可以避免日出和日落时的混叠问题。 [下一页] 它还使 LUT 查找更便宜。

---

## Slide 88

![Slide 88](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_088.png)

**📌 要点汇总**

- **瑞利散射准确性**：大气散射主导照明，精确模拟瑞利散射对视觉效果至关重要。  
- **自定义色彩空间**：借鉴博客方法，采用光谱原色优化渲染，减少瑞利透射率误差。  
- **双步优化策略**：先通过点采样确定三波长（长/中/短），再固定原色调整瑞利系数以提升精度。

> 由于大气散射驱动着我们世界上的大部分照明，因此尝试使瑞利散射尽可能准确对我们来说非常重要。 [下一页] 我们发现 Christian Schüler 发表的一篇博客文章讨论了使用自定义色彩空间来近似光谱渲染，因此我们决定尝试一下。 [下一页] 正如在博客文章中一样，我们在色彩空间中使用了光谱原色。我们最大限度地减少了一系列太阳角度、加权的瑞利透射率误差 浅角度对应日出和日落较多。优化包括两个步骤： [下一页] 首先，我们使用点采样瑞利散射找到了光谱基色的三个波长（长、中和短），可以最大限度地减少此误差 这些波长处的系数。 [下一页] 然后，我们修复了原色并允许瑞利系数变化，从而改进了步骤 1 中发现的结果。

---

## Slide 89

![Slide 89](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_089.png)

> 这显示了光谱瑞利散射与在 Rec.709 RGB 空间中计算的散射以及 Bruneton 散射系数的比较。左边 一半显示透射率，右半部分显示出散射率。正如您所看到的，两者的绝对值存在明显差异 透射率以及色调。

---

## Slide 90

![Slide 90](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_090.png)

**📌 要点汇总**

- **LMS色彩空间与散射系数比较**：展示两种方法在色彩表现上的性能差异。  
- **结果接近光谱渲染**：

> 以下是使用我们的 LMS 色彩空间和散射系数的比较。结果与光谱渲染的结果非常接近。

---

## Slide 91

![Slide 91](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_091.png)

> 这是使用带有 Bruneton08 系数的 Rec.709 色彩空间的场景...

---

## Slide 92

![Slide 92](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_092.png)

**📌 要点汇总**

- **新LMS色彩空间**：结合散射系数优化场景渲染，提升色彩准确性  
- **日出日落差异显著**：新模型在昼夜过渡时段呈现更真实的光影变化  
- **减少绿色色调偏差**：有效抑制旧色彩空间中天空颜色的异常绿色表现

> ...这是使用新的 LMS 色彩空间和散射系数的同一场景。日出和日落时差异最为明显，并且 有助于减少我们有时在旧色彩空间中注意到的天空中的绿色色调。

---

## Slide 93

![Slide 93](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_093.png)

> 以下是新色彩空间的详细信息。请注意，我们使用与 Rec.709 相同的 D65 白点。

---

## Slide 94

![Slide 94](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_094.png)

**📌 要点汇总**

- **云渲染基础**：基于2015年Andrew Schneider及2016年Sebastien Hillaire的课程理念。  
- **低分辨率优化**：采用768x768抛物面图覆盖半球，

> 现在我将更多地讨论我们的云渲染。我们以 Andrew Schneider 在 2015 年本课程中提出的想法为基础，以及 Sebastien Hillaire 在 2016 年的基于物理的着色课程中。 [下一页] 正如我之前提到的，我们将云渲染为覆盖整个半球的抛物面图。出于性能原因，它必须相当低- 分辨率——只有 768x768。 [下一页] 我们使用了其中的三个纹理； [下一页] 我们将两个混合在一起，同时沿着运动方向滚动， [下一页] 一个更新超过 60 帧，以保持尽可能低的开销。 [下一页] 由于分辨率较低，我们需要降低紫外线空间中云位置快速变化的区域的云密度。 [下一页] 为此，我们计算了以下导数： [下一页] 相对于径向纹理坐标的径向云位置， [和] 以及相对于角度纹理坐标的角度云位置。在极坐标下工作使我们能够找到相对简单的解析 这些导数的表达式。 [下一页] 然后，当这些导数的最大值较高时，我们降低了云密度。

---

## Slide 95

![Slide 95](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_095.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 这是关闭密度抗锯齿的云......

---

## Slide 96

![Slide 96](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_096.png)

> ...这是启用密度抗锯齿后它们的样子。请注意，噪声采样伪影和像素化边缘全部消失。

---

## Slide 97

![Slide 97](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_097.png)

> 我们的相位函数的设计对于让云看起来正确非常重要。我们使用 Henyey-Greenstein 相位函数， [下一页] 其中不对称参数 g 的值取决于我们在云中的“深度”。这个想法是前向偏置的单散射占主导地位 在云的低密度、稀疏部分，而随着密度的增加以及沿方向的密度的增加，多重散射变得更加重要 光线增加。 [下一页] 所以，我们使用的产品 [下一页] 光的透过率 [下一页] 以及当前 raymarch 段到 lerp 之间的透射率 [下一页] 后向散射，当乘积为0时， [下一页] 和前向散射，当乘积为 1 时。 [下一页] 这自然会产生背光云上存在的“一线希望”，以及施奈德在演讲中描述的黑暗边缘，而无需使用他的 “糖粉”启发式。 [下一页] 由于反向散射是多重散射的结果，因此我们将反向散射相位函数的亮度缩放了 2.16。 [下一页] 该值是通过使用我们的大气多重散射模型模拟密集的米氏散射层得出的，反照率为 0.9。请注意，限制 在反照率为 1 的均匀散射层的情况下，该比例为 4，这给出了白色朗伯表面。

---

## Slide 98

![Slide 98](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_098.png)

> 这是仅使用前向散射的云......

---

## Slide 99

![Slide 99](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_099.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> ...这是仅使用反向散射时的样子。

---

## Slide 100

![Slide 100](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_100.png)

**📌 要点汇总**

- **前向和后向散射结合**：综合分析散射数据以得出研究结果。  
- **云的黑暗边缘**：通过观测清晰识别云层边缘的暗色特征。  
- **数据可视化效果**：图像展示增强了对云结构特征的理解。

> 结合前向和后向散射给出了这个结果 [下一页] 云的黑暗边缘在这里清晰可见。

---

## Slide 101

![Slide 101](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_101.png)

> 这是背光时云的样子；请注意云顶边缘的一线希望效果。

---

## Slide 102

![Slide 102](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_102.png)

**📌 要点汇总**

- **技术基础**：基于SIGGRAPH 2014和Digital Dragons 2017的体积雾霾渲染方法。  
- **froxel网格参数**：低分辨率128×64×6

> 好的，让我们继续进行体积雾霾照明和渲染。我们以 Bart Wronski 在 SIGGRAPH 2014 和 Michal 描述的技术为基础 2017 年 Digital Dragons 上的 Drobot。 [下一页] 我们使用低分辨率的 froxel 网格，宽度为 128，高度和深度为 64。 [下一页] 这覆盖了整个视锥体，从 10 厘米处的近平面到 100 公里处的远平面。 [下一页] 深度切片呈指数增长，每一个都比前一个厚 20%。 [下一页] 我们将自己限制为两个解析和可积密度函数的组合： [下一页] 第一个是指数高度下降， [下一页] 第二个是 S 形高度衰减，这里 d_1 几乎在所有情况下都为零。 [下一页] 为了添加其他维度的局部变化，我们使用了粒子，我将很快讨论。

---

## Slide 103

![Slide 103](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_103.png)

**📌 要点汇总**

- **froxel网格更新**：通过单计算调度实现高效更新，结合4x4x4线程组的分散与四重混合。  
- **时间过滤优化**：平滑阴影/环境光遮挡与局部光样本，采用差异化重投影策略避免条带伪影。  
- **纹理过滤性能**：双纹理全速率过滤性能等同于Rgba16f采样，异步计算实现0.5ms内复杂场景渲染。

> froxel 网格通过单个计算调度进行更新； [下一页] 它使用 4x4x4 线程组将从前到后的分散与四重混合集成在一起。 [下一页] 我们使用时间过滤来 [下一页] 平滑抖动的阴影和环境光遮挡样本， [下一页] 以及抖动的局部光样本。使用单个 Rgb11f 缓冲区来过滤最终的光值会导致令人反感的条带；这种安排让 对局部灯光使用不同的重投影策略， [下一页] 并且还让我们跳过被遮挡的冷冻素的照明。两种纹理均以全速率进行过滤，因此性能与对单个纹理进行采样大致相同 Rgba16f 纹理（添加早期输出之前）。 [下一页] 我们仍然更新被遮挡的冷冻像素的阴影和环境遮挡项，以减少遮挡伪影。 [下一页] 所有这些都是在基础 PS4 上、在具有大量本地灯光的繁重场景中通过异步计算在大约 0.5 毫秒内完成的。

---

## Slide 104

![Slide 104](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_104.png)

**📌 要点汇总**

- **平铺光剔除

> 我们的平铺光剔除计算着色器还输出一组每个平铺的灯光以供体积雾使用。 [下一页] 线程之间的灯光集的差异会对性能产生很大的影响， [下一页] 因此，我们采用了 Michal Drobot 在 2017 年本课程中描述的平面位阵列技术，这显着加快了着色器速度，在某些情况下 近2X。 [下一页] 有趣的是，对于我们的前向着色材质，我们发现使用排序的光索引列表而不是位数组要快一些，因为 遍历灯光列表的开销比遍历位数组的开销要低一些。

---

## Slide 105

![Slide 105](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_105.png)

**📌 要点汇总**

- **Froxel网格覆盖

> 我们的Froxel网格非常粗糙，但它覆盖了整个视锥体， [下一页] 使用传统方法会导致地平线处出现非常严重的锯齿，并且当使用薄雾层时，由于采样不足的密度变化，会导致非常严重的锯齿。 [下一页] 我们通过存储散射辐射率除以不透明度或一减去透射率来解决这个问题。 [下一页] 因为我们的密度函数是解析函数，所以我们可以重新计算每个像素的透射率，然后在合成到场景中时应用它。这也 意味着我们不必在任何地方存储不透明度，因此我们可以对卷使用 Rgb11f 格式。

---

## Slide 106

![Slide 106](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_106.png)

> 这是没有密度抗锯齿的场景；注意沿着水面平行于地平线的带子。

---

## Slide 107

![Slide 107](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_107.png)

> 应用密度抗锯齿可显着减少这些伪影。

---

## Slide 108

![Slide 108](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_108.png)

> 这是一个绝妙的技巧，但它为什么有效呢？ [下一页] 我们将从一个相当合理的假设开始，即散射 sigma_s 与消光 sigma_e 成正比，比率为反照率 c。 [下一页] 然后考虑距离 d 上的散射辐射率的渲染方程， [下一页] 其中 L_i 是传入辐射率乘以相位函数的球体积分。

---

## Slide 109

![Slide 109](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_109.png)

> [下一页] 然后我们替换 sigma_s，并将反照率 c 拉到积分前面。 [下一页] 现在，我们假设 L_i 相对恒定，在我们的例子中通常是这样，除了阴影之外。然后我们可以像这样分离积分，

---

## Slide 110

![Slide 110](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_110.png)

> [下一页] 并调用第一个积分 L_i 柱，因为它是区间内 L_i 的平均值。 [下一页] 剩余积分有简单的解析解，

---

## Slide 111

![Slide 111](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_111.png)

**📌 要点汇总**

- **alpha定义**：方括号内容为1减去透射率或不透明度alpha  
- **数学推导**：除以alpha后得到反照率乘以Li的平均值（假设d为常数）  
- **函数特性**：在假设成立时，L/alpha比L更平滑

> [下一页] 方括号中的项只是 1 减去透射率或不透明度 alpha [下一页] 因此，如果我们除以 alpha，我们就会得到反照率乘以 L_i 的平均值，作为 d 的函数，假设它是常数。 [下一页] 因此，在该假设成立的情况下，L/alpha 将是比 L 更平滑的函数。

---

## Slide 112

![Slide 112](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_112.png)

> 这样就解决了由于密度造成的锯齿问题，但我们还没有完成。为了减少所有三个维度的混叠，我们使用三次 B 样条对体积进行采样 滤波，需要 8 个三线性抽头。这是令人惊讶的便宜——它只比 PS4 Pro 在 3200x1800 分辨率下的三线性采样多花费 50 us 棋盘缓冲区。 [下一页] 为了帮助优化 ALU，我们使用了三次加权函数的近似值，这根本不影响视觉结果；详细信息在链接中 锁链图。

---

## Slide 113

![Slide 113](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_113.png)

> 这里我们使用三线性过滤， [下一页] 在这里，我增加了对比度，以便您可以更清楚地看到锯齿。

---

## Slide 114

![Slide 114](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_114.png)

**📌 要点汇总**

- **双三次过滤效果**：在x和y中应用双三次过滤可改善图像质量  
- **可见条带问题**：过滤后仍存在部分可见的条带状伪影  
- **优化需求**：需进一步调整参数或结合其他算法减少条带残留

> x 和 y 中的双三次过滤有帮助，但仍然有一些可见的条带。

---

## Slide 115

![Slide 115](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_115.png)

> 三三次过滤几乎完全消除了剩余的混叠。

---

## Slide 116

![Slide 116](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_116.png)

**📌 要点汇总**

- **三线性过滤**：示

> 这是另一个例子，首先使用三线性过滤，x 和 y 中的混叠非常明显。

---

## Slide 117

![Slide 117](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_117.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无

> 双三次过滤修复了...

---

## Slide 118

![Slide 118](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_118.png)

> 三立方滤光有助于将光轴连接到开口。

---

## Slide 119

![Slide 119](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_119.png)

> 请注意，1800cb 指的是 3200x1800 棋盘分辨率，其中每帧渲染 1600x1800 像素。

---

## Slide 120

![Slide 120](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_120.png)

**📌 要点汇总**

- **粒子与雾霾照明**：通过粒子系统及“雾霾照明”模式实现局部雾效果  
- **体积雾度计算**：L_i存储于平行光体积，结合LUT采样、相位函数及阴影/AO处理  
- **本地光融合**：本地光贡献通过froxel光体积采样与粒子不透明度计算实现  
- **过滤优化策略**：三线性过滤至不透明度阈值后切换双三次，省略Z轴

> 正如我之前提到的，我们使用粒子来添加局部雾。我们通过为粒子添加可选的“雾霾照明”模式来做到这一点。 [下一页] 在体积雾度着色器中，我们将 L_i（来自前面的方程）存储在平行光体积中； [下一页] 这是从 LUT 采样的光，乘以相位函数，并应用了阴影和 AO， [下一页] 加上本地光的贡献。 [下一页] 这是通过对 froxel 光体积进行采样并乘以粒子不透明度在粒子着色器中进行采样的。 [下一页] 作为优化，我们使用三线性过滤，直到不透明度超过阈值，此时我们切换到双三次过滤。 （这些颗粒大部分是 面向相机，因此无需在 Z 轴上进行额外的过滤。）

---

## Slide 121

![Slide 121](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_121.png)

> 这是使用我们的标准粒子照明模型照亮粒子的场景......

---

## Slide 122

![Slide 122](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_122.png)

> 在这里，我们已经切换到雾状粒子的雾霾照明模型。这有助于他们更好地融入场景。

---

## Slide 123

![Slide 123](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_123.png)

> 添加粒子雾霾照明后，我们的 FX 艺术家抱怨说，从正面照明时，粒子太难看到。 [下一页] 这是因为雾假设雾层的单次散射，并且主要使用前向散射。 [下一页] 为了解决这个问题，我们添加了一个廉价的多重散射近似项，其工作原理如下： [下一页] 在CPU上，我们计算前向和后向背向散射相位函数与雾度Mie相位函数的比率。我们使用了 使用相同的 Henyey-Greenstein 相函数和 -0.15 的不对称参数来模拟多重散射，就像我们对云所做的那样。 [下一页] 在着色器中，我们根据视图向量和光向量之间的点积在这两个值之间进行调整；这给了我们一个多散射比例因子 r_MS。 [下一页] 我们根据粒子的不透明度从 1 到 r_MS，并使用结果值来缩放粒子亮度。 [下一页] 在实践中，我们特别降低了反向散射效应的强度， [下一页] 因为当缺乏完整的米氏颜色贡献时，粒子显得不自然。

---

## Slide 124

![Slide 124](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_124.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 这是在没有多重散射近似的情况下照亮的粒子......

---

## Slide 125

![Slide 125](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_125.png)

> 这里启用多重散射近似。正如您所看到的，粒子获得了更多的形状和清晰度。

---

## Slide 126

![Slide 126](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_126.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 在本次演讲的最后一部分，我将讨论我们使用的一些色调映射技术。

---

## Slide 127

![Slide 127](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_127.png)

> 首先，关于曝光的一些话。在《臭名昭著：次子》和《第一道曙光》中，我们努力维持物理上合理的漫反射反照率值 资产。 [下一页] 我们的假设是基于亮度的曝光和反照率之间的反馈循环是造成这种情况的主要原因， [下一页] 并导致漫反射反照率值太暗（因此镜面反射分量相对太亮）。 [下一页] 为了帮助艺术家选择更符合物理合理的反照率值，我们创建了一个漫反射颜色参考图表......

---

## Slide 128

![Slide 128](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_128.png)

> 你可以在这里看到。它基于各种物体的反射光谱，转换为 sRGB 颜色。

---

## Slide 129

![Slide 129](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_129.png)

**📌 要点汇总**

- **基于照度的曝光系统**：改用以照度为核心参数的系统，不再依赖反照率计算。  
- **亮度使用条件**：仅当高光亮度超过设定阈值时，才引入

> 我们还改用了主要基于照度的曝光系统，将反照率完全排除在外。 [下一页] 仅当高光亮度超过阈值时，我们才使用亮度； [下一页] 例如，由于火粒子或明亮的镜面高光。

---

## Slide 130

![Slide 130](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_130.png)

**📌 要点汇总**

- **光照差异**：游戏历史导致室内外亮度差异达10 EV，需平衡可见性与避免过亮区域。  
- **间接照明控制**：天空驱动的间接照明需避免因色调映射导致过度饱和，保持艺术效果。  
- **参考方案**：Bart Wronski的博客提供了类似问题的解决方案，可作为深入讨论的补充。

> 由于游戏的历史背景，室内灯光一般都非常昏暗， [下一页] 这导致内部和外部之间的差异高达 10 EV。 [下一页] 我们希望尽可能保持可见性，这意味着使场景中太暗的部分变亮，同时避免场景中的灯光过亮 明亮的区域。 [下一页] 由于我们的天空驱动我们的间接照明，它通常比环境更亮， [下一页] 但从艺术角度来说，防止它因色调映射而变得过于饱和对我们来说很重要。 [下一页] 在我们完成这项工作几个月后，Bart Wronski 写了一篇博客文章，解决了许多相同的问题并提出了类似的解决方案，所以我将参考 您可以进行更完整的讨论。

---

## Slide 131

![Slide 131](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_131.png)

**📌 要点汇总**

- **传统摄影技术**：分级过滤器、特殊照明装置与弹跳卡用于优化光影与对比度  
- **胶片与数字处理**：闪避/加深技术及阴影高光调整实现细节增强与动态范围控制  
- **HDR摄影方法**：多重曝光技术模拟人眼高动态范围感知能力  
- **双边滤镜应用**

> 但是，我将简要回顾一下摄影和电影摄影中用于处理这些问题的一些技术；它们包括使用 [下一页] 分级过滤器， [下一页] 特殊的照明装置和弹跳卡， [下一页] 胶片冲洗过程中的闪避和加深， [下一页] 或者现在，阴影和高光调整， [下一页] 以及在所谓的 HDR 摄影中使用多重曝光。 [下一页] 我们还想模拟人眼的动态范围，它能够感知比相机高得多的动态范围。 [下一页] 我们知道双边滤镜可用于保持图像细节，同时降低整体对比度，因此我们决定对此进行实验，看看是否可以 可以使其表现出色。

---

## Slide 132

![Slide 132](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_132.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 考虑这个场景没有应用任何调整......

---

## Slide 133

![Slide 133](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_133.png)

**📌 要点汇总**

- **对比度降低影响**：降低对比度50%会恢复更多颜色，但显著削弱细节层次  
- **极端调整警示**：此调整为极端示例，仅用于说明对比度

> 如果我们将对比度降低 50%，就会得到这样的结果，它会恢复很多颜色，但会显着使细节变得平坦。请注意，这是一个极端的调整 仅供说明之用

---

## Slide 134

![Slide 134](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_134.png)

> 使用双边滤波器我们得到了这个，这有助于保留大量的局部对比度。

---

## Slide 135

![Slide 135](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_135.png)

> 双边滤波器的简单实现是昂贵的， [下一页] 但双边网格算法允许以较低的内存占用量高效地计算它们。 [下一页] 该算法允许对图像数据进行积极的下采样 [下一页] （我们使用宽度为 64、高度为 32、深度为 64 的体积） [下一页] 并且自然适合与亮度直方图生成一起使用，用于动态曝光。 [下一页] 在 1080p 的 PS4 上，该算法的开销约为 250 us，所以还算不错。

---

## Slide 136

![Slide 136](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_136.png)

**📌 要点汇总**

- **网格填充**：使用同质对数亮度值和权重填充三维网格。  
- **权重选择**：初始权重基于线性Z轴权重，由两个最近Z切片贡献。  
- **模糊策略**：X/Y轴应用宽模糊，Z轴使用窄模糊或省略。  
- **采样归

> 以下是其工作原理的概述： [下一页] 首先，我们用同质对数亮度值 w_i V_i 和 w_i 填充体积（“网格”），其中 w_i 是权重，V_i 是对数亮度。 [下一页] 每个样本的初始权重是根据线性Z轴权重选择的； [下一页] 也就是说，每个样本都会对两个最近的 Z 切片做出贡献。 [下一页] 我们可以跳过 X 和 Y 中的权重，因为我们将在这些轴上应用广泛的模糊。 [下一页] 接下来，我们对网格应用高斯模糊， [下一页] 在 X 和 Y 中使用较宽的模糊，在 Z 中使用较小的模糊。（有时 Z 模糊会被完全省略。） [下一页] 最后，通过对网格进行三线性采样并对结果进行归一化，获得像素的双边滤波值。

---

## Slide 137

![Slide 137](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_137.png)

**📌 要点汇总**

- **输入输出亮度**：I_i为输入图像对数亮度，I_o为输出对数亮度  
- **双边滤波作用**：B表示双边滤波处理后的对数亮度值  
- **中点亮度定义**：M为中点对数亮度，决定对比度调整方向  
- **对比度等级**：c控制对比度增强或减弱的程度  
- **细节强度参数**：d量化图像细节保留的强度水平

> 这是保留细节的对比度调整的基本公式。 [下一页] I_i是输入图像的亮度对数； [下一页] I_o 是输出对数亮度； [下一页] B是双边滤波对数亮度； [下一页] M 是中点对数亮度（也就是说，当我们降低对比度时，亮度值将朝向该点绘制）； [下一页] c是对比度等级； [下一页] d 是细节强度。

---

## Slide 138

![Slide 138](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_138.png)

**📌 要点汇总**

- **振铃伪像**：平滑渐变场景中出现

> 尽管我们在应用于具有平滑渐变的场景时确实遇到了振铃伪像，但效果相当好。 [下一页] 正如您所看到的，这种情况最常发生在云、柔和阴影和镜面高光上 [下一页] 在这里。 [下一页] 这些伪影可以通过使用更大的亮度桶（或更宽的 Z 模糊）来减少，但代价是增加光晕。

---

## Slide 139

![Slide 139](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_139.png)

> 该动画演示了振铃是如何发生的。我们从绿色输入信号开始，对其进行双边模糊以获得紫色曲线。然后我们生产 蓝色输出信号 [下一页] 通过降低模糊曲线的对比度， [下一页] 并添加回细节，即输入信号和模糊信号之间的差异。 （图表链接：https://www.desmos.com/calculator/tieypyafi）

---

## Slide 140

![Slide 140](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_140.png)

> 为了消除这些伪影，我们采用了一种混合方法，将双边滤波器的输出与非常宽的 2D 高斯模糊进行混合。 [下一页] 最后，我们对双边模糊使用了 40% 的权重，对高斯模糊使用了 60% 的权重。 [下一页] 重要的是二维高斯足够宽以避免明显的光晕； [下一页] 我们使用半径为 13 个抽头的滤波器，该滤波器用于 64x32 图像。 [下一页] 然后我们使用双三次 B 样条过滤将其上采样到 256x128， [下一页] 避免了双线性过滤伪影， [下一页] 并添加了更多的模糊。

---

## Slide 141

![Slide 141](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_141.png)

> 该动画显示了双边滤波器和宽高斯滤波器之间的 lerp；请注意如何通过混合更多的振铃伪影来减少振铃伪影 高斯模糊。 （图表链接：https://www.desmos.com/calculator/4afvbmckcv）

---

## Slide 142

![Slide 142](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_142.png)

**📌 要点汇总**

- **双边滤镜效果**：使用双边滤镜处理后图像保持原有结构但对比度降低50%  
- **图像一致性**：处理前后图像内容相同，仅对比度参数发生改变  
- **对比度优化**：通过双边滤镜实现非结构化对比度调整（降低50%）  
- **视觉效果验证**：相同图像对比实验验证滤镜对对比度的独立调节能力  
- **参数影响分析**：对比度降低幅度与双边滤镜参数存在直接关联性

> 这与我们之前看到的图像相同，仅使用双边滤镜对比度降低了 50%。

---

## Slide 143

![Slide 143](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_143.png)

> 这是混合高斯模糊后的同一张图像。整体外观更加自然，同时仍然保留天空的颜色。

---

## Slide 144

![Slide 144](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_144.png)

> 为了进行比较，这里再次是原始图像。

---

## Slide 145

![Slide 145](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_145.png)

> 这是使用一天中这个时间和天气状态的典型游戏内设置的场景。

---

## Slide 146

![Slide 146](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_146.png)

**📌 要点汇总**

- **d参数调整**：通过修改“d”参数可调节局部对比度，增强视觉效果。  
- **参数设置示例**：将“d”设为1.5可提升场景冲击力，属于常用保守实践。  
- **工具价值**：该方法虽保守，但为优化视觉表现提供了实用调整工具。

> 我还没有谈论太多 [下一页] 该方程中的“d”参数，但可以通过改变它来调整局部对比度。这里我将其设置为 1.5，这使得场景更有冲击力。我们用过 这是一个保守的做法，但它可能是一个有用的工具。

---

## Slide 147

![Slide 147](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_147.png)

**📌 要点汇总**

- **每通道色调映射**：将饱和非原色剪辑为青、品红、黄色  
- **Reinhard 运算符**：简化每通道色调映射的实现方式  
- **输入颜色缩放**：确保各通道值不超过 1 以避免溢出

> 众所周知，渲染色彩空间中的每通道色调映射会将饱和的非原色剪辑为青色、品红色和黄色。 [下一页] 在这里，为了简单起见，我们只是对每个通道应用 Reinhard 运算符。 [下一页] 请注意，我们还缩放了输入颜色，以便没有组件超过 1。

---

## Slide 148

![Slide 148](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_148.png)

**📌 要点汇总**

- **色调映射缺陷**：当前方法导致日落场景中饱和黄色与镜面高光的视觉失真  
- **色彩过度饱和**：日落时黄色区域因映射算法出现不自然的高饱和度表现  
- **高光处理问题**：镜面反射区域因色调映射

> 实际上，这种方式的色调映射会产生相当难看的结果 - 请注意日落时的饱和黄色和镜面高光。

---

## Slide 149

![Slide 149](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_149.png)

> 在 2017 年的一次谈话中，Brian Karis 提到他喜欢 ACEScg 作为色调映射空间的滚降到白色行为。 [下一页] 所以我们决定这样做，以及其他几个色彩空间，包括 [下一页] ACES AP0， [下一页] ACEScg（或 AP1）， [下一页] 2020 年建议， [下一页] 和 DCI-P3。

---

## Slide 150

![Slide 150](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_150.png)

**📌 要点汇总**

- **ACEScg色调映射问题**：尽管被公认为最佳，但存在红色过度偏向黄色的缺陷  
- **红色原色x坐标调整**：将0.713修正为0.75后达成视觉效果共识  
- **参数优化验证**：通过坐标调整验证了色彩科学理论与实践的匹配性

> ACEScg 被认为是所有这些中最好的，但我们仍然认为它在色调映射过程中将红色过度偏向黄色。 [下一页] 因此，我们将红色原色的 x 坐标从 0.713 调整为 0.75，这给出了我们都满意的结果。

---

## Slide 151

![Slide 151](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_151.png)

**📌 要点汇总**

- **ACEScg色调线转换**：ACEScg将输入空间的红色和橙色色调线映射为黄色，改变色彩分布特性  
- **红色原色调整**：通过优化红色原色参数可有效减少色调转换过程中的色彩偏移现象  
- **色彩校正技术**：演示了基于色彩空间映射的校正方法对色调准确性的关键影响

> 这里 [下一页] 您可以看到 ACEScg 如何将输入空间中的红色和橙色色调线弯曲为黄色。 [下一页] 通过调整红色原色，可以减少这种偏移。

---

## Slide 152

![Slide 152](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_152.png)

> 该动画展示了如何通过自定义颜色空间中的色调映射来转换颜色空间。请注意，可能仍有改进的空间； 请注意蓝色原色附近的颜色如何相当强烈地转向洋红色。

---

## Slide 153

![Slide 153](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_153.png)

**📌 要点汇总**

- **ACEScg色调映射**：场景采用ACEScg色彩空间进行色调映射处理  
- **镜面高光问题**：需特别关注镜面高光表现，避免颜色偏差  
- **艺术总监反馈**：日落场景中ACEScg颜色倾向不符合艺术总监预期

> 该场景使用 ACEScg 进行色调映射。 [下一页] 特别注意镜面高光；我们的艺术总监非常不喜欢使用 ACEScg 时日落倾向于这种颜色。

---

## Slide 154

![Slide 154](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_154.png)

> 使用自定义色彩空间可以充分减少色彩偏移和饱和度，不会对黄色的色调映射产生不利影响，就像在 金色森林。

---

## Slide 155

![Slide 155](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_155.png)

> 在 Ghost 上我们仍然使用相当老式的颜色分级工具， [下一页] 包括在 Photoshop 中使用嵌入的 32x32x32 sRGB 颜色 LUT 操作屏幕截图。 [下一页] 我们的艺术总监喜欢这个工作流程，所以我们并不急于改变。 [下一页] 然而，由于分辨率有限，我们不得不保守地使用它以避免引入条带伪影， [下一页] 这在很多情况下都过于受限。 [下一页] 我读过 Bart Wronski 的一篇博客文章，讨论了有关白平衡和游戏的一些想法，以及将白平衡控制引入到我们的游戏中的想法。 分级管道很有意义，所以我们尝试了一下。 [下一页] 它在 GPU 性能方面是免费的，因为我们可以将其滚动到 Rec.709 中以进行色调映射颜色空间转换矩阵。 [下一页] 幸运的是，它运行得非常好，以至于我们最终不需要更改我们的评分工具集。

---

## Slide 156

![Slide 156](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_156.png)

**📌 要点汇总**

- **界面设计**：无传统色温/色调滑块，艺术家直接选择目标颜色调整白平衡。  
- **与Lightroom对比**：选择颜色而非中性像素，直观调整场景色调（如选蓝使画面更蓝）。  
- **色彩适应矩阵**：采用Von Kries变换模拟人眼在Bradford

> 我们提供的界面与传统的白平衡工具略有不同。我们没有提供色温和色调滑块，而是让艺术家 选择他们想要将白色更改为*的颜色。 [下一页] 这与 Lightroom 等工具相反，Lightroom 允许您单击应该是中性的像素（如灰卡）。所以在 Lightroom 中你选择的颜色 应更改*为白色*。但我们的做法是，如果你想让场景更蓝，你就选择蓝色，艺术家发现这更直观。 [下一页] 我们使用的变换称为色彩适应矩阵，它模拟人类视觉系统如何适应不同的照明环境。 [下一页] 具体来说，我们在 Bradford LMS 色彩空间中使用了 Von Kries 变换。这会将颜色转换为近似响应的颜色空间 视网膜中的长、中、短锥体，按照该空间中白点的比例缩放它们，然后将它们转换回来。 [下一页] 这对色彩空间做了有趣的事情...... [下一页]

---

## Slide 157

![Slide 157](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_157.png)

**📌 要点汇总**

- **颜色空间转换**：动画展示颜色空间转换为浅蓝色白点，体现映射过程  
- **Rec.709色彩空间限制**：色调映射后仍受限于Rec.709，高亮度需压缩显示为白色  
- **颜色剥离

> 该动画显示颜色空间转换为浅蓝色白点。因为色调映射后我们最终的色彩空间仍然是Rec.709，明亮 颜色仍然会滚落以显示白色，正如您在颜色空间的外层被“剥离”以仅显示低饱和度颜色时所看到的那样。

---

## Slide 158

![Slide 158](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_158.png)

> 这是没有白平衡调整的场景......

---

## Slide 159

![Slide 159](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_159.png)

> ...这是应用艺术白平衡调整后的场景，其中左上角的正方形中的白色变为蓝色。

---

## Slide 160

![Slide 160](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_160.png)

**📌 要点汇总**

- **夜间视觉区分**：需通过光照与色彩调整，使夜晚场景呈现独特氛围而非简单暗化白天。  
- **可见性保障**：优化渲染技术以提升夜间场景对比度与细节清晰度，确保玩家操作体验。  
- **曹论文方法**：采用曹等人的方程与常数参数，经验证可获得更优夜间渲染效果。  
- **视觉模型基础**：研究基于人类视觉系统特性，如亮度适应与色彩感知机制，指导技术实现。

> 我现在将讨论我们用来克服在尝试渲染夜间场景时所面临的挑战的技术之一。 [下一页] 第一个挑战是让夜晚“感觉”像夜晚，而不仅仅是白天的黑暗版本。 [下一页] 第二个挑战是确保玩家在晚上能够看得足够清楚，以便他们能够玩游戏。 [下一页] 我们发现了这个领域的一些研究， [下一页] 这两篇论文中都有描述。柯克论文基于曹等人的论文。论文，但我们发现遵循曹论文中的方程和常数 给出了更好的结果，我在这里主要使用它们的符号。 [下一页] 这项研究基于人类视觉系统的模型和测量，因此我将简要介绍一些背景知识。

---

## Slide 161

![Slide 161](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_161.png)

> 我们的视网膜有四种类型的受体： [下一页] 三种类型的视锥细胞（长、中、短），负责正常的色觉， [下一页] 和杆状细胞，对弱光更敏感，并且是单色的。 [下一页] 然而，人类视觉是 3D，而不是 4D（至少对大多数人来说）， [下一页] 这是因为视杆细胞使用与视锥细胞相同的神经通路。 [下一页] 结果是弱光视觉不是“黑白”， [下一页] 但是当视杆细胞取代视锥细胞时，会产生颜色变化，有时称为浦肯野色变。

---

## Slide 162

![Slide 162](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_162.png)

**📌 要点汇总**

- **对手颜色空间建模**：颜色变化可建模为对手颜色空间中的增量，反映视觉系统特性。  
- **HDR到视锥/视杆转换**：需开发HDR场景颜色与视锥/视杆激励间的转换方法，涉及LMS变换与杆值计算。  
- **LMS变换与Brad

> 这种颜色变化可以建模为对手颜色空间中的增量， [下一页] 这是被认为在视觉系统中使用的色彩空间。 [下一页] 为了使用这种技术，我们需要一种在 HDR 场景颜色和视锥/视杆激励之间进行转换的方法， [下一页] 虽然我们可以尝试使用现有的 LMS 变换（例如前面提到的 Bradford 空间），但我们仍然需要一种计算杆值的方法。 锥体和杆体波长响应曲线可从 Kirk 等处获得， [下一页] 所以我们需要一种方法将场景 RGB 颜色转换为频谱。 [下一页] 这是一个未明确说明的问题；我们使用了 Smits 在本文中描述的方法，该方法找到了一组最大化 RGB 基础光谱 平滑度。

---

## Slide 163

![Slide 163](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_163.png)

> 以下是我们使用 Smit 方法找到的反射光谱；我们限制 RGB 曲线，使它们介于 0 和 1 之间，并且总和为 1。

---

## Slide 164

![Slide 164](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_164.png)

> 首先，我们需要使用 Rec.709 D65 光源计算一个矩阵，以从 Rec.709 RGB 转换到 LMSR 空间。 [下一页] M为转换矩阵； [下一页] i 是 LMSR 响应对应的行索引； [下一页] j是红、绿、蓝原色对应的列索引； [下一页] lambda 是波长，大写 lambda 是我们积分的可见光波长范围； [下一页] E_i是受体i的响应曲线； [下一页] I为D65光源光谱； [下一页] R_j 是使用 Smit 方法找到的红色、绿色或蓝色的反射光谱。

---

## Slide 165

![Slide 165](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_165.png)

**📌 要点汇总**

- **颜色转换

> 然后我们使用这个矩阵将场景颜色 c 转换为 LMSR 响应 q， [下一页] 然后计算乘法增益控制向量 g： [下一页] 仅针对锥体定义， [下一页] 其中 m 是描述视锥细胞灵敏度的常数向量，由该值给出， [下一页] k 是描述 LMS 路径的杆输入强度的向量，其中 k_L 和 k_M 限制为相等。 [下一页] 根据 Cao 的说法，k 随着照度水平的增加而减小，但我们选择遵循 Kirk 并使用此处给出的常数值。请注意，有一些 可以自由选择这些值，并且尝试不同的值会产生不同的结果，因此如果您要实现此值，您可能需要尝试不同的方法 值在这里。

---

## Slide 166

![Slide 166](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_166.png)

> 如果我们让 q-hat 为 LMS 空间中的颜色（去掉 R 分量），则对手空间颜色由以下方程给出： [下一页] 与这里给出的矩阵A。

---

## Slide 167

![Slide 167](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_167.png)

> 我们快完成了；我们现在可以计算棒在对手色彩空间中的增量效应 delta-o， [下一页] 由这个方程给出， [下一页] 其中新项都是常数，此处给出。

---

## Slide 168

![Slide 168](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_168.png)

> 最后，我们可以使用以下公式计算 RGB 颜色变化： [下一页] 其中 M-hat 是 M 的左上角 3x3 子矩阵。 [下一页] 在 GPU 上实现这一点的着色器代码很简单——只有三行代码。

---

## Slide 169

![Slide 169](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_169.png)

**📌 要点汇总**

- **亮度变化**：光亮度从明亮降至约0.05勒克斯，显著影响环境照度。  
- **颜色响应**：较暗颜色在低照度下发生亮度提升与蓝移现象。  
- **视觉效应**：低照度条件下颜色感知变化可能影响视觉表现与应用设计。

> 该动画展示了将光的亮度从明亮的光降低到平均约 0.05 勒克斯的照度的效果。如您所见， 较暗的颜色尤其会变亮并发生蓝移。

---

## Slide 170

![Slide 170](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_170.png)

> 为了再次显示差异，这里是没有任何颜色偏移的输出，

---

## Slide 171

![Slide 171](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_171.png)

> 这是大约 0.05 勒克斯时的色移。

---

## Slide 172

![Slide 172](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_172.png)

> 最后，这是一个没有应用浦肯野位移的游戏示例......

---

## Slide 173

![Slide 173](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_173.png)

**📌 要点汇总**

- **浦肯野

> 这是启用浦肯野位移的同一场景；该场景的平均照度约为 0.05 勒克斯。注意黑暗区域在之后如何变得更亮 应用浦肯野效应，尤其是深蓝色的水和天空。

---

## Slide 174

![Slide 174](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_174.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 在结束之前，我想感谢以下所有人的帮助和支持......

---

## Slide 175

![Slide 175](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_175.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

---

## Slide 176

![Slide 176](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_176.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 以下是本次演讲的参考资料...

---

## Slide 177

![Slide 177](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_177.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

---

## Slide 178

![Slide 178](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_178.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

---

## Slide 179

![Slide 179](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Real-time-samuraicinema-lighting-atmosphere-and-tonemapping/slide_179.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> ..最后，我要非常感谢*您*的关注；如果您有任何疑问，我的 Twitter 账号是@jasminpatry。再次感谢！

---
