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
> 这里的做法是将单点的光照采样变成多点的采样，而为了降低数据存储的开销，会对数据做PCA压缩，之后在运行时基于一定的规则找到一个Virtual的Lighting Position，并通过对压缩的光源数据进行插值得到对应的光照数据，用之对每个顶点进行照明计算。

有了这个数据之后，就可以支持动态光源的GI表现了，如上图所示，在局部光启用的时候，就能够在球体上看到红色砖块二次反弹过来的红色光线。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image23.jpg)

这里也介绍下Far Cry3中的具体做法：

1. 在场景中按照probe的位置来布设Virtual Point Light
2. Virtual Point Light的数据以2阶SH表达，具体的数据是从动态局部光（以及其他光源）采样得到
3. 每个Probe上存储的最大的LPRT（Local PRT？）系数数目是128，按照前面的介绍，总计就是128x4x3个矩阵
   1. 2阶SH总计4个系数，包含3个通道

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image24.jpg)

这里float4格式中的数据采用的是16位的定点浮点数，也就是每个float占用两个字节，在这个格式下，每个probe总计空间占用152个字节。

这里也介绍了sector的尺寸，覆盖64x64平方米的范围，每个sector包含大约70个probe，加上对应的3D Grid的数据存储，总计每个sector的空间占用如上图所示（PC跟主机有所不同，主机性能有限，尤其是显存较小，因此不用LPRT数据）。

在当前的配置下，玩家周围最多有51个sectors同时处于内存中，因此会有上图所示的总计内存占用。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image25.jpg)

接下来看看如何做实时的relighting。

在FC3（Far Cry 3，下同）中，太阳跟天光的照明是通过一系列美术同学手工编辑的gradient参数驱动的。

第一个gradient参数是跟随TOD而变化的太阳光颜色，这个数值会从gradient curve中读取出来，并被投影到SH系数中。

上图分成两行，上面一行是太阳光的颜色相关数据，右边的圆球是重建后的太阳光数据（SH）；下面一行是天光颜色数据。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image26.jpg)

局部动态光源的数据会被直接存储到probe上。

在运行时会计算每个probe与影响这个probe的所有动态光源的距离，并基于一系列的计算，得到这个动态光源对这个probe的贡献，最终我们就将所有动态光源的能量表达为一系列probe上的光照数据，即颜色与强度。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image27.jpg)

这里给出了具体的relighting代码，PC上relighting是在CPU上做的，而主机则放到了SPU上。

整体实现，其实跟GPU也是能很好匹配上的，不过这里是出于节省GPU Cycle考虑而设计的（瓶颈在GPU？）

从实现上来看，有如下的要点：

1. 最终输出的是一个个的color数据，每个color数据包含RGB三个通道，每个color对应于一个SH Basis（如果是2阶的话，每个probe包含4个Basis）
2. 最终的Color（Irradiance）是通过两个SH点乘得到的，其中一个是Basis对应方向的SH，另一个是Radiance Transfer的SH
   1. Radiance Transfer的SH对应的就是该点接收到的来自各个方向的Incoming Radiance Field
   2. 这个数据会将太阳光、天光与局部光的数据都考虑在内，三者的Basis SH各不相同
   3. 天光除了需要考虑其间接光的贡献外，还需要考虑其直接光影响
3. 太阳光、天光用到的Radiance Transfer数据是同一套，对应的是PRT的数据；Local Light用到的则是取自Probe的LPRT数据，是单独一套

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image28.jpg)

天光跟太阳光的间接光贡献，是直接取得PRT（全局数据）SH与相应光照的SH数据的点乘

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image29.jpg)

天光的直接光照明，则是取Basis Dir对应的SH与天光的SH点乘，得到Basis Dir方向上的Irradiance数据，这里还需要乘以天光的可见性数据v。

> Basis Dir具体是什么方向？从basis Index的索引来看，应该是SH Basis对应的几个标准的方向

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image30.jpg)

动态局部光源的计算仅限于PC，计算需要考虑影响当前顶点（像素）的probe，对其进行遍历，之后针对遍历的每个probe来计算其贡献。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image31.jpg)

