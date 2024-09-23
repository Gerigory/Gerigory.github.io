---
layout: post
title: 【Siggraph 2014】Next generation post-processing in call of duty advanced warfare
date: 2024-09-18
img: Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/Page1.PNG # Add image post (optional)
fig-caption: # Add figcaption (optional)
tags: [COD, Post-Processing, Siggraph, 2014]
description: 本文分享的是COD在Siggraph 2014上给出的他们在后处理工作上的一些优化方案
---
![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/Page1.PNG)

COD在Siggraph 2014上分享过他们在后处理方面的一些工作要点，其中的一些内容对今天的游戏开发依然有不小的帮助，这里将其中的一些要点分享出来。

照例，先来对全文的关键信息做一个简短的总结：

1. 

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片2.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片3.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片4.PNG)

分享的技术小哥认为，对于写实风格的作品而言，后处理是游戏效果是否能逼近影视效果的关键。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片5.PNG)

后处理工作的优化思路总结下来有上述几个要点。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片6.PNG)

大纲如上，会从三方面进行介绍：

1. 基本概念
2. 面临问题
3. 对应方案

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片7.PNG)

运动模糊在快速移动的游戏中，会有非常重要的作用。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片8.PNG)

参考[3]：

> 真实世界中，自然光在感光材料上产生光化学作用，形成潜影的过程叫做曝光。
>
> 在这个过程中，如果拍摄对象发生了相对相机的移动，就会导致恒定输入的持续曝光变成非恒定输入的曝光叠加，最终体现为拍摄物体的模糊，也就是常说的运动模糊
>
> 同时，人类肉眼的视觉暂留现象，同样也是因为感光细胞中感光色素形成的延迟形成的
>
> 缺少动态模糊的画面，反而会丧失运动感，使观众失去焦点并从直觉上感觉画面断断续续而不自然

运动模糊是提升效果真实感的重要手段，常见的运动模糊有三类：线性、旋转以及缩放（径向）。而常见的模拟方案有如下几种[3]：

1. Accumulation Buffer：将运动的物体按照运动方向做多次渲染，之后按照一定的权重累加之后，再叠加到静态背景上
2. Velocity Buffer：基于屏幕空间每个像素的速度向量，做一个向前（按照曝光的理论，运动模糊表现为前后两部分的虚化）与向后的颜色扩散，以模拟该像素经过路径上的染色行为

注意：上图中介绍的第二种Stochastic Rasterization的方案不是上面说的Velocity Buffer的方案，而是通过随机噪点的方式来模拟的方案，参考[6]

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片9.PNG)

Accumulation Buffer的方案成本过高，一般没人考虑，本文介绍的方案主要是基于velocity buffer的。

需要注意的是，屏幕空间的方案（后处理），由于并不是所有信息都具备，因此通常不会十分的精确。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片10.PNG)

虽然最终用的不是随机光栅化方案，但是这个方案对本文要介绍的Motion Blur以及DOF方案提供了较多的启发，因此还是把实现思路做一个简单的同步。

这里有一个移动的矩形，处于t-10时刻

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片11.PNG)

在t+10时刻移动到了一个新的位置，而随机光栅化方案则是对该矩形的像素做一个随机处理，基于随机结果将之摆放到前后两个位置中间的某个点上。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片12.PNG)

比如，这个物件的某个像素会出现在t-8的位置

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片13.PNG)

另一个像素则出现在t+6位置

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片14.PNG)

再一个出现在t+3位置。

不过这里有个问题，如果矩形上的每个像素都单独做这么一个随机，就会使得效果噪声过强

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片15.PNG)

但是如果对于某个像素，我们做多次随机，之后将随机到某个位置的数据累加起来的话，效果就会好起来

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片16.PNG)

上述多次随机的过程也可以理解为带有alpha的样本混合，即将一个像素分成多个部分，每个部分分别放到不同的位置

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片17.PNG)

回到最初的输入，我们只有一张color buffer，一张velocity buffer以及一张depth buffer，要怎么实现上述的过程呢？

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片18.PNG)

问题就转化为了，如何将运动的物体沿着对应的方向做一定比例的拉伸，并且将拉伸后的效果按照一定的比例与背景做混合

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片19.PNG)

而我们可以通过：

1. 将前景物体（移动物体）做模糊（线性模糊、径向模糊等）来实现物件的伸缩（伸缩范围对应于模糊半径，对应于移动速度）
2. 前景与背景混合的alpha，则可以通过对该物体移动到该位置时的叠加次数（除以总次数）来得到（甚至这里可以基于移动速度推导出一个公式，避免alpha贴图的需要）

这俩贴图都可以通过scatter-as-you-gather后处理算法计算得到。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片20.PNG)

先来看下最直观的做法：基础散射算法。

我们的运动模糊可以通过将某个像素沿着其运动的方向不停地扩散来得到

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片21.PNG)

比如前面的点，向前向后两边扩散，就得到了这条线

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片22.PNG)

