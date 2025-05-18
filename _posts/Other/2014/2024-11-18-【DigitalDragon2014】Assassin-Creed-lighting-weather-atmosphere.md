---
layout: post
title: 【Digital Dragon 2014】 Assassin's Creed 4 lighting weather atmosphere
date: 2025-4-21
img: Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片1.PNG # Add image post (optional)
fig-caption: # Add figcaption (optional)
tags: [Assassin's Creed 4, Rendering, lighting, weather, atmosphere, 2014]
description: 本文分享的是Assassin-Creed-4在Digital Dragon 2014上介绍到的一些光照相关的技巧

---

今天介绍的是刺客信条4在Digital Dragon 2014分享的光照、天气以及大气相关的渲染方案，分享者是来自育碧（蒙特利尔）的图形程序员Bart Wronski，照例，这里对工作内容做一个总结：

1. 光照方案
   1. 基于FC3的方案改进而来，原方案采用SH2存储数据，精度较低，导致光照细节缺失较多，不能满足项目需要
   2. 将天光与方向光的贡献拆分开来，且假设天气只影响光照颜色与强度，不影响光照路径
   3. 整体实现思路给出如下：
      1. 依然采用probe来存储数据，probe只布设在navmesh周围，probe间隔两米
      2. 通过烘焙8套数据来实现对TOD的支持
      3. 采用Normalized Radiance来存储光照结果（取中性颜色即白色作为输入光颜色），同样存储四个方向（basis）的数据
         1. 之后在运行时基于天气对输出结果进行调制
         2. 在运行时会基于法线对四个方向的烘焙数据进行插值，得到最后的输出irradiance
         3. 由于只烘焙了一层probe，对于距离probe较远的位置（高度），会基于高度对结果进行调制
            1. 会导致结果精度下降，可以考虑烘焙多层probe来优化

      4. 数据以sector为单位进行存储，在运行时可以通过streaming进行加卸载更新
         1. 为了避免CPU/GPU传输导致的卡顿，会延迟数帧取用

      5. 通过环境光模拟多次反射的效果，避免死黑问题
         1. 运行时会基于法线对ambient cube进行采样，之后与天光遮蔽数据相结合（sky occlusion，俯视图的深度图），得到天光照明效果

      6. AO计算
         1. 将AO分为多种不同粒度的信号数据，不同粒度的AO采用不同的技术来实现。
         2. 粗粒度的AO用的是WorldAO，通过对天光遮蔽贴图进行高斯模糊来得到对AO的模拟
         3. 细粒度的AO用的则是SSAO
            1. 采用了泊松圆盘的算法，通过少量的采样点实现较好的AO效果


---

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片2.PNG)

上图是整体效果表现

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片3.PNG)

先来介绍下背景：

1. 产品定位为次世代主机作品
2. 当时研发的技术需要同时被用于之前发布的作品，也就要能够兼容老的作品（硬件，较好的伸缩性）
3. 支持渐进式的对次世代的表现做迭代调优
4. 其他

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片4.PNG)

整体介绍分成两部分：

1. 光照（直接光与间接光）
   1. 相对于AC3的优化改进
   2. GI方案
   3. AO方案：基于temporal-supersampled的SSAO方案
   4. 多分辨率的AO
2. 大气与天气
   1. 下雨相关材质方案
   2. 屏幕空间反射
   3. GPU模拟的雨效
   4. 体积雾

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片5.PNG)

先来看看光照部分

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片6.PNG)

先来看看AC3的光照表现，尤其关注红圈部分。可以看到，被阴影覆盖区域（间接光主导）过于flat（间接光层次感不够，一句话总结就是AO表现不佳），这个会表现为两个明显的问题：

1. 表面的凹凸效果不明显，对应于画面过于平整
2. 缺失了物件之间的位置关系（等同于直接光照亮区域缺失了阴影）

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片7.PNG)