对于每个probe的Radiance Transfer，需要累加来自各个SH Basis方向上的贡献，而每个方向上的贡献又是如前所述，是两个SH之间的点乘。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image32.jpg)

按照2阶SH的存储方式，每个probe就会包含四个颜色数据，每个对应于一个SH Basis方向，而如果内存足够，算力足够的话，Basis也可以扩展到更高阶，从而得到更好的效果。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image33.jpg)

在CryEngine的LPV（Light Propagation Volume）的启发下，这里会设置一个跟随相机而移动的Volume Map，这个Map中的数据会从Relight之后的Probe中插值而来。

之后在计算各点的irradiance的时候，就能够直接从volume map中进行采样得到，这时候还可以借助硬件滤波实现更为平滑的光照结果。与此同时，这个过程可以逐像素进行，从而在大尺寸物件上如船体，也可以得到较为平滑的光照结果。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image34.jpg)

颜色三个通道的数据（RGB）会需要用到三张Volume Map，尺寸跟格式都是一样的：Volume Map的分辨率是96x96x16，格式是RGBA8，这里RGBA四个通道，分别对应于四个SH Basis方向的强度。

volume map上的texel数目较多（147k），要想从头到尾更新一遍，耗时较久：在具有5个SPU的PS3上，耗时约7ms。高耗时主要在于需要完成如下工作：

1. 需要从3D Grid中查找到每个像素周围最近的probe
2. 之后从probe中获取到Basis颜色数据，并将之转换为byte格式



![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image35.jpg)

对volume map更新的条件有两种：

1. TOD变化
2. 相机移动，相对高频，可以服用部分volume数据，采用scroll update的策略

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image36.jpg)

对于贴图而言，我们的寻址模式可以设置为非wrap的，如左图所示，也可以设置成wrap的，如右图所示。

而由于将贴图设置为wrap，在性能上会有损耗（Clamp不需要做算术运算，且空间局部性更高，计算效率自然更高），因此这里的做法是将贴图的寻址模式设置为clamp，之后通过shader的frac指令来模拟wrap寻址。

在主机上（PS3），性能差异能到5倍之大（震惊），不过clamp就不能在边缘上实现连续的平滑滤波了，为了做到这一点，会需要留出几个texel并对数据做复制。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image37.jpg)

 FC3采用的是延迟管线，会先走Base Pass生成GBuffer，之后执行HDR Lighting，最后做后处理计算。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image38.jpg)

GBuffer包含了基色、世界法线、深度以及其他材质属性。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image39.jpg)

在正式的Lighting计算之后，会先做一遍屏幕空间计算，得到各个像素的ambient light结果，存储到一个屏幕尺寸的buffer中。

接着再执行太阳光照明，局部光照明，最后将这些照明结果统合到一起。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image40.jpg)

这是屏幕空间ambient光计算代码，下面逐步分解一下。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image41.jpg)

先获取当前位置在世界空间中采样volume map的uv坐标，这里会对当前位置做一个extrusion（凸出）处理，沿着法线做一个挤出（避免遮挡或陷地之类的情况？）。

拿到UV后，采样得到三个通道下的四个SH basis的强度数值。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image42.jpg)

对上述采样结果进行组装，得到四个新的float3，代表四个SH Basis方向上的颜色数值。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image43.jpg)

接下来基于法线来得到四个SH Basis的权重，通过投影计算得到。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image44.jpg)

权重会做一轮处理，包括scale跟bias，这里可以看到，仅朝下的basis在这里会有影响，相当于做了一个映射，从[0,1]映射到了[0.5, 1]，或者从[-1, 1]映射到了[0, 1]。

之后基于权重对四个方向的irradiance进行加权混合，得到最终的环境光结果。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image45.jpg)

下面来看看环境光的表现，在上图中有大面积的阴影区域，因此环境光在这里会有较为明显的作用

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image46.jpg)

先来看下这个区域的道路排跟树的GI效果，可以看到，即使当前区域是被阴影覆盖的，这俩都接受到了来自地表的强反射效果（因为这里只存储了低频的radiance transfer数据）。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image47.jpg)

