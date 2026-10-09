---
layout: post
title: "【Siggraph 2020】Samurai shading in ghost of tsushima"
date: 2020-08-01
img: Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_001.png # Add image post (optional)
fig-caption: # Add figcaption (optional)
tags: [Siggraph, 2020, Lighting, Rendering]
description: 本文分享的是【Siggraph 2020】Siggraph2020 - Samurai shading in ghost of tsushima相关的技术要点
---

> 来源：D:\迅雷下载\Graphics Materials\Siggraph 2020 - Samurai shading in ghost of tsushima.pdf
> 提取时间：2026-05-14 16:46:32

---

## Slide 1

![Slide 1](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_001.png)

**📌 要点汇总**

- **演讲者身份**：Jasmin Patry，Sucker Punch Productions首席渲染工程师  
- **项目背景**：开发PlayStation 4游戏《对马岛之魂》  
- **技术研究方向**：基于物理的着色（PBR）技术探索与应用

> 你好！我叫 Jasmin Patry，在 Sucker Punch Productions 担任首席渲染工程师。我很荣幸也很兴奋能与您谈论 我们在开发新的 PlayStation 4 游戏《对马岛之魂》时进行了一些基于物理的着色研究。

---

## Slide 2

![Slide 2](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_002.png)

**📌 要点汇总**

- **公司背景**：Sucker Punch自2011年起为索尼旗下工作室，总部位于华盛顿州贝尔维尤。  
- **团队规模**：开发《Ghost》期间团队人数曾达到160人峰值。  
- **过往作品**：曾开发《狡猾的库珀》系列及另一款知名

> 如果您不熟悉 Sucker Punch，我们自 2011 年起就成为索尼互动娱乐公司的一部分，位于华盛顿州贝尔维尤，靠近 西雅图。 [下一页] 在《Ghost》的开发过程中，我们工作室的人数达到了 160 人的顶峰， [下一页] 我们之前的游戏包括 [下一页] 狡猾的库珀系列， [下一页] 以及臭名昭著的系列游戏。

---

## Slide 3

![Slide 3](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_003.png)

> 正如我提到的，我们最近发布了 PlayStation 4 版《对马岛之魂》。

---

## Slide 4

![Slide 4](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_004.png)

> 《幽灵》是一款以 13 世纪封建日本为背景的开放世界动作冒险游戏……

---

## Slide 5

![Slide 5](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_005.png)

> ...您在其中扮演武士Jin Sakai的角色...

---

## Slide 6

![Slide 6](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_006.png)

> ...蒙古入侵对马岛的唯一幸存者...

---

## Slide 7

