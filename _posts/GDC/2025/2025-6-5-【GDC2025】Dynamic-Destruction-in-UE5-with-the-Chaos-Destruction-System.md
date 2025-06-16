---
layout: post
title: 【GDC 2025】Dynamic Destruction in UE5 with the Chaos Destruction System
date: 2025-6-5
img: GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/1.png # Add image post (optional)
fig-caption: # Add figcaption (optional)
tags: [Unreal, UE5, Chaos, Destruction, GDC, 2025]
description: 本文分享的是Epic Games在GDC 2025上介绍到的一些与Chaos Destruction相关的一些最新设计进展

---

本文分享的是Epic Games在GDC 2025上介绍到的一些与Chaos Destruction相关的一些最新设计进展，分享者是epic的物理主程。



照例，这里对工作内容做一个总结：

1. 

---

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/2.png)

这个talk的主题主要涵盖两方面：

1. 在不影响性能的情况下，实现尽可能好的破坏表现；或者对偶的说，在不影响表现的情况下，降低破坏的计算消耗
2. 用尽可能小的侵入成本来实现数百个asset的破坏模拟效果的控制（？）

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/3.png)

这里介绍了asset处理的dataflow

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/4.png)

接下来看看破坏方案的运行时性能

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/5.png)

先来介绍一下资产的大致情况，上述是一个百万面数的照扫资源

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/6.png)

将这个资源复制32份摆到场景里，最开始的时候帧率大约是26，但是当破碎被触发的时候，就会迅速下降到15fps。

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/7.png)

这里介绍两个简单但有效的性能优化方法：

1. 开启Nanite，帧率可以立马从22升到90
2. 使用Root Proxy，帧率还可以进一步提升到100+

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/8.png)

Nanite的启用有两种方式：

1. SM如果启用了，转成GC之后，依然是启用的
2. 也可以手动对GC启用

启用Nanite后有如下的好处：

1. 可以实现GC在渲染时的自适应LOD
   1. 非Nanite的GC是没有LOD的。。。
2. 可以减少GC资源在磁盘、内存上的空间占用
   1. 在cook的时候，会将source data从GC中剥离出去（有个checkbox，能节省大约95%的空间。。）

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/9.png)

Root Proxy可以理解为在破碎被触发前，用于替代破坏物进行渲染的一个Proxy Mesh，相较于原生的GC数据，一体化的Proxy Mesh无疑在渲染上具有更好的绘制效率。

使用Root Proxy有如下的特点：

1. 因为做了属性绑定，因此可以通过GC实现便捷访问
2. 支持LOD、Nanite以及Lumen等特性
3. 可以在编辑器阶段就生效，而非必须要在runtime环境才起作用
4. 还支持合批渲染，这个合批的范围并不是局限在当前的GC资产，而是当前内存中的所有GC资产
5. 对于玻璃等半透物件，使用proxy得到的是整体的未破碎效果，而使用GC绘制得到的是拼接的，虽然没有裂开，但中间会存在裂痕的效果，从体验来看，前者更符合项目需要
6. 不过在制作的时候，由于需要绑定相同的pivot，因此会有一些额外的制作成本（在下个版本，即5.6中会移除此限制）

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/10.png)

除此之外，还有一些其他的手段来进一步优化性能，比如这里提到的Remove On Break，这个特性可以使得破碎后的碎片在与parent脱离后，逐渐的被移除，从而减少碎片导致的持续消耗。

这里还有一个Cluster Crumble的开关，勾选之后，可以强制将一些掉落在地但未破碎的Cluster破碎成小的碎片。

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/11.png)

另外一个特性是Remove On Sleep，比前面的Remove On Break而言，这个特性的Remove时机要靠后一点，得等到碎片稳定下来之后才remove，还为这个特性设置了若干属性来控制remove的效果。

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/12.png)

其他的一些remove控制逻辑有：

1. Game wide time multiplier setting：可以用于实现不同平台的独特控制
2. Allow flags on the component：可以为不同的component单独设置remove的开关

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/13.png)

为了提升性能，这里对交互的类型，或者说破坏碎片的类型做了区分：

1. One way object：指的是不会二次碎裂的碎片
2. Two-way object：还会二次碎裂的碎片

针对碎片类型的交互效果做了约束：

1. One way不会与Two-way发生交互
2. One way之间会采用简单的sphere-sphere交互模拟方式

在使用上，可以实现component级别的自定义，即为不同的component指定从哪一层开始，碎片可以被看成one way

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/14.png)

在不做限制的时候，每一帧有可能会触发多次破碎，也会因此产生大量的碎片，这个会导致性能的失控。

为了控制预算，这里提供了两个参数来实现单帧内破碎频次与碎片数目的控制。

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/15.png)

针对Damage的传导，这里提供了两种机制：

1. Break Propagation：在断裂发生后，断裂处传来的残余strain（用于驱动相邻碎片的进一步断裂）系数
2. Shock Propagation：不考虑断裂情况时，某个碎片的Strain往相邻碎片传导的系数

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/16.png)

