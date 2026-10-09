---
layout: post
title: "Making Waves in Ocean Surface Rendering using Tiling and Blending"
date: 2026-08-21
img: 渲染技巧/Making-Waves-in-Ocean-Surface-Rendering-using-Tiling-and-Blending/img_001.jpg # Add image post (optional)
fig-caption: # Add figcaption (optional)
tags: [Rendering, Pipeline]
description: 基于六边形 Tiling and Blending 纹理合成方法实现非周期性海洋表面实时渲染，解决传统 Tessendorf 模型的重复纹理问题
---

> 来源：https://www.ubisoft.com/en-us/studio/laforge/news/5WHMK3tLGMGsqhxmWls1Jw/making-waves-in-ocean-surface-rendering-using-tiling-and-blending
> 摘录时间：2026-08-21 14:30

---

## 摘要（Key Takeaways）

- **主题**：基于六边形 Tiling and Blending 纹理合成方法实现非周期性海洋表面实时渲染，解决传统 Tessendorf 模型的重复纹理问题
- **核心结论 / 关键要点**：
  - 传统 Tessendorf 模型通过 IFFT 生成周期性位移/法线贴图，在大范围海洋中会产生可见的重复图案（tiling artifacts）
  - 本方法使用六边形网格将 Tessendorf 贴图进行随机采样与协方差保持混合（covariance-preserving blending），生成完全非周期性的海洋表面
  - 每个 texel 由三个六边形贡献混合，权重从中心到边缘平滑衰减
  - Flow Map 允许实时控制波浪方向——在六边形中心采样方向向量转为旋转角度，无需预计算
  - LEAN Mapping 通过预计算法线的均值和协方差函数确保远处高光正确
  - 性能优于多子频谱方案（多次 IFFT），内存占用更少，与 Perlin 噪声方案资源消耗相当但效果更真实
- **适用场景 / 为什么重要**：适用于需要大范围开阔海域的游戏/模拟项目，可直接增强现有 Tessendorf 实现而无需改动生成算法
- **原文信息**：Ubisoft La Forge / 2024-07-25 / 发表于 HPG 2024（High Performance Graphics）

---

