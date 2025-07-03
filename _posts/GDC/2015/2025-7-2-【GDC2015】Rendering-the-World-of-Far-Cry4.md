---
layout: post
title: 【GDC 2015】Rendering the World of Far Cry 4
date: 2025-7-2
img: GDC/2015/Rendering-the-World-of-Far-Cry4/image1.jpg # Add image post (optional)
fig-caption: # Add figcaption (optional)
tags: [Far Cry 4, Rendering, lighting, GDC, 2015]
description: 本文分享的是Far Cry 4在GDC 2015上介绍到的一些渲染技巧

---

本文分享的是Far Cry 4在GDC 2015上介绍到的一些渲染技巧，照例，这里对工作内容做一个总结：

1. 

---

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image2.jpg)

FC4的技术是在FC3的基础上迭代而来的

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image3.jpg)

这里在介绍FC3的实现的时候，也会顺带介绍FC3方案中的相关问题。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image4.jpg)

随着时间流逝，无处可藏……
我们图形团队的任务是引领本世代主机开发，同时保持上世代引擎与《孤岛惊魂3》相同。这给我们带来了诸多限制，因为必须确保上世代版本正常运行，这影响了整个项目中的许多决策。到项目后期，我们不可避免地需要返工优化PS3和Xbox 360版本，但这使得所有平台的成品都超越了《孤岛惊魂3》的品质。

不过今天我将主要聚焦Xbox One和PS4的开发工作，有机会时也会穿插些关于旧主机的小花絮。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image5.jpg)

我们重点改进了五个主要方面，但今天我只谈前四点。希望大家今天早些时候都参加了Ka Chen的演讲，其中介绍了我们开发的虚拟纹理技术，用于提升地形渲染效果。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image6.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image7.jpg)

在2012年SIGGRAPH大会上讨论了《孤岛惊魂3》中基于物理的着色技术。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image8.jpg)

和其他人一样，我们使用的是迪士尼BRDF。迪士尼将“反射率”参数称为“高光”，但我认为前者更贴切。此外，他们使用“粗糙度”而非“光泽度”，但由于历史原因，我们不得不沿用后者。未来我们会进行更改。

我们尝试过迪士尼的漫反射模型，但似乎效果差异不大。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image9.jpg)

今天我们要讨论金属和各向异性。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image10.jpg)

如果我们使用全镜面反射颜色，就必须找到三个G-Buffer通道，这在PS3和360上是不可能的。因此，我们只能替换反射率通道。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image11.jpg)

- 

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image12.jpg)

如果我们使用完整的镜面反射颜色，就必须找到三个G-Buffer通道，这在PS3和360上是不可能的。因此，我们只能替换反射率通道。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image13.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image14.jpg)

我想我应该在这里指出，从技术上讲，alpha参数代表的是粗糙度而非光泽度，而且我们确实应该将光泽度称为“平滑度”，因为这样能更准确地描述其本质。不过，我们还是沿用了《孤岛惊魂3》中的传统命名方式。	

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image15.jpg)

为了紧凑地存储切线空间，我们实际上可以借鉴动画系统的思路。具体来说，Crytek曾在其动画系统中提出将切线空间以四元数形式压缩的方案，BitSquid博客的Niklas Frykholm也做过类似研究。由于若某分量超过其他分量，则其必然成为最大分量，因此三个最小分量的取值范围被限定在[-1/√2, +1/√2]区间内。随后我们可以将该范围重新缩放至[0, 1]以获得更高精度。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image16.jpg)

关于四元数压缩/解压缩的所有着色器代码，请参阅附录。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image17.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image18.jpg)

正交切线空间其实并不差，特别是因为你可以将用于着色的切线空间和用于法线的切线空间解耦。（如果你要做LEAN映射的话这会是个问题，但我们没做。）

对于混合贴花来说，虚拟纹理在这里帮了我们大忙，因为我们所有的地形贴花都被烘焙进了虚拟纹理。对于其他不使用虚拟纹理的对象，比如建筑物上的贴花，只能使用单层贴花是我们给美术人员提出的限制，而他们也找到了解决方法。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image19.jpg)

我很感谢Matt Pettineo让我注意到Don Revie的文章。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image20.jpg)

老实说，这还远远称不上完美……但它比重要性采样快得多，也比什么都不做要好得多。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image21.jpg)

我们解决了一个关于添加各向异性的有趣问题……我们的武器团队总是抱怨说他们想要一个假的镜面反射项，因为他们并不总是能看到高光。而有了各向异性镜面反射后，这些抱怨完全消失了，因为他们总能从各个角度看到一些很酷的效果。值得一提的是，他们想要的这种“假镜面反射”实际上就是一种各向异性——这正是他们在现实世界中觉得缺失的东西。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image22.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image23.jpg)

