---
name: Post_CRUD
description: 管理 GitHub Pages Jekyll 博客（gerigory.github.io）_posts 目录中文章的增删改查。当用户要求创建/修改/删除/发布博客文章、查询文章内容、将本地 Markdown 笔记发布到博客、或提到 _posts 目录时使用。
compatibility: Python 3.10+（标准库），git，PowerShell/任意 shell
---

# Post_CRUD — 博客文章增删改查技能

管理 Jekyll 博客 `G:\Gerigory.github.io` 的 `_posts` 文章目录，提供符合站点规范的创建、修改、删除、查询能力，并封装发布（commit/push）与线上验证流程。

## 站点关键约定

| 项 | 值 |
|---|---|
| 仓库根目录 | `G:\Gerigory.github.io` |
| 文章目录 | `_posts/<分类>/<年份>/YYYY-MM-DD-<slug>.md`（`渲染技巧` 无年份层；`UnrealFest` 无年份层） |
| 图片目录 | `assets/img/<分类>/<年份>/<文章slug>/xxx.png` |
| 站点基址 | `https://gerigory.github.io` |
| 文章 URL | `https://gerigory.github.io/<permalink>/`（permalink 由 title 生成） |
| permalink 规则 | `_config.yml` 为 `:title/`，Jekyll 自动取 title 去掉非法字符、空格转连字符生成 |

## 文章格式规范（创建/修改时必须遵守）

### Front matter 模板

```yaml
---
layout: post
title: 【GDC 2022】Adventures with Deferred Texturing in Horizon Forbidden West
date: 2026-05-11
img: GDC/2022/<slug>/slide_001.png # 封面图，相对 assets/img 的路径，可选
fig-caption: # 图注，可选
tags: [Rendering, Texture, GDC, 2022]
description: 一句话中文摘要（首页与文章页顶部展示）
---
```

- `layout: post` 固定
- `title`：展示标题。讲座类文章用 `【GDC 2022】主题名` 格式（来源+年份+主题），非讲座类直接用主题名
- `date`：YYYY-MM-DD。**用源文档的整理日期**（决定首页排序，新的在前）
- `img`：相对 `assets/img/` 的路径（不含 `assets/img/` 前缀）。无图可省略
- `tags`：行内数组格式 `[tag1, tag2]`。从文章来源/主题提取：讲座来源（GDC/Siggraph/UnrealFest/UFSH + 年份）+ 技术主题（如 Rendering, GI, Vegetation, Ocean）+ 游戏名
- `description`：中文一句话摘要，供首页列表与 SEO

### 文件命名

- `_posts/<分类>/<年份>/YYYY-MM-DD-<slug>.md`
- slug = title 的 ASCII 化转写：空格/特殊符号转 `-`，保留中文，去掉 `【】`，连续 `-` 合并为单个
- 例：title `【GDC 2022】Adventures with Deferred Texturing in Horizon Forbidden West` → slug `GDC2022-Adventures-with-Deferred-Texturing-in-Horizon-Forbidden-West`，date 2026-05-11 → 文件 `2026-05-11-GDC2022-Adventures-with-Deferred-Texturing-in-Horizon-Forbidden-West.md`

### 分类映射（源 → 站点分类）

| 源文件特征 | 分类 | 年份层 |
|---|---|---|
| 名含 `GDC` 或 tags 含 `来源/GDC` | `GDC` | 讲座年份（如 2022） |
| 名含 `Siggraph` 或 tags 含 `来源/Siggraph` | `Siggraph` | 讲座年份 |
| 名含 `UnrealFest` / `UFSH` 或 tags 含 `来源/UFSH` | `UnrealFest` | 无年份层 |
| 其他杂项 | `渲染技巧` | 无年份层 |

### 正文图片引用（关键！）

统一使用**站点绝对 URL**（与现有文章一致）：

```markdown
![](https://gerigory.github.io/assets/img/<分类>/<年份>/<slug>/<图片文件名>)
```

- 从源 md 的 `![alt](<./xxx.assets/img_001.png>)` 或 `![alt](./xxx.assets/slide_001.png)`（可能含 `%20` URL 编码）解析出图片文件名
- 解析后必须 Unescape URL 编码得到真实文件名
- 图片统一拷贝到 `assets/img/<分类>/<年份>/<slug>/` 下（按需压缩，见下）
- **禁止**在正文中使用相对路径（`./`、`../`）——Jekyll 生成页面后相对路径会失效

### 源 front matter 的转换

源笔记 front matter（`tags: 领域/...` 树状标签、`status/type/ingest_status/synthesis` 等字段）**全部丢弃**，只保留 `date` 值（若有）与 tags 树中可用的信息（来源/年份），按站点模板重写。

### 正文结构

- 去掉源文件第一个 `# H1`（与 title 重复）；Jekyll 用 title 渲染页头
- 保留 `> 来源：...` 引用块（溯源信息，建议保留）
- 其余内容原样保留（含中英对照段落、要点列表等）
- 保留级联 `---` 分隔线

## 图片压缩规范

发布前对 PNG 图片压缩（用户选择画质有损压缩以控制仓库体积）：

