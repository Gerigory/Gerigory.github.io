---
layout: post
title: 【GDC 2011】Lighting You Up In Battlefield 3
date: 2024-11-15
img: GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片1.PNG # Add image post (optional)
fig-caption: # Add figcaption (optional)
tags: [Battlefield, Rendering, lighting, GDC, 2011]
description: 本文分享的是战地3在GDC 2011上介绍到的一些光照相关的技巧
---
今天介绍的是战地3在GDC 2011上分享的寒霜引擎2的光照方案，分享者是Kenny Magnusson，是一位美术同学。照例，这里对工作内容做一个总结：

1. 采用的是延迟管线
1. 大尺寸静态物件用的是lightmap方案
1. 小尺寸静态物件跟动态物件则用的是lightprob方案
1. lightprobe不是PRT，而是用SH表达的来自各个方向的输入radiance，通过烘焙多套数据来实现TOD的支持
1. lightprobe的烘焙得到的是中间数据，目的是加速运行时的计算，降低运行时消耗。需要运行时计算的原因是希望支持破坏等动态场景的需要。

---

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片2.PNG)

介绍分三部分：
1. 过去的表现
2. 项目的需求或目标
3. 具体如何达成

最后对全文做一个总结

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片3.PNG)


![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片4.PNG)

过往的两个项目分别使用寒霜1跟UE3开发，两者都是前向管线，其中：
1. Bad Company有如下的一些值得注意的点
    1. 寒霜1的特点：
        1. 为户外场景设计，以动态破坏为主要特点
        2. 最多可以支持100+动态阴影

    2. 方向光阴影是动态的，采用三级CSM，都是1024的分辨率
    3. 每个物件最多受一盏点光影响
        1. 引擎最多可以支持3盏

    4. 没有SSAO与GI
    5. 大尺寸的物件如建筑会需要（静态）天光遮蔽效果，室内等区域则通过天光遮蔽volume来标注

2. 镜之边缘则有：
    1. 不是特别看重动态破坏效果，主要聚焦于City Landscape，因此lightmap+覆盖动态物体的probe就已经足够
    2. 通过烘焙的lightmap来实现静态场景的GI效果
    3. 通过预计算的light probe来对动态物体做relighting

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片5.PNG)



![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片6.PNG)

期望在保持对动态破坏效果支持的同时，还能保有镜之边缘的GI表现，下面对需求做进一步明确。

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片7.PNG)

 Battlefield BC 2（左）的室内光照表现与镜之边缘（右）的差距十分明显，这里期望能达成一致（室内有破坏）

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片8.PNG)

期望能够有较好的户外景色表现以及城市远景表现。

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片9.PNG)

反射效果对于提供一个鲜活可信的场景具有重要意义。

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片10.PNG)

有多光源，有破坏，一个非常自然的需求就是要能够支持光源的可破坏。

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片11.PNG)

当然，这里的目标不只是承袭之前的优点，还希望能够推陈出新。

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片12.PNG)

期望能够实现延迟管线所能够支持的那么多光源（或者说直接支持延迟管线）

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片13.PNG)

更多种类的shading model，比如皮肤的SSS

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片14.PNG)

甚至能支持半透的SSS效果。

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片15.PNG)

期望能够提升光照烘焙的效率。

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片16.PNG)

同时支持多职能以及职能间多成员的协同开发。

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片17.PNG)

期望给特效增加光照逻辑，使得表现跟场景能够较好的吻合。

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片18.PNG)

标配的bloom效果

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片19.PNG)

与之配套的更先进的Filmic Tonemapping效果

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片20.PNG)

期望在寒霜引擎中实现Enlighten方案。

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片21.PNG)

编辑器工作流也需要优化

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片22.PNG)

大多数游戏中主要关注specular跟diffuse lighting，且只关注一次反射，多次反射由于消耗高通常会被忽略。

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片23.PNG)

表面可以分为三种：

1. 完全反射
2. 完全吸收
3. 先吸收，后部分散射出去

对于反射属性比较强烈的表面，这里称之为highly specular

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片24.PNG)

先吸收，后散射（均匀向各个方向）的称之为highly diffuse

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片25.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片26.PNG)

这两者都会将接受到的光线返还给环境。

对于后续发生的多次反射效果则统统用间接光表示，或者这里用GI代指（实际上GI应该包含直接光），最常见的GI方案有两种：

1. 烘焙到lightmap
2. 给场景补光

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片27.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片28.PNG)

lightmap有如下特点：

1. 效果好
2. 需要时间烘焙
3. 需要制作2UV
4. 不支持TOD与动态物件

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片29.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片30.PNG)

补光方案有如下特点：

1. 耗费美术时间
2. 部分情景效果不佳
3. 性能差

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片31.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片32.PNG)

考虑到上述的问题，一个策略就是采用实时GI方案（如上述的Enlighten），Enlighten会给出每个点收到的光强颜色与主光方向（用于计算indirect specular）

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片34.PNG)

