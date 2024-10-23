---
layout: post
title: 【Siggraph 2016】the devil is in the details
date: 2024-10-17
img: Siggraph-2016-the-devil-is-in-the-details/幻灯片1.PNG # Add image post (optional)
fig-caption: # Add figcaption (optional)
tags: [idTech, Rendering, Siggraph, 2016]
description: 本文分享的是idTech在Siggraph 2016分享的一些渲染相关的技巧
---
今天介绍的是idTech在Siggraph 2016分享的一些渲染相关的技巧，分享人是Tiago Sousa & Jean Geffroy，照例，这里对工作内容做一个总结：

1. 

---

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片2.PNG)

本文的重点是渲染，且着重关注少数几个关键特性。

上图给出了id software的工作目标，包括帧率、分辨率、效果、美术同学工作效率等。

因为工期紧张，因此总体的工作原则是KISS（keep it simple stupid），即采用尽可能简洁的工作策略。

这里需要提到的一点是，由于提前做了精心设计，因此最终版本中只包含100个左右的unique shader，大约350个PSO（太省了）。

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片3.PNG)

在60 fps的帧率下，各个pass的耗时统计：

- shadow部分启用了cache逻辑，耗时约3ms
- 耗时最高的为不透明部分的绘制，耗时约6.5ms
- 其他耗时则如上图所示，总体来说，耗时比较节省

这里有几点需要关注：

1. 采用的既不是前向渲染，也不是延迟渲染管线，而是二者的混合，这种做法对于他们的项目来说，更容易达到性能与质量的平衡，所以，对于特定项目而言，定制才是最佳的路，虽然成本会更高
2. 前向部分：
   1. 使用前向管线的好处是，可以收获一些前向管线独有的优势，比如可以开启MSAA，还有一些其他质量上的收益（接下来会说到）
   2. 前向管线也带来了一些约束，比如光照跟shading相关的数据都需要尽可能的提前准备好（目的是？），比如
      1. 光源相关的数据都需要提前准备好，方便在计算的时候进行索引
      2. 阴影也需要做一些处理（这个跟前向有什么关系？），比如shadow cache以及一些smart composite策略
3. 延迟部分：只输出那些必要的特性（反射、高光遮蔽等）所需要的数据
4. 不过上面的数据展示也只是一个示例，实际情况中后处理的消耗会随着情景的不同而有所不同
   1. 比如开启DOF的话，消耗会高一些等（在主机跟vulkan下，后处理是放到Async Compute中执行的）
   2. 比如部分情况下，特效会带来较高的overdraw，这个也会导致性能数据的波动

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片4.PNG)

这里来介绍一下光照与shading的计算逻辑，总体思路是对下述两个talk中的方案的继承，实际上是clustered rendering策略，即基于三维的空间划分，得到的cluster中计算都会被哪些光源影响，从而降低光照计算的复杂度，具体参考[milo的分享](http://miloyip.com/2014/many-lights/)：

- “Clustered Deferred and Forward Shading”, Ola Olson et Al.
- “Practical Clustered Shading”, Emil Person

采用这种管线有如下的一些优势：

1. 透明物件的绘制不用与不透明物件分割开来
2. Depth相关的两点没看明白

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片5.PNG)

这里介绍了clustered rendering中cluster的计算逻辑：

1. 在CPU上基于Frustum的覆盖范围进行划分（没有考虑depth的range？），出于效率考虑，用了多线程计算，每个线程负责一个depth slice
2. 采用的是person的方法，在对数划分的基础上对near/far plane做了处理，基于处理后的near/far plane做对数划分
   1. 采用对数划分，是因为近处精度要求高，所以需要分配更多预算
3. 之后对cluster中的item做归类处理：
   1. item数据包含环境光probe、贴花以及光源（这三者都可以，也都应该做延迟计算）
   2. 归类的方式是将item的OBB（或frustum）做光栅化，之后与与当前cluster屏幕空间的xy以及depth bounds做比较

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片6.PNG)

前面介绍的是常规做法，这里给出优化做法，即将OBB/Frustum光栅化到屏幕空间来判断是否相交的做法改成Plane与AABB的相交（包含）测试，基于这个做法，性能会有较大提升：