这种计算思路叫散射算法，虽然理解直观，但实现起来比较低效。

接下来换个角度看看问题，介绍一下前面说到的scatter-as-you-gather方法：这次我们不再将某个像素沿着其移动的方向做扩散，而是对于每个位置，我们检查其相邻的像素，看看是否会被该像素扩散过来。

扩散方法其实是将一个像素写入多个位置（需要多个pass），scatter-as-you-gather则是从多个像素读取数据写入一个位置（只需要一个pass）。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片23.PNG)

scatter-as-you-gather执行起来较为高效，不过会遇到较多的边界情况，总结起来有上述三个问题需要解决：

1. 如何知道当前像素的采样范围
2. 确定采样范围后，要如何知道哪些像素应该扩散至当前像素
3. 如何恢复背景数据



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片24.PNG)

先来看看采样范围的事情，最简单的方法就是基于当前像素的速度来计算，不过这里会有问题。

如上图所示，假设当前像素的速度为3，那么其采样范围就是前后各三个采样点。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片25.PNG)

而假设蓝色物体的移动速度高过3，那么其扩散的范围就会覆盖到橙色的点，而此时橙色的点按照自己的速度来采样，就会采取不到蓝色物体的数据，从而使得结果异常。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片26.PNG)

再来看第二个问题

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片27.PNG)

假设我们运动模糊的kernel是5（采样周边5个像素），上图中每个像素的高度代表深度的倒数，即越高表示距离相机越近。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片28.PNG)

如上图所示，黄色是当前像素，假设待采样的sample位于右边，其扩散的范围用蓝色box表示，那么这种情况下由于没有覆盖到黄色像素，因此该sample就会被拒绝

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片29.PNG)

而如果sample移动速度快，就会覆盖到黄色像素，同时由于sample距离相机跟进，那么在这两个条件下，就应该被黄色像素所接受。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片30.PNG)

最后一个情况，虽然sample的扩散范围覆盖了当前像素，但是距离相机过远，所以也不会产生贡献。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片31.PNG)

再来看最后一个非常典型的，但是理解起来可能有点困难的问题。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片32.PNG)

假设这里有个水平移动的物体

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片33.PNG)

假设我们采用的是Accumulation buffer方案，那么我们就需要对该物体多帧的数据进行混合。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片34.PNG)

直到我们得到了满意的效果，这就是我们需要的最终的效果

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片35.PNG)

但是将最终的效果跟我们的原始color buffer输入来做比较的话，你会发现该物体的有部分区域已经变得透明了，也就是说会混合其背后的物体的颜色数据，而这些数据在原始的color buffer中我们是没有的。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片36.PNG)

这里用一个真实的图片来做进一步说明

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片37.PNG)

这是运动模糊后的效果，其中红线描边部分是原始角色所覆盖的区域的轮廓线，放大一看就会发现，模糊的数据其实是分布在红线的两边的，那么红线内部的邻近区域是需要获取到背景的天空数据的，在我们只有一张原始贴图的前提下，这部分数据从何而来。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片38.PNG)

针对前面的问题，我们逐一来解答。本文要介绍的方案是基于McGuire的，之后参考了Sousa 2013的vectorization实现逻辑。

据原文作者介绍，McGuire的方案是第一个解决了上述三个问题的方案，本文是在McGuire方案的基础上做了部分改进。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片39.PNG)

先来看看采样范围的问题，其实我们要解决的是，在一个给定的快门时间内，对当前像素产生贡献的所有像素所在的范围，而这个范围不用很精准，可以稍微保守一点。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片40.PNG)

这里用的方案跟McGuire的方案一样，即以tile为单位统计各个tile的最大速度。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片41.PNG)

如果直接以tile的最大速度来推算覆盖范围，就有可能部分像素虽然归属于A tile，但是其相邻的tile的速度更大，也会覆盖到该像素，从而导致覆盖范围计算结果不准确。

这里还增加了一个额外的pass，即对tile做一个3x3（tiles）的最大值处理，从而保证相邻tile的数据都被考虑到了。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片42.PNG)

最后基于该速度来推测当前像素采样的范围（计算消耗有点高，移动端可能接受不了）。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片43.PNG)

再来个直观的展示，这是之前的贴图

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片44.PNG)

如果以当前像素的速度来计算覆盖范围，得到的模糊效果如图所示

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片45.PNG)

而按照前面tile方法的最大速度来计算覆盖范围，得到的效果是这样的，注意看模糊区域过渡效果，这种方案过渡明显更为平滑（前面的方案则有硬边）。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片46.PNG)

再来看第二个问题，依然延续McGuire的思路，不过这里做了一些补充说明。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片47.PNG)

McGuire算法的步骤给出如上图所示：