这里首先会对场景物件做区分处理，分为lightmap覆盖的以及lightprobe覆盖的

1. 前者对应的是不可移动的静态物件，可以接受lightmap光照，也会对周边环境的光照结果产生贡献。

2. 后者对应的是动态物件（或者小尺寸的静态物件，从性能与效果的平衡考虑，不用过于高分辨率的数据），仅接受场景其他静态物件的光照反射输入，不做输出。

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片35.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片36.PNG)

黄色表示lightmap覆盖范围，蓝色表示lightprobe覆盖范围。

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片37.PNG)

 

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片38.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片39.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片40.PNG)

lightmap需要的2uv是自动生成的。

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片41.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片42.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片43.PNG)

为了能够handle所有的radiosity数据（？），这里还需要一个简化模型（？）

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片44.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片45.PNG)



![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片46.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片47.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片48.PNG)

上面介绍了如何从detail model得到简化model

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片49.PNG)

简化模型会需要生成对应的lightmap数据。

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片50.PNG)

之后将高模的lightmap数据迁移到低模的贴图上，还是没解释这么做的意义是啥，用于给probe提供indirect incoming radiance？

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片51.PNG)

再来看lightprobe，通过volume来约束probe的生成区域，结果用grid存储，其实就是VLM的思路。

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片52.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片53.PNG)

每个probe的光照数据（仅包含该probe位置所接收到的来自四面八方的输入光照）用SH来表示

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片54.PNG)

probe数据的生成，需要先在离线走一个预处理pass，这个pass会搜集静态场景的结构，输出一些中间数据，这些数据后面会用于计算dynamic SH数据。

因为这个过程相对比较费（前面的场景大约需要20min），所以放在离线完成，不过由于仅当静态场景变化，才需要触发，所以还好。

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片55.PNG)

运行时的shading管线分为三个步骤：

1. 先完成lightmap跟lightprobe的数据更新
2. 再进行延迟管线Base Pass的渲染，得到GBuffer数据
3. 在lighting pass中，对前面的数据进行取用以完成最终的光照计算

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片56.PNG)

为了保障室内外光照结果的正确，避免室内物件受到来自天光的淡蓝色加持，这里还增加了一项叫做天光可见性的参数用于表征该位置可以接收到的天光的强度。

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片57.PNG)

室内环境贴图的颜色与强度会跟之前计算的dynamic radiosity有关。

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片58.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片59.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片60.PNG)

为了给户外的大尺寸物件照明，这里选择用SH来表达天光照射（为啥不用一张cubemap呢，这样可以得到正确的高光效果呀？）

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片61.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片62.PNG)

地形的lightprobe也是均匀摆放的，不过会自动贴合到对应的高度上

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片63.PNG)

也需要lightmap，两者的分辨率都跟地形的patch size有关。

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片64.PNG)

场景受方向光照射

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片65.PNG)

加了一盏绿色聚光灯

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片66.PNG)

对场景产生了color bleeding反射效果。

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片67.PNG)

这里会将一部分元素从光照体系中剥离出去，主要出于对灵活度的考虑，比如可以实现红色的天空、绿色的墙面的表现

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片68.PNG)

下面介绍一些实际工作中的一些经验建议。

对于复杂物件如可以破坏的房屋，可以考虑将房屋做拆分处理，不可破坏部分用lightmap（灰色），可以破坏部分用lightprobe（红色）。

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片69.PNG)

战地3开发了一个static radiosity maps系统（同样，不知道做啥用的），用于快速完成lightmap跟light radiosity（像是lightprobe SH计算所需要的中间数据？）数据的烘焙。

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片70.PNG)

在小尺寸的区域，比如室内，可以启用enlighten的实时计算部分以避免烘焙消耗

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片71.PNG)

对于大尺寸区域，则是提前烘焙好，运行时streaming

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片72.PNG)

只有在实时enlighten启用的时候，才会支持TOD功能。

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片73.PNG)

不过如果要做TOD，需要约束分段存储的数据的数目，这个会导致内存上的增长。

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片74.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片75.PNG)

需要了解电影的后处理逻辑，通常来说，color grading应该放到最后一个环节。

上面两图展示了color grading的作用：增强对比度。

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片76.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片77.PNG)

根据效果需要，选择合适的filmic tonemapping公式。

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片78.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片79.PNG)

新增lightprobe特性，相比于之前纯粹的lightmap方案的不足：

1. 内存增长了
2. 基于lightprobe的密度，会有一定的性能占用
3. 增加了编辑成本
4. 增加了烘焙成本

优点则是：

1. 相比于lightmap而言，精度更低，且有很大一部分实时计算环节，因此迭代效率更高
2. 可以更好的适配场景的变动
3. 提供了动态、静态物件统一的光照方案

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片80.PNG)



![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片82.PNG)

## 参考

[[1]. 【GDC 2011】 Lighting You Up In attlefield 3](https://media.contentapi.ea.com/content/dam/eacom/frostbite/files/gdc11-lightingyouupinbattlefield3.pdf)