1. 一个Cluster在Clip Space中就是一个AABB，而OBB跟Frustum可以分别转化为6个或者5个Plane
2. 由于对于每个Plane的计算过程是相同的，因此可以使用SIMD来做运算的加速，从而提升计算性能

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片7.PNG)

最终得到的cluster数据结构包含两个list：

1. Offset list：这是一个3D数组，尺寸为[Grid Dim X，Grid Dim Y，Grid Dim Z]，每个数组元素的长度为64bits
   1. 这个数组中存储的是每个cluster对应的数据在Item list中的起始位置
2. Item list：这是一个一维数组，存储的是所有item的信息，item类型为光源、环境光probe以及贴花，其中
   1. 每个item包含24个bits，其中（感觉这里有优化空间，可以留出两位来表示item类型，剩余位数用于表示索引，不是更优吗？）
      1. 前面12位分配给光源，表示的是当前item对应的是哪一个光源（索引）
      2. 中间12位分配给贴花，表示的是当前item对应的是哪一个贴花（索引）
      3. 后面8位分配给环境光probe，表示的是当前item对应的是哪一个环境光probe（索引）
   2. 每个cluster最多包含256个item
   3. 最差情况下，每个cluster都有这么多数据，因此有上图中的最差情况下的该list的尺寸
3. Grid分辨率目前采用的是16x8x24，还是比较低的
   1. GCN部分没看明白？

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片8.PNG)

这里给出cluster debug view，其中红色表示有10个以上的volume overlapping，而绿色表示5个以下的volume overlapping，橙色则是二者之间的，文中介绍，虽然这里还有优化的空间，但是性能表现已经够用了，所以就不改了，直接发吧。。。

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片9.PNG)

管线部分介绍完了，下面来看看如何给场景增加各种各样的细节：

1. 依然开启了VT特性（Mega-Texture），不过相对于此前的引擎版本，做了一些升级
2. VT覆盖了多种类型的数据贴图，从Albedo到Lightmap等：
   1. VT Page做了BC3压缩
   2. 开启了硬件sRGB支持（包含了一系列的特性，比如将线性颜色写入framebuffer时，硬件会自动转成sRGB格式，支持对sRGB贴图做插值、mipmapping等计算，最关键的是基本无性能影响，参考[Wiki](https://en.wikipedia.org/wiki/SRGB#:~:text=sRGB%20is%20a%20standard%20RGB,and%20the%20World%20Wide%20Web.)）
   3. 优化了mipmap的生成算法：参考了Toksvig的[做法](https://www.jianshu.com/p/efabea28ed1a)，将用于消除高光锯齿的数值烘焙到smoothness部分，从而以较低的消耗来移除远景部分的高光锯齿问题
3. VT request的feedback buffer直接输出到final resolution（？）
4. 通过Async Compute完成转码（什么情况下需要？），在数据不相关的时候，这个步骤消耗较高
5. VT本身的缺陷还依然存在，比如
   1. 基于反馈的texture streaming就会带来贴图的popping闪现问题
   2. 只能应用于不透明物件
   3. Page边缘的瑕疵
   4. 滤波问题
   5. dependent lookup带来的额外消耗
   6. 高清贴图跟BC压缩贴图混用带来的异常等

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片10.PNG)

贴花常见的策略如mesh decal或者延迟decal，在trouble case的处理上会比较耗时间（没有具体说明是哪些trouble case？），这里给的策略是将贴花嵌入到正常物件绘制的光栅化逻辑中。

上下文没有给出具体的实现说明，根据已有的信息推断实现过程，可能的策略为：

1. 通过cluster统计出各个cell关联的贴花列表
2. 在物件光栅化的时候，仿造lighting计算，对贴花数据做投影采样
3. 为了避免单个物件在遍历多个贴花时的消耗，这里将贴花放到VT（8k x 8k分辨率，BC7压缩模式）中，从而可以在一个pass中完成多个贴花的遍历

这种策略可以保障在depth不连贯的区域以及跨多个物件的情况下，都能有正确的表现，除此之外，还有一些前面的方法所不具备的优点：

1. 可以很容易实现贴花法线跟依附物法线的混合
2. 支持mipmapping与各向异性效果
3. 支持半透贴花
4. 支持多层贴花的自定义排序
5. 不会因为贴花带来drawcall的新增

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片11.PNG)

