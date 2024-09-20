---
layout: post
title: 【Siggraph 2014】Next generation post-processing in call of duty advanced warfare
date: 2024-09-18
img: Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/Page1.PNG # Add image post (optional)
fig-caption: # Add figcaption (optional)
tags: [COD, Post-Processing, Siggraph, 2014]
description: 本文分享的是COD在Siggraph 2014上给出的他们在后处理工作上的一些优化方案
---

COD在Siggraph 2014上分享过他们在后处理方面的一些工作要点，其中的一些内容对今天的游戏开发依然有不小的帮助，这里将其中的一些要点分享出来。

照例，先来对全文的关键信息做一个简短的总结：

1. 

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片2.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片3.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片4.PNG)

分享的技术小哥认为，对于写实风格的作品而言，后处理是游戏效果是否能逼近影视效果的关键。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片5.PNG)

后处理工作的优化思路总结下来有上述几个要点。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片6.PNG)

大纲如上，会从三方面进行介绍：

1. 基本概念
2. 面临问题
3. 对应方案

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片7.PNG)

运动模糊在快速移动的游戏中，会有非常重要的作用。

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片8.PNG)

参考[3]：

> 真实世界中，自然光在感光材料上产生光化学作用，形成潜影的过程叫做曝光。
>
> 在这个过程中，如果拍摄对象发生了相对相机的移动，就会导致恒定输入的持续曝光变成非恒定输入的曝光叠加，最终体现为拍摄物体的模糊，也就是常说的运动模糊
>
> 同时，人眼的视觉暂留现象，同样也是因为感光细胞中感光色素形成的延迟形成的
>
> 缺少动态模糊的画面，反而会丧失运动感，使观众失去焦点并从直觉上感觉画面断断续续而不自然

运动模糊是提升效果真实感的重要手段，常见的运动模糊有三类：线性、旋转以及缩放（径向）。而常见的模拟方案有如下几种[3]：

1. Accumulation Buffer：将运动的物体按照运动方向做多次渲染，之后按照一定的权重累加之后，再叠加到静态背景上
2. Velocity Buffer：基于屏幕空间每个像素的速度向量，做一个向前（按照曝光的理论，运动模糊表现为前后两部分的虚化）与向后的颜色扩散，以模拟该像素经过路径上的染色行为

注意：上图中介绍的第二种Stochastic Rasterization的方案不是上面说的Velocity Buffer的方案，而是通过随机噪点的方式来模拟的方案，参考[6]

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片9.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片10.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片11.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片12.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片13.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片14.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片15.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片16.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片17.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片18.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片19.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片20.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片21.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片22.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片23.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片24.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片25.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片26.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片27.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片28.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片29.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片30.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片31.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片32.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片33.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片34.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片35.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片36.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片37.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片38.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片39.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片40.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片41.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片42.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片43.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片44.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片45.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片46.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片47.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片48.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片49.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片50.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片51.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片52.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片53.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片54.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片55.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片56.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片57.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片58.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片59.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片60.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片61.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片62.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片63.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片64.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片65.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片66.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片67.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片68.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片69.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片70.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片71.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片72.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片73.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片74.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片75.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片76.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片77.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片78.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片79.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片80.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片81.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片82.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片83.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片84.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片85.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片86.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片87.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片88.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片89.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片90.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片91.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片92.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片93.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片94.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片95.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片96.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片97.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片98.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片99.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片100.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片101.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片102.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片103.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片104.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片105.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片106.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片107.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片108.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片109.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片110.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片111.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片112.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片113.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片114.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片115.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片116.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片117.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片118.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片119.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片120.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片121.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片122.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片123.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片124.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片125.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片126.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片127.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片128.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片129.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片130.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片131.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片132.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片133.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片134.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片135.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片136.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片137.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片138.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片139.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片140.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片141.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片142.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片143.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片144.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片145.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片146.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片147.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片148.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片149.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片150.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片151.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片152.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片153.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片154.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片155.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片156.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片157.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片158.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片159.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片160.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片161.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片162.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片163.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片164.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片165.PNG)

![](https://gerigory.github.io/assets/img/Next-Generation-Post-Processing-in-Call-of-Duty-Advanced-Warfare/幻灯片166.PNG)

## 参考

[[1]. Next Generation Post Processing in Call of Duty: Advanced Warfare](https://www.iryoku.com/next-generation-post-processing-in-call-of-duty-advanced-warfare/)

[[2]. 物体运动模糊(motion blur)](https://zhuanlan.zhihu.com/p/480274106)

[[3]. 运动模糊](https://zhuanlan.zhihu.com/p/441786650)

[[4]. A Reconstruction Filter for Plausible Motion Blur](https://casual-effects.com/research/McGuire2012Blur/McGuire12Blur.pdf)

[[5]. A Fast and Stable Feature-Aware Motion Blur Filter](https://www.cim.mcgill.ca/~derek/files/Guertin2014MotionBlur.pdf)

[[6]. Real-time Stochastic Rasterization on Conventional GPU Architectures](https://research.nvidia.com/sites/default/files/pubs/2010-06_Real-Time-Stochastic-Rasterization/McGuire10Stochastic.pdf)
