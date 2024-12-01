---
layout: post
title: 【GDC 2012】Deferred Radiance Transfer Volumes - Global Illumination in Far Cry 3
date: 2024-11-25
img: GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image1.jpg # Add image post (optional)
fig-caption: # Add figcaption (optional)
tags: [Far Cry 3, Rendering, lighting, GDC, 2012]
description: 本文分享的是Far Cry 3在GDC 2012上介绍到的全局光方案

---

本文分享的是Far Cry 3在GDC 2012上介绍到的全局光方案，照例，这里对工作内容做一个总结：

1. 

---

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image2.jpg)

2012年9月上线，写实射击，其中光照是画面精美的关键因素

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image3.jpg)

其中对GI的需求是比较明确的，但是这里存在一个挑战：

1. 地图尺寸大，lightmap包体过高，内存占用也大
2. 实时GI在性能与效果上无法令人满意

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image4.jpg)

最终采用的是一套自研的GI方案，称之为Deferred Radiance Transfer Volumes，先同步一下该方案的一些特点：

1. 在离线的时候会通过预处理的方式输出一些probe数据，这些probe数据会在运行时用于对场景做relighting（而非probe本身被relighting）
2. 整体方案的性能影响比较小，不论是运行时计算消耗还是内存消耗
   1. 内存大约是几个MB
   2. GPU每帧的Shading耗时则仅仅只有0.5ms（部分消耗转移到CPU执行）

上图展示了该方案的效果（环境光表现）

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image5.jpg)

整体的环境光主要包含三部分，如上图所示：

1. 左上角的小图展示的是太阳光跟天光的bounce lighting（我理解是间接光照），这部分数据会照亮物件的底部，以及一些不被太阳光直接照射（被阴影遮挡）的物件
2. 左下角的小图展示的是天光的直接光，天光以一个方向朝上的半球表示，通过对各个点按照垂直朝下的方式进行照明，可以为物件增加体积感
3. 叠加屏幕空间的SSAO算法

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image6.jpg)

这套方案的一个关键特性就是能够支持光源的动态变化，如上图所示，进入夜晚后，太阳光的反射就消失了，天光的颜色（cubemap）也相应的发生了变化，此处场景的照明就只剩下了天光的直接光照。

这套方案是自动触发的，当光源参数变化时，效果是直接反馈在表现上的，不需要额外的干涉或者烘焙流程触发，制作效率高。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image7.jpg)

此外，relighting还包含对太阳光方向的感知，上图中（类似于VLM，不过貌似这是通用的策略）：

1. 蓝色跟红色的墙体是静态物件，会对生成的GI输出产生贡献
2. 球体是动态物件，只接受GI的照明，但是却不会对GI做贡献

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image8.jpg)

可以看到不同位置的球体会受到来自场景的间接光照明影响，从而呈现出GI特有的color bleeding效果。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image9.jpg)

调整光照方向后，左侧的球体可以接受到来自左侧蓝色墙体（太阳光直接照明）的反弹而呈现更强的蓝色，而右侧的红色墙体由于出于阴影中，因此右侧的球体的红色就没了。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image10.jpg)

除了上述简单测试之外，在实际的场景中，依然能够提供较好的GI表现。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image11.jpg)

GI效果除了能够响应全局光如太阳光以及天光之外，还能响应动态局部光源，上图中局部光源只考虑直接光照的情况下，黑暗部分比较硬。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image12.jpg)

叠加上GI表现后，场景的暗部就变得柔软，在这个的作用下，美术同学也不用再额外补光来提升场景表现，一定程度上还能降低消耗。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image13.jpg)

总体的计算逻辑分为三部分（除了relighting之外，跟VLM不能说相似，只能说是一模一样）：

1. 离线负责完成probe的摆放与相关数据的烘焙
2. 运行时分为CPU跟GPU两部分
   1. CPU负责对probe做relighting以应对光照的动态变化，relighting之后的结果会写入到一个3D贴图中
   2. GPU负责采样3D贴图之后对场景做照明

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image14.jpg)

这里展示了probe摆放的工具，有如下的一些特点：

1. 支持美术同学手动标注需要生成probe的区域（也就是不是所有的区域都需要probe），之后按照规则自动生成probe
2. 支持美术同学手动修正probe的密度以及对局部probe做增减
3. 支持美术同学对probe的各个component做进一步的调节

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image15.jpg)

因为地图尺寸较大，因此必须要走自动摆放逻辑。目前的策略是：

1. 以4m为间隔生成probe
2. 每个probe生成的位置为自上往下打射线，找到命中点，或者是物件或者是地形，之后在命中点上抬一个距离的位置生成probe

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image16.jpg)

针对植被，这里做了特殊处理：

1. 为了避免结果杂乱无章，这里不再以命中的SM的实际位置为probe生成位置，而是以植被的boundingbox作为测试几何体
2. 为了避免预算超标，植被部分的probe摆放间隔从4m改成8m

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image17.jpg)

由于probe本身是稀疏的，因此需要一套高效的数据组织结构。

这里会用3D Grid来存储数据，Grid中的每个Cell用一个byte，这个数值指示的是距离该点最近的probe，在该位置所属section（这里没有解释）下面的所有probes中的索引。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image18.jpg)



![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image19.jpg)

1. 

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image20.jpg)

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image21.jpg)

1. 2. 

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image22.jpg)

1. 1. 

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image23.jpg)



![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image24.jpg)

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image25.jpg)



![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image26.jpg)

- 

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image27.jpg)

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image28.jpg)



![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image29.jpg)



![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image30.jpg)

3. 

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image31.jpg)

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image32.jpg)



![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image33.jpg)



![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image34.jpg)

3. 

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image35.jpg)

4. 

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image36.jpg)



![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image37.jpg)

 

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image38.jpg)

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image39.jpg)

- 

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image40.jpg)

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image41.jpg)

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image42.jpg)

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image43.jpg)

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image44.jpg)

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image45.jpg)



![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image46.jpg)

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image47.jpg)
![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image48.jpg)
![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image49.jpg)
![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image50.jpg)
![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image51.jpg)
![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image52.jpg)
![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image53.jpg)
![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image54.jpg)
![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image55.jpg)
![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image56.jpg)
![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image57.jpg)
![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image58.jpg)
![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image59.jpg)
![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image60.jpg)
![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image61.jpg)
![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image62.jpg)
![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image63.jpg)

## 参考

[[1]. 【GDC 2012】Deferred Radiance Transfer Volumes - Global Illumination in Far Cry 3](https://fileadmin.cs.lth.se/cs/Education/EDAN35/lectures/L10b-Nikolay_DRTV.pdf)