贴花实现的一些细节介绍：

- 哪些物件需要受贴花影响是按照上述的box projected的计算逻辑给出的，被该box覆盖的物件的部分就需要被影响
- 对于每个贴花，在做贴图采样的时候，还需要考虑缩放跟偏移，不过由于需要依赖于计算得到的uv来做贴花的可见性clip，因此这部分没有直接放到box projection的矩阵运算中

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片12.PNG)

关于贴花的其他一些信息：

1. 贴花的布置是美术同学手动完成的，包括每个贴花的配置参数
2. 每一帧可见的贴花的数目（还是贴图分辨率？）限制在4k，通常是1k及以下
3. 美术同学会需要设计贴花的可见距离以实现消耗的lod处理，这个距离会跟画质等级有关系
4. 场景贴花只对静态不可形变的物体生效

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片13.PNG)

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片14.PNG)

上面两图展示了贴花的实际效果。

有的时候，会需要通过多层贴花叠加来提供更为真实的细节，这里当然会有overdraw的消耗，通常这个消耗也会跟屏幕覆盖率有关系。

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片15.PNG)

针对玻璃的各种效果，通常也是通过贴花来完成，如玻璃上的薄雾、水雾凝结、血渍等

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片16.PNG)

接下来介绍光照部分，有如下的一些关键要点：

1. 针对不同的物件（透明、不透等），采用一条统一的光照路径（同样的计算逻辑）
2. 不存在shader变体焦虑
   1. 所有静态物体都走同一条shader计算路径
   2. 更好的避免渲染时的上下文切换
3. 针对不同的光照分量，这里总结如下
   1. indirect diffuse部分，对于静态物体而言，会使用lightmap，动态物体则基于irradiance volume（PRT？）
   2. indirect specular部分的反射计算来自于三部分：环境光probe、SSR以及高光遮蔽
   3. 动态光源，只考虑直接光部分，做动态计算+shadow即可

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片17.PNG)

考虑贴花跟光照部分，每个物体的渲染shader伪代码给出如上：

1. 遍历贴花，基于可见性判断是否跳出贴花相关计算，不跳出则执行贴图的读取与混合
2. 遍历光源，判断是否受该光源影响，受影响则计算BRDF，叠加阴影并做光照的累加

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片18.PNG)

来看下阴影部分的实现细节：

1. 阴影贴图合并成了Atlas
2. 对于符合条件的阴影做了Cache处理，针对不同平台，在分辨率上以及数据格式上做了差异化处理
3. 对于同一盏光源的阴影贴图，会基于距离
   1. 调整分辨率（甚至格式？）
   2. 调整更新策略
4. 用了proxy mesh代替原始mesh来生成阴影
5. 对于光源不变的情况来说，这里会根据具体情况来做区别处理
   1. 首先需要cache静态物件
   2. 其次，针对参与投影的物件是否会有更新来做不同处理
      1. 有更新的话，需要在cache部分上叠加动态的
      2. 无更新那就直接使用cache贴图（不做copy & draw）
6. 将上述方案的控制参数暴露给美术同学

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片19.PNG)

1. 除了shadowmap合并成atlas之外，每盏光源对应的shadow绘制的投影矩阵也需要packed到一起，之后根据光源的索引进行取用
2. 为了降低VGPR（寄存器）压力，这里将所有类型光源（包括方向光）的PCF阴影计算逻辑统一成一套代码（不用为不同类型编写单独的实现逻辑，也就不用占据更多的寄存器？）
3. 方向光的特殊处理
   1. 相邻等级之间会通过dither做过渡（UE没有做这个处理）
   2. 只做一次采样，不做两次采样+混合，可以降低消耗
4. 尝试了VSM以及相关变种，发现存在各种瑕疵，或许对于前向管线而言更为合适

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片20.PNG)

针对FPS游戏，在手臂处开启跟关闭自阴影会有较大区别，这个主要是通过一张单独的shadowmap来实现支持，在主机（性能吃紧）上会关闭这个特性。

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片21.PNG)

clustered 管线下，光照计算逻辑尤其需要关注寄存器压力，这里有一些使用tips：

