---
layout: post
title: 【Unreal Fest 2024】Optimizing Survival Games for Mobile
date: 2024-09-11
img: 【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/0.png # Add image post (optional)
fig-caption: # Add figcaption (optional)
tags: [Unreal, Optimization, Mobile]
description: 本文分享的是Unreal在Unreal Fest 2024上介绍的移动端性能优化相关要点
---
![](https://gerigory.github.io/assets/img/【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/1.png)

本次talk目标是解决移动端上的这些问题：

1.     大量、复杂ISM下instance的剔除效率
       1.      PC可以通过GPU Scene
2.     移动端下局部光在黑暗环境下表现不佳
3.     DrawCommand的重新创建导致的毛刺
4.     运行时的PSO编译时长过久带来的loading体验问题
5.     音频性能
6.     内存profile

![](https://gerigory.github.io/assets/img/【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/2.png)

- 主机跟PC上，可以通过compute shader对GPU Scene中的ISM数据进行逐instance的剔除，效率很高。但如果在移动端开启这个特性，这个indirection逻辑（可见instance的ID Buffer）的成本就很高（需要先读取ID，再基于ID从SSBO中获取Instance等数据，是SSBO读取成本高吗？）
- GPU Scene的经典实现方案，是将（Instance）数据存储到SSBO（[Shader Storage Buffer Object](https://blog.csdn.net/What_can_you_do/article/details/125620229)，一种shader中可读可写的buffer，尺寸比UBO大，基本没有限制，但是速度慢于UBO，通常用于CS）中，之后通过VS对SSBO进行采样，但不是所有的移动端设备都支持SSBO

![](https://gerigory.github.io/assets/img/【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/3.png)

这里给出针对移动端的优化方案：

1. 还是通过CS做逐Instance的剔除，剔除结果不再是单独的ID Buffer，而是直接将Instance+Primitive数据写出去
2. 输出的Buffer也不是低速的SSBO，而是高速的UBO，因为只有可见的Instance，所以尺寸够用（主机跟移动端这里需要做一个伸缩，具体数据上图有给出）
3. 在Instance数目较多的时候，往往不能一个drawcall画完所有instance，这里通常会需要通过多个批次完成提交，不过这些批次之间本身没有状态切换，所以通常来说速度还是会比通常的drawcall要快很多

![](https://gerigory.github.io/assets/img/【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/4.png)

看起来这个特性是UE本身就支持了的，只需要直接启用测试即可。

![](https://gerigory.github.io/assets/img/【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/5.png)

再来看看移动端上怎么保证黑暗环境下的局部光照效果：前向管线下，由于性能问题，局部光表现实在欠佳

![](https://gerigory.github.io/assets/img/【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/6.png)

因为该项目不能用延迟管线，所以这里取了个巧，借用了UE前向管线中的prepass。

prepass会得到一张depth map，之后基于这个depth得到世界坐标，并基于坐标数据计算局部光的输出结果，包括局部光的颜色（叠加）与方向，最终将这些数据合并成两个RT

> 正常情况下，移动端不会将所有的物件都塞到prepass里，因为有HSR等的优化在，只会将一些HSR处理不了的类型如alpha test塞进去，如果选择了这种方式，这里的这个方案就不能用了

RT格式给出如下：

1. 颜色存储在RG11B10中
2. 方向信息采用八面体压缩方式，用12位+12位存储到一张RGBA的前3个通道（24bit）中，最后一个8位的通道用于存储SpecularScale

这些贴图数据在后面可以通过一个pass结合材质的BRDF来使用，不用额外循环所有的光源

下面看下具体的实现细节

![](https://gerigory.github.io/assets/img/【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/7.png)

首先会通过tile based culling来得到每盏局部光源影响的tile list，之后在前面介绍的prepass阶段，就只需要渲染那些被光照影响的tile，按照instance的方式绘制即可

![](https://gerigory.github.io/assets/img/【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/8.png)

在UE中的开启方式，可以通过config文件为给定的平台启用

![](https://gerigory.github.io/assets/img/【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/9.png)

前向渲染中，某个局部光会有多个变体（适配不同的情景，即shader宏），在运行时会当条件变化的时候，就会需要应用不同的变体，那么此前为某个staticmesh cache的mesh draw command(MDC)就会失效，这个时候就需要重新创建，而这个会造成毛刺现象。

为了避免毛刺的产生，这里的做法是即使local light对物件不生效（范围之外），也继续执行local light的shading逻辑（如贴图采样），通过一定的GPU浪费来规避CPU的毛刺。

![](https://gerigory.github.io/assets/img/【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/10.png)

这个功能只需要启用这个命令行就可以生效了

![](https://gerigory.github.io/assets/img/【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/11.png)

PSO Gathering有如下的一些问题：

1. 如上图所示，搜集过程比较繁琐，用起来复杂，且容易出错
2. 需要一个replay功能来实现高效的搜集，从而应对某位同学更改了shader之后效果不正常的问题
3.  需要一个较长的时间才能完成所有搜集好的PSO的编译
   1. 这个过程是在游戏开始的时候触发，也就是说，会影响到loading时长（可能会到十几分钟）
   2. 这个编译过程目的是生成各个平台所需要的shader二进制文件（PSO存储的是中间字节码，需要一个文档对这块进行明晰），而实际上我们正常使用的可能只是所有编译好的文件的5%到10%，浪费较大

![](https://gerigory.github.io/assets/img/【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/12.png)

这里给出一个新的预缓存方案，该方案的做了如下几点优化：

1. 在材质加载的时候（对应的是接下来要用到的PSO），触发对应PSO的编译
2. 最好是能够提前知道哪些材质是可见的，将这部分提取出来做预编译（可能只需要几百毫秒就够）
3. 同时能够支持项目侧根据项目类型或需要做针对性的设计，自主性主要体现在两点：
   1. 可以自主控制硬件层面分配给PSO编译的预算
   2.  可以为新增的proxy所依赖的PSO设置需要的选项，有三种：
      1. 使用默认材质
      2. 阻塞等待PSO编译完成
      3. 或者不予显示？
4. android这边有一些限制，GL不支持，Vulkan有限制（具体没太听清楚，后面可以查下资料了解一下细节）

![](https://gerigory.github.io/assets/img/【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/13.png)

这是unreal insights下截取的ios precaching的截图，这里总计用了5个线程池，从截图的消耗来看，precache的耗时最多可以去到300+ms，还是非常恐怖的，而这也表明了precache的必要性

![](https://gerigory.github.io/assets/img/【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/14.png)

这里做一下总结，这里的这个优化将可以带来如下的提升：

1. 减少shader编译的耗时
2.  不需要额外的gathering system（为啥？前面只说了材质加载的时候进行编译，还说需要提前知道哪些是需要的，但是没有具体说究竟怎么知道哪些是可用的）
3. 支持更灵活的配置，可以基于项目需要进行控制



不过这个方案也有一定的代价：

1. PSO的编译需要放到运行时，会带来一定的mem/cpu成本
2. 当有问题的时候（材质在某个平台上的precache有问题），发现的时机会比较滞后（在运行时才发现）
3. 容易出现材质没有precache而导致的毛刺

![](https://gerigory.github.io/assets/img/【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/15.png)

这个功能的支持要到5.4（Android）跟5.5（Metal）了，可以提前关注，有需要就做合入

![](https://gerigory.github.io/assets/img/【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/16.png)

下面看下性能相关的内容

![](https://gerigory.github.io/assets/img/【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/17.png)

先来看下音频部分的问题：

1. 大约会占用一个核总体消耗的20%~30%（而部分主机可能就只有2~3个核），分析发现了下面两个问题：
   1. 在内存上会有大量的分配以及zero/copy等操作
   2. 代码并没有做到的很好并行化

这里做了如下的一些优化：

1. 只在使用的时候才触发memzero
2. 启用基于ARM的并行化代码
3. 将循环展开（？）

目前优化已经在UE5.4上了，下面展示一些具体的代码优化细节

![](https://gerigory.github.io/assets/img/【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/18.png)



![](https://gerigory.github.io/assets/img/【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/19.png)



![](https://gerigory.github.io/assets/img/【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/20.png)

接下来看看C++改动构建耗时的问题，这些问题主要在android手机上比较明显（ios不也存在吗？还有windows）：只简单更改几行代码，需要等很久才能完成Package & Lauch，比如大型项目上可能会去到5min（堡垒） 或者更长时间（主要耗时在repackaing以及re-installing环节）。

![](https://gerigory.github.io/assets/img/【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/21.png)

andriod打包流程可以抽象为上述的示意图：

1. 先从源码经由UBT，以Unity Build的概念转换成.o文件（一个模块一个.o），对于中等尺寸的项目，开启Unity Build的话，这个环节可能会花费一两分钟
   1. 为了优化，这个地方会做特殊处理，将改动的文件从Unity Build中移除，从而加速编译
2. 之后经由编译器链接成.so文件
   1. 这里的做法是将dynamic library剥离出来，并与.java文件一起提供给Gradle
3. .so文件跟.java文件一起，经过Gradle处理，得到.apk
   1.  apk本质是一个zip文件，这里为了加速，不用重新创建整个apk，而只是将新的内容添加到末尾，之后调整下指向该数据的index就行，不过这种方式就会导致每次编译一次，生成的apk文件尺寸就会遭遇一次暴涨
   2. 要想解决apk尺寸暴涨的问题，就得删掉重新打包，这个就会花较多时间，也就是说，如果只更改少量代码的话，这个环节耗时是最多的

![](https://gerigory.github.io/assets/img/【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/22.png)

而由于代码的改变只影响libUnreal.so，所以这里的解决方案是，将这个文件放到apk外部，从而快速降低构建的耗时！

![](https://gerigory.github.io/assets/img/【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/23.png)

该功能在5.4上也已经支持了，提供了一个配置选项

![](https://gerigory.github.io/assets/img/【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/24.png)

下面来看下用USB安装的耗时问题：首先操作系统是不会告知当前USB安装的带宽的，而USB2跟USB3的带宽差距很大

![](https://gerigory.github.io/assets/img/【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/25.png)

针对这个问题，解决方案就是：

1. 保证相关硬件（线、端口等）的带宽是足够的
2. 通过一些工具对实际的带宽进行测试（上面列举了部分可用工具）

![](https://gerigory.github.io/assets/img/【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/26.png)

最后是android设备上的Memory Insights的支持，这个在5.4上已经ok了，实测这个工具不会对性能造成过重的负担。

![](https://gerigory.github.io/assets/img/【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/27.png)

这里给了具体的启用步骤，可以参考

![](https://gerigory.github.io/assets/img/【Unreal-Fest-2024】Optimizing-Survival-Games-for-Mobile/28.png)

android上有部分内存不是由UE分配的，而是由系统分配的，比如基于libc.so完成分配，针对这部分内存，可以在应用启动之前先将一个lib预加载进来就行，具体来说，就是在构建apk的时候传入一个参数即可。

## 参考

[[1]. Optimizing Survival Games for Mobile | Unreal-Fest-2024](https://www.youtube.com/watch?v=X_ir86-Cpvk)