针对这个问题，拟采用的方案需要满足如下几点要求：

1. 允许在离线烘焙部分数据
2. 要支持开放世界，能够覆盖物件稀疏、密集等多种应用场景
3. 支持动态的天气与时间
4. 在当前主机上能够跑到1MB的显存与1ms的单帧GPU消耗
5. 对于当前的工作生产流不要产生过大的影响

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片8.PNG)

之前开发过一套支持TOD与大世界的GI方案（详见FC3的分享），因此想先将这套方案集成进来试试（引擎变迁，大约一到二人周的投入）

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片9.PNG)

经过验证，FC3方案所列举的优点在原型场景中得到了较好的验证，不过在验证的过程中也发现了该方案的问题：FC3方案在野外表现较好，在城区等需要高精数据的区域表现就会比较差，表现为：

1. GI变化过于低频，导致城区画面的对比度过低
2. 在白天，随着TOD的变化，GI的响应不是太明显

经分析主要在于Probe中存储的数据（2阶SH）精度过低，无法存储相对精细的物件之间的遮挡关系（提交SH阶数能否解决这个问题？）。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片10.PNG)

基于上述评估，认为需要有一个新的方案，该方案研发前有一些基于对生活的观察发现，将基于这些发现来设计方案：

1. 在晴朗的天气下，大部分的GI数据都是由方向光（太阳）贡献的
2. 在现有的引擎功能实现中，提供了较好的基础用于实现方向光与天光（以及他们的间接光反射）的分离
3. 天气只会对光照的强度、颜色产生影响，而不会影响光照的传播与计算逻辑（意思是可以将天气的影响留到最后作为一层叠加）
4. 对于只考虑diffuse间接光的情况，可以通过预计算的方式基于基色、法线与阴影信息来存储一些光照相关的中间数据

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片11.PNG)

这里展示的是最终的方案表现？

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片12.PNG)

新方案的名字叫Deferred Normalized Irradiance Probes，下面看看实现细节。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片13.PNG)

先来看看什么叫Normalized Irradiance（Radiance考虑方向，Irradiance不考虑）。

所谓的Normalized Irradiance，指的是按照传统方式来计算得到的Irradiance，不同的是，这里的计算过程不考虑入射光的颜色，统一用中性颜色（也就是白色）来表示，但是需要存储光照的阴影信息（是否需要考虑光强？）

同时，这里还说到了一点，那就是不考虑多次反弹的情况，为了避免（pitch-black）死黑的情况，这里会用一个环境光（ambient）常量来模拟（多次反弹效果）。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片14.PNG)

整体过程分为离线跟运行时两部分，先看看离线部分的大概：

1. 基于GPU Cubemap Capture与GPU卷积来完成针对四个Basis Vectors（基向量）的Irradiance的计算
2. 覆盖64x64m的单个sector会共用一张大的shadowmap
3. 整体场景的probe分布是一个2.5D的空间结构，对应的probe数据会被存储在一张2D贴图上（会做压缩）

接下来看看具体细节

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片15.PNG)

首先会基于navmesh来完成probe的摆放（剔除掉不可达区域的probe数据，避免浪费）。

接着会对相邻probe的数据做重用（如何重用？）以解决插值问题（具体指的是什么？）

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片16.PNG)

针对TOD，会进行8次Capture，时间选择的是：3AM, 6AM, 9AM, 12PM, 3PM, 6PM, 9PM。

Probe间隔是2m

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片17.PNG)

对于每个probe，会烘焙8个cubemap（对应8个时间点，每3个小时一个）：

1. 离线烘焙的时候，太阳光会被设置为白色，从而可以在运行时基于天气的变化来动态调控颜色等变化
2. 这里还会设置一个optional的环境光属性，以模拟多次反弹

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片18.PNG)

对于每个cubemap，由于需要考虑四个方向（basis vector），因此总计需要存储3x4=12个数据，其中3代表的是irradiance的颜色（三通道），最终12个数据会被存储到3张RGBA cubemap中。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片19.PNG)

