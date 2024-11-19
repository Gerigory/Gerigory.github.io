---
layout: post
title: 【GDC 2011】Lighting You Up In attlefield 3
date: 2024-11-15
img: GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片1.PNG # Add image post (optional)
fig-caption: # Add figcaption (optional)
tags: [Battlefield, Rendering, lighting, GDC, 2011]
description: 本文分享的是战地3在GDC 2011上介绍到的一些光照相关的技巧
---
今天介绍的是战地3在GDC 2011上分享的寒霜引擎的光照方案，分享者是Kenny Magnusson，是一位美术同学。照例，这里对工作内容做一个总结：

1. 

---

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片2.PNG)

介绍分三部分：
1. 过去的表现
2. 项目的需求或目标
3. 具体如何达成

最后对全文做一个总结

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片3.PNG)


![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片4.PNG)

过往的两个项目分别使用一代寒霜跟UE3开发，两者都是前向管线，其中：
1. Bad Company有如下的一些值得注意的点
    1.方向光阴影是动态的，采用三级CSM，都是1024的分辨率
    1. 每个物件最多受一盏点光影响
    2. 没有SSAO
    3. 大尺寸的物件如建筑会需要（静态）天光遮蔽效果，室内等区域则通过天光遮蔽volume来标注
2. 镜之边缘则有：
    1. 通过烘焙的lightmap来实现静态场景的GI效果
    2. 通过预计算的light probe来对动态物体做relighting

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片5.PNG)



![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片6.PNG)

2. 

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片7.PNG)

1. 1. 

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片8.PNG)



![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片9.PNG)

1. 6. 

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片10.PNG)

5. 

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片11.PNG)

- 

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片12.PNG)

4. 

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片13.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片14.PNG)



![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片15.PNG)



![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片16.PNG)

1. 3. 

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片17.PNG)

2. 

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片18.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片19.PNG)

1. 

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片20.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片21.PNG)

1. 2. 

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片22.PNG)

1. 1. 

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片23.PNG)



![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片24.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片25.PNG)



![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片26.PNG)

- 

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片27.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片28.PNG)



![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片29.PNG)



![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片30.PNG)

3. 

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片31.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片32.PNG)



![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片33.PNG)



![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片34.PNG)

3. 

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片35.PNG)

4. 

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片36.PNG)



![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片37.PNG)

 

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片38.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片39.PNG)

- 

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片40.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片41.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片42.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片43.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片44.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片45.PNG)



![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片46.PNG)

![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片47.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片48.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片49.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片50.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片51.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片52.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片53.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片54.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片55.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片56.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片57.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片58.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片59.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片60.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片61.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片62.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片63.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片64.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片65.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片66.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片67.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片68.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片69.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片70.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片71.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片72.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片73.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片74.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片75.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片76.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片77.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片78.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片79.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片80.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片81.PNG)
![](https://gerigory.github.io/assets/img/GDC/2011/Lighting-You-Up-In-Battlefield3/幻灯片82.PNG)

## 参考

[[1]. 【GDC 2011】 Lighting You Up In attlefield 3](https://media.contentapi.ea.com/content/dam/eacom/frostbite/files/gdc11-lightingyouupinbattlefield3.pdf)