1. 对于有较长生命周期的向量数据，可以考虑转成标量，同时调整数据格式
2. 尽量缩短寄存器的常驻时间
3. 减少嵌套循环，从而降低最差情况下的寄存器占用
4. 减少分支（多分支寄存器占用叠加，如果是动态分支就没事了吧？）
5. PS4上只有56个寄存器，PC上会高一些
6. 对于不同的GPU品牌，使用倾向也有所不同，比如
   1. 英伟达芯片倾向于使用UBO/ConstantBuffer等
   2. AMD则倾向于SSBO/UAV

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片22.PNG)

Transparents are generally FX from game team

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片23.PNG)

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片24.PNG)

Observation
Particles are generally low frequency / low res
Maybe render a quad per particle and cache lighting result ?
Similar to Texel / Object space Shading ( amd ), but lighting only
Decouples lighting frequency from screen resolution = Profit
Lighting performance independent from screen resolution
Adaptive resolution heuristic depending on screen size / distance
E.g. 32x32, 16x16, 8x8
Exact same lighting code path
Final particle is still full res
Loads lighting result with a Bicubic kernel.

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片25.PNG)

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片26.PNG)

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片27.PNG)

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片28.PNG)

I’m asked frequently about the post processing on DOOM / idTech – fyi it’s essentially my 2013 Siggraph lecture

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片29.PNG)

The GCN architectures features a scalar unit that can be leveraged by shader code to share some work within a wavefront. In particular, it can be really interesting to fetch data through this scalar unit rather than through vector memory operations. This has a few benefits. More data can be fetched at once (64 bytes vs 16 bytes). The data can be stored in SGPRs, thus potentially saving some precious VGPRs. Finally, since the data is scalar at this point, branching is guaranteed to be non-divergent, meaning that both code paths do not have to executed. This can be a powerful lever to speed up some rendering passes.

Something to bear in mind when writing code using scalar data fetching is that we can expect VGPR savings only if this is the main code path instead of a fast path that can only be dynamically enabled. If multiple paths can be executed, register pressure cannot be lowered.

Let’s have a look at how we can leverage this scalar unit for our main opaque pass, which takes about half of the GPU frame duration.

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片30.PNG)

This is a pretty standard arena featured in Doom. Let’s have a look at access patterns for our clustered forward shading.

In green, we can see all the waves that only access one node from the cluster. This covers the majority of the screen, and naturally matches the setup of the cluster cells. We can easily exploit this to speed up how we fetch data. Let’s focus now on those wavefronts that are reading from different cells.

We can see that those, in red, still cover an important part of the screen. However, this isn’t telling the whole story. Let’s look more in depth at the actual lighting data that’s being fetched from those cells.

What we’re looking at now is how much data is being shared across all threads within a wavefront. In blue wavefronts, all threads are accessing the exact same light and decal data. Red waves have 5 or more items that aren’t being access by every single thread. As we can see here, the vast majority of cluster data, meaning lights and decals, are being accessed in a very coherent manner within one wavefront. Even when touching multiple cells, the content of those cells is mostly identical, and that’s a property we should try and leverage.

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片31.PNG)

We’ve seen that with a clustered lighting approach, most wavefronts only touch one cell. This is mostly independent from geometric complexity. But the interesting part is that even when touching multiple cells, most of the actual lighting data is still shared, because lights and decals often overlap across multiple cells within the cluster. Overall, threads within a given wavefront mostly end up fetching the exact same data.

This means that independently fetching this data per thread is clearly not optimal, since we’re not exploiting this convergence at all. What we could do instead is serialize the way we’re gathering the data so that we can use the scalar unit.

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片32.PNG)

First, let’s review our setup. Every cell within the cluster stores a sorted list of light and decal offsets. By the very nature of the algorithm, every thread within a wave will potentially be accessing a different cell, and therefore end up iterating on those sorted arrays independently from the other threads.

What we want to do is serialize this iteration. In a simplified example where 3 threads are independently iterating over [A, B, C], [B, C, E] and [A, C, D, E], we could instead serially iterate over [A, B, C, D, E]. In total, we’d be running more iterations of our lighting loop, but fetching data would then be significantly faster, and we’d potentially save quite a few registers in the process.

