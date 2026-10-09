#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Post_CRUD 核心脚本：文章查询(search)、校验(validate)、统计(list/stats)。

用法：
  python post_crud.py search 关键词1 [关键词2 ...] [--posts-dir DIR] [--limit N]
  python post_crud.py validate <md路径> [--site-root DIR]
  python post_crud.py list [--posts-dir DIR] [--category CAT]
  python post_crud.py stats [--posts-dir DIR]

查询对 front matter 的 title/tags 与正文全文做多关键词 OR 匹配，按命中数排序。
"""
import argparse
import json
import os
import re
import sys
import urllib.parse
from pathlib import Path

FRONT_MATTER_RE = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.S)


def parse_front_matter(text):
    """极简 YAML front matter 解析（仅支持本站点用到的扁平/行内数组字段）。"""
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return None, text
    fm_text = m.group(1)
    body = text[m.end():]
    fm = {}
    for line in fm_text.splitlines():
        if line.startswith('#') or not line.strip():
            continue
        mm = re.match(r'^([A-Za-z_-]+):\s*(.*)$', line)
        if mm:
            key, val = mm.group(1), mm.group(2).strip()
            if val.startswith('[') and val.endswith(']'):
                inner = val[1:-1].strip()
                fm[key] = [v.strip().strip('"\'') for v in inner.split(',') if v.strip()]
            else:
                # 去掉行内注释
                val = re.sub(r'\s+#.*$', '', val).strip()
                fm[key] = val
        elif line.startswith('  - ') or line.startswith('- '):
            # 树状 tags（源笔记格式）也收集到 tags
            tag = line.strip().lstrip('-').strip()
            if tag:
                fm.setdefault('tags', [])
                if isinstance(fm['tags'], list):
                    fm['tags'].append(tag)
    return fm, body


def iter_posts(posts_dir):
    """遍历 _posts 下所有 md（递归）。"""
    posts_dir = Path(posts_dir)
    if not posts_dir.exists():
        return
    for p in sorted(posts_dir.rglob('*.md')):
        if p.is_file():
            yield p


def load_post(path):
    try:
        text = Path(path).read_text(encoding='utf-8')
    except UnicodeDecodeError:
        text = Path(path).read_text(encoding='utf-8', errors='replace')
        return {'path': str(path), 'decode_error': True, 'fm': {}, 'body': ''}
    fm, body = parse_front_matter(text)
    return {'path': str(path), 'fm': fm or {}, 'body': body}


def cmd_search(args):
    keywords = [k for k in args.keywords if k]
    if not keywords:
        print(json.dumps({'error': 'no keywords'}, ensure_ascii=False))
        return 1
    results = []
    for p in iter_posts(args.posts_dir):
        post = load_post(p)
        if post.get('decode_error'):
            continue
        title = str(post['fm'].get('title', ''))
        tags = post['fm'].get('tags', [])
        if isinstance(tags, str):
            tags = [tags]
        tag_text = ' '.join(str(t) for t in tags)
        desc = str(post['fm'].get('description', ''))
        date = str(post['fm'].get('date', ''))
        title_hits = sum(1 for k in keywords if k.lower() in title.lower())
        tag_hits = sum(1 for k in keywords if k.lower() in tag_text.lower())
        body_hits = sum(post['body'].lower().count(k.lower()) for k in keywords)
        if title_hits or tag_hits or body_hits:
            # 评分：标题命中权重最高
            score = title_hits * 10 + tag_hits * 5 + min(body_hits, 50)
            results.append({
                'title': title,
                'date': date,
                'path': post['path'].replace('\\', '/'),
                'description': desc[:120],
                'score': score,
                'title_hits': title_hits,
                'tag_hits': tag_hits,
                'body_hits': body_hits,
            })
    results.sort(key=lambda r: -r['score'])
    results = results[:args.limit]
    print(json.dumps({'count': len(results), 'results': results}, ensure_ascii=False, indent=2))
    return 0


IMG_REF_RE = re.compile(r'!\[[^\]]*\]\(([^)]+)\)')


def cmd_validate(args):
    md_path = Path(args.md_path)
    if not md_path.exists():
        print(json.dumps({'error': f'file not found: {md_path}'}, ensure_ascii=False))
        return 1
    site_root = Path(args.site_root).resolve()
    issues = []
    warnings = []
    fname = md_path.name
    if not re.match(r'^\d{4}-\d{2}-\d{2}-.+\.md$', fname):
        issues.append(f'文件名不符合 YYYY-MM-DD-<slug>.md 模式: {fname}')
    text = md_path.read_text(encoding='utf-8', errors='replace')
    fm, body = parse_front_matter(text)
    if fm is None:
        issues.append('缺少 front matter（--- ... ---）')
        fm = {}
    for field in ('layout', 'title', 'date', 'tags', 'description'):
        if field not in fm or fm[field] in (None, '', []):
            issues.append(f'front matter 缺少字段: {field}')
    if 'layout' in fm and fm['layout'] != 'post':
        issues.append(f"layout 应为 post，当前: {fm['layout']}")
    if 'date' in fm and not re.match(r'^\d{4}-\d{2}-\d{2}$', str(fm['date'])):
        issues.append(f"date 应为 YYYY-MM-DD，当前: {fm.get('date')}")
    # H1 检查（建议）
    if re.search(r'^# ', body, re.M):
        warnings.append('正文含 H1 标题，建议删除（页面标题由 front matter title 渲染）')
    # 图片引用检查
    img_root = site_root / 'assets' / 'img'
    n_ok = 0
    for m in IMG_REF_RE.finditer(body):
        ref = m.group(1).strip()
        ref_clean = ref.strip('<>').split(' ')[0]
        if ref_clean.startswith('./') or ref_clean.startswith('../') or '.assets/' in ref_clean:
            issues.append(f'图片引用为相对路径/未转换: {ref_clean[:100]}')
            continue
        if '%20' in ref_clean or '%E' in ref_clean or '%C' in ref_clean:
            # 站点绝对 URL 中允许 percent-encoding，但本地文件校验需解码
            pass
        if not ref_clean.startswith('https://gerigory.github.io/assets/img/') and not ref_clean.startswith('/assets/img/'):
            issues.append(f'图片引用非站点绝对 URL: {ref_clean[:100]}')
            continue
        rel = urllib.parse.unquote(ref_clean.replace('https://gerigory.github.io/assets/img/', '').replace('/assets/img/', ''))
        target = img_root / rel
        if not target.exists():
            issues.append(f'图片文件不存在: assets/img/{rel}')
        else:
            n_ok += 1
    print(json.dumps({
        'file': str(md_path),
        'issues': issues,
        'warnings': warnings,
        'images_ok': n_ok,
        'pass': len(issues) == 0,
    }, ensure_ascii=False, indent=2))
    return 0 if not issues else 1


def cmd_list(args):
    out = []
    for p in iter_posts(args.posts_dir):
        post = load_post(p)
        fm = post['fm']
        rel = p.relative_to(args.posts_dir)
        cat = rel.parts[0] if len(rel.parts) > 1 else '.'
        if args.category and cat != args.category:
            continue
        out.append({
            'title': str(fm.get('title', p.stem)),
            'date': str(fm.get('date', '')),
            'category': cat,
            'path': str(p).replace('\\', '/'),
        })
    out.sort(key=lambda x: x['date'], reverse=True)
    print(json.dumps({'count': len(out), 'posts': out}, ensure_ascii=False, indent=2))
    return 0


def cmd_stats(args):
    cats = {}
    total = 0
    for p in iter_posts(args.posts_dir):
        total += 1
        rel = p.relative_to(Path(args.posts_dir))
        cat = rel.parts[0] if len(rel.parts) > 1 else '(root)'
        cats[cat] = cats.get(cat, 0) + 1
    print(json.dumps({'total': total, 'categories': cats}, ensure_ascii=False, indent=2))
    return 0


def main():
    ap = argparse.ArgumentParser(description='Post CRUD for Jekyll blog')
    sub = ap.add_subparsers(dest='cmd', required=True)
    sp = sub.add_parser('search', help='按关键词查文章')
    sp.add_argument('keywords', nargs='+')
    sp.add_argument('--posts-dir', default=r'G:\Gerigory.github.io\_posts')
    sp.add_argument('--limit', type=int, default=20)
    sp.set_defaults(func=cmd_search)
    vp = sub.add_parser('validate', help='校验一篇文章')
    vp.add_argument('md_path')
    vp.add_argument('--site-root', default=r'G:\Gerigory.github.io')
    vp.set_defaults(func=cmd_validate)
    lp = sub.add_parser('list', help='列出全部文章')
    lp.add_argument('--posts-dir', default=r'G:\Gerigory.github.io\_posts')
    lp.add_argument('--category')
    lp.set_defaults(func=cmd_list)
    st = sub.add_parser('stats', help='统计文章')
    st.add_argument('--posts-dir', default=r'G:\Gerigory.github.io\_posts')
    st.set_defaults(func=cmd_stats)
    args = ap.parse_args()
    sys.exit(args.func(args))


if __name__ == '__main__':
    main()
