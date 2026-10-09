---
layout: post
title: "Inside Marvel's Spider-Man 2 - The Insomniac Games Tech Breakdown"
date: 2026-07-08
img: 渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_001.png # Add image post (optional)
fig-caption: # Add figcaption (optional)
tags: [Rendering]
description: 本文分享的是Inside Marvel's Spider-Man 2 - The Insomniac Games Tech Breakdown相关的技术要点
---

> 来源：D:\迅雷下载\Graphics Materials\Inside Marvel's Spider-Man 2： The Insomniac Games Tech Breakdown!.mp4  
> 提取时间：2026-07-08 18:54:45

---

## Slide 1 — 00:00:00

![Slide 1](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_001.png)


**📌 要点汇总**
- 本次采访由Digital Foundry主持，受访者为Insomniac Games的Mike Fitzgerald。  
- Mike Fitzgerald是Insomniac核心技术部门的负责人，负责游戏引擎和工具的开发。  
- 该团队为多个项目提供技术支持，包括《漫威蜘蛛侠2》。

> Hello and welcome to a special Digital Foundry interview. I'm John Lineman, of course, and I'm joined today by a very special guest, coming straight to us from Insomniac Games, having just finished Marvel's Spider-Man 2. Mike Fitzgerald, welcome to the show. Thank you so much. It's exciting to get to talk about this game finally. And just for those that aren't aware, what do you do on the Spider-Man project? So I'm the director of our core technology department at Insomniac. We're a cross-project team, so we're doing the engine and tools that our game teams use to build the games.
>



---

## Slide 2 — 00:00:41

![Slide 2](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_002.png)


**📌 要点汇总**
- （过渡内容，无关键要点）

> And that underpin the runtime of the games themselves. So I get to have my hands in everything going on in the studio, which is fun. Obviously, I've been playing Spider-Man 2. Just put out a video on it as I'm talking to you now, but I wanted.
>



---

## Slide 3 — 00:00:57

![Slide 3](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_003.png)


**📌 要点汇总**
- （过渡内容，无关键要点）

> To get your first impressions and first thoughts on the approach you wanted to take in building this new game—what were the key features that stood out in your mind? Where were you like, okay, this is where we want to take the technology for this next title? Well, the fun thing to do is always take a photo of New York City and put it next to the game, try and find the exact perspective, right, and then say...
>



---

## Slide 4 — 00:01:23

![Slide 4](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_004.png)


**📌 要点汇总**
- 当前目标并非追求完全逼真（photoreal），而是类似漫威或游戏中的视觉效果（Marvel real 或 game real）。  
- 所需的是某种夸张且富有戏剧性的表现方式，而非严格的真实再现。

> Well, where are we? Where are we falling short of this? Now, you know, photoreal is not exactly the goal. I think it's more Marvel real, or game real, or something. Some sort of somewhat exaggerated, dramatic interpretation of it.
>



---

## Slide 5 — 00:01:39

![Slide 5](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_005.png)


**📌 要点汇总**
- 建筑在远处显得扁平化  
- 光照效果在远处减弱  
- 缺乏细节和纹理变化

> But some of the things we pointed out were our buildings got a bit flat in the distance. The lighting would drop out. They didn't have a lot of macro break up and variation.
>



---

## Slide 6 — 00:01:49

