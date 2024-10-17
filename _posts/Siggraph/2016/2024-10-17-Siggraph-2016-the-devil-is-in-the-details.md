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

In the latest id Tech iteration, there was a big amount of updates/changes. But, for today, our focus is Rendering of course. 

For sake of time, we will focus on couple interesting topics, albeit there are many areas that were updated.

Our main goal, was from the start 60hz at 1080p across all platforms, all this while aiming at a high quality visual bar.

For this new iteration and given our relatively short development time, we had to pick our fights careful, has there was a substantial catchup todo, we tried as much as possible mitigate potential time consuming work – tl;dr keep it simple.

One thing I’m particularly happy, is that we have a fairly minimal amount of shaders due to careful design. About 100 unique shaders. Could actually be less if some tidy up.

Other very important goal was where could we help art doing their job, how to save their precious time and where could we speedup their workflow;

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片3.PNG)

At a high level a frame in DOOM looks something as this

We do a Hybrid approach, by using opaque passes and deferred for a nice quality / performance ratio.

Using Forward also has some auto-magic benefits for quality ( which we will talk soon ) and things like MSAA.

As you might have guessed, being Forward forces us to prepare all lighting and shading data ahead of time as much as possible.
. That means things like the data structure used to index into things like Light sources, are prepared ahead of time.
. Shadows are other obvious case. We do quite some work keeping costs down here, resorting to things like caching and smart composite to mitigate costs when update required.

For the deferred stage, we output the minimal data required for doing things like reflections, specular occlusion and so on.

I mention approximated times has times are always variable. For example posts can grow when DOF is enabled or some game related Post Process – albeit posts run in Async on consoles and Vulkan.
Or the usual Particles, where we can get cases with some heavy overdraw.

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片4.PNG)

A derivation from
“Clustered Deferred and Forward Shading”, Ola Olson et Al.
“Practical Clustered Shading”, Emil Person
Just works ™
Works implicitly on transparent surfaces
Independent from depth buffer
No false positives along depth

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片5.PNG)

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片6.PNG)

Important to mention: If volume intersecting view frustum, we perform frustum clipping, which increases number of planes

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片7.PNG)

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片8.PNG)

Can be better / improved – perf was quite ok already, ship it

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片9.PNG)

Mega-Texture was still used in this project, some relevant updates
Albedo, Specular, Smoothness, Normals, HDR Lightmap
Allows dynamic lighting
Fairly packed, BC3 page files ( an atlas )
HW sRGB support
Improved mipmap generation 
Baked Toksvig into smoothness for specular anti-aliasing
Feedback buffer UAV output directly to final resolution
Async compute transcoding
Old CPU transcoding ran slow on new consoles
Cost is now mostly irrelevant
Old design troubles still present
Overall, low texture quality
Reactive texture streaming = texture popping
Opaque geometry only
Page borders artefacts, low quality filtering, etc
Extra costs due to dependent lookups 
HDPhoto / BC compression artefacts

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片10.PNG)

Who here ever implemented deferred/geometry decals ? Raise your hands…

How fun was it dealing with all the trouble cases ?

*Have to compute your own derivatives, but just works across geometry edges and depth discontinuities

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片11.PNG)

Some math recap

Relevant to mention: we don’t concatenate scale and bias into matrix, as we rely on normalized uv coordinates for fragment clipping

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片12.PNG)

Limited to 4k per view frustum
Lodding
Art setups max view distance
Quality settings affect view distance as well
Works on non-deformable geometry
Apply object transformation to decal

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片13.PNG)

Some results

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片14.PNG)

Some results – this type of details are usually approximated in a relatively brute force way with multiple layers (per drawcall), on our case the cost is proportional to screen coverage

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片15.PNG)

Glass is another good example: the haze / condensation / blood – is all decaling modifying surface properties.

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片16.PNG)

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片17.PNG)

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片18.PNG)

Shadows are cached ahead of time into an Atlas
PC: 8k x 8k atlas ( high spec ), 32 bit 
Consoles: 8k x 4k, 16 bit
Variable resolution based on distance
Time slicing also based on distance
Optimized mesh for static geometry
Light mostly static ? 
Cache static geometry shadow map
No updates ? Ship it
Updates ? Composite dynamic geometry with cached result
Art setup and quality settings affects all
Resolution, time sliccing, etc

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片19.PNG)

Index into shadow frustum projection matrix
Then scale / bias into atlas
Same PCF lookup code for all light types
Less VGPR pressure
This includes directional lights cascades
Dither used between cascades 
Single cascade lookup  
Attempted VSM and derivatives
All with several artefacts
Conceptually has good potential for Forward
Eg. decouple filtering frequency from rasterization

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片20.PNG)

First person arms self-shadows.
Dedicated atlas portion.

![](https://gerigory.github.io/assets/img/Siggraph-2016-the-devil-is-in-the-details/幻灯片21.PNG)

Dynamics Indirect lighting 
Irradiance Probes approximation
SH 2 encoded
Volume texture

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

[[1]. Siggraph 2012 talk : Local Image-based Lighting With Parallax-corrected Cubemap](https://seblagarde.wordpress.com/2012/11/28/siggraph-2012-talk/)

[[2]. Game Connection 2012 talk : Local Image-based Lighting With Parallax-corrected Cubemap](https://seblagarde.wordpress.com/wp-content/uploads/2012/08/parallax_corrected_cubemap-gameconnection2012.pptx)
