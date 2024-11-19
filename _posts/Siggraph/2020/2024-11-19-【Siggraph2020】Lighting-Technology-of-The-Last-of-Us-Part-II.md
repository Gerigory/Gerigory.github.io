---
layout: post
title: 【Siggraph 2020】Lighting Technology of The Last of Us Part II
date: 2024-11-19
img: Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片1.PNG # Add image post (optional)
fig-caption: # Add figcaption (optional)
tags: [Last of us II, GI, Rendering, lighting, Siggraph, 2020]
description: 本文分享的是Last of us 2在Siggraph 2020上介绍到的光照方案


---

本文分享的是Last of us 2在Siggraph 2020上介绍到的光照方案，照例，这里对工作内容做一个总结：

1. 

---

![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片2.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片3.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片4.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片5.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片6.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片7.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片8.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片9.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片10.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片11.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片12.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片13.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片14.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片15.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片16.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片17.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片18.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片19.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片20.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片21.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片22.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片23.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片24.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片25.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片26.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片27.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片28.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片29.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片30.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片31.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片32.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片33.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片34.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片35.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片36.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片37.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片38.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片39.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片40.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片41.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片42.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片43.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片44.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片45.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片46.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片47.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片48.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片49.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片50.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片51.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片52.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片53.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片54.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片55.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片56.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片57.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片58.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片59.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片60.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片61.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片62.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片63.PNG)
![](https://gerigory.github.io/assets/img/Siggraph/2020/【Siggraph2020】Lighting-Technology-of-The-Last-of-Us-Part-II/幻灯片64.PNG)

## 参考

[[1]. 【Siggraph 2013】Lighting Technology of The Last of Us or "old lightmaps -new tricks"](http://miciwan.com/SIGGRAPH2013/Lighting%20Technology%20of%20The%20Last%20Of%20Us.pdf)
[[1]. 【Siggraph 2020】Lighting Technology of The Last of Us Part II](https://s3.amazonaws.com/nd.images/research/2020_siggraph/GpuParticles.pptx)