- 工具：Pillow（PIL 12.3.0，已装）
- 规则：PNG → PNG（保持格式与文件名不变，站内既有文章均为 PNG/JPG 原名引用）
  - 长边 > 1600px → 等比缩放到长边 1600px
  - 量化 palette 256 色（`Image.quantize`）效果不佳时（图内照片细节多）回退到 `optimize=True` 无损压缩
  - 目标：单张 ≤ 300KB，单篇图片总量降为原来的 10%–30%
- JPG/GIF 不动（本身已小）
- 压缩脚本见 `scripts/compress_assets.py`

## 目录与工具

```
skills/Post_CRUD/
├── SKILL.md           # 本文件
├── scripts/
│   ├── post_crud.py   # 核心脚本：查找/校验/统计
│   ├── publish.py     # 批量发布：转换源md → _posts + 压缩图片 → git提交
│   └── compress_assets.py  # 图片压缩
└── references/
    └── publish-example.md  # 转换示例（首次发布后补全）
```

## 操作指南

### 查询（Read）

自然语言找文章：先从用户话中提取关键词（中英文皆可），然后：

```
python skills/Post_CRUD/scripts/post_crud.py search <关键词1> [关键词2 ...] [--posts-dir G:\Gerigory.github.io\_posts]
```

- 脚本对 title（front matter）、tags、正文全文做关键词匹配，输出每篇的匹配得分与文件路径、date、description
- 多关键词为 OR 语义（任一命中即返回），按命中行数排序
- 中文关键词直接匹配（文件为 UTF-8）
- 命中后用 `read_file` 读文件头部 front matter 与命中行上下文给用户
- 库外记忆：也可对 `D:\MarkdownSpace\LLMWorkspace\TechniqueDocs` 源目录执行同样的 search（`--posts-dir` 指定）以查询未发布文章

### 创建 & 修改（Create/Update）

**场景 A：全新文章（无源文件）**
1. 从用户需求生成 title、tags、description、正文
2. 按「文章格式规范」写 front matter；正文图片引用用站点绝对 URL
3. 先把图片文件放入 `assets/img/<分类>/<年份>/<slug>/`（若 >100KB 走压缩）
4. 写 `_posts/<分类>/<年份>/YYYY-MM-DD-<slug>.md`
5. 校验：`python scripts/post_crud.py validate <md路径>`
6. 发布：`git add _posts assets/img && git commit && git push`（在仓库根目录）

**场景 B：从本地笔记发布（有源 md）**
1. 读源 md，按「分类映射」确定分类与年份层
2. 转换 front matter（丢弃源字段，提取 date 与 tags 信息重写为站点格式）
3. 转换正文：去 H1、图片引用改为站点绝对 URL（Unescape `%20`）
4. 图片处理：源 `.assets` 目录（图片与 md 同名）中**被引用的图片**拷贝到 `assets/img/<分类>/<年份>/<slug>/`，压缩
5. 校验 + 发布（同场景 A）

批量场景使用 `scripts/publish.py`（封装了上述 2–5 步）：

```
python skills/Post_CRUD/scripts/publish.py --source <源md路径> --site-root G:\Gerigory.github.io [--publish] [--compress]
```

### 删除（Delete）

1. 定位文章 md（通过 search）
2. 删除 md 文件；若 `assets/img/<分类>/<年份>/<slug>/` 目录仅该文章使用，一并删除
3. `git add -A _posts assets/img && git commit -m "remove post: <title>" && git push`
4. 线上生效后 URL 返回 404

### 发布与线上验证

1. 提交推送后，GitHub Pages 自动构建（1–10 分钟）
2. 验证方式：
   - `git log` 确认 commit 到达远端
   - 轮询 `https://gerigory.github.io/<permalink>/` 直到返回 200 且含文章 title（用 `Invoke-WebRequest`，间隔 60s，最多 15 次）
   - 抽查图片 URL 可达（200）
3. permalink 生成规则（`flexible-jekyll` 主题 `:title/`）：title 去掉 `【】` 等 Jekyll 认为不安全的字符，空格转 `-`，中文保留原样（URL 中呈现为 percent-encoded）。**不确定时**：本地 `bundle exec jekyll serve` 预览，或推送后从首页 HTML 解析实际链接
4. 大批量发布注意：
   - 单次 push 总量 ≤ 1.5GB（防超 2GB 限制），分批提交
   - 每批推送后线上验证再继续
   - GitHub 仓库建议上限 5GB，接近时需评估

## 校验清单（validate 子命令）

`post_crud.py validate <md>` 检查：
1. 文件名 `YYYY-MM-DD-*.md` 模式
2. front matter 完整性：layout/title/date/img/tags/description
3. title 格式建议（讲座类含 `【来源 年份】`）
4. date 格式 YYYY-MM-DD
5. 正文图片引用是否为站点绝对 URL 且指向的图片文件存在（在 `assets/img/` 下）
6. 无残留相对路径图片引用（`./`、`%20` 未解码等）
7. 正文不含 H1（应为 title 渲染）——建议但非强制
8. tags 数组格式
9. 文件 UTF-8 编码
