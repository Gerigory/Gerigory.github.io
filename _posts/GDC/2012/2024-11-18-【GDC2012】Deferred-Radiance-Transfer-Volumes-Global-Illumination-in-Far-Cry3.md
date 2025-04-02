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
2. 左下角的小图展示的是天光的直接光，天光以一个方向朝上的半球表示，通过对各个点按照垂直朝下的方式进行照明，可以为物件增加体积感（可以理解为大颗粒度的AO效果）
3. 叠加屏幕空间的SSAO算法

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image6.jpg)

因为probe数据会在运行时做relighting，因此这套方案的一个关键特性就是能够支持光源的动态变化，如上图所示，进入夜晚后，太阳光的反射就消失了，天光的颜色（cubemap）也相应的发生了变化，此处场景的照明就只剩下了天光的直接光照。

这套方案是自动触发的，当光源参数变化时，效果是直接反馈在表现上的，不需要额外的干涉或者烘焙流程触发，制作效率高。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image7.jpg)

此外，relighting还包含对太阳光方向的感知，上图中（类似于VLM，不过貌似这是通用的策略）：

1. 蓝色跟红色的墙体是静态物件，会参与GI的计算，因此能对场景的光照表现产生影响
2. 球体是动态物件，只接受GI的照明，但是却不会参与GI的计算

换句话说，静态场景会参与Probe数据的计算，而动态物件则仅仅接受Probe的输出

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image8.jpg)

可以看到不同位置的球体会受到来自场景的间接光照明影响，从而呈现出GI特有的color bleeding效果。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image9.jpg)

调整光照方向后，左侧的球体可以接受到来自左侧蓝色墙体（太阳光直接照明）的反弹而呈现更强的蓝色，而右侧的红色墙体由于出于阴影中，因此右侧的球体的红色就没了（似乎也并不合理，正确的结果应该是红色反弹变弱）。

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

1. 支持美术同学手动标注需要生成probe的区域，之后按照规则自动生成probe
   1. 并不是所有的区域都需要probe

2. 支持美术同学手动修正probe的密度以及对局部probe做增减
3. 支持美术同学对probe的各个component做进一步的调节

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image15.jpg)

因为地图尺寸较大，因此必须要走自动摆放逻辑。目前的策略是：

1. 以4m为间隔生成probe（2D水平面上）
2. 每个probe生成的位置为自上往下打射线，找到命中点，或者是物件或者是地形，之后在命中点上抬一个距离的位置生成probe

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image16.jpg)

针对植被，这里做了特殊处理：

1. 为了避免结果杂乱无章，这里不再以命中的SM的实际位置为probe生成位置，而是以植被的boundingbox作为测试几何体
2. 为了避免预算超标，植被部分的probe摆放间隔从4m改成8m

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image17.jpg)

由于probe本身是稀疏的，因此需要一套高效的数据组织结构。

这里会用3D Grid来存储数据，Grid中的每个Cell用一个byte，这个数值指示的是距离该点最近的probe，在该位置所属section（这里没有解释）下面的所有probes中的索引：

- 整个场景会被分割成多个section，这是probe的一个组织单位与容器
- 每个section包含了一个probe列表（不超过256个，按照probe间隔4m来看，section的尺寸不超过32m）
- 每个section用一个3D Grid来表示其覆盖的范围，Grid中的每个cell存储一个byte，用于指示距离该点最近的probe在section的probe列表中的索引

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image18.jpg)

Probe上会存储两个数据：

1. 低频的PRT（Precomputed Radiance Transfer），细节可以参考Sloan 2002的Siggraph文章
2. 天空可见性：Sky Visibility

PRT存储的是一套与光照输入解耦的环境光照结构数据，简单解释如下：

> PRT存储的其实是将光源的输入Radiance按照SH基向量拆成多个分量，之后输出每个单位分量下的输出Radiance分布，以一个SH向量表示，多个方向就是多个SH向量组成的矩阵。
>
> 运行时只需要将输入Radiance转成SH向量：
>
> 1. 之后与矩阵相乘，就得到对应反射方向上的输出Radiance，即为Specular光照。
> 2. 而Diffuse通常会假设成Lambert Surface，这时候SH向量就坍缩为一个单一的数值，矩阵就变成了SH向量，与表达输入Radiance Field的SH Vector点乘，就得到了最终的Irradiance数据。

在这里，Probe的数据是通过RayTracing计算得到的。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image19.jpg)

Sloan的PRT方案是针对单个mesh来设计的，在烘焙计算的时候，需要拿到对应位置的surface normal。

而Probe本身是一个empty space，没有法线的概念，怎么办呢？

这里的做法是为probe指定几个"虚拟法线"的方向，这些方向可以称之为transfer basis，选定的basis总共包含四个方向，其中三个方向指向上方，最后一个则指向下方（不够具体）。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image20.jpg)

如前所述，针对每个方向，最终都会烘焙出一个SH向量，这里选用二阶SH，就是一个四维向量，四个方向，就是一个4x4的矩阵，其中每个元素都是一个float。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image21.jpg)

这里还需要存储sky visibility数据，这个数据在这里的含义其实是表示某个basis方向的天空是否可见的一个低频sky mask，低频到什么程度？每个方向存储一个scalar（bit？），最后一个向下的方向虽然数值总是为0（朝向地面），但出于数据对齐的考虑，这个数值并没有被优化掉。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image22.jpg)

在PC上，还会烘焙额外的一套local radiance transfer数据，这个是基于Kristensenet等人在Siggraph 2005上发表的方案开发的，算法框架如下图所示：

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image64.png)

> Sloan的方案有一个假设，即输入光源来自于一个较远的距离（或者从一个较远的位置反射过来），在这种情况下，模型上各个顶点的输入光源数据就可以看成是同一套。而如果是近距离的光照输入，模型上各个顶点的光照输入就不能假设为是相同，因此就不能Sloan的算法。
>
> 

有了这个数据之后，就可以支持动态光源的GI表现了，如上图所示，在局部光启用的时候，就能够在球体上看到红色砖块二次反弹过来的红色光线。

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
