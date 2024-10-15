---
layout: post
title: 【Siggraph 2012】Local Image-based Lighting With Parallax-corrected Cubemap
date: 2024-10-15
img: Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片2.PNG # Add image post (optional)
fig-caption: # Add figcaption (optional)
tags: [Cubemap, Reflection, Siggraph, 2012]
description: 本文分享的是基于cubemap的反射效果的优化方案
---
今天介绍的是基于cubemap的环境反射效果的优化方案，基于此方案，可以有效缓解cubemap捕获位置跟相机位置不重叠导致的反射效果异常问题。

增强游戏画面品质常用的手段是提供更为真实的间接光效果，而其中有一项常用的手段是基于IBL的环境光反射方案。

本文的关注点是静态光滑物件表面的高光反射效果，因为是静态，所以数据可以走离线生成。

IBL方案主要有两个应用场景：

1. 近景光照模拟
2. 远景光照模拟

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片3.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片4.PNG)

先来看看远景部分。

远景的光照通常是通过一张存储了较远的场景元素（如天空山脉等）的cubemap贴图来表示，这张贴图通常不需要关联一个特定的局部坐标点，其数据会被用于户外物件的照明，这种cubemap大多是手绘的。

在实际运行的时候，会将地图分割成一个个的sector，每个sector关联一张cubemap，在两个相邻的sector过渡的时候，会需要对两张cubemap做采样并混合，这也就是为什么这种方法被称之为Camera-based（即什么时候取用哪张cubemap是由相机位置决定，而非物件本身决定）的由来。

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片5.PNG)

再来看看局部照明IBL。

局部照明的cubemap是程序捕获的，而非手绘。每个cubemap有个对应的捕获点，这种cubemap多用于室内、局部照明效果。

在运行时，某个物件该取用哪张cubemap是提前分配好的，跟camera本身的位置无关，因此这种方法也被称之为Object-based IBL。

这种方法在局部细节上表现较好，问题在于两点：

1. 由于局部性的作用，相邻的两个物体可能会被分配给不同的两个cubemap，造成效果不连贯
2. 因为捕获的数据偏局部，在相机位置跟捕获点不重合的时候，就会存在视差问题

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片6.PNG)

这里对问题做了进一步解释。

左图展示的是一块地板被分割成多个区域，每个区域由一个local cubemap所覆盖，导致在边界位置存在明显的接缝问题。作者表示，虽然项目组尝试了局部cubemap的混合策略，但是发现效果依然不能让人满意。

与此同时，对于一块较大的可能会需要由多个cubemap覆盖的物体（墙体、地板）而言，考虑到shading的高效性，还需要将之拆分出来（单个cubemap影响，多个cubemap混合影响）多个部分，对生产效率也会有较大影响。

右图展示的是视差问题，这里有个[视频](https://www.youtube.com/watch?v=ZH6s1hbwoQQ)。

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片7.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片8.PNG)

本文给出的方案被称之为POI-based方法，其基本思路为：

1. 基于某个点对当前视角中需要关注的cubemap做混合，之后基于混合后的cubemap为场景中所有物件做光照处理
2. 混合点可以是相机位置、角色位置或者其他某个dummy actor的位置
3. 混合权重由美术同学基于需要给出（可能是某种策略，比如基于距离、角度、可见性等）

应用了这个方案之后，前面的接缝问题就都能解决了。

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片9.PNG)

基于上述混合的方案之后，前面提到的接缝问题就没了，如这里展示的一样。不过还有两个问题需要处理：

1. 视差问题依然存在
2. 远景部分的反射精度有所下降

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片10.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片11.PNG)

左图是存在视差问题的效果截图，右边是期望达成的效果

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片12.PNG)

先来看下右边的示意图：

1. C点是cubemap捕获点
2. 目前相机需要采样地表反射位置（P点）的颜色
3. 那我们就只需要连接C点跟P点，找到cubemap上交点坐标并采样即可