我要提到我们团队中三个人完成的工作。杰里米·摩尔负责天空遮挡部分，加布里埃尔·拉松德负责环境贴图，而我负责间接光照。

提高天空遮挡的分辨率可能是我们优先考虑的事项，而不是提高间接光照的分辨率，因为这样做干扰较小（这对我们的跨世代制作很重要），而且也更简单——我们知道这是可以实现的。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image24.jpg)

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image25.jpg)

换句话说，我们生成了场景的高度图，并利用它来生成可见性信息。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image26.jpg)

- 

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image27.jpg)

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image28.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image29.jpg)

我们根据地形上方的高度将天空遮挡从完全遮挡过渡到完全可见——在地形高度处，我们使用完整的天空遮挡值，但在模糊高度图中存储的高度处，我们将像素视为完全可见。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image30.jpg)

3. 

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image31.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image32.jpg)

你可能会注意到这里生硬的衰减效果——这是经过艺术指导的，因为我们提供了一些调整最终效果的控制选项。



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image33.jpg)

如果你观察建筑物与地面的交界处，会发现现在两个表面的光线协调多了。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image34.jpg)

3. 

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image35.jpg)

4. 

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image36.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image37.jpg)

 

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image38.jpg)

阴影和遮挡要求我们使用深度缓冲区来重建位置。
我们使用环境项的亮度而非颜色，因为我们发现这样可以更好地在全天保持立方体贴图的正确效果。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image39.jpg)

看山间光影变幻

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image40.jpg)

我们采用了与Sebastien Lagarde和Charles de Rousiers相同的运行时环境贴图滤波方法。滤波重要性采样绝对是关键——首先，用简单的盒式滤波器快速生成mipmap，然后使用滤波重要性采样生成GGX滤波的mipmap，这显著减少了所需的采样次数和内存带宽。将立方体贴图的面（如果可能的话，还包括立方体贴图的mip级别）批量处理对性能至关重要——否则，你会在非常小的表面上运行大量任务，导致GPU占用率很低。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image41.jpg)

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image42.jpg)

尽管采用了重要性采样过滤，我们仍然受限于带宽。我们的HDR纹理格式在这方面并无帮助——微软的David Cook建议我们尝试改用R10G10B10A2格式，但我们尚未有时间进行相关实验。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image43.jpg)

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image44.jpg)

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image45.jpg)

因此，一个单元可能来自任何mip级别和任何尺寸。最终，我们并不真正关心这些——我们有一个光照探针单元，只需要从中获取一个光照探针。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image46.jpg)

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image47.jpg)

我们如何在GPU上存储单元？简单来说，我们只需分配一个固定数量的单元，这些单元可以一次性加载。
在这里提到虚拟缓冲区时，我应该说明这完全是软件层面的操作——我们并没有在硬件上做任何处理。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image48.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image49.jpg)

当我说分配时，显然内存已经被分配了——我们只是将其标记为已分配，并从CPU复制数据。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image50.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image51.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image52.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image53.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image54.jpg)

老实说，我这部分的代码运行速度挺慢的。最后我可能会把它放到GPU上运行。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image55.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image56.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image57.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image58.jpg)

但如何在探针之间进行插值呢？我们必须进行四次昂贵的采样操作，
这就是为什么我们转而采用剪辑贴图注入技术...

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image59.jpg)

剪辑贴图是一个32x32x5的纹理数组——每个"mip层级"需要与上一层级保持相同尺寸，因为它覆盖的区域更大。
在上世代主机中，我们仅使用这个剪辑贴图的单层来替代旧版体积贴图，后者需要占用大量内存空间。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image60.jpg)

天空照明和间接照明的全屏处理显然耗时最多。
目前它受到VGPR的限制。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image61.jpg)

质量问题对我们来说是个大问题——每8米一个轻量探针显然不够，而二阶辐射传输根本无法捕捉高频全局光照数据。不过，在必须跨世代主机使用相同数据的限制下，我们在《孤岛惊魂3》中很好地解决了所面临的问题。

你可能会好奇，既然本世代硬件内存有所提升，为什么我们反而比《孤岛惊魂3》降低了内存需求……嗯，我们成功在上世代主机上也实现了内存优化，这为我们节省了几兆字节的空间。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image62.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image63.jpg)

感谢菲利普·加尼翁（Philippe Gagnon）和让-塞巴斯蒂安·盖伊（Jean-Sebastien Guay）开发了这个系统。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image64.jpg)

Grass also covers small plants

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image65.jpg)

Grass also covers small plants

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image66.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image67.jpg)

Everything is rendered with alpha test; no alpha blending is used.

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image68.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image69.jpg)