之后cubemap的数据会以sector为单位进行打组。每个sector包含16x16个probe。上图中的每个像素代表的是一个probe的（一个通道）数据。

每个组的数据会作为一个entity存在，之后跟其他物件一样，走streaming逻辑。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片20.PNG)

如果不做优化，完成一张地图的probe数据的烘焙，大概有如下的计算结论：30 000 probes, 6 cube faces x 8 time of day = 1 440 000 renders -> 400 mn(6h40)，耗时太久，需要优化。

> P.S 如果不做之前说到的基于navmesh的剔除的话，probe数目更多，能去到110 000，耗时能到26h

针对上述情况，做了如下的一些优化：

1. 对参与cubemap烘焙的数据进行限制，比如限制far plane的距离，以及逐渐减少参与烘焙的物件数目（越远越少）等
2. 针对不同时间段的cubemap，可以对GBuffer数据进行复用，这套数据不会随着时间而变化
3. 同一个sector上的所有probe不再单独烘焙shadowmap，而是共享一张大的shadowmap
4. 针对frustum culling，设置专门的简化计算逻辑
5. 为了避免lock贴图导致的CPU阻塞，这里采用了延迟取用逻辑

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片21.PNG)

接下来看看runtime部分。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片22.PNG)

对probe数据的取用，首先需要完成irradiance的denormalization，这个过程是放到PS上执行的，在PS3上大概耗时0.1ms。

具体计算过程给出如下：

1. 基于当前时间计算需要采用的cubemap，之后基于当前位置计算采样坐标
2. 之后基于当前位置到相机的XY方向上的距离，对采样结果进行插值，得到一个neutral value。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片23.PNG)

接下来看看怎么基于irradiance得到间接光（上图的左边部分）：

1. 先得到对应于四个basis vector的4个irradiance
2. 之后基于当前像素的法线来对上述irradiance进行插值
3. 另外上述插值得到的结果是对应于场景不透像素表面的数值，之后如果想要得到高于表面的某个位置的间接光，会基于当前数值经过一个计算，逐渐过渡到一个neutral value上

再来看看怎么得到天光（上图右边部分）：

1. 基于法线对ambient cubemap进行采样得到ambient颜色
2. 将上述颜色与天光的遮蔽数据（可见性）相结合，得到最后的天光照明结果。

将间接光（主光源）与天光结果相结合，得到中间的照明结果。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片24.PNG)

接下来对照明结果的组成元素进行拆解展示，上图是直接光部分。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片25.PNG)

这是天光（叠加了AO）部分

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片26.PNG)

这是（主光的）间接光部分。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片27.PNG)

这是所有的光照结果叠加到一块（还加上了SSAO）之后的结果表现。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片28.PNG)

将光照结果与基色叠加到一起，得到了最终结果。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片29.PNG)

这里展示了场景中的probe数据布置。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片30.PNG)

来看看GPU的耗时：

1. PS3、XBox 360硬件下，在未开启stencil mask优化（跳过天空与海洋部分）的时候，全分辨率计算耗时1.2ms
   1. 在上述消耗的基础上，如果叠加CSM（包括cascade的选择与PCF过滤），耗时增加到1.8ms
2. 在PC与次世代主机上，光照计算的耗时相对于shadow mask计算的耗时则可以完全忽略

再来看看存储的消耗：

1. 在玩家周边，会同时存在25个sector，每个sector包含16x16个probe，每个probe包含8套cubemap，每套cubemap包括3张RGBA cubemap，最终显存占用为：25 RGBA textures sized 48x128 = 600kb of VRAM
2. 如果考虑PC，由于DXTC的存在，且我们同一时刻只有两套（TOD）cubemap，那显存的占用则基本可以忽略

再来看看CPU的消耗：

