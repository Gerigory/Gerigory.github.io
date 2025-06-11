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



![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/14.png)



![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/15.png)



![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/16.png)

1. 3. 

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/17.png)

2. 

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/18.png)

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/19.png)

1. 

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/20.png)

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/21.png)

1. 2. 

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/22.png)

1. 1. 

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/23.png)



![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/24.png)

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/25.png)



![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/26.png)

- 

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/27.png)

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/28.png)



![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/29.png)



![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/30.png)

3. 

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/31.png)

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/32.png)



![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/33.png)



![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/34.png)

3. 

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/35.png)

4. 

![](https://gerigory.github.io/assets/img/GDC/2025/Dynamic-Destruction-in-UE5-with-the-Chaos-Destruction-System/36.png)



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