![](https://gerigory.github.io/assets/img/渲染技巧/Making-Waves-in-Ocean-Surface-Rendering-using-Tiling-and-Blending/img_001.jpg)

*Figure 1: Traditional methods fall short in avoiding repetitive patterns. In comparison, our method efficiently produces aperiodic oceans.*

*图1：传统方法无法避免重复图案。相比之下，我们的方法能高效生成非周期性海洋。*

## Introduction（引言）

Ocean rendering is a challenging yet essential task for creating immersive virtual environments. Traditional methods often fall short in avoiding repetitive patterns, known as tiling artifacts, especially when dealing with large ocean surfaces. These repetitive patterns break immersion and limit visual realism in games and simulations.

海洋渲染是创建沉浸式虚拟环境中一项极具挑战性但不可或缺的任务。传统方法常常无法避免重复图案（即 tiling artifacts），尤其在处理大范围海洋表面时。这些重复图案会打破沉浸感，并限制游戏和模拟中的视觉真实度。

This article presents a novel approach using texture synthesis to generate an aperiodic, realistic ocean surface efficiently. The method was presented at HPG 2024 (High Performance Graphics).

本文提出了一种使用纹理合成的新方法，能够高效地生成非周期性的真实海洋表面。该方法发表于 HPG 2024（高性能图形学会议）。

## Traditional Ocean Simulation（传统海洋模拟）

![](https://gerigory.github.io/assets/img/渲染技巧/Making-Waves-in-Ocean-Surface-Rendering-using-Tiling-and-Blending/img_002.jpg)

*Figure 2: Conventional approach for simulating ocean surfaces based on the Tessendorf model*

*图2：基于 Tessendorf 模型的传统海洋表面模拟方法*

The conventional approach for simulating ocean surfaces relies on the Tessendorf model, which uses an Inverse Fast Fourier Transform (IFFT) to compute realistic wave displacements as a seamless texture each frame. This process generates periodic displacement maps and normal maps through IFFT computations, enabling tiling of generated patches across the entire ocean surface.

传统的海洋表面模拟方法依赖于 Tessendorf 模型，该模型使用逆快速傅里叶变换（IFFT）在每帧计算真实的波浪位移，生成无缝纹理。此过程通过 IFFT 计算生成周期性的位移贴图和法线贴图，使生成的 patch 可以在整个海洋表面上进行 tiling。

However, when viewed from a distance, the tiling becomes visually apparent, compromising realism. The method produces coherent wave behavior but inherently creates periodicity that becomes noticeable at scale, limiting visual plausibility for large open water environments.

然而，从远处观察时，tiling 会变得明显可见，破坏真实感。该方法虽能产生连贯的波浪行为，但本质上产生的周期性在大尺度下会变得明显，限制了大面积开阔水域环境的视觉可信度。

## Previous Approaches（先前方法）

![](https://gerigory.github.io/assets/img/渲染技巧/Making-Waves-in-Ocean-Surface-Rendering-using-Tiling-and-Blending/img_003.jpg)

*Figure 4: Tessendorf model used with 3 sub-displacement maps*

*图4：使用 3 个子位移贴图的 Tessendorf 模型*

Two established methods have been used to address tiling artifacts:

已有两种公认的方法用于解决 tiling artifacts：

**Noise Blending（噪声混合）**: Combining periodic displacement maps with aperiodic noise like Perlin noise. However, there is a critical trade-off: adding too little noise fails to hide the periodicity, while adding too much noise can distort the appearance. Finding the right balance is difficult and scene-dependent.

**噪声混合**：将周期性位移贴图与 Perlin 噪声等非周期性噪声相结合。然而，存在一个关键权衡：噪声添加太少无法隐藏周期性，添加太多又会扭曲外观。找到正确的平衡点很困难，且依赖于具体场景。

**Sub-spectra Decomposition（子频谱分解）**: The ocean spectrum is divided into multiple frequency ranges, each computed via separate Inverse Fast Fourier Transforms (IFFTs) and combined. While this increases the period length, repetitions are still very visible for low frequency waves, and it requires multiple computationally expensive IFFT operations.

**子频谱分解**：将海洋频谱划分为多个频率范围，每个范围通过单独的 IFFT 计算后合并。虽然这增加了周期长度，但对于低频波浪重复仍然非常明显，而且需要多次计算开销高昂的 IFFT 运算。

## Tiling and Blending（Tiling 与混合）

![](https://gerigory.github.io/assets/img/渲染技巧/Making-Waves-in-Ocean-Surface-Rendering-using-Tiling-and-Blending/img_004.jpg)

*Figure 5: Tiling and Blending*

*图5：Tiling and Blending 方法示意*

The proposed method adapts a real-time texture synthesis algorithm using hexagonal tiling. The algorithm blends the content of multiple hexagonal tilings on a regular grid while preserving statistical properties. Three hexagonal tiles blend per texel using covariance-preserving blending.

所提出的方法改编了一种使用六边形 tiling 的实时纹理合成算法。该算法在规则网格上混合多个六边形 tiling 的内容，同时保持统计特性。每个 texel 由三个六边形 tile 通过协方差保持混合进行融合。

The blending weights follow a pattern where they equal 1 at the hexagon center and decrease to 0 at edges, enabling smooth transitions between hexagonal regions. The blending is covariance-preserving rather than linear, meaning that synthesized vectors remain coherent with the exemplar. This mathematical property ensures displacement vectors maintain realistic wave characteristics during synthesis.

混合权重遵循这样的规律：在六边形中心等于 1，向边缘递减至 0，从而实现六边形区域间的平滑过渡。混合是协方差保持的而非线性的，这意味着合成的向量与原始样本保持一致。这一数学性质确保位移向量在合成过程中保持真实的波浪特征。

The content from each hexagon is chosen randomly in the exemplar, producing fully aperiodic output. Random hexagon content selection creates aperiodic output while the covariance-preserving blending ensures no visible seams at hexagon boundaries.

每个六边形的内容在样本中随机选取，产生完全非周期性的输出。随机的六边形内容选择创建了非周期性输出，同时协方差保持混合确保六边形边界处没有可见接缝。

## Our Approach（我们的方法）

![](https://gerigory.github.io/assets/img/渲染技巧/Making-Waves-in-Ocean-Surface-Rendering-using-Tiling-and-Blending/img_005.jpg)

*Figure 6: Our Approach*

*图6：我们的方法*

The method takes periodic displacement and normal maps generated via the Tessendorf model as input. Any existing implementation can be enhanced from this point without changing the generation algorithm. This makes the technique a flexible enhancement layer that can be retrofitted onto existing ocean rendering systems.

该方法以 Tessendorf 模型生成的周期性位移贴图和法线贴图作为输入。任何现有实现都可以从此处进行增强，而无需更改生成算法。这使得该技术成为一个灵活的增强层，可以加装到现有的海洋渲染系统上。

The key innovation is applying the hexagonal tiling and blending approach directly to ocean displacement and normal maps, treating them as the exemplar texture to be synthesized into an aperiodic result. This produces a truly aperiodic ocean, resulting in more realistic open seas.

核心创新在于将六边形 tiling 和混合方法直接应用于海洋位移贴图和法线贴图，将它们作为待合成为非周期性结果的样本纹理。这产生了真正非周期性的海洋，使开阔海域更加真实。

## Flow Map（流图）

![](https://gerigory.github.io/assets/img/渲染技巧/Making-Waves-in-Ocean-Surface-Rendering-using-Tiling-and-Blending/img_006.jpg)

*Figure 7: Flow map strategy implementation*

*图7：Flow Map 策略实现*

A directional control system allows wave orientation authoring through a vector map. The strategy involves sampling a vector of the flow map in the center of each hexagon, turning it into a rotation angle, and applying corresponding rotations to both hexagon geometry and sampled values.

方向控制系统允许通过向量图来编排波浪朝向。策略是在每个六边形的中心采样 flow map 的向量，将其转化为旋转角度，然后对六边形几何体和采样值同时施加对应的旋转。

This enables a smooth shift from one ocean wave direction to another across the surface. Since no pre-computations are needed, the flow map can be modified in real-time, enabling dynamic wave direction changes during gameplay. This gives artists direct control over wave behavior in different areas of the ocean.

这使得海洋表面上波浪方向可以从一个方向平滑过渡到另一个方向。由于不需要预计算，flow map 可以实时修改，在游戏过程中实现动态波浪方向变化。这让美术可以直接控制海洋不同区域的波浪行为。

## LEAN Mapping

![](https://gerigory.github.io/assets/img/渲染技巧/Making-Waves-in-Ocean-Surface-Rendering-using-Tiling-and-Blending/img_007.jpg)

*Figure 9: Comparison between normal mapping, ground truth and LEAN mapping*

*图9：法线贴图、ground truth 与 LEAN mapping 的对比*

LEAN mapping is a filtering technique that converts normal maps into BRDFs at reduced resolutions, ensuring accurate specular rendering across viewing distances. It works by pre-computing the means and covariance functions of the BRDF for each resolution, requiring the computation of an additional texture.

LEAN mapping 是一种滤波技术，将法线贴图在降低分辨率时转换为 BRDF，确保不同观察距离下高光渲染的准确性。它通过为每个分辨率级别预计算 BRDF 的均值和协方差函数来工作，需要计算一张额外的纹理。

These statistical measurements allow the system to represent how each screen pixel's footprint interacts with the shaded surface. The authors demonstrated compatibility with both tiling/blending and flow maps, showing how to implement it when using flow maps, correcting the specular lobe without additional pre-computations.

这些统计量允许系统表示每个屏幕像素的覆盖范围如何与着色表面交互。作者展示了与 tiling/blending 和 flow maps 的兼容性，说明了在使用 flow maps 时如何实现 LEAN mapping，无需额外预计算即可修正高光瓣。

## Implementation（实现）

The method integrates into GPU shader pipelines for real-time performance. The displacement map is synthesized in the vertex shader, while the normal map and LEAN map (if necessary) are synthesized in the fragment shader. The approach supports systems using derivative maps instead of normals.

该方法集成到 GPU 着色器管线中以实现实时性能。位移贴图在顶点着色器中合成，而法线贴图和 LEAN 贴图（如有需要）在片段着色器中合成。该方法支持使用导数贴图（derivative maps）替代法线的系统。

The system dynamically manages detail levels through texture filtering and geometry tessellation, adjusting displacement map resolution based on viewer distance — maintaining high fidelity nearby while reducing computational overhead for distant surfaces.

系统通过纹理过滤和几何细分动态管理细节层级，根据观察者距离调整位移贴图分辨率——在近处保持高保真度，同时降低远处表面的计算开销。

## Results（结果）

<!-- 注：Figure 10 和 Figure 11 原始 URL 返回 404，保留外链供参考 -->

*Figure 10: Side-by-side comparison with traditional methods. From top to bottom: ocean rendering (top), displacement map over 4 periods and corresponding (middle) and positive autocorrelation (bottom)*

*图10：与传统方法的并排对比。从上到下：海洋渲染（上）、4 个周期的位移贴图及对应图（中）和正自相关（下）*

*Figure 11: GPU times*

*图11：GPU 时间*

Performance comparisons demonstrate superiority over traditional methods. The team measured periodicity using autocorrelation functions — a low autocorrelation value at high distances indicates reduced periodicity. The autocorrelation function of our ocean is closer to that of a real ocean for the same reason.

性能对比表明该方法优于传统方法。团队使用自相关函数来衡量周期性——高距离处的低自相关值表示周期性降低。我们的海洋的自相关函数更接近真实海洋，原因相同。

The method is faster than traditional methods that combine multiple sub-displacements and requires less memory than multi-IFFT approaches. It uses equivalent resources to Perlin noise blending while achieving a truly aperiodic ocean, resulting in more realistic open seas.

该方法比组合多个子位移的传统方法更快，且比多 IFFT 方案所需内存更少。它与 Perlin 噪声混合方案资源消耗相当，同时实现了真正非周期性的海洋，使开阔海域更加真实。

## Conclusion（结论）

The authors present their work as advancing ocean simulation through texture synthesis, delivering realistic, aperiodic ocean surfaces efficiently. The technique addresses traditional method limitations while offering enhanced creative control through flow maps and visual fidelity through LEAN mapping for gaming and research applications.

作者将其工作定位为通过纹理合成推进海洋模拟，高效地交付真实的、非周期性的海洋表面。该技术解决了传统方法的局限性，同时通过 flow maps 提供增强的创意控制，通过 LEAN mapping 提供视觉保真度，适用于游戏和研究应用。

## References（参考文献）

[1] Tessendorf, J. *Simulating Ocean Water*, SIGGRAPH 2001 Course Notes

[2] NVIDIA, *Ocean Surface Simulation*, NVIDIA Graphics SDK 11 Direct3D

[3] Deliot, T. & Heitz, E. *Procedural Stochastic Textures by Tiling and Blending*, GPU Zen 2: Advanced Rendering Techniques

[4] Olano, M. & Baker, D. *LEAN Mapping*, Proceedings of 2010 ACM SIGGRAPH Symposium on Interactive 3D Graphics and Games