1. CPU的消耗主要在于对当前所需的world height data的解压缩，即使使用了向量运算，最终的计算耗时依然是不可忽略的
   1. 同时，解压后数据对内存的占用也是不能忽略的

总的来说，更新耗时大约为0.6ms，不过有些逻辑实际上并不是十分必要，比如可以只在需要的时候，触发高度数据的更新等。

前面说了probe的数目，在不做处理大约是11000个，限定到navmesh上，则是3000个，在单个GTX 680上，构建8个时间段的数据大约需要8分钟，因此不用做分布式。

不过这里也做了增量的烘焙以及编辑期的异步烘焙逻辑

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片31.PNG)

后续工作：

1. 将irradiance basis替换成其他更高精度的格式
2. Half-Life 2的basis，其“wrap-around"向量是朝下的，导致效果并不是很好，需要优化一下
3. 权重没有归一化，导致部分方向上的光照强度过大
4. 在边边角角区域容易出现漏光问题

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片32.PNG)

5. 尝试增加probe的密度以提升精度，同时支持分层probe，而非像现在这样通过height blend的方式来实现高度上的光照变化
6. 放弃“normalized” irradiance，尝试采用多个天气presets来替代
7. 添加对多次反射的支持
8. 尝试将部分Probe的更新放到GPU上

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片33.PNG)

这是场景的AO表现

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片34.PNG)

这里对AO的实现算法做了优化，主要基于两层扩展：

1. 其一是借鉴了McGuire的算法
2. 其二则是自研的时域超采样算法，与传统的为不同的frame设置不同的采样pattern不同，这里采用了类似泊松圆盘的采样策略，每帧旋转一个角度，得到三种不同的pattern，通过时间对三种pattern进行混合，可以得到接近3倍采样数目的效果表现，这里需要在数据复用的时候，做好判断，拒掉错误数据。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片35.PNG)

这里用三种颜色代表了一种采样pattern分别旋转120度与240度之后的样子，下面看下具体表现

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片36.PNG)

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片37.PNG)

 噪点得到了较好的平滑。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片38.PNG)

这里有个视频。。。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片39.PNG)

针对AO，有如下的一些结论：

1. 仅使用SSAO，没有办法完全表达天光的遮蔽效果
2. 即使在SSAO的基础上，通过不同的计算半径叠加（多分辨率方案，参考下面介绍），得到的结果也不能满足需要（？）
3. 想要得到较好的效果，最好的方法就是将AO拆解成多个不同频率带的信号
4. 针对不同的频率带采用不同的算法来计算

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片40.PNG)

这里展示了Inigo Quilez提出的多分辨率方案的计算结果，将场景的AO分解为不同尺寸的遮蔽，之后将这些遮蔽数据叠加得到最终的结果。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片41.PNG)

World AO是在刺客信条3提出的，用于为建筑、高大乔木等大尺寸物件提供遮蔽效果的AO方案（天光遮蔽），具体可以参考GDC 2013上St-Amour的分享。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片42.PNG)

在刺客信条3中World AO的表现如上图所示：

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片43.PNG)

这里对World AO的算法做一个简单介绍，总体分成离线跟运行时两个环节。

1. 离线阶段
   1. 从顶视角绘制场景的深度
   2. 之后对深度图按照7x7的filter size进行高斯模糊，结果写入World AO中
      1. 高斯模糊可以将高低落差通过blend的方式传递给周边区域，而AO对应的遮蔽关系也可以理解为身边遮挡物的遮挡程度，落差越大，遮挡程度越高，通过这种方式来建立二者的联系
2. 运行时阶段
   1. 对World AO贴图进行采样，并基于采样结果来估算遮挡物的高度
   2. 基于法线的XY分量对偏移量进行采样（作用是？）
   3. 将计算得到的AO项叠加到天光的环境光部分上（不要叠加到其他部分）
      1. 这里的AO跟第一步采样的AO的关系是？

