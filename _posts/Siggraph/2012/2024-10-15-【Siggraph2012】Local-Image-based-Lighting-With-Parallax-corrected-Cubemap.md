---
layout: post
title: 【Siggraph 2012】Local Image-based Lighting With Parallax-corrected Cubemap
date: 2024-09-18
img: Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片2.PNG # Add image post (optional)
fig-caption: # Add figcaption (optional)
tags: [Cubemap, Reflection, Siggraph, 2012]
description: 本文分享的是基于cubemap的反射效果的优化方案
---

今天介绍的是基于cubemap的环境反射效果的优化方案，基于此方案，可以有效缓解cubemap捕获位置跟相机位置不重叠导致的反射效果异常问题。

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片2.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片3.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片4.PNG)



![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片5.PNG)


![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片6.PNG)



![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片7.PNG)



![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片8.PNG)



![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片9.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片10.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片11.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片12.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片13.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片14.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片15.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片16.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片17.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片18.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片19.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片20.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片21.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片22.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片23.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片24.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片25.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片26.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片27.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片28.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片29.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片30.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片31.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片32.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片33.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片34.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片35.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片36.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片37.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片38.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片39.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片40.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片41.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片42.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片43.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片44.PNG)

![](https://gerigory.github.io/assets/img/Local-Image-based-Lighting-With-Parallax-corrected-Cubemap/幻灯片45.PNG)


## 参考

[[1]. Siggraph 2012 and Game Connection 2012 talk : Local Image-based Lighting With Parallax-corrected Cubemap](https://seblagarde.wordpress.com/2012/11/28/siggraph-2012-talk/)