在实际执行上：

1. 美术同学会用一个box volume来近似代表包围着cubemap的一个几何体，即图中的黑色方框
2. box volume的中心点跟cubemap的捕捉点不一定重叠
3. 在查找被反射点的时候，就以该box volume的边界为准（即P点是落在box volume上的）
4. 找到反射点后，就如前面所说，通过CP连线找到采样点即可

这个方法其实也不是这里最先发明，这里也指出，在更早的时候就已经被其他项目的人采用过了。

如果没有指定box，可以考虑使用无穷远作为box，这样就可以把天光跟局部环境光反射统一起来了

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片13.PNG)

上述方案效果很好，唯一的问题是计算消耗比较高，并且随着需要混合的cubemap数目增多，这个消耗还要在这个基数上翻倍。

参考Nvidia跟ATI的方案，这里给出了一个简化版本，总体的思路是以sphere作为外接形状，如上图所示，我们需要的是从Pp点反射出去撞到外接球的P点，而从cubemap中心点C出发到P点的向量$\vec D$ = $\vec{C \cdot Pp} + \vec{Pp \cdot P}$，对这个公式乘以一个系数K，就得到了上图中的伪代码。

从这里也可以看到，系数K准确来说应该是跟反射点位置、球体半径等是有关系的，而文中说的K是一个与球体半径、物件本身尺寸有关的参数，由美术同学手动给出，这个会给美术同学增加较大的工作量来做效果的调校。

经过这个优化后，PS3上单个cubemap的校正指令数就从21下降到8，同时值得一提的事Tri Ace research也用了类似的方案。

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片14.PNG)

这里给出了简化方案的效果，左侧是没做修正的，右侧是修正完成的

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片15.PNG)

前面说到了如果需要美术同学手动调校每个物件上的系数K，效率会比较低，这里的解决方案是将局部cubemap的采样处理独立出来，而非集成到物体本身的绘制shader中，而采用这种方式，就需要一个新的视差校正方案（因为在这个地方，就不知道像素的位置？）

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片16.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片17.PNG)

不用反射点的坐标，这里添加了一个反射平面，基于反射平面，可以拿到反射向量，同样的，该向量会与box volume相交，之后拿到该点在cubemap上的数据即可。

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片18.PNG)

大概解释一下伪代码的实现逻辑：

1. ReflCamera指的是相机相对于反射平面的Virtual camera的位置
2. RayWS指的是从ReflCamera出发的射线，RayLS则是转换到unit box space的方向
3. Unitary-ReflCameraLS指的是ReflCamera到unit box的边界的向量，也可以理解为在三个方向上还有多少的延展空间，这个向量除以RayLS，可以理解为RayLS方向上走多远的距离能分别跟三个（轴）平面相交
4. -Unitary-ReflCameraLS同理，则是另外三个负方向的轴平面的步进距离
5. 基于这两个相交向量（三维），我们取最大值（一正一负，取一正；两正则取远一点的平面）作为我们需要的相交点的步进距离
6. 基于上述步进距离，我们就可以求得cubemap上的交点在cubemap上的坐标


针对这个实现，目前有两点疑问：

1. 这里需要针对单一的反射平面，如果我们要反射的物体本身不是平面，该怎么办
2. 针对单一反射平面，我们要怎么实现逐cubemap texel的计算，是需要绘制一个cube，之后在PS中执行上述代码吗？

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片19.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片20.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片21.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片22.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片23.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片24.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片25.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片26.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片27.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片28.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片29.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片30.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片31.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片32.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片33.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片34.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片35.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片36.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片37.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片38.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片39.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片40.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片41.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片42.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片43.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片44.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片45.PNG)

## 参考

[[1]. Siggraph 2012 and Game Connection 2012 talk : Local Image-based Lighting With Parallax-corrected Cubemap](https://seblagarde.wordpress.com/2012/11/28/siggraph-2012-talk/)