这里有个大石头，接受到了从植被反弹过来的光照，这个反射颜色跟地表的颜色有明显的区别，同时这个光照表现还会跟随法线而变化，从而使得这个岩石的光照结果变得立体而不那么扁平。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image48.jpg)

再来看看另一个户外场景

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image49.jpg)

这里可以看到，地表以及低矮植被从上方采集的树叶的绿色反射光照

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image50.jpg)

以及这里的石头获取的来自地表的反弹颜色

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image51.jpg)

在夜晚的时候，来自太阳光的间接光比例就变得很低，因此场景的环境光变化主要来自于天光的直接照明部分。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image52.jpg)

在这张图里可以感受到一个较强的近似AO的效果，这个效果的数据基本上都是来自probe。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image53.jpg)

在这个视角下，就能看到由于天光的gradient（方向变化？）而导致的颜色变化，因为在屏幕之外有一个落日的效果，因此靠近落日方向的表面会被染色成橘色。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image54.jpg)

由于半透物件如玻璃、粒子等不能通过延迟管线完成渲染，这里还需要为前向渲染管线添加支持。具体做法为：

1. 在CPU上计算每个物件所能感知到的最近的probe
2. 将probe的相关参数作为shader constants传递到shader中，供前向渲染使用

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image55.jpg)

FC3还有较多的室内场景，室内场景的光照强度与复杂度跟室外场景差别显著，而这也是室内容易触发漏光的最主要原因。

上图就是一个典型的漏光问题的示例，其中室内采集到了户外的probe数据，从而使得地表被染色成了蓝色。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image56.jpg)

针对上述情况的应对策略相对简单：

1. 在离线为每个室内环境配置一个volume，并为该volume指定一个probe
2. 运行时会将该volume的geometry绘制到一个屏幕空间的mask buffer上，并对该buffer做模糊处理，以实现室内外光照结果的平滑过渡
3. 被volume覆盖的像素，光照计算时就从该volume配对的probe上获取光照数据，从而避免上述漏光问题

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image57.jpg)

这里还有一个问题需要解决，那就是远景物件，尤其是植被的ambient lighting，如果直接用天光的数据，那远景效果就会带有一种蓝色染色效果，看起来就不太正常。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image58.jpg)

为了解决上述问题，这里增加了一个俯视角（top-down）的2D遮挡图，这个图存储的遮挡信息来自于probe的可见性数据。为了做streaming，这里会以sector为单位，将该贴图划分成一个个的tile，每个sector对应于一个tile，在某个sector的probe streaming in的时候，就会触发对应tile的数据的更新。

在运行时采样的时候，就可以基于这个遮挡信息来判断当前的ambient数据是否能够取用probe上的颜色，从而屏蔽掉被遮挡区域的天光影响，同时这里还会存储每个位置的probe的高度，从而可以根据到probe的距离来调整染色的强弱（与地表反弹颜色的混合权重），实现更为真实的染色效果

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image59.jpg)

因为volume map的更新是发生在CPU的，如果GPU的读取与CPU的更新发生时刻重合的话，就有可能导致效果的闪烁。

解决这个问题的常用策略是采用double buffer，但这种做法会有额外的显存（内存）消耗，FC3采用的是另一种策略，即通过自定义的job scheduling。

如上图所示，SPU负责更新volume map，RSX负责GBuffer的计算与SSAO的计算，PPU则负责创建jobs并准备好相关的计算数据。里面的JTS是Jump to self command的简写（不是太明白作用）

因为GBuffer Pass的计算不需要用到volume map，因此会考虑将两者放到同时并行完成，在GBuffer以及SSAO完成之后，会等待volume map的更新完成，通过并行跟barrier等待的方式来解决前面的问题。

![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image60.jpg)



![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image61.jpg)



![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image62.jpg)



![](https://gerigory.github.io/assets/img/GDC/2012/Deferred-Radiance-Transfer-Volumes-Global-Illumination-in-Far-Cry3/image63.jpg)





## 参考

[[1]. 【GDC 2012】Deferred Radiance Transfer Volumes - Global Illumination in Far Cry 3](https://fileadmin.cs.lth.se/cs/Education/EDAN35/lectures/L10b-Nikolay_DRTV.pdf)