![Slide 7](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_007.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> ...当他为解放家园而奋斗时。

---

## Slide 8

![Slide 8](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_008.png)

**📌 要点汇总**

- **材质升级**：

> 完成《臭名昭著：次子》和《第一道光》后，我们的目标之一是提高材质和照明的质量， [下一页] 特别是对于我们的性格。 [下一页] 其中一个目标是支持新型材料，例如丝绸，它具有很强的各向异性镜面反射响应，以及天鹅绒等具有很强的各向异性镜面响应的材料。 粗糙散射。 [下一页] 我们还想提高皮肤着色的保真度；特别是我们的次表面散射的质量。 [下一页] 另一个目标是让基于扫描材料的细节图的使用更加容易； [下一页] 我们已经在使用普通细节贴图，但我们希望能够轻松直观地使用反照率、光泽度和镜面细节贴图创作材质， 为了缩小纹理尺寸，同时保留细节特写。

---

## Slide 9

![Slide 9](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_009.png)

> 现在我来谈谈《Ghost》中的灯光；我们的艺术方向要求“风格化的现实主义”——所以我们在这个项目上的目标并不是照片写实主义。 [下一页] 然而，我们的光照模型是基于物理的，我们的材质是使用物理上合理的值和一些摄影测量来创作的。 这使得我们的材料能够以一致的方式响应光。 [下一页] 我们确实偏离了物理正确性的地方是在照明阶段。我们为灯光艺术家提供了一组旋钮，使他们能够进行全局调整 各种照明参数（例如环境漫反射和镜面平衡、天空亮度等）以实现所需的外观。 Typically this is most 通常以我们的天气系统中的天气和一天中的时间状态的粒度来完成。
>
> [补充说明] 其他基于物理的照明位： * 节能 * GGX 镜面 NDF * 史密斯可见度函数 * 石里克菲涅尔 *朗伯漫反射+可选节能半透明+可选模糊 * SH 源自天空能见度与天空 SH 的卷积 * 动态重新照亮环境镜面反射探针，在运行时与 GGX NDF 进行卷积 * 物理照明值 * 节能区域灯

---

## Slide 10

![Slide 10](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_010.png)

> 在渲染技术方面，《Ghost》中的大部分光照都是延迟的； [下一页] 默认情况下我们使用朗伯漫反射， [下一页] 具有可选的半透明照明模型， [下一页] 以及可选的粗糙体散射模型。 [下一页] 镜面反射使用各向同性 GGX， [下一页] 通过金属通道可选择彩色镜面反射。 [下一页] 具有不同要求的材料是前向照明的，例如在使用时 [下一页] 各向异性 GGX 镜面反射， [下一页] 我将在本次演讲稍后讨论的完全各向异性粗糙散射 BRDF， [下一页] 或次表面散射。 [下一页] 我将更详细地讨论这四个突出的要点。

---

## Slide 11

![Slide 11](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_011.png)

**📌 要点汇总**

- **各向异性镜面

> 我把这次演讲分为四个部分： [下一页] 首先，我将讨论我们存储和过滤各向异性镜面贴图的方法； [下一页] 接下来我将讨论我们新的各向异性粗糙散射 BRDF； [下一页] 然后我将讨论我们对次表面散射模型所做的改进； [下一页] 由于时间限制，讨论详细地图的最后部分将仅作为附赠幻灯片提供。

---

## Slide 12

![Slide 12](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_012.png)

> 首先，让我描述一下我们存储和过滤各向异性镜面贴图的方法。

---

## Slide 13

![Slide 13](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_013.png)

**📌 要点汇总**

- **各向异性GGX镜面反射限制**：早期仅支持网格切线空间对齐的镜面反射  
- **Ghost项目方向需求**：支持任意空间变化方向，用于扫描材料数据可视化评估  
- **法线方差过滤扩展**：需实现类似各向同性镜面法线的光泽贴图过滤功能  
- **SGGX论文启发**：Heitz等人研究为实现目标提供新方法思路

> 在我们早期的游戏中，我们支持各向异性 GGX 镜面反射，但它仅限于网格切线空间的对齐。 [下一页] 对于 Ghost，我们希望支持任意的、空间变化的方向，部分原因是我们正在评估提供此数据的扫描材料， 我们希望能够在引擎中将其可视化。 [下一页] 我们还希望支持法线方差过滤，就像我们已经为各向同性镜面法线和光泽贴图所做的那样。 [下一页] 大约在我们从事这项工作的同时，Heitz 等人发表的 SGGX 论文发表了，这为我们提供了一些新方法的想法 实现这些目标。

---

## Slide 14

![Slide 14](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_014.png)

**📌 要点汇总**

- **LEAN Mapping**：使用贝克曼NDF过滤法线贴图实现各向异性抗锯齿  
- **存储优化**：8位纹理需谨慎选缩放因子，16位存储更优

> 之前在这个领域已经做过一些工作，我首先要讨论的是 2010 年的 LEAN Mapping。 [下一页] 它使用类似贝克曼的 NDF 来过滤法线贴图以产生各向异性抗锯齿结果。 对于存储，需要仔细选择缩放因子，尤其是在使用 8 位纹理时，这使得 16 位存储更可取。 [下一页] 对于平坦法线，精益过滤给出的结果与我们的算法等效，但随着法线变得更陡，结果确实会发生偏差。 [下一页] 虽然 LEAN 过滤基于 Beckmann NDF，但它可以使用此方程进行调整以与基于 GGX 的 BRDF 一起使用，其中 sigma 是 Beckmann 粗糙度来自纸张使用的配方，而 alpha 是 GGX 粗糙度。这就是我们为下面的比较所做的。

---

## Slide 15

![Slide 15](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_015.png)

**📌 要点汇总**

- **LEADR映射演进**：基于LEAN映射，整合位移映射并全面考虑BRDF模型  
- **NDF与过滤方法**：采用Beckmann NDF及与LEAN一致的存储与过滤技术  
- **方法差异**：使用GGX NDF与Smith遮蔽项，引入基于SGGX的新过滤方案  
- **内容排除**：未涉及漫反射微面及位移贴图相关处理

> 2013 年的 LEADR 映射建立在 LEAN 映射的基础上， [下一页] 通过合并位移映射并考虑整个 BRDF，而不仅仅是正态分布函数。 [下一页] 它还使用 Beckmann NDF，以及与 LEAN 相同的存储和 NDF 过滤方法。 [下一页] LEADR 与我们的方法类似，不同之处在于我们使用 GGX NDF 和相关的 Smith 遮蔽项，并且我们使用基于 SGGX 的新方法 我将很快描述过滤方法。我们这里也不包括漫反射微面或位移贴图。

---

## Slide 16

![Slide 16](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_016.png)

**📌 要点汇总**

- **SGGX模型**：开发用于各向异性参与介质的微片分布表示  
- **分布扩展**：将GGX正态分布函数从半球域扩展至球域  
- **椭球体NDF**：通过热图可视化椭球体法

> 我简单介绍一下SGGX；它被开发为代表各向异性参与介质的微片分布。 [下一页] 它将GGX正态分布函数从半球域扩展到球域。 它描述了椭球体的 NDF；如果您要在右侧绘制动画椭圆体的法线密度，您将得到显示的热图 椭球体下方。 [下一页] SGGX 的另一个优点是 GGX 是一种特殊情况，这使得我们可以将其用于我们的应用程序，即表面着色。

---

## Slide 17

![Slide 17](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_017.png)

**📌 要点汇总**

- **S

> SGGX 的特点是 S 矩阵， [下一页] 其定义如下 [下一页] 其中 omega i 是椭球体的主轴（也是 S 的特征向量） [下一页] 而对角线上的项是特征值，也是每个轴上椭球投影面积的平方......

---

## Slide 18

![Slide 18](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_018.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> ...这可以在这里更好地看到。

---

## Slide 19

![Slide 19](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_019.png)

**📌 要点汇总**

- **GGX特例**：GGX是特定情况下的模型，具有独特的数学定义和应用限制。  
- **投影面积参数**：法线方向投影面积为1，切线方向为alpha_t，双切线方向为

> 正如我提到的，GGX 是一个特例， [下一页] 可以这样写 [下一页] 其中法线方向的投影面积定义为1，切线方向的投影面积为alpha_t， 双切线方向的投影面积为 alpha_b。值得注意的是，GGX 仅定义在该椭球体的上半部分。

---

## Slide 20

![Slide 20](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_020.png)

> 我们也可以写GGX [下一页] 在这种形式中，使用法线贴图后网格的切线空间（而不是各向异性切线和双切线向量），并旋转 各向异性基础合并到 2x2 左上子矩阵中。这样在存储方面更加紧凑，因为我们只需要存储这三个 子矩阵项。 [下一页] t_n 和 b_n 是法线贴图切线和双切线， [下一页] 而 n 是法线映射法线，它们一起形成正交基础。 [下一页] 这三项形成 2x2 对称 GGX 子矩阵，它编码各向异性粗糙度和方向。
>
> [补充说明] 这张幻灯片是对原始版本的更正，原始版本错误地使用了单位向量 i 和 j 而不是 t_n 和 b_n。

---

## Slide 21

![Slide 21](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_021.png)

> SGGX 论文描述了一种参数估计算法，该算法将任意 NDF 作为输入并生成具有以下内容的 SGGX NDF 属性： [下一页] 椭球体与输入 NDF 协方差矩阵的特征向量具有相同的轴 [下一页] 并且它保留了沿这些轴的微米薄片投影面积。这意味着如果算法给出 SGGX NDF 作为输入，它将返回相同的结果 中性纤维。在我们看来，这些似乎是 GGX 过滤算法所需要的属性。 [下一页] 作为示例，这里是一个输入 NDF，它是两个 SGGX NDF 的线性组合。 [下一页] 将参数估计算法应用于它会得到右侧的 NDF。 [下一页] 该论文表明，如果输入 NDF 是 SGGX NDF 的混合，那么对其 S 矩阵进行滤波通常会产生参数的良好近似值 估计。 [下一页] 线性滤波的结果如下所示；正如你所看到的，它与参数估计的结果非常接近。事实上，在很多情况下，比赛实际上是 准确。

---

## Slide 22

![Slide 22](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_022.png)

> 该动画显示了一个输入 NDF，它是两个 SGGX NDF 的混合，底部有三种不同的过滤方法。线性滤波和 在大多数情况下，参数估计匹配得非常接近，而精益过滤则差异更大。我要指出的第一个场景就在这里。

---

## Slide 23

![Slide 23](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_023.png)

**📌 要点汇总**

- **方法比较**：LEAN方法在处理偏离宏观法线的输入NDF时，比SGGX方法更易出现过度模糊现象。  
- **输入NDF结构**：由两个各向同性GGX分布（alpha_t=alpha_b=0.2）构成，与Z轴呈45度角。  
- **场景设定**：宏观表面法线指向球体中心，观察方向沿Z轴正方向。

> 由于输入 NDF 法线偏离宏观表面法线（这是球体的中心，因为我们直接向下看 Z 轴），LEAN 与基于 SGGX 的方法相比，倾向于过度模糊。这里，输入 NDF 由两个各向同性 GGX 分布 (alpha_t = alpha_b = 0.2) 组成 与 Z 轴成 45 度角。

---

## Slide 24

![Slide 24](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_024.png)

**📌 要点汇总**

- **输入NDF法线方向**：与Z轴成45度

> 在这种情况下，输入 NDF 法线仍与 Z 轴成 45 度，但它们是各向异性“纤维状”分布，其中 alpha_t = 1 (alpha_b = 0.2 和以前一样）。请注意，输入 NDF 围绕 Z 轴表现出对称性，这是通过线性滤波和参数估计捕获的，但不是通过 精益。

---

## Slide 25

![Slide 25](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_025.png)

> 我现在将描述我们的过滤和存储算法。 [下一页] 我们首先使用以下方程将法线和 2x2 各向异性 GGX 矩阵转换为 3x3 SGGX S 矩阵 S， [下一页] 其中M_n是将z轴旋转到n上的矩阵，这里给出仅供参考。

---

## Slide 26

![Slide 26](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_026.png)

**📌 要点汇总**

- **mipmap生成**：线性过滤S矩阵以生成mipmap层级  
- **矩阵处理**：提取过滤后S'的法线n'与2x2 GGX矩阵  
- **幂

> 然后我们在 mipmap 生成期间线性过滤 S 矩阵， [下一页] 然后对于每个过滤后的矩阵 S'，我们提取一个新的法线 n' 和新的 2x2 GGX 矩阵 [下一页] 我们使用幂迭代找到新的法线 n'，从沿 z 轴的单位向量开始，反复将其乘以 S' 并归一化，其中 收敛得非常快。
>
> [补充说明] 这张幻灯片是在原始版本的基础上进行更正的；原始幻灯片缺少第一个方程右侧的除法，这确保了 左侧矩阵的右下元素（对应于法线方向的投影面积）为 1。

---

## Slide 27

![Slide 27](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_027.png)

**📌 要点汇总**

- **纹理存储方案**：BC5存储法线，BC7存储2x2各向异性矩阵  
- **编码优化**：基于SGGX论文但采用2x2对称GGX矩阵替代3x3版本

> 我们将过滤后的法线存储在 BC5 纹理中，将 2x2 各向异性矩阵存储在 BC7 纹理中， [下一页] 使用这种编码，它基于 SGGX 论文建议的编码，但用于 2x2 对称 GGX 矩阵而不是 3x3 SGGX 矩阵。注意事项 这些分量的范围都在 0 到 1 之间。 [下一页] 这就是 aniso 贴图的样子；这是标题幻灯片中马的身体所使用的地图。

---

## Slide 28

![Slide 28](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_028.png)

**📌 要点汇总**

- **运行时纹理解码**：在着色器中实时解码纹理以确保动态效果  
- **非正定矩阵处理**：通过提取特征值限制范围避免硬件过滤导致的矩阵问题

> 然后我们在运行时在着色器中解码该纹理； [下一页] 我们需要注意的一件事是，纹理编码的硬件过滤可能会导致非正定矩阵，因此我们需要处理这个问题。 [下一页] 我们选择提取特征值和特征向量，这使我们能够将特征值限制在有效范围内。无论如何我们都需要这样做 因为我们需要特征向量来进行环境镜面反射近似，所以这不会产生显着的开销。 [下一页] 具体来说，我们计算 alpha_t^2、alpha_b^2、alpha_t 和 alpha_b 的乘积，以及正切和双切线，用于此处所示的 NDF， 以及阴影屏蔽功能。
>
> [补充说明] 该 NDF 是各向异性 GGX，从其他来源（例如 Burley 2012）稍微重新排列，因为分子和分母已乘以 (alpha_t * alpha_b)^4，消除一些除法。

---

## Slide 29

![Slide 29](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_029.png)

> 这是我们用来解码纹理样本的着色器代码 [下一页] 该函数获取纹理样本以及法线贴图切线和双切线，并返回我们需要的各向异性镜面数据。 [下一页] 该值用于将 alpha 值限制为至少与对应于最大光泽度值的 alpha 值一样大（其中光泽度为 1.0） 几乎完全平滑，对应的 alpha 值约为 0.001）。 [下一页] 然后我们反转纹理编码以提取 Sxx、Sxy 和 Syy 值； [下一页] 由于我们正在求解 2x2 矩阵的特征值，因此我们正在求解二次方程，这是判别式的 sqrt 及其倒数。 [下一页] 然后，我们求解 alpha_t 平方和 alpha_b 平方，同时钳位在 alpha_min 平方和 1 之间，并计算 alpha_t 和 alpha_t 的乘积 阿尔法_b [下一页] 然后我们计算各向异性旋转角度的余弦和正弦 [下一页] 并用它们来计算各向异性正切和双切线。

---

## Slide 30

![Slide 30](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_030.png)

**📌 要点汇总**

- **自定义节点**：艺术家使用自定义Substance Designer节点创作aniso贴图  
- **输入参数**：节点以两个光泽贴图和方向图作为输入  
- **方向图来源**：方向图通过Substance Painter绘制流程图生成  
- **编码输出**：节点基于先前描述的编码逻辑生成aniso贴图

> 在创作我们的 aniso 贴图时，我们的艺术家使用了自定义的 Substance Designer 节点， [下一页] 它以两个光泽贴图作为输入 [下一页] 加上方向图 [下一页] （通过在 Substance Painter 中绘制流程图创作）； [下一页] 该节点使用我们之前描述的编码输出 aniso 图。

---

## Slide 31

![Slide 31](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_031.png)

> 现在我将展示一些结果，将我们基于 SGGX 的过滤与 LEAN 过滤进行比较

---

## Slide 32

![Slide 32](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_032.png)

**📌 要点汇总**

- **各向同性GGX镜面反射**：地面实况图像采用各向同性GGX模型实现镜面反射效果，未引入其他反射特性。  
- **法线贴图驱动各向异性**：图像中观察到的各向异性效果完全由法线贴图生成，而非材质本身的物理属性。  
- **高采样密度渲染**：每个像素使用256个样本进行着色，显著提升渲染精度但可能增加计算成本。

> 这是地面实况图像，仅使用各向同性 GGX 镜面反射；各向异性纯粹来自法线贴图。使用 256 个样本进行着色 每个像素。

---

## Slide 33

![Slide 33](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_033.png)

**📌 要点汇总**

- **SGGX过滤应用**：基于SGGX

> 我们基于 SGGX 的过滤给出了这个结果，它给出了宽度大致相同的突出显示[来回翻转几次]。主要区别 发生在掠射角。

---

## Slide 34

![Slide 34](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_034.png)

> 精益过滤给出了这个结果，它比地面实况或 SGGX 具有更广泛的亮点。

---

## Slide 35

![Slide 35](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_035.png)

> 这是与之前相同的场景，但减少了曝光以避免剪切高光。

---

## Slide 36

![Slide 36](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_036.png)

> 与地面真实情况相比，SGGX 高光的亮度仅略有降低......

---

## Slide 37

![Slide 37](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_037.png)

**📌 要点汇总**

- **精益高光**：整体亮度显著下降，影响视觉表现  
- **高光最亮部分**：亮度衰减最明显，可能引发技术缺陷  
- **性能问题**：高光区域处理存在明显不足，需优化

> ...而精益高光明显变暗，尤其是在高光最亮的部分。

---

## Slide 38

![Slide 38](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_038.png)

**📌 要点汇总**

- **mip级别增加**：展示各向异性贴图在不同mip层级下的行为变化  
- **明暗稳定性**：贴图在多尺度下保持明暗对比的稳定性  
- **外观一致性**：各向异性贴图在不同尺度下整体外观无明显差异  
- **多尺度表现**：贴图行为在多个尺度上均保持视觉一致性  
- **技术验证**：通过视频验证

> 该视频展示了随着 mip 级别的增加，我们的各向异性贴图的行为方式。明暗相当稳定，外观总体保持一致 在多个尺度上。

---

## Slide 39

![Slide 39](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_039.png)

**📌 要点汇总**

- **纹理编码限制**：未直接插值S矩阵值可能导致伪影，但现实

> 这种方法有一些限制，主要与纹理编码有关。由于我们没有直接对 S 矩阵值进行插值，因此可以 导致伪影。实际上，对于现实世界的材质，我们没有遇到任何问题——限制 alpha 值似乎在这里效果很好。 [下一页] 当使用大、小 alpha_t 和 alpha_b 值的组合时，可能会出现精度问题，从而导致伪影；我将用一个例子来演示。

---

## Slide 40

![Slide 40](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_040.png)

> 此处，使用 alpha_t 为 0.29 和 alpha_b 为 0.04 时，没有任何伪影。

---

## Slide 41

![Slide 41](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_041.png)

> 如果我们将 alpha_t 增加到 0.87，保持 alpha_b 恒定，我们会看到一些伪影， [下一页] 此处放大显示。

---

## Slide 42

![Slide 42](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_042.png)

> 如果 alpha_b 从 0.04 增加到 0.1，这些伪影就会消失。在实践中，我们没有遇到这些现实世界材料的工件，所以我们没有花费 任何时候试图解决这个问题，但这是需要注意的事情。

---

## Slide 43

![Slide 43](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_043.png)

**📌 要点汇总**

- **SGGX过滤方法**：实现简单，参数与

> 总之，我提出了一种新的基于 SGGX 的过滤方法 [下一页] 实施起来很简单； [下一页] 它具有与 LEAN 相同数量的参数； [下一页] 并且具有大致相同的着色成本； [下一页] 并且对于具有强法线和高度各向异性 NDF 的情况产生了良好的结果。 [下一页] 我还展示了基于 SGGX 编码的各向异性粗糙度的新纹理编码 [下一页] 它与 BC7 压缩配合良好，生成的纹理大小为 LEAN 编码大小的 1/4 到 1/8，具体取决于所使用的位深度。
>
> [补充说明] 这些发展或多或少是相互正交的。即，可以在我们的编码中使用精益过滤方法，或者反之 反之亦然。

---

## Slide 44

![Slide 44](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_044.png)

> 接下来，我将讨论我们新的各向异性粗糙散射 BRDF。

---

## Slide 45

![Slide 45](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_045.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 因为那是一口 [下一个]x5

---

## Slide 46

![Slide 46](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_046.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

---

## Slide 47

![Slide 47](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_047.png)

**📌 要点汇总**

- **各向异性模糊性**：Sucker Punch 术语，描述光照下表面模糊特性差异  
- **模糊效果示例**：通过桃子与油桃对比展示不同材质的模糊表现  
- **亮度均匀性对比**：桃子正面光照更均匀，油桃因朗伯衰减呈现明显明暗差异

> 我将其称为各向异性模糊性或模糊性，这就是我们在 Sucker Punch 中所说的。 [下一页] 这里我们有一个关于模糊效果的典型例子，桃子与油桃， [下一页] 很明显，与具有强烈朗伯衰减的油桃相比，正面照明时桃子的亮度更加均匀。

---

## Slide 48

![Slide 48](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_048.png)

> 这个新的 BRDF 是在外观开发过程中研究的，

---

## Slide 49

![Slide 49](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_049.png)

> 在项目的那个阶段，早在 2015 年初， [下一页] 真实的天鹅绒，包括压碎的天鹅绒所表现出的各向异性行为，很重要，尽管项目设置的变化意味着天鹅绒 类似的材料并没有出现在运输游戏中。 [下一页] 该 BRDF 在 Ghost 中用于其他材质，例如苔藓、毛毡、马衣和一些布料。

---

## Slide 50

![Slide 50](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_050.png)

**📌 要点汇总**

- **旧模型不足**：临时旧模型未达Ghost质量标准，需改进。  
- **逆高斯模型**：2013年课程中Neubelt与Pettineo提出基于microfacet框架的模型。  
- **模糊性建模**：Koenderink与Pont论文提出薄单散射层叠加传统基层方法。  
- **各向异性需求**：现有模型不支持各向异性，影响碎天鹅绒等材质的准确再现。  
- **自研BRDF**：为满足各向异性需求，团队决定开发全新BRDF模型。

> 就之前的工作而言，我们有一个临时的旧模型，没有达到我们希望使用 Ghost 实现的质量标准。 [下一页] 在 2013 年的这门课程中，Neubelt 和 Pettineo 展示了他们的模型，这是一种逆高斯模型，是使用 microfacet 框架导出的。 [下一页] 引起我们注意的一篇论文是 Koenderink 和 Pont 于 2002 年发表的“The Secret of Velvety Skin”；它将模糊性建模为薄的单散射层 在传统的基层之上。 [下一页] 但现有模型都不支持各向异性，而这对于准确再现碎天鹅绒等材料是必要的，因此我们决定开发 我们自己的 BRDF。

---

## Slide 51

![Slide 51](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_051.png)

**📌 要点汇总**

- **模型扩展**：基于Koenderink

> 我们的模型基于 Koenderink 和 Pont 的模型， [下一页] 并扩展以支持各向异性，通过对基础层进行遮蔽以节省能量。我们还导出了一种适合与球形一起使用的形式 谐波照明，即我们用于漫射间接照明的照明。这确保了外观在所有照明场景中保持一致。 [下一页] 这是模型的示意图；我们有一个传统的基础层，顶部有一个厚度为 delta 的散射层，表面法线为 n； [下一页] u 为光线方向； [下一页] p是相位函数； [下一页] v 是视图方向； [下一页] 如果 lambda 是平均自由程， [下一页] 然后我们将 d 定义为 delta 与 lambda 的比值，我们称之为密度，并且假设它远小于 1。

---

## Slide 52

![Slide 52](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_052.png)

**📌 要点汇总**

- **BRDF公式**：散射层的BRDF表达式包含反照率c_f参数  
- **各向同性散射特性**：相位函数恒定，BRDF余弦项曲线呈橙色，与蓝色

> 在这些假设下， [下一页] 散射层的 BRDF 如下所示， [下一页] 其中 c_f 是散射层的反照率。 [下一页] 在各向同性散射情况下，相位函数恒定，BRDF 乘以余弦项的图看起来像橙色曲线；的 蓝色虚线曲线是余弦波瓣。需要注意的一件事是，这条曲线在整个半球上几乎是恒定的。我们稍后会用到它。
>
> [补充说明] 单击左下角的图表打开交互式版本，或使用以下 URL：https://www.desmos.com/calculator/icwwbkbtkw

---

## Slide 53

![Slide 53](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_053.png)

> 散射的幅度也非常依赖于观察方向，这可以在此处看到，并且与我们观察到的材料相匹配 像天鹅绒。

---

## Slide 54

![Slide 54](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_054.png)

> 在他们的论文中，Koenderink 和 Pont 展示了黑色天鹅绒的散射图，如下所示：

---

## Slide 55

![Slide 55](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_055.png)

**📌 要点汇总**

- **后向散射波瓣强度**：具有显著的后向散射波瓣特征  
- **前向散射波瓣**：前向散射波瓣相对较小  
- **相位函数研究**：旨在寻找能重现波瓣特性的相位函数

> 它有很强的后向散射波瓣 [下一页] 和一个较小的前向散射波瓣； [下一页] 我们想尝试找到一个可以重现这一点的相位函数。

---

## Slide 56

![Slide 56](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_056.png)

**📌 要点汇总**

- **Schlick近似改进**：基于Kajiya-Kay模型，将相函数改为依赖半矢量

> 我们从 Henyey-Greenstein 相函数的 Schlick 近似开始， [下一页] 并且，受 Kajiya-Kay 头发渲染模型的启发，我们对其进行了修改，使其依赖于半矢量与纤维之间角度的正弦 方向t。这破坏了相位函数的标准化，因此我们添加了一个额外的项 r 来纠正这一点。由于我们没有找到解析形式 为此，我们使用了近似且保守的形式，这导致了一些能量损失。
>
> [补充说明] 我们将 Schlick k 作为“Spread”参数公开，其中 k = -0.99 * (1.0 - spread)。

---

## Slide 57

![Slide 57](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_057.png)

> 在 BRDF 中使用这个新的相位函数， [下一页] 我们得到一个看起来像这样的散射图， [下一页] 其基本形状与天鹅绒散射图相同。
>
> [补充说明] 单击图表打开交互式版本，或使用以下 URL：https://www.desmos.com/calculator/hwp7tga0vk

---

## Slide 58

![Slide 58](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_058.png)

**📌 要点汇总**

- **Schlick k参数动画**：调整Schlick k参数可显著改变3D渲染中的光线散射效果  
- **极角与方位角配置**：光纤及视角的极角、方位角参数直接影响光线分布与视觉表现  
- **切向散射现象**：多种配置下均出现强烈切向散射，需注意其对渲染真实感的影响  
- **标准化幅度差异**：图表虽

> 在 3D 中它看起来像这样， [下一页] 如果我们为 Schlick k 参数设置动画，效果如下： [下一页] 光纤极角， [下一页] 视角极角， [下一页] 和视角方位角。 请注意许多配置中的强烈切向散射。另请注意，这些图具有标准化幅度；实际上它们的规模发生了变化 相当大。

---

## Slide 59

![Slide 59](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_059.png)

> 在最近的工作中，在发布 Ghost 后，我们想尝试解决能量损失问题，因此我们决定不使用基于 Schlick 的相位函数 尝试类似光纤的 SGGX 相位函数， [下一页] 具有分析标准化。 [下一页] 相位函数由两部分组成；第一个是此处显示的 NDF。 Alpha 是 GGX 粗糙度，或微米薄片的投影面积 纤维方向t；垂直于 t 的投影面积为 1，这使其成为“纤维状”分布。 [下一页] 相位函数中的第二项是微米薄片在光方向 u 上的投影面积，由此给出。 [下一页] 相位函数就是 NDF 除以四倍投影面积。
>
> [补充说明] 就着色器代码而言，这与前一阶段函数的成本大致相同。我们使用以下方法从着色器“spread”参数计算 alpha： 阿尔法 = sqrt(传播) * 0.85 + 0.15, 与基于 Schlick 的相位函数相比，它给出了类似的响应。

---

## Slide 60

![Slide 60](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_060.png)

> 使用此相位函数的散射图如下所示，比 Schlick 版本稍有斑点，但仍然具有很强的后向散射 具有较小前向散射分量的分量。实际上，它们在外观上非常相似，但由于精确的原因，SGGX 稍微亮一些。 节约能源。
>
> [补充说明] 单击图表打开交互式版本，或使用以下 URL：https://www.desmos.com/calculator/botqtjpnus

---

## Slide 61

![Slide 61](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_061.png)

**📌 要点汇总**

- **3D可视化**：通过动态展示光纤参数在三维空间中的表现形式  
- **参数动画**：基于纤维投影面积对关键参数进行动态调整与演示  
- **角度参数**：涉及光纤极角、视角极角

> 在 3D 中它看起来像这样， [下一页] 再次从纤维投影面积开始对参数进行动画处理， [下一页] 光纤极角， [下一页] 视角极角， [下一页] 和视角方位角。请注意，与我们基于 Schlick 的模型相比，当光与光纤方向对齐时，会有更强的反射。

---

## Slide 62

![Slide 62](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_062.png)

**📌 要点汇总**

- **光传输概率**：P_p表示光线穿透散射层到达基础层的概率  
- **反射路径概率**：P_e描述基础层反射光沿特定方向穿透散射层的概率  
- **散射方向控制**：P_s与相位函数积分相关，决定光线是否朝向基础层散射  
- **BRDF作用**：散

> 为了节省能量，我们需要考虑有多少入射光传输到基础层，以及有多少光散射在基础层上。 朝着眼睛的方向。 [下一页] 我们只考虑这里的主要相互作用； [下一页] 要考虑的第一项是光线穿过散射层到达基础层的概率；我们称其为 P_p，由此给出； [下一页] 由基础层反射的光线沿 v 方向穿过散射层的概率由下式给出；我们称之为 P_e； [下一页] 最后，我们将 P_s 称为被散射层散射的光线朝基础层散射而不是远离材料的概率。是平等的 一减去半球上相位函数的积分。远离材料散射的光线由散射层负责 双向反射分布函数；这是剩下的部分。

---

## Slide 63

![Slide 63](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_063.png)

**📌 要点汇总**

- **基础层衰减因子公式**：由P_p、P_s、P_e三部分概率相乘构成，反映光线穿透与散射过程  
- **P_s近似处理**：因无解析解，需通过曲线拟合确定常数c_i进行近似计算  
- **运行时优化**：近似函数需在着色器

> [下一页] 我们可以将这三项组合成一个基础层衰减因子，它等于 [下一页] P_p，渗透到基层的概率，加上纤维颜色乘一减去P_p， [下一页] 乘以 P_s，向下分散到基础层的概率， [下一页] 全部乘以 P_e，即沿 v 方向穿过散射层向眼睛逃逸的概率。 [下一页] 不幸的是，P_s 没有解析表达式， [下一页] 因此我们使用以下近似值，其中常数 c_i 使用曲线拟合确定。
>
> [补充说明] P_s(u) 的这种近似必须在运行时（在着色器中）进行评估，因此它需要相对便宜。这些 c_i 也取决于 Schlick k （或 GGX alpha），以及光纤倾斜角。我们进一步将曲线拟合到曲线常数，以降低着色器编译时的计算成本）；一个 也可以使用 LUT。详情请参阅补充材料。

---

## Slide 64

![Slide 64](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_064.png)

**📌 要点汇总**

- **各向异性可见性**：确保间接照明下各向异性特性持续可见，需特殊处理。  
- **球谐照明与反射探头**：采用该技术组合实现间接光照

> 我们希望各向异性在间接照明下继续可见； [下一页] 对我们来说，这意味着球谐照明 + 反射探头。 [下一页] 我们的 BRDF 渲染方程如下所示，其中蓝色框中的项与我们之前看到的各向同性散射图成正比。

---

## Slide 65

![Slide 65](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_065.png)

> 我们称之为 g；回想一下，它在整个半球上几乎是恒定的， [下一页] 所以我们要近似积分 [下一页] 将 g 取出并乘以它 [下一页] 半球的平均值；即 g 在半球上的积分除以两个 pi。

---

## Slide 66

![Slide 66](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_066.png)

> [下一页] 我们再次做同样的事情，假设 L_i 近似恒定， [下一页] 所以我们把它从积分中取出来 [下一页] 并再次乘以半球的平均值。

---

## Slide 67

![Slide 67](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_067.png)

**📌 要点汇总**

- **半球积分近似**：G~通过曲线确定常数，用于g的积分近似  
- **SH系数计算间接光**：半球平均

> 所以我们剩下三个积分； [下一页] 第一个，g 在半球上的积分，可以通过这个表达式很好地近似，我们称之为 G~，常数再次使用曲线确定 装修； [下一页] 第二个积分是半球间接光的平均值，很容易从 SH 系数计算出来； [下一页] 最后一项，即半球上相位函数的积分，是 1 减去我们之前看到的 P_s 函数，这次在视图中计算 方向。该术语负责各向异性响应。
>
> [补充说明] 有关第一个积分的近似形式的详细信息，请参阅补充材料。
>
> 对于第二个积分，如果我们从 SH 系数开始直接评估（余弦加权）辐照度，如 [RH01a] 所示，则 SH 系数 通过将前三个 SH 波段分别乘以 1/pi、3/(4*pi) 和 0 即可获得半球上的平均亮度的近似值。

---

## Slide 68

![Slide 68](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_068.png)

**📌 要点汇总**

- **环境漫射光辐照度**：E_p和E_s分别表示穿透与散射至基层的光辐照度，受散射层概率影响。  
- **基础层亮度公式**：L_{d,o}由逃逸概率、朗伯BRDF、E_p与E_s之和共同决定。  
- **E_p与E_s的积分计算**：E_p依赖穿透概率积分与亮度余弦项，E_s涉及纤维反照率与散射概率积分。  
- **散射层概率模型**：P_p积分描述光穿透与散射概率，影响基层辐照度与亮度计算。  
- **反照率作用机制**

> 同样，为了节省能量，我们需要考虑散射层对基础层的环境阴影。我们首先考虑环境漫射光 仅。 [下一页] 定义以下术语： E_p是透过散射层到达基层的光的辐照度 E_s 是被散射层向基层散射的光的辐照度 c_b 是基础层的漫反射反照率 L_{d,o} 是由于环境漫射光而沿视图矢量看到的基础层的亮度 [下一页] L_{d,o} 由以下方程给出， [下一页] 即 P_e 的乘积，沿 v 穿过散射层逃逸的概率， [next] 乘以朗伯 BRDF，[next] 乘以辐照度值 E_p [next] 和 E_s 之和。 [下一页] E_p 由该方程给出， [下一页] 即 P_p 的乘积在半球上的积分，穿透散射层的概率， [next] 乘以 u 方向上的亮度，[next] 乘以余弦项。 [next] 同样，E_s 由该方程给出，[next] 是纤维反照率 [next] 乘以 1 - P_p 的乘积在半球上的积分，即被散射层散射的概率， [next] 乘以向基础层散射的概率，[next] 乘以 u 方向上的亮度， [next] 乘以余弦项。

---

## Slide 69

![Slide 69](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_069.png)

> 首先，我们将考虑 E_p 的表达式，即穿透散射层的辐照度。 [下一页] 我们将通过假设 L_i 是常数来进行近似， [下一页] 并将积分分解为 [下一页] 半球上 P_p 的余弦加权平均值的乘积， [下一页] 以及表面的辐照度。

---

## Slide 70

![Slide 70](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_070.png)

**📌 要点汇总**

- **曲线拟合近似**：使用曲线拟合方法近似第一个

> [下一页] 我们使用曲线拟合来近似第一个积分，我们称之为 Q~， [下一页] 而第二个积分就是简单的 E，即表面的辐照度，可以根据标准 SH 系数计算，如 [RH01a] 中所示。
>
> [补充说明] 有关第一个积分的近似形式的详细信息，请参阅补充材料。

---

## Slide 71

![Slide 71](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_071.png)

**📌 要点汇总**

- **E_s定义**：基础层辐照度由散射引起，需通过特定方程近似计算。  
- **余弦加权平均**：分散概率与向基础层散射概率均采用余弦加权平均处理。  
- **公式组合**：

> 现在我们将考虑 E_s，即由于散射而导致的基础层上的辐照度。 [下一页] 使用这个方程近似它，即纤维颜色时间 [下一页] 分散概率的余弦加权平均值， [下一页] 乘以向基础层散射的概率的余弦加权平均值， [下一页] 乘以表面的辐照度。 [下一页] 请注意，这对于各向同性散射和均匀照明来说是准确的。

---

## Slide 72

![Slide 72](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_072.png)

**📌 要点汇总**

- **第一个积分表达式**：1 - Q~

> [下一页] 第一个积分就是 1 减去 Q~，这是我们之前为 E_p 近似中的第一个积分开发的两张幻灯片的表达式； [下一页] 第二个积分对于恒定扩散（即 Schlick k 或 GGX α）和光纤倾斜是恒定的，因此可以进行数值评估； [下一页] 而最后一个积分又是表面的辐照度，我们在两张幻灯片前也看到过。
>
> 现在，我们拥有了计算由于环境漫射照明而导致的基础层亮度所需的所有部分，并通过散射层进行阴影处理 考虑到。
>
> [补充说明] 有关我们如何计算第二个积分的详细信息，请参阅补充材料。

---

## Slide 73

![Slide 73](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_073.png)

> 将 E_p 和 E_s 的近似值结合到 L_{b,o} 的方程中，我们可以导出漫反射环境衰减的表达式 c_atten 此处给出的散射层照明。

---

## Slide 74

![Slide 74](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_074.png)

**📌 要点汇总**

- **镜面阴影处理**：借鉴漫反射阴影方法简化

> 为简单起见，我们以与漫反射环境阴影类似的方式处理镜面环境阴影， [下一页] 用过滤后的反射探针样品替换用于评估辐照度的 SH 样品。 [下一页] 因此，我们使用针对漫射环境照明导出的相同衰减项，这避免了额外的运行时间成本。

---

## Slide 75

![Slide 75](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_075.png)

**📌 要点汇总**

- **BRDF简化版本**：Eric Wohllaib实现简化BRDF

> 对马岛的世界绿意盎然，郁郁葱葱，有许多长满青苔的岩石和建筑物，以及其他毛茸茸的材料，例如用于制作毛毡的毛毡。 蒙古包，因此我们的渲染程序员之一 Eric Wohllaib 实现了 BRDF 的简化版本以实现延迟着色。 [下一页] 它有一个单一的参数，一个7位的模糊值； [下一页] 所有其他参数全局设置如下： [下一页] 密度为0.5，相当高； [下一页] “散布”是 0.9，几乎是均匀的，事后看来我们可以使用均匀散布并保存一些指令； [下一页] 纤维方向设置为顶点法线（尽管由于分布较大，影响很小）； [下一页] 纤维反照率固定为漫反射反照率的五倍。 [下一页] 出于性能原因，我们没有包含基础层阴影， [下一页] 但我们混合使用了 Lambertian 和模糊 BRDF；由于每种物质本身都守恒能量，因此混合物也是守能量的。

---

## Slide 76

![Slide 76](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_076.png)

**📌 要点汇总**

- **顶点法线倾斜**：通过调整顶点法线方向，实现散射层外观的平滑处理。  
- **顶点法线不一致**：环境艺术资源的顶点法线差异过大，需额外处理以适配着色需求。  
- **节能包裹照明**：采用该技术优化光照计算，进一步软化散射层视觉效果。  
- **mipmap法线混合**：低分辨率mipmap

> 在前向着色版本中，我们通过允许法线向顶点法线倾斜来平滑散射层的外观。 [下一页] 对于我们的环境艺术资源，顶点法线太不一致，无法直接用于着色， [下一页] 所以我们使用节能包裹照明 [下一页] 这有助于软化散射层的外观。
>
> [补充说明] 对于某些资源，通过与使用法线贴图的较低分辨率 mipmap 计算的法线混合来平滑法线可提供更好的结果 而不是与顶点法线混合。

---

## Slide 77

![Slide 77](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_077.png)

> 我现在将展示一些结果。在其最终形式中，Ghost 没有任何充分利用 BRDF 功能的压碎的天鹅绒状材料； [下一页] 为了演示，我通过修改马着色器创建了一匹柔软的马。 [下一页] 请注意，这些结果使用新的 SGGX 阶段，这不是 Ghost 中附带的， [下一页] 尽管结果在质量上非常相似。 [下一页] 请原谅程序员的艺术！

---

## Slide 78

![Slide 78](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_078.png)

> 您可以在阴影一侧看到材料的各向异性行为仍然可见； 作为参考，该材料使用密度 0.2、扩展 0.2，对应于 0.53 的 GGX alpha、23 度的光纤极角和噪声 纤维方向图。

---

## Slide 79

![Slide 79](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_079.png)

> 让我来分解一下；这里我们只有基础层，没有散射层

---

## Slide 80

![Slide 80](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_080.png)

> 如果我们添加没有基础层衰减的散射层，它看起来像这样；

---

## Slide 81

![Slide 81](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_081.png)

**📌 要点汇总**

- **基础层衰减设置**：定义P_s时假设散射光分数为0，影响基础层表现  
- **材料颜色特征**：终止线区域颜色更深，与衰减参数相关  
- **阴影面各向异性**：P_s为0导致阴影面无方向性反射特性  
- **原始版本错误**：幻灯片曾误将P_s设置为1

> 添加基础层衰减（但在定义 P_s 时，假定向基础层散射的散射光的分数等于 0）， 看起来像这样；请注意，材料颜色较深，尤其是沿着马脖子上可见的终止线。 【来回翻动几次】 由于P_s为0，阴影面没有任何各向异性；
>
> [补充说明] 该幻灯片的原始版本错误地指出 P_s 在此设置为 1。

---

## Slide 82

![Slide 82](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_082.png)

**📌 要点汇总**

- **实现P_s**：通过特定算法实现P_s，是构建BRDF模型的关键步骤。  
- **BRDF结果**：最终获得的BRDF与视频中展示的反射特性完全一致。  
- **验证一致性**：通过视频对比验证BRDF的准确性，确保模型可靠性。

> 实现 P_s 得到最终的 BRDF，与视频中显示的相同。

---

## Slide 83

![Slide 83](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_083.png)

> 这是各种模型参数的影响；首先我们改变密度； [下一页] 然后是纤维颜色值或亮度； [下一页] 纤维颜色饱和度； [下一页] 点差（对应于 GGX alpha） [下一页] 最后是纤维极角，左边的纤维笔直向上，而右边的纤维平放在表面上。

---

## Slide 84

![Slide 84](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_084.png)

> 这是显示延迟版本的示例；这是带着它的，

---

## Slide 85

![Slide 85](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_085.png)

> 这仅使用朗伯漫反射。 [来回切换几次]

---

## Slide 86

![Slide 86](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_086.png)

> 这是一个显示阴影区域的特写镜头，该区域也保留了模糊的外观。

---

## Slide 87

![Slide 87](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_087.png)

> 与朗伯漫反射。 [来回切换几次]。

---

## Slide 88

![Slide 88](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_088.png)

**📌 要点汇总**

- **各向异性模糊BRDF**：提出新型BRDF模型，提升材质渲染精度  
- **碎天鹅绒外观再现**：支持直接/间接光照下的复杂材质视觉效果  
- **PS4硬件兼容性**：低成本实现高性能渲染，适配主流游戏主机

> 总之，我提出了一种新的各向异性模糊 BRDF， [下一页] 它能够在直接和间接光线下再现碎天鹅绒等材料的外观， [下一页] 而且价格便宜，足以在 PS4 硬件上使用。

---

## Slide 89

![Slide 89](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_089.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 接下来，我将讨论皮肤着色以及我们在那里所做的改进。

---

## Slide 90

![Slide 90](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_090.png)

> 自臭名昭著的次子以来，我们一直在使用预集成的皮肤着色， [下一页] 它使用 LUT 来计算次表面散射；例如，对于准时光源，它使用由光源之间角度的余弦参数化的 LUT 一个轴上的光和表面法线，另一轴上的曲率 kappa（曲率半径的倒数）。
>
> [补充说明] 我们使用预集成的皮肤着色而不是屏幕空间技术，因为它非常适合我们现有的照明管道，并且不需要任何 额外的 G 缓冲区存储。我们的皮肤着色器还支持“茬”功能，该功能也需要前向着色，因此合并预着色是有意义的 将皮肤着色集成到该通道中。我们的艺术家还编写了自定义散射配置文件来模拟除 人类皮肤，这对于屏幕空间技术来说会更加困难。

---

## Slide 91

![Slide 91](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_091.png)

> 值得重新审视这个 LUT 背后的假设，因为很容易出错。 [下一页] 在本文中，积分是在“环”上执行的，如下所示，我们针对不同的曲率和光角度对 theta 进行积分，

---

## Slide 92

![Slide 92](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_092.png)

**📌 要点汇总**

- **圆柱体模型**：采用圆柱体模拟皮肤的2D表面以优化建模过程  
- **光方向曲率**：优先关注光传播方向的曲率而非平均曲率  
-

> 但最好将其视为在圆柱体上执行，该圆柱体具有类似于我们正在建模的皮肤的 2D 表面。 [下一页] 从这个角度来看，我们注意到两件事： [下一页] 首先，我们想要的是光方向上的曲率，而不是平均曲率； [下一页] 我们还需要注意我们使用的散射剖面。

---

## Slide 93

![Slide 93](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_093.png)

**📌 要点汇总**

- **径向轮廓**：通过点光源测量散射光获得，用于球体积分。  
- **线性轮廓**：基于无限线性光源，适用于圆柱轴对称积分。  
- **对称性影响**：圆柱轴

> [下一页] 该方程中的散射剖面为 R； [下一页] 在文献中，您通常会看到径向轮廓，这是通过将亮光照射在一个点上并测量散射光来获得的。 [下一页] 您可以使用的另一种类型的轮廓是线性轮廓，如果您使用无限线性光源，就会得到这种轮廓。 [下一页] 由于沿圆柱轴的对称性，在环上积分时应使用线性轮廓， [下一页] 这可以通过预先整合部首轮廓来获得。
>
> [补充说明] 请注意，针对 SH 纬向谐波进行积分时。你想使用径向轮廓，并在球体上积分——圆柱体不是根本性的 对称！

---

## Slide 94

![Slide 94](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_094.png)

**📌 要点汇总**

- **方向曲率**：需关注方向曲率而非仅平均曲率，以更精确描述曲面特性  
- **曲率张量与主方向**：通过曲率张量（第二基本形式）计算主方向（d1/d2）及对应主曲

> 我们提到的另一件事是我们需要方向曲率，而不仅仅是平均曲率。 [下一页] 我们可以使用曲率张量计算方向曲率，也称为第二基本形式，或简称为“二”。 d1 和 d2 是主要的 方向，而 kappa1 和 kappa2 是相应的主曲率。 [下一页] 特定方向 l（“ell”）上的曲率由这个简单的公式给出。

---

## Slide 95

![Slide 95](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_095.png)

**📌 要点汇总**

- **曲率存储优化**：将平均曲率存储于

> 由于曲率张量是对称的 2x2 矩阵， [下一页] 我们可以将其加上用于环境照明的平均曲率存储在 4 字节顶点通道中。 [下一页] 我们使用 Rusinkiewicz 在 2004 年的论文中描述的算法计算切线空间曲率张量作为预处理。 [下一页] 我们发现有必要模糊所得的曲率张量，以平滑孤立顶点（例如嘴角或嘴角）处的非常高的曲率。 眼睛周围。我们在与次表面散射发生的比例相似的比例上进行模糊处理，这给出了良好的结果。当在这里模糊曲率时，它是 将负凹曲率限制为零很重要，这样凹区域就不会“抵消”附近的凸曲率。

---

## Slide 96

![Slide 96](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_096.png)

> 为了计算网格的曲率张量，我们首先计算每个面的曲率张量， [下一页] 这是使用具有以下约束的最小二乘法完成的。未知数是左侧对称 2x2 曲率张量的三个分量。 [下一页] 一旦我们有了这些，我们就将面张量组合到顶点上；我会请您参阅该论文以了解详细信息。

---

## Slide 97

![Slide 97](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_097.png)

> 我现在将展示一些之间的比较 [下一页] 无曲率， [下一页] 平均曲率， [下一页] 和方向曲率。

---

## Slide 98

![Slide 98](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_098.png)

> 这是到处曲率为零的结果，

---

## Slide 99

![Slide 99](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_099.png)

> 这是平均曲率的结果

---

## Slide 100

![Slide 100](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_100.png)

> 这是使用方向曲率时的结果。

---

## Slide 101

![Slide 101](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_101.png)

**📌 要点汇总**

- **调整环境设置**：关闭环境照明并调整曝光、色调映

> 由于在那里很难看到效果，因此我将在关闭环境照明并调整曝光和色调映射的情况下再次显示相同的内容，以使 散射更加明显。再说一次，这不是曲率，

---

## Slide 102

![Slide 102](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_102.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 平均曲率，

---

## Slide 103

![Slide 103](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_103.png)

> 和方向曲率。

---

## Slide 104

![Slide 104](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_104.png)

**📌 要点汇总**

- **定向曲率 vs 平均曲率**：鼻梁定向曲率导致更多散射，因光线方向与曲率方向一致  
- **鼻孔散射差异**：定向曲率减少垂直光方向的不自然散射，优于平均曲率  
- **嘴唇散射优化**：定向曲率显著降低平均曲率下出现的远距离散射现象  
-

> 在顶部，我们有用于着色的相应曲率值；我将在这里指出一些差异。 [下一页] 在鼻梁上，使用定向曲率时会出现更多散射，因为光线来自侧面，曲率最高 朝那个方向。 [下一页] 而鼻孔上的散射较少，因为曲率主要垂直于光方向。使用定向散射可以减少 使用平均曲率时我们看到的不自然散射。 [下一页] 类似地，当使用平均曲率时，嘴唇也具有非常远距离的散射，而当使用方向曲率时，这种散射会减少。

---

## Slide 105

![Slide 105](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_105.png)

**📌 要点汇总**

- **光线传播特性**：光线几乎笔直向下，体现特定传播路径特征  
- **平均曲率影响**：使用平均曲率时，脸颊区域出现远距离散射现象  
- **方向曲率优化**：采用方向曲率后，散射范围显著缩小至更真实水平

> 这是另一个例子，光线几乎笔直向下； [下一页] 在这里，当使用平均曲率时，我们看到沿着脸颊的远距离散射， [下一页] 当使用方向曲率时，它会减少到更真实的范围。

---

## Slide 106

![Slide 106](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_106.png)

**📌 要点汇总**

- **参数需求**：计算方向曲率需切线、双切线、曲率张量及光线方向作为输入参数。  
- **投影优化**：跳过光线方向标准化投影，因对LUT影响可忽略，优化计算效率。  
- **曲率生成**：光方向与曲率张量相乘，直接生成方向曲率作为最终输出结果。

> 以下是一些着色器代码，显示如何计算方向曲率。 [下一页] 我们有一个函数需要 [下一页] 切线， [下一页] 双切线， [下一页] 曲率张量， [下一个], 和光线方向； [下一页] 这里我们将光线方向投影到切平面上； [下一页] 作为优化，我们跳过了投影光方向的标准化，因为它在实践中没有明显的差异；这是因为皮肤 当 N dot L 较大时，即归一化前投影光方向最短时，LUT 变化不大。 [下一页] 这是光方向与曲率张量的乘积， [下一页] 从而产生方向曲率。

---

## Slide 107

![Slide 107](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_107.png)

**📌 要点汇总**

- **预集成皮肤着色**：提出新方法，强调线性散射轮廓或柱面积分在计算正点光LUT中的关键作用  
- **SH照明LUT优化**：结合径向

> 总之，我提出了一种思考预集成皮肤着色的新方法， [下一页] 它强调了在计算正点光 LUT 时使用线性散射轮廓或柱面积分的重要性。 [下一页] 我还要在这里提到，在计算 SH 照明 LUT 时，将径向轮廓与“球形”积分一起使用也很重要。 [下一页] 我还演示了使用方向曲率的重要性，它提高了通过该技术计算的次表面散射的质量。

---

## Slide 108

![Slide 108](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_108.png)

**📌 要点汇总**

- **角色设计流程**：结合传统绘画与数字工具，确保细节表现力与艺术风格统一  
- **团队协作规范**：建立跨部门协作流程，明确原画师、3D建模师与动画师的分工标准  
- **细节优化技术**：通过高精度扫描与纹理映射技术，实现服装褶皱与材质的逼真还原  
- **文化考据方法**：参考历史文献与实物资料，确保角色服饰与武器设计符合时代背景  
- **动态表现方案**：采用骨骼绑定与物理模拟技术，提升角色动作的自然度

> 在本节中，我将讨论我们在《对马岛之魂》中创作角色细节图的方法。

---

## Slide 109

![Slide 109](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_109.png)

**📌 要点汇总**

- **细节贴图优化**：平衡纹理细节保留与内存使用减少  
- **高频/低频内容分离**：物理材料库支持高频，直观创作低频（如磨损）  
- **运行时动态组合**：需高效整合高频物理材料与低频细节内容

> [下一页] 使用细节贴图时，我们的主要目标是保留高水平的纹理细节，同时减少内存使用。 [下一页] 我们还希望能够使用可平铺的物理材料库作为高频内容的基础， [下一页] 同时允许直观地创作低频内容，例如磨损、污垢等， [下一页] 我们需要能够在运行时有效地组合这两个组件。 [下一页] 重新定向法线贴图解决了法线贴图的这个问题， [下一页] 但我们想要一些也适用于其他类型地图的东西。

---

## Slide 110

![Slide 110](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_110.png)

**📌 要点汇总**

- **传统工作流程**：从低频内容开始，逐步添加高频细节  
- **物理意义缺失**：地图结果可能无物理意义，需交互调整匹配目标外观  
- **生成方法不明确**：扫描材料生成细节图缺乏明确方法，依赖预处理  
- **压缩伪影增加**：独立压缩纹理结合导致压缩伪影问题加剧

> 传统上，细节图工作流程从创作的低频内容开始，然后添加平铺的高频细节 [下一页] 对于许多类型的地图，无法保证结果在物理上有意义，并且通常需要交互式调整以匹配所需的结果 外观。 [下一页] 我们不清楚如何最好地从扫描材料生成这些地图，因为细节图通常需要预处理。 [下一页] 最后，我们意识到传统的工作流程结合了两个独立压缩的纹理，因此可能会导致压缩伪影增加。

---

## Slide 111

![Slide 111](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_111.png)

> 相反，我们决定从平铺材质开始，并在顶部绘制低频内容以创建“目标”地图。 [下一页] 然后我们合成一个地图，使得 [下一页] 将合成地图与平铺细节层混合，与创作的目标地图相匹配（尽可能接近）。 [下一页] 在下面的幻灯片中，合成地图将为 s，平铺细节地图将为 d，目标地图将为 t。

---

## Slide 112

![Slide 112](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_112.png)

**📌 要点汇总**

- **工具与节点匹配**：艺术家使用Substance Designer/Painter创建目标图，需添加与着色器UV和HSV变换匹配的节点。  
- **材质设置限制**：支持最多3层平铺材质，结合遮罩进行分层处理。  
- **目标图生成流程**：通过绘画生成目标地图后导出，供着色器使用。  
- **资产编译处理**：读取目标贴图、平铺图层及蒙版，通过反转混合生成合成贴图。

> 艺术家使用 Substance Designer 和 Painter 来创作目标图；这需要添加与我们的着色器 UV 和 HSV 变换相匹配的设计器节点。 [下一页] 艺术家首先设置平铺材质（我们支持最多 3 个，结合遮罩）， [下一页] 然后他们在这些上面绘画以生成目标地图， [下一页] 导出以供我们的着色器使用。 [下一页] 在资产编译时，我们读取目标贴图以及平铺图层和蒙版，并通过反转混合生成新的合成贴图 运营商。

---

## Slide 113

![Slide 113](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_113.png)

**📌 要点汇总**

- **混合运算符选择条件**：需确保对所有d和t值

> 我们需要选择一个混合运算符， [下一页] 这样对于 d 和 t 的所有值，混合方程中 s 都存在解。 [下一页] 这排除了一些运营商， [下一页] 但是由这个方程给出的叠加混合效果相当好。
>
> [补充说明] Overlay 有一个很好的特性，如果 s 或 d 中的任何一个为 0.5，则另一个值将不加修改地传递。

---

## Slide 114

![Slide 114](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_114.png)

> [下一页] 对于从左到右的合成梯度， [下一页] 混合有 [下一页] 从下到上的细节渐变， [下一页] 叠加混合的结果 [下一页] 是这个。

---

## Slide 115

![Slide 115](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_115.png)

**📌 要点汇总**

- **s值覆盖d轴输出范围**：任意d值均可通过特定s值实现完整输出范围  
- **d影响随s趋近0/1减弱**：极端s值下d对输出的贡献逐渐降低  
- **低频s增强暗细节d**：3D视图中低频合成图s通过增亮作用强化暗部细节d

> [下一页] 向下看 d（高频细节）轴，我们看到输出值的整个范围可以通过任意 d 值的某个 s 值来实现，即 我们需要什么。 [下一页] 相反的情况则不然——当我们接近 0 或 1 时，d 的影响会减弱（从斜率下降可以看出）。 [下一页] 在 3D 中，它看起来像这样。 [下一页] 注意箭头所指的曲线部分，它对应于被低频合成图 s 增亮的暗细节 d。

---

## Slide 116

![Slide 116](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_116.png)

**📌 要点汇总**

- **梯度影响精度**：s轴方向梯度在d接近0/1时显著，导致精度下降，尤其在d接近时相对精度差  
- **BC1压缩质量下降**：使用BC1压缩时因精度问题导致图像质量明显降低  
- **混合算子精度提升**：针对t接近时的场景（如深色瓷砖层），优化混合算子以提高精度  
- **平滑叠加修改**：通过调整混合运算符实现更稳定的精度表现，命名为“平滑叠加”

> [下一页] 由于当 d 接近 0 或 1 时，s 轴方向的梯度较大，因此此处的精度会受到影响，并且当 d 接近时，相对精度尤其差 当s略大于0.5时趋近于0。 [下一页] 这导致使用 BC1 压缩时质量明显下降。 [下一页] 假设目标层和细节层通常相似，我们决定在 t 接近时提高混合算子的精度 d，特别是在提亮深色瓷砖层时。 [下一页] 这导致我们对混合运算符进行了如下修改；我们称之为“平滑叠加”。

---

## Slide 117

![Slide 117](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_117.png)

**📌 要点汇总**

- **多维度视角**：算子图形分别从t轴、d轴、s轴三个方向进行投影展示  
- **三维

> [下一页] 算子的图形看起来像这样，从 t 轴往下看， [下一页] 沿 d 轴向下看， [下一页] 沿 s 轴向下看， [下一页] 以及 3D 形式。

---

## Slide 118

![Slide 118](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_118.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 这里再次使用标准覆盖版本进行比较。

---

## Slide 119

![Slide 119](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_119.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 让我们看一个例子。

---

## Slide 120

![Slide 120](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_120.png)

> 这是游戏中材质的放大图，这是混合合成层和细节层的结果。

---

## Slide 121

![Slide 121](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_121.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 如果没有细节层，它看起来像这样......

---

## Slide 122

![Slide 122](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_122.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> ...如果我们只看细节的话，它看起来是这样的。

---

## Slide 123

![Slide 123](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_123.png)

> 这些是相同材质的反照率图；运行时仅使用合成贴图和细节贴图。

---

## Slide 124

![Slide 124](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_124.png)

> 这是未压缩的目标图，由艺术家创作。 [下一页] 缩放区域由左图中的白框显示。

---

## Slide 125

![Slide 125](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_125.png)

**📌 要点汇总**

- **BC1压缩应用**：游戏目标地图直接使用BC1压缩技术进行呈现  
- **RMSE指标定义**：均方根误差基于8位unorm编码（0-255）量化图像质量  
- **优化方向**：RMSE数值越低表示压缩后图像与原图差异越小

> 如果我们直接在游戏中使用 BC1 压缩的目标地图，这就是目标地图的样子。 RMSE 是均方根误差，基于 8 位 unorm 编码（0-255），所以越低越好。

---

## Slide 126

![Slide 126](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_126.png)

> 使用标准叠加混合会导致缩放区域中出现一些丑陋的色带， [下一页] 以及此处圈出的区域。 （但是请注意，整个地图的误差实际上低于 BC1 压缩目标地图！误差为 所提到的图像部分较高，但总体较低。）

---

## Slide 127

![Slide 127](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_127.png)

**📌 要点汇总**

- **平滑叠加混合运算符**：消除条带和色移，提升图像质量  
- **消除条带和色移**：解决图像处理中的常见伪影问题  
- **降低误差值**：优化算法性能，减少计算

> 使用我们的平滑叠加混合运算符可以消除条带和色移，并降低误差值。

---

## Slide 128

![Slide 128](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_128.png)

> 仅查看最大 RGB 误差，目标图的 BC1 压缩如下所示。

---

## Slide 129

![Slide 129](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_129.png)

> 标准叠加混合看起来错误如下所示；请注意，图像的许多部分的误差较低，但其他部分的误差也较高。

---

## Slide 130

![Slide 130](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_130.png)

> 使用平滑叠加混合运算符可显着减少错误。

---

## Slide 131

![Slide 131](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_131.png)

**📌 要点汇总**

- **混合压缩纹理**：加剧压缩伪影，因压缩错误不相关  
- **合成纹理生成**：使压缩误差负相关，降低混合总误差  
- **mip层级处理**：仅对非顶部mip操作，顶部mip用于多细节放大

> 正如我之前提到的，混合两组压缩纹理可能会加剧压缩伪影，因为压缩错误是不相关的。 [下一页] 通过针对压缩的平铺贴图生成合成纹理，我们可以使各个压缩误差更加负相关， 这减少了混合后的总误差。 [下一页] 我们可以对除顶部（最大）mip 之外的所有 mip 执行此操作，因为该 mip 针对多个细节 mip 进行了放大。

---

## Slide 132

![Slide 132](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_132.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片

> 为了演示这一点，我们将使用围巾资产的不同示例。

---

## Slide 133

![Slide 133](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_133.png)

> 这是混合合成层和细节层的缩放。

---

## Slide 134

![Slide 134](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_134.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 这是没有细节层的结果......

---

## Slide 135

![Slide 135](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_135.png)

> ...这是仅包含细节层的结果。

---

## Slide 136

![Slide 136](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_136.png)

**📌 要点汇总**

- **材质图类型**：展示合成图、细节图及目标反照率图，用于材质表现分析  
- **运行

> 这些是围巾材质的合成图、细节图和目标反照率图；同样，在运行时仅使用合成贴图和细节贴图。

---

## Slide 137

![Slide 137](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_137.png)

> 这是未压缩的目标图，由艺术家创作。 [下一页] 缩放区域由左图中的白框显示。

---

## Slide 138

![Slide 138](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_138.png)

> 这是在不使用压缩补偿的情况下混合的结果；也就是说，通过针对未压缩的细节贴图生成合成贴图。

---

## Slide 139

![Slide 139](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_139.png)

**📌 要点汇总**

- **压缩补偿**：通过优化压缩细节生成合成贴图，提升图像质量。  
- **合成贴图生成**：基于压缩后的细节贴图进行补偿处理，减少信息损失。  
- **误差优化**：均方根误差降低约18%，验证方法有效性。

> 这是经过压缩补偿后的结果；也就是说，通过针对压缩的细节贴图生成合成贴图。均方根误差为 减少约18%。

---

## Slide 140

![Slide 140](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_140.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 这是没有压缩补偿的最大 RGB 误差...

---

## Slide 141

![Slide 141](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_141.png)

> ...这与压缩补偿的误差相同。使用压缩补偿主要有助于减少混合结果中的噪声。

---

## Slide 142

![Slide 142](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_142.png)

**📌 要点汇总**

- **细节图方法误差**：使用细节图方法导致平均 RMS 误差增加 2.5%，但传统方法可能误差更高。  
- **平滑叠加混合优势**：平滑叠加混合比标准叠加混合降低 RMS 误差 1.5%，优于标准细节混合。  
- **压缩补偿效果**：启用压缩补偿可减少 RMS 误差 1.1% 和 RMSE 44%，但不适用于顶部 mip 级别。

> 以下是在发行游戏中使用此技术的所有纹理编译的一些统计数据，查看合成的第二个 mipmap 级别 只图，这样我们就可以分析平滑叠加算子和压缩补偿的效果。 [下一页] 如果我们只使用压缩的目标图而不进行任何混合，我们将得到 5.67 的平均 RMS 误差。 [下一页] 使用我们的细节图方法会导致平均 RMS 误差为 5.81，比不使用细节图差 2.5%。请注意，我们不能轻易 将其与传统的细节图进行比较，因为我们必须编写新的细节图。然而，我们期望传统的细节图也有 与混合未压缩贴图并压缩结果相比，RMS 误差更高。 [下一页] 使用标准叠加混合而不是平滑叠加混合会导致 RMS 误差高出 1.5%。与我们详细信息中的误差增加相比 混合时，使用标准细节混合的误差增加高出 61%。 [下一页] 如果没有压缩补偿，平均 RMS 误差会增加 1.1%，RMSE 会增加 44%。回想一下压缩 补偿应用于除顶部（最大）mip 之外的所有 mip。

---

## Slide 143

![Slide 143](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_143.png)

**📌 要点汇总**

- **平滑叠加混合运算符**：用于大多数地图类型，采用重新定向法线混合法线贴图，实现细节增强。  
- **二维牛顿法**：通过反转混合算子计算合成贴图，提升数值计算精度。  
- **alpha混合与参数约束**：各

> 除了一些特殊情况外，我们对大多数类型的地图都使用了平滑叠加混合运算符。使用重新定向法线混合法线贴图 贴图，这是应用细节法线贴图的一种原则性且实用的方法。 [下一页] 合成贴图仍然是通过反转混合算子来计算的，我们使用二维牛顿法进行了数值计算。 [下一页] 各向异性镜面反射贴图无法使用叠加混合进行混合，因为它不保留矩阵的结构。我们选择使用 alpha 混合， 作为可调整着色器参数公开的 alpha 参数。通过反转该混合算子再次生成合成的茴香图， 受到各向异性矩阵的特征值在 (0, 1] 范围内的约束。

---

## Slide 144

![Slide 144](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_144.png)

**📌 要点汇总**

- **细节贴图方法成功**：Ghost

> 总之，这种创作细节贴图的方法对于 Ghost 来说被证明是非常成功的，正如大量纹理所证明的那样。 以这种方式创作详细地图。 [下一页] 相对于传统细节贴图方法的一个优点是能够选择性地消除细节纹理的低频分量； [下一页] 另一个是更大的纹理重用的潜力，因为细节图可以直接用作材质，因为它们不需要任何类型的预处理。 [下一页] 生成合成贴图会导致纹理处理时间稍长（尽管这并没有被证明是令人望而却步的）， [下一页] 与无细节相比，颜色纹理的 RMS 误差平均略高。 [下一页] 请注意，可以通过将细节图的直方图居中来减少此错误，这与通常对传统细节进行的预处理类型相同 地图。

---

## Slide 145

![Slide 145](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_145.png)

> 我要感谢以下人员的贡献； 首先我要感谢我的家人，他们在我从努力完成《人鬼情未了》到努力做这个演讲的过程中给予了我耐心； 我还要感谢 Sucker Punch 渲染团队的辛勤工作； 我要感谢艺术团队成员为本次演讲提供的资源帮助； 以及 Sucker Punch 的每个人，感谢你们让这里成为一个很棒的工作场所； 最后，我要感谢史蒂夫和史蒂夫提供的宝贵反馈。

---

## Slide 146

![Slide 146](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_146.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 以下是本次演讲的参考资料；您可以在线咨询；

---

## Slide 147

![Slide 147](https://gerigory.github.io/assets/img/Siggraph/2020/Siggraph2020-Samurai-shading-in-ghost-of-tsushima/slide_147.png)

**📌 要点汇总**

- **（无内容）**：此幻灯片无演讲内容

> 最后，我要非常感谢*您*的关注。

---