The way we do this is by having each thread maintain an index within the light/decal ID array it’s iterating on. We then compute the smallest item ID across all threads (using a combination of swizzle and readlane instructions). The resulting light/decal ID is then uniform (the value is the same for all threads). We can therefore fetch the content through the scalar unit and then process the item. Threads that were referring to this item (i.e. their divergent value is the same as the wave min value) then increment their local index and move to the next item. This ultimately guarantees that all items are processed exactly once and in order.

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片33.PNG)

The approach just discussed provides a significant boost in most cases, but there are some refinements we can do on top.

First of all, if only one cell is accessed by an entire wavefront, we can use a dedicated fast path. By doing so, we can avoid computing the smallest item ID, which isn’t cheap on 1 & 2. We can also use scalar operations to fetch cell content. This fast path will not result in any VGPR reduction since it has to live with the other path we just described, but can still result in an additional performance increase for those wavefronts touching only one cell.

Also, it is worth noticing that the main reason this scalar approach works is because most of the data that’s been accessed by a wave is shared by all threads, because of their locality. If for some reason threads become spread apart too much in world space, this could actually seriously hurt performance. This typically isn’t something to worry about for an opaque pass, but with the decoupled approach we use for particle lighting, it became an issue, since samples could be pretty far apart from each other. In that case, sticking to divergent fetches was actually faster.

Overall, using those optimizations approach, we were able to get a 30% speedup on the opaque pass at 1080p on PS4. Using the fast path alone results in a significant boost already, but doesn’t increase occupancy. Using the scalar iteration on the merged cell content allows us to get rid of the divergent code path altogether, thus saving some more registers and gaining us an extra wavefront.

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片34.PNG)

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片35.PNG)

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片36.PNG)

To conclude, I’d like to share a couple of common sense tips. GCN lets you setup some limits on how wavefronts are being scheduled. This is something that’s definitely worth spending a bit of time with during the later stages of a project. There’s no reason not to frequently update those limits. We’ve found out for instance that disabling vertex shader parameter cache late allocation during static geometry rendering, where each triangle is potentially yielding a significant number of pixels was beneficial.

If using async compute, those limits should definitely be tweaked again. Assigning too many or too little wavefronts to an async compute task can result in an effective serialization of the task. Using async compute can in general result in more frequent thrashing of GPU caches. Restricting the number of waves allowed to be in-flight, or locking a task to only a subset of the compute units can mitigate this.

Overall, by fine-tuning wave limits throughout the whole frame, as opposed to sticking to the default values, we were able to save up to 1.5ms in some scenes on Doom.

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片37.PNG)

One last thing that’s worth spending a bit of time fine tuning is register allocation. VGPRs in particular are extremely precious, and will most of the time control the maximum occupancy a shader can have. Aiming for strict divisors of 256 when optimizing register pressure of a given shader, might not always give the best results, contrary to one’s original intuition. It is important to bear in mind that a given shader will often not run in complete isolation. Some PS waves will likely run in parallel with some VS waves of the matching or subsequent draw calls. Also, if you’re using async compute, there’s going to be some more contention on those registers. It can therefore be beneficial to aim for other values when it comes to register allocation. As an example, in Doom we aimed to 56 VGPRs for our opaque pass PS, and 24 VGPRs for the matching VS. This allowed us to have more waves in flight overall compared to a naïve 64VGPR solution, which would have prevented anything from running in parallel with 4 PS waves. Overall, this saves more than half a millisecond.

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片38.PNG)

Some results 

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片39.PNG)

Decoupling frequency of costs = Profit
Room for improvements on our side
Texture quality
Global illumination
Overall detail
Workflows
etc
Room for improvement on IHVs side
Profiling tools in general are about 1 decade behind what we have on consoles
AMD: please fix your shader compiler
Can we get Barycentric coordinates on all HW exposed?
Sampler Rect 
Better filtering

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片40.PNG)

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片41.PNG)

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片42.PNG)

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片43.PNG)

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片44.PNG)

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片45.PNG)

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片46.PNG)

Take best from both worlds
Performance & Screen Space Approx. from Deferred
Simplicity & unified from Forward.

No fat render targets used on idTech. Not GCN / console friendly
Normals also used for GPU Particles

Main Lighting Buffer: R11G11B10F

## 参考

[[1]. Siggraph 2016 talk : The devil is in the details](https://advances.realtimerendering.com/s2016/Siggraph2016_idTech6.pdf)

