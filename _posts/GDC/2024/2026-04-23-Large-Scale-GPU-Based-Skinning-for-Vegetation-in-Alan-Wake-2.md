---
layout: post
title: "【GDC 2024】Large Scale GPU-Based Skinning for Vegetation in 'Alan Wake 2'"
date: 2026-04-23
img: GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_001.png # Add image post (optional)
fig-caption: # Add figcaption (optional)
tags: [GDC, 2024, Rendering, Vegetation, Performance, Optimization]
description: 本文分享的是【GDC 2024】Large Scale GPU-Based Skinning for Vegetation in 'Alan Wake 2'相关的技术要点
---

> **演讲者**：Kiyavash Kandar（Remedy Entertainment 图形程序员）  
> **来源**：[2024 GDC 演讲原视频 + KM 精译版](https://km.woa.com/group/29321/articles/show/577145)（字幕校对：mingqizhou）  
> **提取时间**：2026-04-23 14:21:12

---

## 📖 技术概要

> 本节内容整理自 [KM 精译版](https://km.woa.com/group/29321/articles/show/577145)，对自动转录的翻译错误进行了修正与补充。

---

### 1. 背景介绍

Remedy Entertainment 使用自研引擎 **Northlight** 开发《心灵杀手2》（Alan Wake 2），其中的森林动画面临以下核心设计目标：
- **密集可交互**：玩家穿过森林时，植被需弯曲并对玩家做出反应
- **全场景 BVH**：所有几何图形须准确出现在光线追踪的**边界体积层次结构（BVH）**中
- **高真实感**：使用高精度多边形网格，拒绝简单的顶点摆动（vertex wobbling），要求复杂的层次化骨骼动画
- **性能目标**：在 Xbox Series S 上以 30 FPS 稳定运行

**Xbox Series S GPU vs RTX 4080**

|指标|Xbox Series S|RTX 4080|
|---|---|---|
|**架构**|AMD RDNA 2|NVIDIA Ada Lovelace|
|**计算单元/核心**|20 CU|9728 CUDA Cores|
|**FP32 算力**|**4 TFLOPS**|**~48.7 TFLOPS**|
|**显存**|10 GB GDDR6 (共享)|16 GB GDDR6X (独立)|
|**显存带宽**|224 GB/s|716.8 GB/s|
|**光线追踪**|硬件 RT（1st gen，有限）|3rd gen RT Cores|
|**AI 加速**|无专用单元|4th gen Tensor Cores|
|**帧生成 (Frame Gen)**|✗|✓ DLSS 3|
|**定位分辨率**|1080p / 1440p|4K Ultra|
|**TDP**|~100W|~320W|

**关键差距：**

**算力比：约 12:1**。RTX 4080 的 FP32 算力是 Series S 的 12 倍以上，带宽也是 3 倍以上。

**与 Alan Wake 2 的相关性：**  
正是这一差距决定了文章中大规模 GPU 植被蒙皮的 LOD 策略与预算划分——Series S 的 4 TFLOPS 预算极为有限，GPU Skinning 管线必须在 **compute shader dispatch 数量、骨骼矩阵缓存** 等方面做严格裁剪，而 RTX 4080 版本则可以负担更高密度的植被实例和更精细的蒙皮层级。

**内存架构差异也很关键：** Series S 使用统一内存（CPU/GPU 共用 10 GB），实际 GPU 可用量更少；RTX 4080 拥有独立的 16 GB GDDR6X，这对大规模骨骼矩阵的 buffer 存储影响显著。

这些目标共同指向一个结论：对整片森林（每棵树、每丛灌木、每片草地）使用**骨骼层次结构蒙皮（skeletal skinning）+ 计算着色器（compute shader）**驱动。

---

### 2. 《控制》中的蒙皮管线

《控制》（Control）的蒙皮管线是《心灵杀手2》的起点：

- 骨骼在 **CPU 端更新**，最终骨骼变换复制到 GPU
- 在**光栅化**过程中，顶点着色器按材质和骨骼权重对顶点进行蒙皮
- 为向光线追踪 BVH 输出几何图形，需在**独立计算着色器**中再次蒙皮，将变换后的几何图形写入顶点缓冲区后馈入 BVH
- 由于两次蒙皮成本较高，《控制》仅对**扩展相机视锥体**内的对象执行额外蒙皮

**局限性**（不满足《心灵杀手2》需求）：

| 问题 | 原因 |
|------|------|
| 网格着色器内蒙皮成本过高 | 转向 GPU 驱动 + 网格着色器的渲染管线后，每个着色器变体都会增加光栅化成本 |
| 几何体规模庞大 | 热点区域有近 5,000 个独特蒙皮网格，约 700 万顶点，两次蒙皮带宽压力过大 |
| 无法依赖扩展视锥体裁剪 BVH | 低角度阳光 + 路径追踪间接光照要求所有内容都在 BVH 中，否则产生缺失阴影伪影 |

---

### 3. 《心灵杀手2》中的预蒙皮管线（Pre-Skinning）

核心思路：将《控制》中为 BVH 复制皮肤几何图形的计算着色器**移至渲染预处理通道**，改为只蒙皮一次。

**工作流程**：
1. 预蒙皮计算着色器将几何图形输出到**大型顶点缓冲区**（以 64 MB 页为单位分配）
2. 几何图形输出后，光栅化与 BVH 均直接使用，无需额外蒙皮或额外着色器变体
3. 页面使用引用计数管理，无引用时释放，不做碎片整理

**预蒙皮着色器规格**：
- 3 个着色器变体，分别对应骨骼权重 1、4、8
- 每次蒙皮前在计算着色器中生成 128 顶点的批次（batch）
- 每个顶点缓冲区页面上启动大小为 128 的 thread group，每顶点一个线程
- **关键限制**：预蒙皮必须在渲染开始前全部完成

---

### 4. 压缩顶点数据

**背景**：Cauldron Lake 区域仅皮肤顶点数据就接近 **2 GB**，必须压缩。

**基础方法（失败）**：简单降低数据类型位数 → 精度过低，法线/切线出现明显阶梯状伪影。

**最终方案**：

| 数据      | 压缩方法                                           |
| ------- | ---------------------------------------------- |
| 法线 / 切线 | **OXT 编码**，转为两个 32 位浮点后再压缩                     |
| 顶点位置    | 使用**绑定球体（bound sphere）**归一化后转为有符号整数，每分量精度分布更均匀 |

**效果**：每顶点节省约 50%，结合团队其他优化，峰值皮肤顶点内存从 **2 GB 降至 100–170 MB**。

> 压缩后皮肤网格在移动时需动态更新压缩边界：预蒙皮着色器以 T-pose 边界解压源网格 → 蒙皮 → 重新压缩边界（全程在预蒙皮着色器内完成）。

---

### 5. 网格变体（Mesh Variants / Instancing）

大型树木（红雪松、铁杉）体积巨大、细节丰富，但间距大且不可交互（枝条过高无法触及），适合实例化。

**Northlight 引擎变体（Variants）机制**：
- 一份顶点数据 + 一个网格，在世界中以不同位置/方向多次渲染
- 网格编辑器中可设置每个网格同时激活的变体数量
- 最终方案：大型树木仅使用 **3–4 个变体**，在质量与性能间取得平衡
- 效果：节省数百个独立实例和大量顶点内存，同时保留灌木、草地等小网格的独立性（保证可交互性）

---

### 6. 几何变换着色器（Geometry Transform Shaders, GTS）

将骨骼动画的 CPU 端工作移至 GPU，获得带宽和规模优势。

**核心机制**：
- 加载时将骨骼一次性复制到 GPU；每帧通过**计算着色器程序化驱动**骨骼层次结构动画
- 每个线程在局部空间输出 `float3` 平移 + `float4` 四元数旋转，后处理通道转换为 4×3 矩阵
- 向美术师暴露着色器 API，可读写骨骼 ID、静止姿势（rest pose）、世界空间信息等

**迭代历程**：

**第一次迭代（失败）**：按层次结构级别过滤骨骼，每级分派一个计算着色器通道 + 屏障（barrier），在循环中串行执行。
- 问题：GPU 利用率低，调度 + 屏障开销大；工作量与内容结构强相关，不可预测
- 每帧需要 **137 次**调度和屏障

**第二次迭代（最终方案）**：
1. 过滤出**叶片骨骼（leaf bones）**
2. 为每个叶片骨骼启动一个线程
3. 每个线程在着色器内完整遍历从根到叶片的整条层次链，沿途存储所有骨骼变换
4. 重复计算但数据完全并行化，仅需 **1 次调度 + 1 次屏障**

效果：**速度提升 3 倍**，每帧调度从 137 次降至 **8 次**，达到性能目标。

**对象边界计算**：
- GTS 网格的对象边界仅存在于 GPU 端（适配 Northlight 的 GPU 剔除）
- 使用 **wave intrinsics**（每骨骼一个 lane）缩小 AABB，转为绑定球体
- 后续计算着色器将每变体边界传播到每实例的世界空间边界（每实例一个线程）

**性能数据（热点区域"叠界 / The Overlap"）**：

| 指标 | 数值 |
|------|------|
| 独特蒙皮网格数 | ~5,000 |
| 总顶点数 | ~700 万 |
| 皮肤顶点数据 | 80 MB |
| GTS 独立着色器数 | 8 |
| PS5 耗时 | ~1.5 ms |
| Xbox Series S | 需开启植被密度图形设置（节省约 100 万顶点）|

> GTS 不限于植被，也用于水面浮动碎屑、风中摇摆的电线等。

---

### 7. 光线追踪

**BVH 接入**（预蒙皮 + 压缩后）：
- 将底层加速结构（BLAS，即光线追踪网格）指向顶点缓冲区页面，调整顶点格式
- 将压缩边界作为顶层加速结构（TLAS，即网格实例）上的变换，确保解压后顶点位置比例正确
- 标准蒙皮网格在 CPU 端处理，GTS 网格在计算着色器中处理

**性能问题与解决方案**：

"全量放入 BVH" 初始方案性能极差：
- **CPU 瓶颈**：需为每个 BLAS 和 TLAS 单独发出命令，数量庞大
- **GPU 瓶颈**：高几何密度导致 BLAS 构建时间过长

由于低角度阳光设置，从 BVH 中移除对象会迅速产生缺失阴影伪影，故选择**降低重建频率**：

**级联方案（Cascaded BVH Update）**：

| Cascade | 距离 | 更新频率 |
|---------|------|---------|
| Cascade 0 | 相机附近 | 每帧全速 |
| Cascade 1 | 10 m 外 | 每 2 帧 |
| Cascade 2 | 20 m 外 | 每 3 帧 |
| … | … | … |

- 角色网格**始终全速更新**（对视觉质量影响关键，不允许有伪影）
- 需针对性调整光栅化参数，隐藏 BVH 与屏幕几何图形之间的不匹配（闪烁问题）

**最终效果**：结合多线程优化，BVH 构建时间减少近一半。  
**当前瓶颈**：CPU 端 BLAS 构建命令缺乏 Indirect API 支持；GPU 端几何体分割为大量小块（meshlet），现有 BVH 构建 API 对此不友好。

---

### 8. 总结

| 目标 | 达成情况 |
|------|---------|
| 密集可缩放的森林 | ✅ 关卡规模接近开放世界，远景植被风中摇曳效果良好 |
| 高多边形动画网格 | ✅ 预蒙皮管线支持高精度多边形网格动画 |
| 光栅化性能 | ✅ 蒙皮与光栅化解耦，网格着色器保持精简 |
| 逼真运动 | ✅ 计算着色器程序化骨骼动画优于顶点摆动 |
| 全量 BVH | ✅ 级联更新策略保证所有皮肤几何图形在 BVH 中 |

---

## 🎞️ 幻灯片逐帧转录

> 以下为 ASR 自动转录 + 机器翻译内容，部分片段已根据 KM 精译版修正，仅供参考。

---

## Slide 1 — 00:00:22

![Slide 1](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_001.png)

**📌 要点汇总**

- 本演讲介绍《心灵杀手2》森林动画的制作方法：如何为数千个独特网格执行完整骨骼动画，以及如何保证其性能良好。
- 演讲结构：《控制》蒙皮管线回顾 → 《心灵杀手2》改进方案 → 最终效果评估。

> 我们将分享《心灵杀手2》游戏中森林动画的制作方法以及解决方案的实施，也就是我们如何为数千个独特网格执行完整的骨骼动画的，最重要的是，我们如何确保它的性能良好。我们首先看一下在《控制》这款游戏中使用的蒙皮管线，然后看看为了达到《心灵杀手2》的要求，我们对这个管线做了哪些调整，接下来再看看最后的效果如何。
>



---

## Slide 2 — 00:00:38

![Slide 2](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_002.png)

**📌 要点汇总**

- Remedy Entertainment，1995 年成立于芬兰，代表作包括《马克思·佩恩》《量子破碎》《控制》《心灵杀手》系列。
- 使用完全自研的 **Northlight 引擎**（今日演讲重点）。
- PEGI 18 级游戏。

> 如果大家还没有听说过绿美迪娱乐公司（Remedy），我们是一家于 1995 年在芬兰创立的游戏公司。我们最出名的游戏包括《马克思·佩恩》、《量子破碎》、《控制》，当然还有《心灵杀手》。在 Remedy，我们使用自己的内部引擎 Northlight，这个引擎完全是内部开发的，它是我们自己的定制技术栈，也是今天讨论的重点。PEGI 18。联邦调查局特工，把刀放下。
>



---

## Slide 3 — 00:01:18

![Slide 3](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_003.png)


**📌 要点汇总**
- (Content too short, no key points)

> 让我看看死亡。联邦调查局，放下刀子。
>



---

## Slide 4 — 00:01:46

![Slide 4](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_004.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 5 — 00:01:46

![Slide 5](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_005.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 6 — 00:01:46

![Slide 6](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_006.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 7 — 00:01:46

![Slide 7](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_007.png)

**📌 要点汇总**

- 《心灵杀手2》2023 年 10 月发售，双主角：Saga Anderson（FBI 特工，调查美国西北部森林邪教）和 Alan Wake（困于噩梦现实）。
- 森林设计四大核心目标：**密集**、**可交互**（玩家走过时植被弯曲反应）、**全量 BVH**（光线追踪精确表示）、**逼真运动**。
- 最终选择：对每棵树、每丛灌木、每片草地使用**完整骨骼蒙皮（skeletal skinning）+ 计算着色器**驱动。

> 《心灵杀手2》去年 10 月发布，是 2010 年那款经典动作恐怖游戏的续作，这次有两个主角：Saga Anderson，她是一名联邦调查局特工，负责在美国西北部的森林中调查邪教，我们今天讨论的就是森林的动画制作；另一个是 Alan Wake，他陷入了噩梦般的现实并试图逃脱。我们希望森林密集、可交互，所有几何图形都能在边界体积层次结构（BVH）中实时且准确地表示，效果必须看起来非常逼真。我们使用非常高精度的多边形网格，不用顶点摆动，而是要实现复杂、层次化、逼真的骨骼动画——也就是对整片森林的所有对象使用骨骼层次结构蒙皮，并通过计算着色器确保性能。
>



---

## Slide 8 — 00:03:30

![Slide 8](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_008.png)

**📌 要点汇总**

- **《控制》蒙皮管线**：CPU 更新骨骼 → 复制到 GPU → 顶点着色器在光栅化期间蒙皮，BVH 需再次单独蒙皮（成本高，仅对扩展视锥体内对象执行）。
- **《心灵杀手2》的挑战**：转向网格着色器渲染管线，热点区域约 5,000 个蒙皮网格、700 万顶点；低角度阳光要求全量 BVH，无法再依赖视锥体裁剪，两次蒙皮代价过高。

> 大家现在看到的是 **Cauldron Lake** 区域所有绑定几何图形的骨骼，这个区域位于便利店附近。我们大部分都是在 GPU 上实现的——这些都是真的骨骼，真的蒙皮，全部由计算着色器驱动。《控制》的蒙皮管线：CPU 更新骨骼 → 将骨骼变换复制到 GPU → 顶点着色器按材质和骨骼权重在光栅化期间蒙皮。为将几何图形输出到 BVH，还需在独立计算着色器中再次蒙皮，写入顶点缓冲区后馈送到 BVH。成本高，《控制》仅对扩展相机视锥体内的对象执行这个额外的蒙皮。对《心灵杀手2》来说，这个方案不足够——转向网格着色器后，每帧约 1000–2000 万个三角形，热点区域有约 5,000 个独特蒙皮网格和 700 万个顶点，且低角度阳光加路径追踪的复杂布光设置要求所有内容都在 BVH 中，不能依赖扩展视锥体裁剪。
>



---

## Slide 9 — 00:06:56

![Slide 9](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_009.png)

**📌 要点汇总**

- **预蒙皮（Pre-Skinning）核心**：将《控制》中为 BVH 复制几何图形的计算着色器移至渲染预处理通道，只蒙皮一次；输出到 64 MB 页顶点缓冲区，光栅化与 BVH 共用，无需额外着色器变体。
- **预蒙皮着色器规格**：3 个变体（骨骼权重 1/4/8），128 顶点 batch，thread group 大小 128（每顶点一线程）。
- **顶点压缩**：法线/切线用 OXT 编码，位置用绑定球体归一化后转有符号整数；每顶点节省约 50%，Cauldron Lake 皮肤顶点内存从 **~2 GB 降至 100–170 MB 峰值**。
- **网格变体（Instancing）**：大型树木（红雪松、铁杉）使用 3–4 个变体，节省大量顶点内存，同时保留灌木草地的独立性（保证可交互）。
- **几何变换着色器（GTS）**：加载时将骨骼复制到 GPU 一次，之后通过计算着色器程序化驱动骨骼动画；目标 Xbox Series S 上每毫秒 100 万根骨骼。

> **预蒙皮**：在《心灵杀手2》中，我们不再两次蒙皮，而是在计算着色器预处理通道中只蒙皮一次——“预蒙皮”。预蒙皮将几何图形输出到大型顶点缓冲区（64 MB 分页分配，无碎片整理），光栅化和 BVH 直接使用，无需额外蒙皮或着色器变体。预蒙皮着色器有 3 个变体（骨骼权重 1、4、8），以 128 顶点为批次，每顶点启动一个线程。
>
> **顶点压缩**：Cauldron Lake 区域皮肤顶点数据接近 2 GB，必须压缩。简单降位数质量太低（法线/切线出现阶梯状伪影）。最终方案：法线/切线用 OXT 编码转为两个 32 位浮点后再压缩；位置用绑定球体归一化后转有符号整数。每顶点节省约 50%，峰值皮肤顶点内存降至 100–170 MB。
>
> **网格变体**：大型红雪松和铁杉不可交互（枝条过高），用 3–4 个变体实例化，节省数百个独立实例和大量顶点，同时灌木草地保持独立（保证可交互性）。
>
> **几何变换着色器（GTS）**：将骨骼动画的 CPU 端工作移至 GPU。加载时骨骼一次性复制到 GPU，之后用计算着色器程序化驱动。每线程在局部空间输出 `float3` 平移 + `float4` 四元数旋转，后处理通道转为 4×3 矩阵。植被专用 GPU 动画路径。目标：Series S 上每毫秒 100 万根骨骼。
>



---

## Slide 10 — 00:17:28

![Slide 10](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_010.png)


> *（该幻灯片时间段内未检测到语音内容）*

---
## Slide 11 — 00:17:28

![Slide 11](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_011.png)

**📌 要点汇总**

- **第一次迭代（失败）**：按层次结构级别过滤骨骼，每级分派一个计算着色器通道 + 屏障（barrier），在循环中串行执行，无法有效利用 GPU 并行性，每帧需 137 次调度和屏障。
- 额外问题：美术师通过 LOD 逐步减少骨骼数量来降低成本，但 LOD 切换时骨骼层次结构对齐极其困难，是美术师的主要痛点。

> **第一次迭代及其失败原因**：我们最初使用了暴力方法，按层次结构级别过滤骨骼，为每个层次结构级别分配一个计算着色通道，从 0 级开始一直到最后。在循环中进行调度和使用屏障的成本和开销导致性能很差，我们没能把工作转移到 GPU 上，而且工作量也难以预测，与内容结构密切相关。美术师们通过对植被骨骼进行 LOD 处理来降低成本（每个 LOD 逐渐减少骨骼数量直到网格变成完全静态），但 LOD 切换时骨骼层次结构和几何变换着色器必须完全吻合，否则会有 LOD popping，这是美术师最主要的抱怨。
>



---

## Slide 12 — 00:17:44

![Slide 12](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_012.png)


**📌 要点汇总**
- (Content too short, no key points)

> 当然。嗯，我的意思是。
>



---

## Slide 13 — 00:17:46

![Slide 13](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_013.png)

**📌 要点汇总**

- **第二次迭代（最终方案）**：过滤出**叶片骨骼（leaf bones）**，每叶片骨骼启动一个线程，线程在着色器内完整遍历从根到叶片的层次链并存储所有骨骼变换。仅需 1 次调度 + 1 次屏障。
- 速度提升 **3 倍**：每帧调度从 137 次降至 **8 次**，达到性能目标。
- **对象边界计算**：用 wave intrinsics（每骨骼一个 lane）缩减 AABB 为绑定球体，用于 GPU 剔除和预蒙皮顶点压缩。
- **热点区域"叠界"性能**：~5,000 蒙皮网格，700 万顶点，80 MB 皮肤顶点数据，8 个 GTS，PS5 约 **1.5 ms**。GTS 不限植被，亦用于水面浮动碎屑、电缆摇摆等。

> **第二次迭代**：不再按层次结构分级调度，而是先过滤出叶片骨骼（红色标注），为每个叶片骨骼启动一个线程。线程在着色器内完整遍历从 0 级到叶片骨骼的整条层次链，计算连续变换并存储沿途每个骨骼的变换。虽然重复计算了上级骨骼的变换，但成功并行化了数据，只需 1 次调度 + 1 次屏障。速度提升 3 倍，每帧调度从 137 次降至 8 次，达到性能目标，这就是最终发布的方案。
>
> **对象边界计算**：几何变换网格的对象边界仅存在于 GPU 端（适配 Northlight 的 GPU 剔除）。基于每个皮肤网格变体的骨骼范围计算 AABB，用 wave intrinsics（每骨骼一个 lane）缩减，然后对每组进行最终缩减，转为绑定球体。后续计算着色器将每变体边界传播到世界空间每实例边界（每实例一线程）。这也是预蒙皮顶点压缩所用的绑定球体。
>
> **热点区域"叠界（The Overlap）"性能**：约 5,000 个蒙皮网格，700 万个顶点，80 MB 皮肤顶点数据，8 个几何变换着色器。PS5 约 1.5 ms。GTS 不仅用于植被，还用于水面浮动碎屑、风中摇摆的电线，用途广泛。
>



---

## Slide 14 — 00:22:30

![Slide 14](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_014.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 15 — 00:22:30

![Slide 15](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_015.png)


**📌 要点汇总**
- (Content too short, no key points)

> 框架的一小部分。
>



---

## Slide 16 — 00:22:32

![Slide 16](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_016.png)


**📌 要点汇总**
- (Content too short, no key points)

> 花费在对这么多几何体进行蒙皮上，之后您根本不需要触摸它。
>



---

## Slide 17 — 00:22:36

![Slide 17](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_017.png)


**📌 要点汇总**
- (Content too short, no key points)

> 已准备好进行渲染。
>



---

## Slide 18 — 00:22:38

![Slide 18](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_018.png)


**📌 要点汇总**
- (Content too short, no key points)

> 但这个成本对于 S 系列来说有点太高了，所以我们。
>



---

## Slide 19 — 00:22:42

![Slide 19](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_019.png)

**📌 要点汇总**

- Xbox Series S 成本稍高，需添加植被密度图形设置（节省约 100 万顶点，约几百个实例）。
- **BVH 接入**：BLAS 指向顶点缓冲区页面，TLAS 上应用压缩边界变换，确保解压后顶点比例正确。
- **级联 BVH 更新策略**：Cascade 0（相机附近）全速；Cascade 1（10m 外）每 2 帧；Cascade 2（20m 外）每 3 帧；角色网格始终全速。
- 经过多线程优化，BVH 构建时间减少近一半；瓶颈在 CPU 端 BLAS 构建命令缺乏 Indirect API 支持。

> Xbox Series S 上成本偏高，需添加植被密度图形设置，节省约 100 万顶点。《心灵杀手2》在 Series S 上以 30 FPS 运行，预蒙皮着色器占约三分之二的蒙皮时间，性能主导因素是顶点数量。
>
> **光线追踪 BVH 接入**：通过预蒙皮 + 压缩，只需将 BLAS（底层加速结构/光线追踪网格）指向顶点缓冲区页面并调整顶点格式；将压缩边界作为 TLAS（顶层加速结构/网格实例）上的变换，确保解压后顶点位置比例正确。
>
> **全量 BVH 初始方案性能极差**：CPU 端需为每个 BLAS 和 TLAS 单独发出命令；GPU 端因几何密度高导致 BLAS 构建时间过长。由于低角度阳光设置，从 BVH 中移除对象很快产生缺失阴影伪影，只能选择降低重建频率。
>
> **级联 BVH 更新策略**：Cascade 0（相机附近）全速；10m 外第 2 帧更新；20m 外第 3 帧更新，以此类推。角色网格始终全速。需调整光栅化参数隐藏 BVH 与屏幕几何图形的不匹配（闪烁问题）。结合多线程优化，BVH 构建时间减少近一半，但 CPU 端 BLAS 构建命令耗时仍很长，缺乏 Indirect API 支持。
>



---

## Slide 20 — 00:27:02

![Slide 20](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_020.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 21 — 00:27:02

![Slide 21](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_021.png)


**📌 要点汇总**
- (Content too short, no key points)

> 几何体被分成许多小块。
>



---

## Slide 22 — 00:27:06

![Slide 22](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_022.png)

**📌 要点汇总**

- GPU 端几何图形被分割为大量小块（meshlet），当前 BVH 构建 API 不支持在 API 中直接构建 meshlet，这是性能瓶颈所在，已达到当前 API 能力极限。

> 当前的 BVH 构建 API 对此并不是非常友好。几何图形被分割成许多小块，在 BVH 构建 API 中不支持 meshlet 级别的构建，我认为我们已经达到了当前 API 的极限。
>



---

## Slide 23 — 00:27:20

![Slide 23](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_023.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 24 — 00:27:20

![Slide 24](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_024.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 25 — 00:27:20

![Slide 25](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_025.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 26 — 00:27:20

![Slide 26](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_026.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 27 — 00:27:20

![Slide 27](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_027.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 28 — 00:27:20

![Slide 28](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_028.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 29 — 00:27:20

![Slide 29](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_029.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 30 — 00:27:20

![Slide 30](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_030.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 31 — 00:27:20

![Slide 31](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_031.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 32 — 00:27:20

![Slide 32](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_032.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 33 — 00:27:20

![Slide 33](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_033.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 34 — 00:27:20

![Slide 34](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_034.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 35 — 00:27:20

![Slide 35](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_035.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 36 — 00:27:20

![Slide 36](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_036.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 37 — 00:27:20

![Slide 37](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_037.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 38 — 00:27:20

![Slide 38](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_038.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 39 — 00:27:20

![Slide 39](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_039.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 40 — 00:27:20

![Slide 40](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_040.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 41 — 00:27:20

![Slide 41](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_041.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 42 — 00:27:20

![Slide 42](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_042.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 43 — 00:27:20

![Slide 43](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_043.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 44 — 00:27:20

![Slide 44](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_044.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 45 — 00:27:20

![Slide 45](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_045.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 46 — 00:27:20

![Slide 46](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_046.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 47 — 00:27:20

![Slide 47](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_047.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 48 — 00:27:20

![Slide 48](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_048.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 49 — 00:27:20

![Slide 49](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_049.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 50 — 00:27:20

![Slide 50](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_050.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 51 — 00:27:20

![Slide 51](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_051.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 52 — 00:27:20

![Slide 52](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_052.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 53 — 00:27:20

![Slide 53](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_053.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 54 — 00:27:20

![Slide 54](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_054.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 55 — 00:27:20

![Slide 55](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_055.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 56 — 00:27:20

![Slide 56](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_056.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 57 — 00:27:20

![Slide 57](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_057.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 58 — 00:27:20

![Slide 58](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_058.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 59 — 00:27:20

![Slide 59](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_059.png)

**📌 要点汇总**

- 最终方案实现了所有目标：关卡规模接近开放世界的密集植被、顶点压缩 + 网格变体保证密度、预蒙皮管线支持高多边形动画网格。
- 计算着色器程序化骨骼动画（GTS）获得比顶点摆动更自然的运动效果，且性能良好、可扩展。
- 级联 BVH 更新策略使所有皮肤几何图形进入光线追踪，搭配光栅直接光和路径追踪获得更好的视觉效果。

> 那么，我们如何才能实现最初的愿景呢？这几乎是一切就位了。好吧，首先，我们确实设法得到了可以扩展的东西。 《心灵杀手 2》的关卡在大小上与开放世界非常相似。我们拥有完整的远景，您可以看到巨大的森林景观在风中非常漂亮地移动，并且我们应用了顶点压缩和智能。
>



---

## Slide 60 — 00:27:46

![Slide 60](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_060.png)


**📌 要点汇总**
- (Content too short, no key points)

> 使用变体可以帮助我们获得所需的植被密度。
>



---

## Slide 61 — 00:27:50

![Slide 61](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_061.png)


**📌 要点汇总**
- (Content too short, no key points)

> 我们有数千个独特的皮肤网格及其实例。
>



---

## Slide 62 — 00:27:56

![Slide 62](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_062.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 63 — 00:27:56

![Slide 63](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_063.png)

**📌 要点汇总**

- 我们的预蒙皮管道使我们能够提供高多边形动画网格。
- 单独进行蒙皮也可以使我们的网格着色器保持精简，以获得更好的光栅化性能。
- 然后，使用由计算着色器程序驱动的骨骼动画，使我们获得比通过顶点摆动获得的更自然的运动。

> 我们的预蒙皮管道使我们能够提供高多边形动画网格。单独进行蒙皮也可以使我们的网格着色器保持精简，以获得更好的光栅化性能。然后，使用由计算着色器程序驱动的骨骼动画，使我们获得比通过顶点摆动获得的更自然的运动。我们的最终解决方案也具有相当的性能和可扩展性。
>



---

## Slide 64 — 00:28:22

![Slide 64](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_064.png)

**📌 要点汇总**

- 通过以平衡的精度有选择地更新光线追踪 BVH，我们可以在光线追踪中表示所有皮肤几何形状，从而通过停止直接照明和路径追踪获得更好的视觉效果。

> 通过以平衡的精度有选择地更新光线追踪 BVH，我们可以在光线追踪中表示所有皮肤几何形状，从而通过停止直接照明和路径追踪获得更好的视觉效果。谢谢。
>



---

## Slide 65 — 00:28:40

![Slide 65](https://gerigory.github.io/assets/img/GDC/2024/Large-Scale-GPU-Based-Skinning-for-Vegetation-in-Alan-Wake-2/slide_065.png)

**📌 要点汇总**

- 如果您有任何疑问，我认为那边有一个总结区。
- 如果您想过来聊天或给我发电子邮件，都可以。

> 请不要忘记填写反馈表。如果您有任何疑问，我认为那边有一个总结区。如果您想过来聊天或给我发电子邮件，都可以。谢谢。
>



---