整体算法执行耗时低，不过有如下两点不便：

1. 效果的好坏依赖于美术同学对magic value的手动调校
2. 场景如果可以用heightfield来表达就没问题，但是如果存在中空的孔洞（多层结构），就不太行了

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片44.PNG)

依然是World AO在AC3（刺客信条3）中效果

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片45.PNG)

这里是World AO启用之前的老式AO方案，用的是ambient cube，时间大约是晚上7~8点的样子，这时候光照方向接近水平，场景处于阴影之中，Ambient cube没能提供充足的间接光遮蔽效果，导致画面偏扁平，法线的凹凸效果也被掩盖了。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片46.PNG)

叠加了（间接）反射光照之后，表现如上图所示。反射光照的获取需要考虑方向（当前像素的法线方向），同时考虑阴影遮蔽，计算得到的光照不但会跟随方向而变化，也会跟随位置而变化。

经过这个处理之后，在地表上的凹凸效果就出来了。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片47.PNG)

将反射的间接光与（通过光照cubemap表示的）天光照明结果叠加到一起之后，就能够得到具有多光照变化细节的场景照明结果

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片48.PNG)

最终的AO包含了World AO（参考GDC 2013的分享）跟SSAO

这里来看下probe的布局，probe按照2m的间隔摆放，覆盖navmesh能够抵达的区域。上图中的绿色线条表示相邻probe因为遮挡原因无法被使用的情况，这时候就不能对这些遮挡的probe进行复用，否则有漏光问题。

图中还展示了irradiance vector basis的四个方向，红绿蓝方向指向上方，白色指向下方以捕捉来自地表的反射光照。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片49.PNG)

下面看看天气与大气相关内容。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片50.PNG)

先看下背景：

1. 加勒比热带气候不好预测
2. 气候变化速度快
3. AC3中已经有了一套天气方案
4. 不过需要对其进行更新迭代

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片51.PNG)

基于GPU的程序化生成雨水涟漪效果

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片52.PNG)

无涟漪时的表现

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片53.PNG)

添加涟漪后的表现

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片54.PNG)

另一个示意图

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片55.PNG)

整个涟漪的实现分为三个部分：

1. 第一个部分是涟漪的创建过程，通过CS完成，这个过程会给出涟漪的位置、生命周期等基础信息
2. 第二个部分则是基于第一个部分的输出，通过PS将涟漪的形状写入到SDF贴图上
3. 第三个部分则是将上一步输出的SDF转化为法线贴图

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片56.PNG)



![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片57.PNG)

涟漪形状的绘制过程，由于是多个geometry的重复执行，因此这里采用了Geometry Shader

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片58.PNG)

有如下的一些实现细节：

1. 涟漪会通过一个单一的pass将之应用到屏幕空间的buffer，并基于这个buffer对现有的法线buffer结果进行扰动
2. 会基于前面的world ao贴图来遮挡不必要的涟漪效果（室内）
3. 涟漪的生成、更新与贴图生成耗时大约在0.2ms
4. 对法线的扰动可以用一个单独pass，或者与光照pass结合到一起

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片59.PNG)

针对雨天的湿润材质，有如上的一些细节：

1. 表面的湿润度参数会被写入到GBuffer中
2. 上述参数可以支持离线烘焙得到，或者通过运行时动态计算得到
3. 在光照pass中会基于这个参数来对gloss、albedo进行计算
4. 湿润度越高，gloss程度越高，albedo就越暗
5. 技术实现路径与AC3差不多，不过这里增强了屏幕空间反射效果

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片60.PNG)



![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片61.PNG)

上面两图展示了屏幕空间反射效果的作用

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片62.PNG)

对于雨水飘落效果，也期望能做到高度volume effect，即通过程序（GPU，CS或者GS）生成，但是效果则是由美术驱动。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片63.PNG)

雨水效果完全是在GPU上实现的，包括模拟与渲染。

