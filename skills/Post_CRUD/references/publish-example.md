# 【GDC 2022】Adventures with Deferred Texturing in Horizon Forbidden West

这是 `Post_CRUD` skill 的转换示例。展示源 md → 站点 md 的完整映射。

## 源文件（TechniqueDocs 中的笔记格式）

```markdown
---
tags:
  - 领域/游戏研发/渲染/植被
  - 来源/GDC/2022
  - 类型/技术笔记
date: 2026-05-11
status: active
type: raw
ingest_status: processed
synthesis: "[[GDC2022 - ...-要点提炼]]"
---

# GDC2022 - Adventures with Deferred Texturing in Horizon Forbidden West

> 来源：D:\迅雷下载\GDC 2022 - ....pptx
> 提取时间：2026-05-12 10:14:42

## 📋 全文内容摘要
...

## Slide 1

![Slide 1](<./GDC2022 - ....assets/slide_001.png>)
```

## 转换后（_posts 站点格式）

```markdown
---
layout: post
title: "【GDC 2022】Adventures with Deferred Texturing in Horizon Forbidden West"
date: 2026-05-11
img: GDC/2022/GDC2022-Adventures-with-Deferred-Texturing-in-Horizon-Forbidden-West/slide_001.png # Add image post (optional)
fig-caption: # Add figcaption (optional)
tags: [GDC, 2022, Rendering, Vegetation]
description: （从摘要块提取的一句话中文摘要）
---

> 来源：D:\迅雷下载\GDC 2022 - ....pptx
> 提取时间：2026-05-12 10:14:42

## 📋 全文内容摘要
...

## Slide 1

![](https://gerigory.github.io/assets/img/GDC/2022/GDC2022-Adventures-with-Deferred-Texturing-in-Horizon-Forbidden-West/slide_001.png)
```

## 转换要点对照表

| 项 | 源 | 目标 |
|---|---|---|
| front matter | 树状 tags + status/type 等笔记字段 | layout/title/date/img/tags/description 站点六字段 |
| title | H1 原文 | 【来源 年份】+ 去冗余前缀的标题 |
| date | `date: 2026-05-11` | 同值（决定首页排序） |
| H1 | 正文首行 | 删除（title 由页面模板渲染） |
| 图片引用 | `![Slide 1](<./xxx.assets/slide_001.png>)`（可能含 %20） | `![](https://gerigory.github.io/assets/img/<分类>/<年>/<slug>/slide_001.png)` |
| 图片文件 | `<源md名>.assets/` 目录 | `assets/img/<分类>/<年>/<slug>/`（压缩后） |
| 分类/年份 | 从文件名或 tags 推断（GDC2022 → GDC/2022） | `_posts/GDC/2022/` |
| slug | title 转写 | `GDC2022-Adventures-with-Deferred-Texturing-in-Horizon-Forbidden-West` |

## 特殊情况

1. **双 assets 目录**（如 Alan Wake 2）：md 引用 `<H1标题>.assets/` 而非 `<文件名>.assets/`
   → 脚本自动在多个候选目录中解析真实位置（见 `batch_publish.py` 的 `resolve_src`）
2. **URL 编码引用**（`%20`）：Unescape 后取真实文件名
3. **杂项文章**：无来源前缀 → 分类 `渲染技巧`，无年份层
4. **title 冗余前缀**：`【GDC 2021】GDC2021 - Xxx` → `clean_title_prefix()` 自动剥离