为了提升真实性，可能会需要生成大量的细小碎片，而碎片数目过多会导致性能的下降，这里设计了一个Tiny Geo的工具，可以将细小碎片合并到相邻的大尺寸的碎片上，从而实现二者的兼顾。

细小的碎片，可以通过Niagara生成。

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/17.png)

接下来看看针对破碎效果的可控性的一些使用建议。

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/18.png)

早期版本中，需要手动实现GC与Anchor Field Actor的连接操作，这个过程存在如下的几点问题：

1. 对于起伏变化的地形而言，这种方式会使得地形与其上的大量GC的连接性的维持变得困难
2. 与Anchor连接的部分由于经常卡在原地，因此很难一次性激活整个actor
3. 还需要一个单独的Field Actor，这个增加了管理与维护成本

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/19.png)

为了优化上述体验，目前已经可以在fracture模式下降GC的bone单独设置为Anchored或者Kinematic，这个是针对Asset而生效的，也就是说多个Component会共享一份数据。

经过上述设置后：

1. Anchors破碎后，整个actor就可以被一次性激活
2. 而被设置为Kinematci的碎片则会如期维持在不受影响的状态

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/20.png)

如果摩擦力跟restitution采用默认值的话，具有不同质量的碎片，破碎后的效果就看着很相似

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/21.png)

通过调整这两个参数，就可以得到更为真实的破碎表现

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/22.png)

可以通过物理材质来实现对物理资产的物理参数与物理行为做精细控制：

1. Density参数是现实世界的一个重要的物理参数
2. 可以通过多种方式设定
3. 物理参数还可以与音频、特效等效果做绑定

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/23.png)

UE中用于实现GC破碎最常用、简便的方式是Field，但是复杂的Field往往会存在性能问题

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/24.png)

这里提供一种轻量的破碎方法，即通过调用ApplyExternalStrain的方式来模拟子弹或者激光的作用。

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/25.png)

替代Field的另种方法是Collision，使用这种方法需要启用Damage Propagation Data与Enable Damage from Collision等属性。

不过这种方法在过于活跃的场景中会存在问题，比如速度过大，就可能会直接穿过去等。

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/26.png)

想要得到更令人满意的结果，常用的做法是将上述两种方法结合起来

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/27.png)

一个好的破坏效果，往往需要将物理破碎跟特效表现结合起来，UE提供了一个Niagara Data Channel来实现从Chaos Destruction到Niagara System数据与接口的便捷访问。

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/28.png)

这里给了个示例来介绍二者是如何结合的。

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/29.png)

通过调整参数与策略，可以实现更为复杂的配合效果。

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/30.png)

小尺寸的残骸粒子也都是经由Niagara完成绘制，且绘制时的性能消耗，可以通过蓝图属性面板进行控制。

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/31.png)

看看最终的视频效果

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/32.png)



![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/33.png)

UE5.5增加了一对Get/Set初始位置的节点，这俩节点可以用于实现数据、状态的恢复

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/34.png)

基于这个节点，可以实现破碎表现数据的缓存与播放，步骤如下：

1. 将模拟的过程按照时间顺序缓存下来，数据主要包括各个碎片的transform数据
2. 之后在运行时按照时间顺序进行播放，并在两个关键帧之间进行插值
3. 虽然性能上不算非常优秀，但是对于一些相对复杂的模拟效果来说，算是一种非常有效的策略（还可以用于实现网络同步效果）

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/35.png)

这个播放的过程，还可以通过曲线来控制速率

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/36.png)

在前面的基础上，还可以借助sequencer来实现更为灵活复杂的控制效果

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/37.png)

 

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/38.png)

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/39.png)

- 

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/40.png)

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/41.png)

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/42.png)

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/43.png)

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/44.png)

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/45.png)



![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/46.png)

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/47.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/48.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/49.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/50.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/51.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/52.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/53.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/54.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/55.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/56.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/57.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/58.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/59.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/60.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/61.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/62.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/63.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/64.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/65.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/66.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/67.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/68.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/69.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/70.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/71.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/72.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/73.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/74.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/75.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/76.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/77.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/78.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/79.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/70.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/71.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/72.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/73.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/74.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/75.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/76.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/77.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/78.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/79.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/80.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/81.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/82.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/83.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/84.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/85.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/86.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/87.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/88.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/89.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/90.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/91.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/92.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/93.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/94.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/95.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/96.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/97.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/98.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/99.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/100.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/101.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/102.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/103.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/104.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/105.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/106.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/107.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/108.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/109.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/110.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/111.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/112.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/113.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/114.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/115.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/116.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/117.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/118.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/119.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/120.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/121.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/122.png)
![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/123.png)

## 参考

[[1]. 【GDC 2015】Rendering the World of Far Cry 4](https://ubm-twvideo01.s3.amazonaws.com/o1/vault/gdc2015/presentations/McAuley_Stephen_Rendering_the_World.pdf)