如果我们调整剔除相机并环视四周，会发现树后方的叶片簇具有较低的细节层次（LOD）。
显然要记住，我们生成这些叶片簇的LOD不仅基于相机周围的不同视角，还考虑了距离因素——当距离足够远时，整棵树会变成蓝色。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image70.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image71.jpg)

蜂鸣器的视频。你可以看到蜂鸣器产生的风如何影响树木、灌木丛以及草地。虽然草地没有进行模拟，但我们使用了与水面波纹模拟非常相似的技术。稍后我会介绍一些类似的技巧，我们通过这些方法为植被添加最后的修饰。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image72.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image73.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image74.jpg)

这个冒牌系统的问题在于纹理数量导致的高内存需求。未来我们可能会考虑减少视图数量。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image75.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image76.jpg)

虽然此处未作演示，但当树木从侧面被照亮或两个远处的树木替身相交时，这种方法确实非常有效。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image77.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image78.jpg)

之所以能渲染这么多顶点，全靠我们采用的LOD（细节层次）系统。我们会大幅剔除高分辨率LOD模型。实际渲染时，红木模型的顶点数最多约为8万个。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image79.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image80.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image81.jpg)

这很简单，但非常有效。显然，这是一个极端的例子，但我想这与我在佛蒙特州秋天看到的树木并没有太大不同。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image82.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image83.jpg)

No noise on the left, noise on the right.

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image84.jpg)

Video of noise on/off.

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image85.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image86.jpg)

我们的抗锯齿方法由Michal Drobot在2014年SIGGRAPH大会上展示，因此请参阅该演示文稿以获取更多详细信息。当然，所有的功劳（以及所有棘手的问题）都应归功于Michal为此付出的努力。该方法结合了三种技术……

边缘抗锯齿——这应该是不言自明的。

时间抗锯齿——这指的是两个连续帧之间的锯齿——我们也希望使其看起来平滑。

时间超采样——超采样是以更高的分辨率进行渲染——我们希望通过每帧对较大图像的不同像素进行采样，在时间上实现这一点。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image87.jpg)

以下是当前情况的概述……别担心……我们会在接下来的几分钟内详细讲解。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image88.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image89.jpg)

我们没有在《孤岛惊魂4》中实现色彩流动一致性，因此游戏中会出现一些闪烁现象。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image90.jpg)

实际上使用了3x3窗口的中心像素而非平均值，因为过度平滑会导致太多误报。另外，强烈推荐阅读Brian Karis在2014年SIGGRAPH上的精彩演讲，其中讨论了其他各种验收指标。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image91.jpg)

这是对我们接受度指标的可视化展示，希望能让情况更加清晰明了。我们再次使用了中心像素而非平均值。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image92.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image93.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image94.jpg)

2xRG has 2 unique columns and 2 unique rows

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image95.jpg)

QUINCUNX通过共享相邻像素的角样本来优化图案。
它覆盖3个独特的行和3个独特的列，相比2xRG有所改进。
它增加了0.5半径的模糊效果（可通过0.5像素锐化掩模处理部分恢复）。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image96.jpg)

4xRG has 4 unique columns and 4 unique rows

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image97.jpg)

FLIPQUAD是一种高效的2样本/像素方案，通过共享像素边界边缘的采样点，实现有效的4倍超级采样。它结合了QUINCUNX和旋转网格模式的优点，覆盖4个独立行和4个独立列，性能优于2xRG和QUINCUNX，与4xRG相当。该方案还增加了0.5半径的模糊效果（可通过0.5像素锐化掩模处理部分恢复）。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image98.jpg)

图片由 [Akenine 03] 提供
我们可以看到 FLIPQUAD 的表现与 4xRotated Grid 类似。
可以说它能提供更高质量的结果。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image99.jpg)

误差估计值E较低 -> 更接近1024超采样参考值。
图片由[Laine 06]提供

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image100.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image101.jpg)

当然，这听起来是个好主意，但在实践中会遇到问题……你必须在采样位置对UV进行插值才能实现真正的超采样，然后你会发现导数计算是错误的。这会导致一些棘手的问题，比如以下情况……

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image102.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image103.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image104.jpg)

如果我们重新排列样本，使得红色框中的样本2和3实际上是样本0和1，那么梯度就会相似。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image105.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image106.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image107.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image108.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image109.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image110.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image111.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image112.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image113.jpg)

是的，这个场景完全在预算范围内！有时候跨世代合作确实有帮助。

![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image114.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image115.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image116.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image117.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image118.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image119.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image120.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image121.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image122.jpg)



![](https://gerigory.github.io/assets/img/GDC/2015/Rendering-the-World-of-Far-Cry4/image123.jpg)



## 参考

[[1]. 【GDC 2015】Rendering the World of Far Cry 4](https://ubm-twvideo01.s3.amazonaws.com/o1/vault/gdc2015/presentations/McAuley_Stephen_Rendering_the_World.pdf)