1. 首先针对当前像素，筛选出待采样范围内的sample，哪些是前景，哪些是背景
2. 之后基于如下的三个条件来计算出每个sample的权重
   1. 前景数据需要满足其速度能够覆盖当前像素
   2. 背景数据也要满足速度能够覆盖当前像素（背景指的是深度低于当前像素的，也能对当前像素产生贡献？后面会说，这部分数据是用于替代被遮挡的背景数据的，用于实现inner blur）
   3. sample的速度跟当前像素的速度相似的（指的是方向跟大小都相似？），这种情况下，这两个像素会相互贡献（没明白？）

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片48.PNG)

针对前面的算法，这里做了改进，第一个改进点就是：能够更精准的计算各个sample的贡献，参考上图两者的效果对比，左侧效果存在硬边，右侧的效果更为平滑。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片49.PNG)

对于某个像素而言，能够对它产生贡献的采样点会有一个非0的权重，这些权重不一定需要等于1。

之后我们做加权平均，并进行归一化，如上图所示。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片50.PNG)

再来看这个经典的水平移动的蓝色矩形。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片51.PNG)

水平的移动会产生两个模糊的区域，分别是outer blur跟inner blur。其中inner blur需要混入我们所缺失的背景数据。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片52.PNG)

对于outer blur而言，如果周边的sample距离相机比当前像素近，并且其覆盖范围能够覆盖当前像素，那么就会对当前像素产生贡献，得到的结果就是outer blur。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片53.PNG)

而inner blur则是在当前像素的速度覆盖范围内混合入背景数据而导致的模糊效果，而由于背景本身是缺失的，因此这里的做法是将相邻区域的背景数据合入进来。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片54.PNG)

听起来好像还不错，不过inner blur跟outer blur之间会存在一条明显的界线，从而导致过渡较为生硬。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片55.PNG)

再来看这个原始的例子

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片56.PNG)

我们可以计算出橙色像素的覆盖范围，假设覆盖范围内每个像素的权重都是1，那么该像素的混合结果就是4/7，其后一个像素的混合结果为5/7、6/7，都还比较平滑。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片57.PNG)

而来到outer blur的第一个像素，我们看到，左边的三个背景像素被拒绝了，不再参与到混合中，那么权重原来除以7，现在就变成除以4，导致结果变成了1，从而触发了前面的突变。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片58.PNG)

这里的解决方法，就是维持权重的稳定，将当前像素的权重从1改为4（4 = 7 - 3，可以理解为维持总权重的稳定，有值的采样点为3，那么当前像素的权重就要相应提高到4）

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片59.PNG)

同样，再往前一个像素，本身的权重为5

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片60.PNG)

这里为6

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片61.PNG)

理论上，要按照前面的权重的方法对每个采样点做加权求和，不过实际实现的时候采用了一种简单的方法，就是：

1. 按照McGuire的方法来做前景跟背景数据的累加
2. 不过在累加后对累加结果做一个梯度处理

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片62.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片63.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片64.PNG)

这里给出了具体的实现代码

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片65.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片66.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片67.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片68.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片69.PNG)





![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片70.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片71.PNG)





![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片72.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片73.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片74.PNG)





![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片75.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片76.PNG)





![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片77.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片78.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片79.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片80.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片81.PNG)





![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片82.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片83.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片84.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片85.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片86.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片87.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片88.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片89.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片90.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片91.PNG)





![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片92.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片93.PNG)





![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片94.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片95.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片96.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片97.PNG)





![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片98.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片99.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片100.PNG)





![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片101.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片102.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片103.PNG)





![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片104.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片105.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片106.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片107.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片108.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片109.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片110.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片111.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片112.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片113.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片114.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片115.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片116.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片117.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片118.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片119.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片120.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片121.PNG)





![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片122.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片123.PNG)





![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片124.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片125.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片126.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片127.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片128.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片129.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片130.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片131.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片132.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片133.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片134.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片135.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片136.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片137.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片138.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片139.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片140.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片141.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片142.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片143.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片144.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片145.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片146.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片147.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片148.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片149.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片150.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片151.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片152.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片153.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片154.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片155.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片156.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片157.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片158.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片159.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片160.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片161.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片162.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片163.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片164.PNG)



![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片165.PNG)





![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片166.PNG)



## 参考

[[1]. Next Generation Post Processing in Call of Duty: Advanced Warfare](https://www.iryoku.com/next-generation-post-processing-in-call-of-duty-advanced-warfare/)

[[2]. 物体运动模糊(motion blur)](https://zhuanlan.zhihu.com/p/480274106)

[[3]. 运动模糊](https://zhuanlan.zhihu.com/p/441786650)

[[4]. A Reconstruction Filter for Plausible Motion Blur](https://casual-effects.com/research/McGuire2012Blur/McGuire12Blur.pdf)

[[5]. A Fast and Stable Feature-Aware Motion Blur Filter](https://www.cim.mcgill.ca/~derek/files/Guertin2014MotionBlur.pdf)

[[6]. Real-time Stochastic Rasterization on Conventional GPU Architectures](https://research.nvidia.com/sites/default/files/pubs/2010-06_Real-Time-Stochastic-Rasterization/McGuire10Stochastic.pdf)