![Slide 6](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_006.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 7 — 00:01:54

![Slide 7](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_007.png)


**📌 要点汇总**
- 对PS5首发游戏中的光线追踪反射效果感到兴奋  
- 内部场景构建中仍存在许多技巧和虚假表现  
- 对于内部场景的优化是一个令人期待的挑战

> That was one thing we were excited about. Ray traced reflections on our PS5 launch titles were awesome, but there were still a lot of tricks and fakes around when building interiors, which was a fun area we were excited to tackle, and then.
>



---

## Slide 8 — 00:02:08

![Slide 8](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_008.png)


**📌 要点汇总**
- 项目涉及跨河场景，需处理水体渲染等独特挑战  
- 环境规模和复杂度是主要技术难点

> As soon as we knew we were doing Brooklyn and Queens, we knew we'd be going across the river, and we'd be having a whole set of unique challenges with the water rendering and things there. But really, it's about the scale and the complexity of the environment.
>



---

## Slide 9 — 00:02:21

![Slide 9](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_009.png)


**📌 要点汇总**
- 游戏开发团队在完成一款游戏后，会重新审视目标并尝试更具野心的创意。  
- 《Ratchet and Clank Rift Apart》为《Spider-Man》的加载和流式处理提供了新思路。  
- 本演讲重点聚焦于游戏中的建筑内部设计。  
- 每一座摩天大楼的内部细节都经过精心设计。

> You get to the end of one game, and the whole team gets to pick up and look a bit farther to the metaphorical horizon about what they're doing, and get ambitious and think about crazy things they want to try. And so everyone has their own little pet thing to do. Sure, doing that's awesome. Doing Ratchet and Clank Rift Apart gave us a lot of fun ideas about how to do loading and streaming differently in Spider-Man as well. Oh yeah, and that's something we do want to get to. But I actually want to start with one of the things that really caught my eye when looking at the game, myself, and it's the building interiors. So, for those watching the video, you may have noticed this: every single building, every one of these skyscrapers, now.
>



---

## Slide 10 — 00:03:04

![Slide 10](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_010.png)


**📌 要点汇总**
- 展示了高度详细的室内场景建模  
- 动态角色在房间内活动  
- 体现复杂环境与角色交互能力

> Features what looks like a fully modeled interior with dynamic characters even sitting around inside these rooms, and.
>



---

## Slide 11 — 00:03:12

![Slide 11](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_011.png)


**📌 要点汇总**
- 提出假设后希望听到实际解决方案  
- 询问对方如何实现目标及解决问题的方法  
- 肯定对方工作成果，指出棋盘格图案是光线追踪的标志

> We had our hypothesis, but I'd actually like to hear directly from you. What are you guys doing to pull it off? How did you solve this problem? Yeah, I saw it. Great job! I think noticing the checkerboarding was a great tell. So those are ray traced.
>



---

## Slide 12 — 00:03:28

![Slide 12](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_012.png)


**📌 要点汇总**
- （过渡内容，无关键要点）

> Interiors for rooms, and what we're doing is.
>



---

## Slide 13 — 00:03:33

![Slide 13](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_013.png)


**📌 要点汇总**
- 使用立方体贴图技术实现前作游戏中的环境渲染  
- 尝试在内部空间添加视差深度以增强3D感  
- 通过光线追踪技术将室内渲染扩展至地下32个“假房间”  
- 光线追踪技术可用于渲染更复杂的几何形状和场景细节

> Path tracing that space in a sense with sort of simplistic geometry and lighting, but taking a step back, I think we had the cube map technique in the previous games, which is always clever and fun — fun to crawl around corners and look in and notice all the oddnesses of it. And we actually had another technique we were trying on top of that, which was to add sort of a parallax depth to the interior, and you could get these sort of 3D shapes, especially along the back wall. Like if you wanted to put a desk back there or bookshelves on the sides, like that sort of convex geometry along the walls and back looked quite good.
>
> But a couple really talented folks on our render team sort of proposed this idea of, "Hey, every window we hit, we're tracing rays out into the world. Why not?" Render an interior by using that same system and tossing rays elsewhere. So, we have I think thirty-two fake rooms deep underground the city, buried somewhere below the ground plane, and they all have sort of...
>



---

## Slide 14 — 00:04:39

![Slide 14](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_014.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 15 — 00:04:53

![Slide 15](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_015.png)


**📌 要点汇总**
- 介绍基础布局设计  
- 展示家具和装饰的不同变化方案  
- 强调空间灵活性与个性化配置

> Basic layout, and then different variations on furniture and decor.
>



---

## Slide 16 — 00:04:58

![Slide 16](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_016.png)


**📌 要点汇总**
- 使用唯一 ID 标识房间以追踪进入情况  
- 通过 ID 追踪人物进入房间的路径

> Characters that might be in there, and then as you trace into a room, we use sort of an ID for that.
>



---

## Slide 17 — 00:05:05

![Slide 17](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_017.png)


**📌 要点汇总**
- （过渡内容，无关键要点）

> Okay, so floor five, window three of the building at this corner. We'll use this room and this.
>



---

## Slide 18 — 00:05:14

![Slide 18](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_018.png)


**📌 要点汇总**
- 使用 BVH（包围体积层次）结构来过滤特定房间内的对象，包括动画对象  
- 支持预计算光照和通过真实窗户投射光线以模拟自然光和阴影  
- 可以处理如吊扇、人物等动态对象，并与场景互动（如看电视）

> Sort of a random set of interiors for that room, and then we can filter the BVH down to that, hitting exactly some set of objects in there, even animated objects like ceiling fans or characters who might be watching TV. We have some pre-calculated lighting in there, and we also can cast rays back through the real window to get a sense for the key light, where the sun is, and where the shadows might be entering the room, and all that. It.
>



---

## Slide 19 — 00:05:44

![Slide 19](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_019.png)


**📌 要点汇总**
- 该技术方案成功实现，效果令人满意  
- 动态感的加入显著提升了游戏内部场景的表现力  
- 精确的阴影渲染得益于光线追踪技术的应用

> It worked. I guess that's really all there is to say about it. It comes together really nicely. You get that sense of movement back there that adds a lot, and that's how we did the interiors for this game. Also, those perfect shadows — of course, a benefit of tracing into those scenes.
>



---

## Slide 20 — 00:06:00

![Slide 20](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_020.png)


**📌 要点汇总**
- (Content too short, no key points)

> I think shadow.
>



---

## Slide 21 — 00:06:05

![Slide 21](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_021.png)


**📌 要点汇总**
- 建筑侧面的细节设计（如后门）增强了场景的真实感和深度  
- 该技术实现了复杂的反射效果，包括反射中的反射  
- 这种深度处理方式在游戏开发中属于高难度问题  
- 该实现被认为是目前最优雅的解决方案之一  
- 该技术在《Miles Morales》中已有初步展示

> Maps that would be expensive and probably not look very good. Yeah, not for each window. Certainly. No, no, no, no. Yeah, I also liked how even on the sides of buildings, you could sometimes see an office and look, and there'd be a back door at the rear of that office that seemed to go around into the other side of the building. It's a very clever trick, and that is seriously a very difficult problem to solve. I think this is the first time I've seen a game tackle it in such an elegant fashion, where you really do get the feeling of depth on all the buildings.
>
> Another aspect of this depth that really caught my interest is the way you handled basically secondary reflections. So, like, this is something I pointed out in my video for Miles Morales back at the launch of PS5. When you have two windows side by side, they're going to reflect on each other, and then the reflection within the reflection should also appear in that. And that was absolutely stunning.
>



---

## Slide 22 — 00:07:03

![Slide 22](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_022.png)


**📌 要点汇总**
- 二次反射的来源需要进一步确认  
- 主要采用普通反射技术实现效果  
- 未明确说明具体解决反射问题的方法

> In those original games, but I notice here, it is actually present, and I'm wondering what the source is for those secondary reflections. How did you actually solve this problem? Yeah, mostly we use just a plain sort of reflection technique.
>



---

## Slide 23 — 00:07:21

![Slide 23](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_023.png)


**📌 要点汇总**
- （过渡内容，无关键要点）

> Probe of that area. You know what reflections were before we had ray traced reflections. We can follow.
>



---

## Slide 24 — 00:07:27

![Slide 24](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_024.png)


**📌 要点汇总**
- 使用运行时或预计算方法处理粗糙表面周围环境  
- 不需要像光线追踪反射那样精确追踪运动细节  
- 优化性能的同时保持视觉效果合理性

> Back to that technique anywhere, just like we do on any very rough surfaces in that area. We're using some sort of runtime or baked calculation of what's around there, because you don't really need to see movement in it the way you need to with ray traced reflections.
>



---

## Slide 25 — 00:07:46

![Slide 25](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_025.png)


**📌 要点汇总**
- 该技术适用于建筑物的二次反弹和反射场景。  
- 可作为次级反射的可靠替代方案。

> And so, it's a great fallback for a secondary bounce and a reflection as well. It works for buildings.
>



---

## Slide 26 — 00:07:51

![Slide 26](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_026.png)


**📌 要点汇总**
- 提到汽车反射效果之前显得不够立体  
- 新技术改善了汽车在反射中的视觉表现

> It helps with cars a lot too, which I think looked a bit flat in reflections before, and when.
>



---

## Slide 27 — 00:07:57

![Slide 27](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_027.png)


**📌 要点汇总**
- （过渡内容，无关键要点）

> They have a nice, good point. Clear coat on them — you want to give a bit of that.
>



---

## Slide 28 — 00:08:02

![Slide 28](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_028.png)


**📌 要点汇总**
- （过渡内容，无关键要点）

> Yeah, I noticed the nice clear coat on those cars. Zooming in, very sparkly paint. We put a lot of work into that. That was always a pet peeve. Yeah, in the last games, like, uh...
>



---

## Slide 29 — 00:08:11

![Slide 29](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_029.png)


**📌 要点汇总**
- 提到汽车着色器（car shader）还有改进空间  
- 展示了视频中的部分画面，但受限于视频运行时间  
- 漆面着色器（paint shader）效果出色

> The car shader could be a little bit better. So I know I actually have some shots in my video. I'm going to show them here now because I could. We couldn't exceed a certain amount of runtime in the video, so I didn't get to show everything I wanted to. And that's one of the things — the paint shader. It looks awesome. So that's.
>



---

## Slide 30 — 00:08:29

![Slide 30](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_030.png)


**📌 要点汇总**
- 材料质感有显著提升，尤其在小物件上表现更细腻  
- 光线追踪技术被用于水反射，提升真实感  
- 水面反射效果更自然，考虑了光线与粗糙水面的交互  
- 该改进是本次更新的重要亮点之一  
- 传统游戏可能未充分考虑水面反射的复杂性

> Another nice, nice touch and a big improvement. Some materials, folks, will love hearing that. Yes, absolutely. They did an awesome job. The materials in general definitely feel like a step up, especially on the more minute objects, the smaller objects. But I don't want to get away from ray tracing just yet, obviously, because another big thing, obviously, one of the biggest things then, is the water reflections, which are now ray traced. This discussion has been interesting because I think a lot of people, especially with the way games used to work, maybe didn't consider how rough, choppy water actually behaves when light sort...
>



---

## Slide 31 — 00:09:08

![Slide 31](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_031.png)


**📌 要点汇总**
- 提到光线在表面反射和折射的挑战  
- 询问如何利用现有光线追踪功能解决该问题  
- 询问如何处理表面粗糙度等复杂情况

> Refracts and reflects off its surface, right? But I'm curious to see how you tackled this challenge, both in terms of how you leverage the existing ray tracing features, but also how you handle something like this rough.
>



---

## Slide 32 — 00:09:20

![Slide 32](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_032.png)


**📌 要点汇总**
- 水面反射效果不同于光滑表面，呈现更分散的反射  
- 初期游戏中的水面反射效果较差，建筑反射出现严重问题  
- 早期尝试实现水面反射时，角色轮廓在反射中显得不自然  
- 团队意识到需要改进反射技术，但初期实现方式较为简单粗暴

> Water, which is obviously not like a smooth, glossy surface, the reflection is more diffuse. So, what kind of extra cost are we looking at? How'd you pull it off? Let's hear some secrets here. There's always a lot of balance with this. I think pretty early on, as soon as we had gameplay happening over the water, whether it was a mission like we showed in our first gameplay demo, or some early wingsuit, or wasn't even wingsuit then, but just trying to get over to where the Brooklyn and Queens were, you very quickly see it fall apart. And actually, there's a lot of screenshots of the first game on PS4, where the building reflections fall apart really bad. You get this full silhouette of the character in front of it, and we just knew we could do better, but when you sort of naively drop Ray.
>



---

## Slide 33 — 00:10:10

![Slide 33](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_033.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 34 — 00:10:17

![Slide 34](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_034.png)


**📌 要点汇总**
- 水面追踪导致性能显著下降，成本过高  
- 尝试使用平面反射技术渲染水下场景以优化效果  
- 渲染完整场景的替代方案未能有效解决问题

> Tracing on that water, the performance spikes far, far too high. It was really expensive. We even tried to get around it a few other ways. We tried doing a kind of planar reflection technique, like rendering from underneath up through the water at the full scene. But rendering a whole other...
>



---

## Slide 35 — 00:10:36

![Slide 35](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_035.png)


**📌 要点汇总**
- 光线追踪技术成本高昂，但效果更佳  
- 将水的粗糙度转换为其他参数未达预期  
- 通过优化光线追踪性能来解决性能问题  
- 图形程序员在该领域表现突出，提出有效方案

> Is really expensive, as well. And then, trying to translate that into the roughness of the water didn't quite work. And so, we sort of got to a point where we said, "Yeah, no, the ray tracing is going to be the right way to do this. So, how can we mitigate that performance?" Our graphics programmers are awesome. And the one in particular who focuses on this stuff, he did a great job.
>



---

## Slide 36 — 00:11:05

![Slide 36](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_036.png)


**📌 要点汇总**
- 水面反射在水平方向以四分之一分辨率渲染，因拉伸效果不明显  
- 优化过程中常遇到需要权衡取舍的挑战  
- 优化细节在不同场景下（如水与窗户）表现差异明显

> Trying to find the right compromises that you don't notice in the same way when you're looking at water as opposed to windows. So we actually render the water reflections at quarter res on horizontal because they're so stretched out—you don't notice that at all. And this is always this fun march of when you're focused on optimizing.
>



---

## Slide 37 — 00:11:28

![Slide 37](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_037.png)


**📌 要点汇总**
- 通过减少光线数量可显著降低性能成本，同时保持视觉效果一致  
- 水的表面粗糙导致光线分散，影响光线追踪效率  
- 需要寻找方法对光线进行分组（binning），以提升硬件处理效率

> One thing, you get the progress updates during the day, and it's like, "Hey, here's a side by side. This one is literally half as many rays, half the performance cost. It looks exactly the same to everyone, right?" And everyone's like, "Yeah, pretty much." And so it's like finding those little bits where you can save time and effort to do that.
>
> A big one for water that makes it so expensive is it's so choppy that your rays shoot in all different directions. And that's really inefficient for ray tracing hardware. So how can you bin them? How can you?
>



---

## Slide 38 — 00:12:04

![Slide 38](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_038.png)


**📌 要点汇总**
- 通过调整方向以提高硬件性能，而非精确对准  
- 重复优化过程最终实现性能模式的高质量表现  
- 强调了持续优化对性能模式质量的关键作用

> How can you, maybe not shoot them in exactly the right direction, but one that's close enough, and yet is more coherent with what's nearby, where you can get pull some extra performance out of the hardware. And really, it's just pulling that thread over and over repeatedly, and eventually getting to a point where we could do it in performance mode as well, which was huge for the quality of performance mode.
>



---

## Slide 39 — 00:12:28

![Slide 39](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_039.png)


**📌 要点汇总**
- 开发团队希望实现60 FPS或更高的光线追踪水效果  
- 曾考虑放弃传统渲染方式，全面转向光线追踪  
- 对早期未使用光线追踪的游戏截图感到不满  
- 希望避免性能与画质之间的巨大妥协  
- 直到今年年初才正式决定采用光线追踪方案

> It's interesting. So, I was wondering about hitting 60 FPS or higher with ray-traced water. So, I guess there was a point. Actually, that's another question in general. Like, do you remember the point where you're like, you know what? We're just going to go all ray tracing here and drop the fallbacks. Like, did that happen early in development? Was that always the goal, or was it just like you just happened to get enough performance that you were able to say, yeah, we can actually do this. Well, it has always pained me whenever I see a screenshot of the first couple Spider-Man games, or Ratchet and Clank with ray tracing turned off, and I always know it immediately when I see a screenshot. It always bums me out, and so it was always an aspiration for this one. I think it was like, man, wouldn't it be great if we didn't have to have that big compromise in there? If we got back to sort of a pure performance and resolution trade-off. And I don't think we committed to it until earlier this year, but I think basically we...
>



---

## Slide 40 — 00:13:35

![Slide 40](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_040.png)


**📌 要点汇总**
- （过渡内容，无关键要点）

> Saw the way performance was trending, and we said, "You know, it'll be work, but let's go for it." I feel like we got there with the last games, but we always got there.
>



---

## Slide 41 — 00:13:48

![Slide 41](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_041.png)


**📌 要点汇总**
- 项目在上线一周或截止日期时出现问题  
- 团队对结果缺乏信心  
- 此次尝试最终未能成功

> Like a week after launch, or right at the deadline, and we were never quite confident enough, and so this time it just didn't work out.
>



---

## Slide 42 — 00:13:56

![Slide 42](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_042.png)


**📌 要点汇总**
- 优化游戏时需提前规划，如60 FPS模式不能临时决定  
- 光线追踪技术在粒子反射方面有显著提升，是新特性  
- 早期游戏中并未实现粒子在光线追踪反射中的渲染  
- 宣传预告片与实际游戏画面存在差距，团队会避免使用未来技术的场景  
- 当前游戏画面质量已优于预告片，但预告片制作时需考虑未来技术更新

> Took a bit of, no, we're gonna do it, and we can get to where it needs to be. I like the word "trending" because that's something I think that's really important to consider when optimizing any of these games. You have to think very far ahead in the future, right? Like, you can't just say at the last minute, like, yeah, we're gonna do a 60 FPS mode. It's gonna be something that's really planned early on and worked towards. Yeah. And obviously, that must have been a lot of hard work to get going with. All that ray tracing going on because yeah, it's good stuff.
>
> But another thing about the ray tracing that was interesting is it seems like the particles, not all of them, but many of the particles are now rendered in the ray traced reflection. And this is something that was definitely not the case in the last games. And it seems like it wasn't even in one of the earlier trailers either. So like, what's the story there?
>
> Trailers are so funny. You make them, and I think there's this sort of perception that, like, well, it's all smoke and mirrors, and the real shipping game is not even going to look that good. But when our media team, who's awesome, is capturing those trailers, we're always thinking, well, don't put that scene in because we know we have this thing coming that's going to make it look better. And I think when the trailers come out, I know our core tech team is always thinking, oh, it.
>
> But it looks better now. Why couldn't how it looks now be what's in the trailer? So yeah, in particular, I think it was the story trailer. In one of them, you're getting pulled up behind by a lizard up the side of a building, and there's this whole truck bouncing around, and there's all this.
>



---

## Slide 43 — 00:15:43

![Slide 43](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_043.png)


**📌 要点汇总**
- 游戏中实现了火焰和烟雾效果，但建筑本身没有受到火焰和烟雾的影响。  
- 该功能在 trailers 发布当天就已实现并应用到游戏中。  
- 团队认为效果提升明显，希望展示该场景以展示改进成果。

> Fire and smoke, and none of that fire and smoke is reflected in the building. And I think the day the trailer came out is the day that we got that feature up and running and looked at that scene in the game. And we're like, ah, but it looks better now. So maybe you can find that scene and show people how it looks. Yeah, exactly, exactly. That's the thing about that is, so I guess kind of like other things in the world, you can.
>



---

## Slide 44 — 00:16:09

![Slide 44](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_044.png)


**📌 要点汇总**
- 需要确定哪些粒子应包含在BVH中  
- 当前仍有部分粒子使用SSR方法处理  
- SSR是传统方法，可能影响性能或效果

> Which particles you want to be included in the BVH, basically, because I notice there's still some particles that are done with SSR, which is typically the more traditional method for.
>



---

## Slide 45 — 00:16:19

![Slide 45](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_045.png)


**📌 要点汇总**
- 提到渲染过程存在困难  
- 引发对实际渲染方法的疑问

> That I think, because it is difficult. But how do you actually render them, though?
>



---

## Slide 46 — 00:16:24

![Slide 46](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_046.png)


**📌 要点汇总**
- 类似于3D空间中RT中的粒子，这种现象在数学上具有挑战性。  
- 描述了某种复杂的行为模式，但具体实现方式尚不明确。

> Like particles in an RT in a 3D space, like that. That's just a strange thing, mathematically tricky, just in terms of how.
>



---

## Slide 47 — 00:16:33

![Slide 47](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_047.png)


**📌 要点汇总**
- 粒子系统通常作为2D对象运行  
- 粒子系统的实现涉及复杂编程工作  
- 提到Abdul是负责该系统的程序员

> Particles work. They're just 2D objects, right? Usually. Yeah. So how does it work? I want to say that Abdul, who's the programmer who handles all this stuff, I want to say he had to.
>



---

## Slide 48 — 00:16:46

![Slide 48](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_048.png)


**📌 要点汇总**
- 使用 BVH billboarding 机制将物体朝向光线来源方向  
- 确保所有对象沿正确方向重新投影以正确显示在反射中

> Set up a sort of BVH billboarding mechanism to hit something that would be billboarded towards the source of the ray, and make sure that everything is reprojected in the right direction to then appear correctly in the reflection.
>



---

## Slide 49 — 00:17:03

![Slide 49](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_049.png)


**📌 要点汇总**
- 在游戏接近尾声时，会针对特定场景优化粒子和视觉效果的反射  
- 不希望全局应用所有优化，以免影响性能  
- 需要谨慎选择优化时机和范围，避免性能下降  
- 优化需在不影响整体平衡的前提下进行

> So, that's pretty neat, actually. You know, like you said, we sort of pick and choose. A lot of what we do is, as we're approaching the end of a game, we say, "Well, this can look better," and then you make it so that certain types of particles can be in the reflection, certain VFX can be there. But then you don't want to necessarily blanket apply it everywhere because you might tank performance in some scene where it doesn't really matter, and it's too late to sort of balance it all out. So, we carefully pick and choose, and find opportunities to make things.
>



---

## Slide 50 — 00:17:37

![Slide 50](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_050.png)


**📌 要点汇总**
- （过渡内容，无关键要点）

> Look better. Sure, that makes sense. I do actually want to ask you a little bit about.
>



---

## Slide 51 — 00:17:42

![Slide 51](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_051.png)


**📌 要点汇总**
- 该游戏的光照效果处理得当，包括全局光照和烘焙光照方法  
- 有改进光照的潜在空间  
- 需要再次解释预计算光照流程，以帮助理解  
- 全局光照烘焙覆盖了城市和任务中的自定义室内场景

> The lighting is well done for this game, and the way you handled global illumination and the different baked lighting methods, and if there are any improvements there. But first, maybe start by explaining again, because I was discussing this with somebody, and I think there's actually interest in understanding again the way you guys do your pre-calculated lighting pass. So if you could quickly break that down for us. So we have a GI bake across the city and in all the custom interiors for missions and things like that.
>



---

## Slide 52 — 00:18:08

![Slide 52](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_052.png)


**📌 要点汇总**
- 城市规模庞大，光照烘焙质量需持续提升，包括分辨率、反射率和高光等细节  
- 光照烘焙耗时极长，且城市在开发过程中不断变化，难以频繁重新烘焙  
- 项目团队在幕后优化了非显眼的流程，以提升迭代效率和整洁度

> The city's enormous, and it's twice as big in this game. We always want to be increasing the quality of that bake, whether it's resolution, reflectance, or specular, as well. Like all these different factors of the light that we're baking in and exposing to the real-time part of the game.
>
> It's funny. This stuff takes ages to bake across the city, and also the city is changing every day during development. So you can't just ask a team, "Well, if you're working on this street corner, make sure you rebake all the lighting there." They don't want to sit there for an hour to rebake it all just because they move some stuff around.
>
> In this game, we actually worked quite a bit on the non-glamorous part that doesn't show up in the final product, in a sense, but lets us iterate on all that more easily and cleanly.
>



---

## Slide 53 — 00:19:01

![Slide 53](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_053.png)


**📌 要点汇总**
- 以前需要多台机器耗时一周完成任务，现在一台机器即可快速完成。  
- 显著提升了计算效率和资源利用率。

> And we're able to. We used to have a farm of machines that were baking the city over a week, and now it's like one machine can bake the sunset.
>



---

## Slide 54 — 00:19:24

![Slide 54](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_054.png)


**📌 要点汇总**
- 光影设置需要四天左右，是一个持续迭代的过程  
- 动态光影在一定距离后必须停止  
- 已实现整个场景的光照烘焙，可一次性加载  
- 实际效果与真实纽约存在差异，需注意细节处理

> Of lighting set up in four days or something like that. So that's a big iterative thing for us as we go. Looking at the city, and I mentioned some big picture things about it versus real New York. One is all our dynamic lighting had to stop at some point in the distance, and as well, now we have a version of the light bake for the entire level, the entire world that can be loaded at one time, so you still...
>



---

## Slide 55 — 00:19:59

![Slide 55](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_055.png)


**📌 要点汇总**
- 描述从曼哈顿东岸看向布鲁克林的远距离景观  
- 强调视野中无遮挡物的视觉体验  
- 对比曼哈顿通常有近处建筑的视觉特点  
- 突出远处目标成为唯一关注焦点的场景

> Get that if you're looking towards the opposite end of the city. This is another thing — across the river, made tough is looking from the east side of Manhattan across to Brooklyn. You're looking at something very far away, but also there's nothing in between you and it, right? In Manhattan, there's a lot of far away stuff, but usually there's buildings close, and that's where you're seeing. But this was something far, far away that was also all you cared about and wanted to look at.
>



---

## Slide 56 — 00:20:21

![Slide 56](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_056.png)


**📌 要点汇总**
- 确保照明效果良好是项目的重要部分  
- 实时动态照明与建筑物间的GI烘焙效果在远距离表现优异  
- 对比展示了真实照明与静态烘焙照明的差异

> So we needed to make sure our lighting over there was good as well. It's a nice side by side of seeing how much farther real dynamic lighting at street level and real GI bakes in between the buildings holds up at a distance.
>



---

## Slide 57 — 00:20:39

![Slide 57](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_057.png)


**📌 要点汇总**
- 提到不同时间段的烘焙处理是独立进行的  
- 光照数据规模远大于《蜘蛛侠》PS4版本  
- 因硬件限制，光照处理面临较大挑战

> Yeah, and there's a good amount of time of days — times of day in this, so each one of those is its own separate bake. Like, just offhand, do you have any idea roughly how much larger the lighting data is compared to, say, Spider-Man on PS4? I don't recall exactly what it was on PS4, but I know we were so constrained by how.
>



---

## Slide 58 — 00:21:00

![Slide 58](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_058.png)


**📌 要点汇总**
- 开放世界的光照数据可能占磁盘空间的三分之一  
- 光照数据是数据中非常重要的组成部分  
- 数据量较大，需高效处理和存储

> Big things were, and to stream it off the disk, that it couldn't have been quite large. I want to say that the lighting data for the open world is maybe a third of the disk, something like that. It's a pretty substantial component of the data.
>



---

## Slide 59 — 00:21:19

![Slide 59](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_059.png)


**📌 要点汇总**
- 团队投入大量工作对数据进行压缩和存储优化  
- 采用高效的数据存储方式以适配PS5的Kraken压缩器  
- 使用多种技巧提升数据压缩效果

> And the team goes through a lot of work to compress that data, find efficient ways of storing it, putting it in formats that can be nicely compressed by the Kraken compressor on the PS5, and so there's all sorts of tricks to get stuff.
>



---

## Slide 60 — 00:21:40

![Slide 60](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_060.png)


**📌 要点汇总**
- 需要适配蓝光光盘，这对存储空间是一个挑战  
- 游戏文件大小需控制在可流媒体播放的范围内

> To fit on a Blu-ray, which is a challenge of its own, and then also stay small enough to stream in as we as you play the game.
>



---

## Slide 61 — 00:21:49

![Slide 61](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_061.png)


**📌 要点汇总**
- PS5 上使用光线追踪全局光照（ray traced global illumination）存在性能成本问题  
- 反射（reflection pass）对性能影响较大，需权衡取舍  
- 在纽约市等场景中，反射对视觉效果至关重要，不可轻易牺牲  
- 快速移动镜头和镜头切换对渲染技术提出更高时间要求  
- 光线追踪全局光照需要时间“稳定”，在某些场景中难以实时实现

> Cool, yeah. Thinking about the lighting, though, real quick. I'm just wondering if you've looked forward — you guys are really pushing ray tracing on the PS5. Have you examined, explored the cost of something like doing ray traced global illumination? Do you think it's actually feasible on these platforms in a game like this, or is it still just a little bit too much, especially if you factor in the reflection pass? Every game has its own trade-offs and environment and style of play. I think one thing we looked at was — we're in New York City. The reflections are just hugely important for that, the look of that space. Yeah, and we wouldn't want to sacrifice any of that for something else.
>
> Another component is we move so fast through that space that we can't afford much time for rendering techniques to sort of resolve — that's moving through it. That's also camera cuts and things like that. Noising it. And it's something I notice as a compromise of ray traced GI is that these scenes need time to settle. I mean, that's a broad generalization. Some people are doing some awesome stuff with it, but for us, I know we wanted to sure focus on reflections and make sure you know.
>



---

## Slide 62 — 00:23:12

![Slide 62](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_062.png)


**📌 要点汇总**
- 城市快速移动时表现稳定且正确  
- 新 York 的高密度环境带来更多交通和细节  
- 细节更贴近玩家视角，提升沉浸感

> Any quick traversal through the city was really looking stable and correct, I guess, as much as we could as you were moving through it. But all that stuff is so exciting. I mean, you can do some gorgeous stuff with those techniques, so we won't be ignoring them. There we go.
>
> Of course, you mentioned New York, and another part of New York is, of course, the density of stuff, and that's something I really noticed and picked up on here. It's just like there's so much more traffic—just pedestrians, plus just more general detail from any perch where you just look. It feels like there's detail closer to the player.
>



---

## Slide 63 — 00:23:51

![Slide 63](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_063.png)


**📌 要点汇总**
- 不同细节层次（LOD）和多种系统共同影响画面细节表现  
- 纹理根据摄像机距离动态加载和混合  
- 远距离建筑使用“imposter”系统进行简化表示

> And maybe you could talk a little bit about all those different factors and how that's changed for this game. It's funny to see people talk about it a bit because there's this notion of, oh, there's LODs and you just watch everything transition in and out of them. But I think there's like ten or fifteen interlocking systems that all factor into how detailed something might look. You have textures streaming in and out at different distances to the camera and blending into each other. You have models with LODs that you see at different distances. You have our imposter system, which is for distant buildings. How do you represent those?
>



---

## Slide 64 — 00:24:30

![Slide 64](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_064.png)


**📌 要点汇总**
- 使用低多边形模型以保持内存占用低  
- 可随时运行并查看布鲁克林和皇后区的全貌  
- 需要高效表示高分辨率场景  
- 引入新的高分辨率 imposters 提升视觉效果  
- 新增中距离版本的建筑模型细节更丰富

> In a low poly way that you can keep in memory all the time. At any time, run up a building, look—you can see the whole world in Brooklyn and Queens now. How do we represent those efficiently? When do we transition to something better looking, etc.? So in this game, we added a new high-res version of those imposters. So there's a new middle distance version of a building that has more.
>



---

## Slide 65 — 00:24:58

![Slide 65](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_065.png)


**📌 要点汇总**
- （过渡内容，无关键要点）

> Geometric detail than the far ones, but isn't yet independent models for different pieces that we need to render, but you.
>



---

## Slide 66 — 00:25:06

![Slide 66](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_066.png)


**📌 要点汇总**
- （过渡内容，无关键要点）

> Get real reflective windows on those. It's like that's part of the transition, Pete. We also have a lot of.
>



---

## Slide 67 — 00:25:15

![Slide 67](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_067.png)


**📌 要点汇总**
- 提到需要在远处存在的物体，如大型空调设备。  
- 强调物体在远距离场景中的重要性。  
- 用于说明环境构建或视觉设计中的考虑因素。

> Objects that need to exist at a distance, things like big air conditioning units or.
>



---

## Slide 68 — 00:25:24

![Slide 68](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_068.png)


**📌 要点汇总**
- 建筑或水塔顶部的天线会影响轮廓呈现  
- 即使是小物体也需要考虑其影响  
- 不同场景下效果会有明显差异

> Antennas on top of buildings or water towers, which affect silhouettes. So even though that's a small object, you'd want to stream in. It's going to vary obviously.
>



---

## Slide 69 — 00:25:33

![Slide 69](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_069.png)


**📌 要点汇总**
- 近距离物体需动态出现以增强真实感  
- 远距离建筑需突出轮廓与独特形状  
- 不同距离使用独立模型以提升视觉效果  
- 窗户采用特定技术实现不同距离的融合效果

> Pop in as you get close to it, or appear. And we want far buildings to have those sort of distinctive shapes on top of their silhouettes. So, those exist as sort of these independent models that we have showing at different distances, far away and close. The windows have their own techniques to blend at different distances.
>



---

## Slide 70 — 00:25:51

![Slide 70](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_070.png)


**📌 要点汇总**
- 材料具有不同细节层次，如高度、高度效果和视差遮挡  
- 细节随距离变化而出现或消失  
- 目标是让这些变化不可见，使大脑自动补充远处细节  
- 让用户感觉场景与真实体验一致

> Distances—the materials have their own levels of detail, such as height, height effects, and parallax occlusion, which come in and out as you get close and far. The goal is to make all of this invisible, so your brain fills in the details for the far stuff and makes you feel like it's the same as if you were.
>



---

## Slide 71 — 00:26:10

![Slide 71](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_071.png)


**📌 要点汇总**
- 提到在PS4平台上开发时，场景中建筑物的多样性受到限制  
- 原始设计中建筑物在远处会简化为方块状  
- 开发者在高处观察时特别注意到这种视觉简化问题

> Yeah, that's definitely something I really noticed, especially sitting up on some of those perches. Just the general variety across the scene, because, you know, in the original, you kind of look out at the buildings, and there's a point where they just kind of turn to blocks. You know what I mean? And it's, you know, within the constraints of a PS4, right?
>



---

## Slide 72 — 00:26:26

![Slide 72](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_072.png)


**📌 要点汇总**
- 远距离观察时，表面细节的微妙变化显著提升整体质量  
- 视觉体验还受其他因素影响，需综合考虑

> But here, it feels like there's much more subtlety on every surface from a distance, which does make a huge difference in terms of quality. And then, of course, there are other factors that contribute to the overall visual experience.
>



---

## Slide 73 — 00:26:40

![Slide 73](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_073.png)


**📌 要点汇总**
- 在建筑模型中引入“烘烤”步骤，模拟长期天气影响如雨水侵蚀。  
- 通过几何分析预测污渍和磨损模式，如窗台和建筑侧面。  
- 该过程生成动态输入，增强建筑外观的真实感。

> Well, so to speak, to the wear and tear on buildings. Oh, yeah, please. Since you mention it, sort of the blocky, flat sides. One thing we did was we introduced this bake step on buildings, kind of that looks at their geometry and says, "Well, if it had been raining here for 50 years, like here's where the grime would be around the windowsills, or this is a wear pattern on the side of this building." That can be a dynamic input.
>



---

## Slide 74 — 00:27:09

![Slide 74](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_074.png)


**📌 要点汇总**
- 使用烘焙的 imposters 可以将材质和着色器直接嵌入到特定的 imposter 中  
- 通过添加宏观破损效果，使砖材质更具真实感和多样性  
- 建筑物上的褪色壁画效果提升了整体视觉的真实感  
- 这种技术有助于减少卡通化效果，使场景更贴近现实

> To a material and shader when you're close to it, but since we bake those imposters, we can bake it right into that unique imposter. So you can get, yes, that's a brick building, and we have one. Well, no, we have many brick materials. But for the side of that building, it's a brick material, but we get to feed in this sort of macro break up to that brick material that gives it. Oh, there was a mural here, and it faded away 10 years ago, and so you have this sort of chunky color over here, like that, that type of thing, and that has added a lot of variety. Looking out over a Manhattan that makes it feel less cartoony and more real.
>



---

## Slide 75 — 00:27:45

![Slide 75](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_075.png)


**📌 要点汇总**
- 提到 traversal 速度提升，是原游戏的 3-4 倍  
- 新功能让摄像机可以更流畅地穿越场景  
- 该改进对 Miles 和 Spider-Man 重制版有明显影响

> Actually, thinking of that, I mentioned traversal, and I'm curious if you can speak on that a little bit because that's another new thing. It's like the speed of traversal. What did that look like for you guys in terms of implementing that? Because the camera can now just fly across the screen. It feels like three or four times as much, three or four times the speed of what was possible in the original game. Yeah, certainly that was something we felt. The potential for Miles and Spider-Man remastered, but.
>



---

## Slide 76 — 00:28:18

![Slide 76](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_076.png)


**📌 要点汇总**
- 确保游戏在PS5和PS4上体验一致  
- 已实现游戏平衡性和兼容性优化

> Didn't want those games to feel different on PS5 versus PS4. We had balanced that gameplay and had all this.
>



---

## Slide 77 — 00:28:25

![Slide 77](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_077.png)


**📌 要点汇总**
- 计划进一步推进项目，机翼设计提供了良好机会。

> Put it out, and so we knew we wanted to push it a bit farther. The wings were a great opportunity to do that.
>



---

## Slide 78 — 00:28:33

![Slide 78](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_078.png)


**📌 要点汇总**
- 游戏升级后移动速度提升至原来的两倍  
- 建筑顶部的超级弹弓发射速度是普通弹弓的三倍  
- 有快速移动摄像机的电影化场景设计，增强游戏体验

> As you upgrade yourself in the game, I think you can go about twice as fast as in the first couple of games. And then there's the super slingshots on the building tops that fire you off about three times as fast. There's some cinematic moments that I think you caught in your video, your review video, that really have fun with moving the camera quickly through that space. It's fun.
>



---

## Slide 79 — 00:28:59

![Slide 79](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_079.png)


**📌 要点汇总**
- 主机硬件性能非常出色，特别是超快的SSD。  
- 这一点我们已经讨论过无数次，但接下来需要关注的是如何充分利用这些硬件。

> It's the hardware in the console that's extremely good. It's very fast SSD and all this. We've talked about this a million times, but part of what you need to do then is
>



---

## Slide 80 — 00:29:14

![Slide 80](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_080.png)


**📌 要点汇总**
- 强调引擎处理数据加载速度的重要性，这是性能瓶颈所在  
- 探讨如何减少数据加载量以提升效率  
- 鼓励在数据优化方面进行创新尝试

> Work on well. How fast can your engine interpret that data as it's loading it in? Because that's now your bottleneck on stuff. And we also do a lot of work on how we can get less data—how much less can you load? Does that make sense? There's a lot of creativity around that.
>



---

## Slide 81 — 00:29:35

![Slide 81](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_081.png)


**📌 要点汇总**
- （过渡内容，无关键要点）

> One of the ones I really liked in this game is one of our animation programmers came up with a way to stream animations, in a sense. Now, how do I describe this?
>



---

## Slide 82 — 00:29:45

![Slide 82](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_082.png)


**📌 要点汇总**
- 动画数据量庞大，但并非所有动画需同时加载  
- 游戏需实时响应，无法提前预知所需动画  
- 每隔3至4帧加载动画，保持部分动画常驻内存  
- 需要时从SSD读取剩余帧，实现流畅过渡  
- 最坏情况下仅需1帧过渡即可保持动画连贯性

> Spider-Man is like a very complex character. He's got a million different moves and blends and state machines, and he can fly, swing, and punch guys. The amount of animation data you have for a character is enormous. But what if we're not playing them all simultaneously? You don't need all that data at the same time. However, the gameplay needs to be reactive. You might need it next frame or two frames from now, and not know ahead of time. You can't get ready for that. And so he came up with a system where many animations load with every third or fourth frame resident in memory all the time. Then, when you go to play it, we hit the SSD and fill in all the extra frames of animation. At worst, you're looking at one frame that blends in.
>



---

## Slide 83 — 00:30:47

![Slide 83](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_083.png)


**📌 要点汇总**
- 动画流媒体成本降低75%至80%  
- 不同团队间的创意无缝衔接  
- 实现跨团队协作的流畅体验

> Imperfectly into the next, but really, it's like completely seamless, and you just cut your animation streaming costs by seventy-five or eighty percent. So that type of creativity across different groups—you don't see that, but you know—it comes through.
>



---

## Slide 84 — 00:30:58

![Slide 84](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_084.png)


**📌 要点汇总**
- 快速遍历和加载世界依赖于特定技术实现  
- 该技术在游戏开发中常被讨论  
- 类似功能（如传送门）在其他游戏（如 Ratchet & Clank）中已有应用

> That's the sort of thing that enables that fast traversal and streaming through the world. And so, this is actually an interesting discussion point that I've seen brought up often, actually, with this traversal and fast loading and all that. Conceptually, being able to load, like, to go directly down into a map, or like, load quickly to another area, or use portals—this stuff has existed in other games prior to. Like Ratchet prior to the Spider.
>



---

## Slide 85 — 00:31:29

![Slide 85](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_085.png)


**📌 要点汇总**
- 提到游戏开发中数据传输量是关键因素  
- PS4 上已有类似“假象系统”（imposter system）的低速率处理概念

> Man, games, but I think based on what you've said here and other things, just knowing about this game, the difference isn't so much what you're doing; it's the amount of data that's being moved to do it, right? I can't speculate too much on what they're doing, but here's some of what's gotten us to where we are. One is that even on PS4, we had that sort of imposter system notion. We have this notion of a low rate.
>



---

## Slide 86 — 00:32:00

![Slide 86](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_086.png)


**📌 要点汇总**
- 使用城市版本作为基础，有助于实现光线追踪反射系统  
- 该版本为反射系统提供了坚实的基础  
- 同样适用于其他相关系统的开发

> Version of the city that's always around. That was a great boon when it came time to do ray-traced reflections, because that was the foundation of that system. Similarly, it's a great boon.
>



---

## Slide 87 — 00:32:08

![Slide 87](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_087.png)


**📌 要点汇总**
- （过渡内容，无关键要点）

> Just jumping into a fast travel system of some sort.
>



---

## Slide 88 — 00:32:14

![Slide 88](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_088.png)


**📌 要点汇总**
- 早期接触 PlayStation Five 硬件，提升了系统灵活性和动态性  
- 纹理流传输优先级优化，确保高效运行  
- 硬件体验推动了系统设计的改进

> There's something ready there, right? And it looks a lot like that pause map. We were able to work with PlayStation Five hardware very early. We've gotten a lot of time with this hardware, and it has pushed us in that sense to make a lot of these systems more flexible and dynamic. To make sure our texture streaming is prioritizing things correctly and efficiently hitting that hard.
>



---

## Slide 89 — 00:32:45

![Slide 89](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_089.png)


**📌 要点汇总**
- （过渡内容，无关键要点）

> Where to make sure we can unload stuff as dramatically.
>



---

## Slide 90 — 00:32:51

![Slide 90](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_090.png)


**📌 要点汇总**
- 强调快速移除不再需要的功能的重要性  
- 从早期游戏到《Ratchet and Clank》再到当前游戏，持续优化迭代  
- 保持只保留下一次开发所需的核心功能

> And quickly as we can when we no longer need it, and really it has been an iterative walk through those early games through our launch titles through Ratchet and Clank to this game, where we are continually building on that ability to quickly get rid of what we don't need, only keep what we need next time.
>



---

## Slide 91 — 00:33:14

![Slide 91](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_091.png)


**📌 要点汇总**
- 需要从远处流式传输纹理到门户另一侧，以确保视觉一致性  
- 多个系统需协同工作，接近性能极限  
- 声音传播和反射是已有技术，但需适配复杂场景  
- 需要合适的工具来创建和优化声音效果  
- 运行时需高效处理声音，以提供沉浸式体验

> Bring in the most important stuff, and let some more come in as we go. Even knowing, as you look through a portal, I need to stream in this texture on the other side of the portal, even though it's dramatically far from where my camera happens to be at the moment, right? And making sure all those systems fit together really nicely. So we're probably coming up on the limit here, but I'd be remiss if I didn't ask you about sound. Because this is something I really picked up on, especially as a user of a surround sound system. And I'm wondering if you can talk about how some of these things work. How does the room propagation work? How does the sound reflections work? These are techniques that have sort of been around for a while. And one of the problems is how to consistently apply them to a complicated world. How to give the right tools for authoring them? How to make something that can run efficiently? At runtime, truly give a sense for that. So there's sound propagating through rooms.
>



---

## Slide 92 — 00:34:23

![Slide 92](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_092.png)


**📌 要点汇总**
- 游戏中使用了声音反射系统，模拟建筑物间的回声效果  
- 雨天场景中，系统能动态识别周围环境并调整音效交互  
- 该技术增强了沉浸感，提升了玩家的环境感知体验

> There's sound, sort of reverberating in the correct way when you're between buildings. One of my favorite ones, actually, is there are some rainy moments in the game, and that system sort of projects out around you, understands all the surfaces that it interacts with.
>



---

## Slide 93 — 00:34:40

![Slide 93](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_093.png)


**📌 要点汇总**
- 雨声效果需根据场景正确混音  
- 屋顶场景需考虑空调材质对声音的影响  
- 需确保环境音与背景音融合自然

> Rain might be hitting, and then plays the correct sort of sounds and mixes it correctly. So if you're on a rooftop, and there is an aluminum AC.
>



---

## Slide 94 — 00:34:50

![Slide 94](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_094.png)


**📌 要点汇总**
- 通过不同材质（铝 vs 橡胶）的雨声实现空间化音效  
- 音频团队在场景中应用了多种声音定位技术  
- 随着角色靠近事件点，声音效果会动态变化

> Event ten feet away from you. Then, as you walk towards it, you will hear the sound of rain hitting aluminum, as opposed to the rain hitting a rubber rooftop, and you will hear it spatialized correctly in that space. So, I know the audio team and our audio programmers take a lot of pride in that and how they've sort of applied these techniques through the spaces that we have. I wish I could show.
>



---

## Slide 95 — 00:35:15

![Slide 95](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_095.png)


**📌 要点汇总**
- PlayStation 最新固件新增 Dolby Atmos 支持，可将 Tempest 音频数据转化为 3D 空间音效  
- 默认情况下 Tempest 音频数据已适配 Atmos 环境，但更新后可更精准地针对 Atmos 进行混音  
- 游戏的音效团队为该功能进行了大量定制 Atmos 混音工作，一经确认即刻执行

> You can debug the visualization for the rain. It's really cool. It's all these hexagons around you that visualize the space and show you what it's hitting and finding. So, thinking of spatial audio, one of the big features in the recent PlayStation firmware was the addition of Dolby Atmos support, where it can take the Tempest audio data and create a real 3D effect in a setup that has Atmos support. I'm curious, what kind of visibility you, as a developer, have on that feature? And if you can actually do any sort of custom mix for Atmos, or if it's just taking the Tempest audio data that's created for headphones and applying it over. By default, we get a great application of the Tempest 3D spatialization to an Atmos setup. But with the new updates, we can actually have the game target Atmos more specifically. Our cinematics audio team did a ton of custom Atmos mixing for this game. As soon as they knew it was coming, they did it immediately.
>



---

## Slide 96 — 00:36:18

![Slide 96](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_096.png)


**📌 要点汇总**
- 首款支持自定义Atmos混音的PlayStation游戏  
- 游戏与Atmos混音功能同步推出，时机把握良好

> And we're super excited to be—what I think is the first PlayStation game, or at least one of the first—that has custom Atmos mixes for its game. So, yeah, I think we're right as this feature came out, so I think we timed it well.
>



---

## Slide 97 — 00:36:30

![Slide 97](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_097.png)


> *（该幻灯片时间段内未检测到语音内容）*


---

## Slide 98 — 00:36:35

![Slide 98](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_098.png)


**📌 要点汇总**
- 游戏使用 Atmos 技术实现高质量的 Cinematics 混音效果  
- 开发者特别提到 Blu-ray 光盘容量限制是重要挑战  
- 游戏体积仅比《蜘蛛侠重制版》大约 20%  
- 需要在有限的存储空间内实现更高的画质和电影级表现

> Just about right. So yes, if you do have an Atmos setup, you get some awesome mixes through Cinematics, and yeah, that stuff's really really cool. So is there anything else you want to wrap up with? Anything you're especially proud of in the game? Something you wanted to highlight? Something you're just like, man, this was, this is something I really loved working on. Any thoughts on that? That's a tricky one to pull out of my head. But I want to give a shout out to some of the mundane problems that you don't see, like in the action, right? Yeah, yeah. As you play the game, but are so important. There's like, like I mentioned before, that we have to fit this game on a Blu-ray disc. I mean, you can go multiple Blu-rays, but the goal is to fit it on one. And this game, I want to say, is only maybe 20% larger than Spider-Man Remastered, as far as the disc size is concerned. But the amount of extra fidelity and quality and cinema.
>



---

## Slide 99 — 00:37:38

![Slide 99](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_099.png)


**📌 要点汇总**
- （过渡内容，无关键要点）

> We packed in there is huge, and this factors into.
>



---

## Slide 100 — 00:37:44

![Slide 100](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_100.png)


**📌 要点汇总**
- 游戏中包含大量高细节动画数据，如面部和身体动画  
- 一段30秒的电影动画文件大小达到1GB，占用磁盘空间过高  
- 技术动画团队采用反向蒙皮和关节设置等方法优化动画数据  
- 多个团队合作使用压缩技术，减少纹理和数据体积  
- 优化后游戏体积仅略大于前作，但质量显著提升

> Streaming and how we utilize that bandwidth as well. So one example, we have a ton of animation data in this game. Our faces are more detailed. Our bodies are more detailed. One of the first things we showed was a cinematic with Kraven where he's kind of like hunting another hunter and kind of bored because it's not challenging enough for him. We made that cinematic, and the animation team animated the way they wanted, and then it was like a gigabyte in size. We were like, "This is a 30-second cinematic shot. It can't take up more than a full percent of the disk. We're never going to ship a game," so finding ways to take that data, our technical animation team came up with some awesome sort of like reverse skinning and joint setups.
>
> A lot of teams, a couple folks in my department, put a lot of work into understanding the cracking compressor and how we can work with textures and things to just cram everything down small, fit it on a disc, make sure people have a good size download that's not too onerous to fit on their console, and deliver something that I think you put it side by side, it feels head and shoulders above the first game, and yet is only like a little bit larger. That's the kind of behind the scenes thing that's fun. What else?
>



---

## Slide 101 — 00:39:15

![Slide 101](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_101.png)


**📌 要点汇总**
- 行人现在可以自由进出建筑物和商店，行为更真实  
- 车辆悬挂系统和行为逻辑已改进，更贴近现实  
- 行人与车辆的交互行为更加复杂和多样化

> You mentioned pedestrian and open world stuff. Yeah, vehicles have suspensions and behave differently now. You see a lot more behavior around pedestrians in cars. The pedestrians walking around the world can go in and out of buildings and shops, which they didn't do before.
>



---

## Slide 102 — 00:39:31

![Slide 102](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_102.png)


**📌 要点汇总**
- 之前模型生成的角色体型差异较大  
- 服装搭配更加随机且多样化  
- 外观多样性显著提升

> Before, they have varying body sizes, and their outfits are much more randomized and swapped around. So you get a lot more just diversity in appearance.
>



---

## Slide 103 — 00:39:41

![Slide 103](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_103.png)


**📌 要点汇总**
- 角色和空间具有多样性，能够进行互动对话。  
- 采用模块化对话系统，支持围绕特定主题展开交流。

> Diversity of space and character. They have conversations with each other. There's this whole modular conversation system where they can have a topic.
>



---

## Slide 104 — 00:39:54

![Slide 104](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_104.png)


**📌 要点汇总**
- （过渡内容，无关键要点）

> And discuss it, and then one disagrees, and the other knows how to disagree or change the topic, and you know it's.
>



---

## Slide 105 — 00:40:02

![Slide 105](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_105.png)


**📌 要点汇总**
- （过渡内容，无关键要点）

> Not, you know, it's really fun to just sit and kind of listen to people around the city have these sort of reasonable conversations with each other as you walk around. There's all sorts of little touches.
>



---

## Slide 106 — 00:40:12

![Slide 106](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_106.png)


**📌 要点汇总**
- 游戏设计希望玩家能发现随机内容并产生惊喜和赞叹的时刻  
- 开场战斗（如Sandman fight）旨在立即给玩家留下深刻印象  
- 之前发布的预告片中展示了该战斗，引发玩家“剧透”讨论

> I'm excited for people to spend some time with the game, find random stuff, hopefully have some wow moments and "how did they do that" moments, and that's part of the fun of a new game, I guess. Yeah, you kind of get that right from the start with the Sandman fight, where it's just like, oh, okay, this is huge right away. That's cool. Yeah, I know we showed it in the last launch trailer, and people said, "Oh, spoiler," and I'm just like...
>



---

## Slide 107 — 00:40:44

![Slide 107](https://gerigory.github.io/assets/img/渲染技巧/Inside-Marvel-s-Spider-Man-2-The-Insomniac-Games-Tech-Breakdown/slide_107.png)


**📌 要点汇总**
- 该场景为专属丛林地图，用于特定过场动画  
- 地图中需实现真实的丛林光照与树叶动态效果  
- 技术美术团队投入大量精力确保画面质量  
- 无缝切换至不同场景是技术挑战之一  
- 团队重视细节，力求每个画面都达到高标准  
- 自研技术对打造独特游戏体验至关重要

> There's so much stuff to experience. This is not ruining anything for anybody. I hope you're excited. Even just that one fight has so many surprises and twists and turns. Indeed. And there's some really awesome work that went into the bosses and cinematic moments across this game. So. I also appreciate you mentioning the Craven cutscene at the beginning, but that's not even in the city, right? Like that's a completely different, like map, I guess, bespoke jungle map that was made just for that. It's a little jungle space. So you get this little jungle space, and that stuff's cool. You're able to seamlessly transition to these different spaces, and there's a bit more of that in there as well. That's. It was a fun challenge for our technical art team to say, "Well, yeah, it's only for this one cinematic, but we really want to have a realistic jungle and light propagation through a canopy, and the leaves have to have the right subsurface, and they have to slowly wave around and all that." So a lot of just effort goes into individual shots and spaces, but it's one of the great parts about working at the studios. People really care about their craft and want every little bit of it to look good and come across to players. And I'm really happy to hear all that, and I'm glad that you guys are still pushing your own in-house technology. I know that's not easy to support, but it's something that people notice and appreciate, and it does help create these unique experiences. I think. Well, well done on the game is what I will say. I. Thank you very much. Thank you. I'm just again excited for players to spend some time with it and have a good time. All right. Well, I've probably used up enough of your time. We're coming up on forty five minutes here, so it was a pleasure to have you join us here to chat about Marvel Spider-Man Two. So, I guess we'll find you in the credit somewhere, obviously, when people get there. But yeah, hopefully you guys enjoyed this little interview, and we'll see you next time.
>



---