1. 会通过CS来完成雨水的生成与物理模拟
2. 之后通过GS将点转化成雨水的几何形状（线条等）
3. 为了避免性能问题，同时又能保证较为平滑的雨水出现效果，这里将场景划分为一个个的cell，之后基于frustum与cell的相交情况，触发对应cell的雨水计算逻辑

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片64.PNG)

对于雨水的程序化模拟生成过程，需要考虑多个方面：

1. 希望能够支持雨滴的质量与形状的随机化
2. 要考虑风力与重力的影响
3. 要能够支持场景物件的遮蔽效果，避免室内的湿润、雨水出现（低分辨率，128x128的遮挡贴图）

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片65.PNG)

这里展示了遮挡贴图的大致样子，这里是没有包含动态物件（地表都没有）的，但是渲染性能消耗非常低。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片66.PNG)

还有一些细节：

1. 遮挡贴图跟world ao是共用的，因此消耗可以均摊（不过分辨率跟精度有所不同）
2. 会基于depth buffer执行一遍屏幕空间的碰撞检测
3. 在检测到碰撞的位置，生成一个粒子（水花）

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片67.PNG)

雨水的更新过程描述如下：

1. 基于遮挡贴图，会在可见cell的随机位置生成一些雨滴，并将之叠加到上一帧的buffer上，这一步通过CS完成
2. 基于雨滴的信息（速度、质量等）完成雨滴位置的更新计算逻辑。这一步会考虑雨滴运动过程中与屏幕空间depth buffer的碰撞情况
   1. 碰撞后会生成一个splash效果，这个效果会生成6个相对大尺寸的雨滴，这些雨滴的生命周期会被设置得很短
3. 通过GS对雨滴进行渲染
4. 这一帧得到的雨滴位置的buffer会在下一帧被使用。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片68.PNG)

这里有个视频

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片69.PNG)

再来看下性能消耗，整体表现完美符合预期：

1. CS对雨滴位置的更新耗时基本可以忽略。
   1. 这个消耗还包含了一部分不可见雨滴的更新计算
   2. 省略了CPU/GPU之间的同步与等待耗时
2. 这里还有一些实现上的技巧
   1. 运行时随机生成雨滴过程并不那么容易，这里的做法是将随机过程放到离线，运行时对数据进行取用
   2. 检测到雨滴碰撞后，会需要对生成的雨滴再执行一次CS
3. 即使雨滴的位置更新是放到CS的，GS的消耗还依然比较高，成为整个方案的消耗瓶颈，后面需要对这个地方做重度优化
   1. 如果不做CS优化，整个计算过程放到GS上，会需要耗费20ms。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片70.PNG)

针对GS的优化：略。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片71.PNG)

下面看下体积雾的一些实现技巧。体积雾的实现对应于一系列特性效果：

1. Fog，Mist，Haze
2. God Ray
3. Light Shaft
4. Dusty/Wet air
5. Volumetric Shadows

这些特性其实描述的都是大气的in/out scattering效果。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片72.PNG)

在大气散射方程作用下，可以支持多光源的正确光照表现。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片73.PNG)

这里展示了最终的体积雾效果。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片74.PNG)

这里介绍了一些实现细节，在主机上，整体只需要1.1ms即可完成整体模拟，具体细节可以参考GDC 2014的演讲内容

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片75.PNG)

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片76.PNG)

再来两张图展示下最终的结果。

![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片77.PNG)



![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片78.PNG)



![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片79.PNG)



![](https://gerigory.github.io/assets/img/Other/2014/Assassin-Creed-4-lighting-weather-atmosphere/幻灯片80.PNG)



## 参考

[[1]. 【Digital Dragon 2014】 Assassin's Creed 4 lighting weather atmosphere](https://bartwronski.com/wp-content/uploads/2014/05/assassin_s-creed-4-digital-dragons-2014-no_notes.pdf)
