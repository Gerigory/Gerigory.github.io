#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""发布脚本：将本地源 md 转换为站点格式并发布。

转换规则见 SKILL.md：front matter 重写、H1 移除、图片引用转站点绝对 URL、
图片从同名 .assets 目录拷贝到 assets/img/<分类>/<年份>/<slug>/（可选压缩）。

用法：
  python publish.py --source <源md路径> --site-root G:\\Gerigory.github.io
                    [--publish] [--compress] [--date YYYY-MM-DD] [--dry-run]

--dry-run 只输出转换计划不写文件。--publish 在转换后执行 git add/commit/push。
"""
import argparse
import json
import re
import subprocess
import sys
import urllib.parse
from pathlib import Path

IMG_REF_RE = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
FM_RE = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.S)
SITE_BASE = 'https://gerigory.github.io/assets/img'

CAT_MAP = [
    (re.compile(r'GDC\s*(\d{4})', re.I), 'GDC'),
    (re.compile(r'Siggraph\s*(\d{4})', re.I), 'Siggraph'),
    (re.compile(r'Unreal\s*Fest\s*(\d{4})', re.I), 'UnrealFest'),
    (re.compile(r'UFSH\D*(\d{4})', re.I), 'UnrealFest'),
]


def parse_source_fm(text):
    m = FM_RE.match(text)
    if not m:
        return {}, text
    fm_text, body = m.group(1), text[m.end():]
    fm = {'tags': []}
    for line in fm_text.splitlines():
        mm = re.match(r'^([A-Za-z_-]+):\s*(.*)$', line)
        if mm:
            key = mm.group(1)
            val = mm.group(2).strip().strip('"\'')
            if key == 'tags':
                if val:
                    fm['tags'] = [v.strip() for v in val.strip('[]').split(',') if v.strip()]
                else:
                    fm['tags'] = []
            else:
                fm[key] = val
        elif re.match(r'^\s+-\s+', line):
            if not isinstance(fm.get('tags'), list):
                fm['tags'] = []
            fm['tags'].append(line.strip().lstrip('-').strip())
    return fm, body


def slugify(title):
    """title -> URL slug：去掉【】、空格转-、压缩连续符号。保留中文与字母数字。"""
    s = re.sub(r'【[^】]*】', '', title)
    s = s.replace('—', '-').replace('——', '-')
    s = re.sub(r"[\s/\\:'\"?,#()\[\]{}<>|*!@&+=~`^%$;]+", '-', s)
    s = re.sub(r'-{2,}', '-', s)
    s = s.strip('-.')
    s = re.sub(r'\b(GDC|Siggraph|UFSH|Unreal-Fest)-(\d{4})\b', r'\1\2', s, flags=re.I)
    return s


def detect_category(source_name, fm):
    """返回 (分类, 年份)。"""
    name = source_name
    for pat, cat in CAT_MAP:
        m = pat.search(name)
        if m:
            year = m.group(1) if m.groups() else ''
            if cat == 'UnrealFest':
                return cat, None
            return cat, year
    tagtext = ' '.join(fm.get('tags', []))
    m = re.search(r'来源/(GDC|Siggraph|UFSH)/(\d{4})', tagtext)
    if m:
        cat = 'UnrealFest' if m.group(1).upper() == 'UFSH' else m.group(1)
        return cat, (None if cat == 'UnrealFest' else m.group(2))
    return '渲染技巧', None


DOMAIN_MAP = {
    '光照': 'Lighting', '渲染': 'Rendering', '植被': 'Vegetation', '地形': 'Terrain',
    '海洋': 'Ocean', '阴影': 'Shadow', '后处理': 'PostProcessing', '材质': 'Material',
    '性能': 'Performance', '优化': 'Optimization', '管线': 'Pipeline',
    '全局光照': 'GI', '反射': 'Reflection', '云': 'Cloud', '大气': 'Atmosphere',
    '粒子': 'Particles', '抗锯齿': 'AA', '纹理': 'Texture', '贴图': 'Texture',
    '毛发': 'Hair', '皮肤': 'Skin', '水': 'Water', 'LOD': 'LOD',
    '光线追踪': 'RayTracing', '虚拟阴影': 'VSM', 'Nanite': 'Nanite',
    '音频': 'Audio', '工作流': 'Workflow', 'LLM': 'LLM', 'Agent': 'Agent',
}


def derive_tags(source_name, fm, cat, year):
    tags = []
    if cat != '渲染技巧':
        tags.append(cat)
        if year:
            tags.append(year)
    for t in fm.get('tags', []):
        for zh, en in DOMAIN_MAP.items():
            if zh.lower() in t.lower() and en not in tags:
                tags.append(en)
    seen, out = set(), []
    for t in tags:
        if t and t not in seen:
            seen.add(t)
            out.append(t)
    return out[:8]


def clean_title_prefix(title):
    """去掉【来源 年份】后跟的冗余来源前缀（如 '【GDC 2021】GDC2021 - Xxx' → '【GDC 2021】Xxx'）。"""
    hm = re.match(r'^(【[^】]*】)(.*)$', title)
    if not hm:
        return title
    head, rest = hm.group(1), hm.group(2)
    pats = [
        re.compile(r'^(GDC|Siggraph|UnrealFest|UFSH)\s?\d{0,4}\s*-\s*'),
        re.compile(r'^Unreal\s?Fest\s?\d{0,4}\s*-\s*'),
        re.compile(r'^\[UFSH\d{4}\]\s*'),
    ]
    while True:
        stripped = False
        for pat in pats:
            nm = pat.match(rest)
            if nm:
                rest = rest[nm.end():]
                stripped = True
        if not stripped:
            break
    return head + rest.strip()


def gen_description(fm, body, title):
    """从正文摘要块提取一句话中文 description。"""
    m = re.search(r'##\s*摘要[^\n]*\n+(.+?)(?=\n#|\n!|\Z)', body, re.S)
    if m:
        block = m.group(1)
        # 逐行找第一个可读句（跳过纯符号与列表标记）
        for line in block.splitlines():
            txt = re.sub(r'^\s*[-*]\s*', '', line).strip()
            txt = re.sub(r'^\*\*[^*]*\*\*[:：]?\s*', '', txt).strip()
            txt = re.sub(r'[*#>`]', '', txt).strip()
            # 去掉“主题：”类前缀标签
            txt = re.sub(r'^(主题|核心结论|关键要点|一句话总结)[:：]\s*', '', txt)
            if 15 <= len(txt) <= 100 and not txt.startswith('-'):
                return txt
        # 整块压缩
        txt = re.sub(r'[\s*#>`\-]+', ' ', block).strip()
        return txt[:90]
    return '本文分享的是' + title + '相关的技术要点'


def convert(source, site_root, args):
    text = source.read_text(encoding='utf-8', errors='replace')
    sfm, body = parse_source_fm(text)
    cat, year = detect_category(source.stem, sfm)
    h1 = re.search(r'^#\s+(.+)$', body, re.M)
    title = h1.group(1).strip() if h1 else source.stem
    if cat in ('GDC', 'Siggraph') and year and not title.startswith('【'):
        title = '【' + cat + ' ' + year + '】' + title
    elif cat == 'UnrealFest' and not title.startswith('【'):
        m = re.search(r'(?:Unreal\s*Fest|UFSH)\D*(\d{4})', source.stem, re.I)
        if m:
            title = '【Unreal Fest ' + m.group(1) + '】' + title
    title = clean_title_prefix(title)
    date = args.date or sfm.get('date') or '2026-10-09'
    date = re.sub(r'\s+.*$', '', date)
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', date):
        date = '2026-10-09'
    slug = slugify(title) or slugify(source.stem)
    tags = derive_tags(source.stem, sfm, cat, year)
    desc = gen_description(sfm, body, title)
    body = re.sub(r'^#\s+.+?\n', '', body, count=1)
    assets_dir = source.parent / (source.stem + '.assets')
    img_rel_dir = '/'.join(x for x in [cat, year, slug] if x)
    used_images = []

    def repl(m):
        alt, ref = m.group(1), m.group(2)
        ref_clean = ref.strip().strip('<>').split(' ')[0]
        ref_dec = urllib.parse.unquote(ref_clean)
        fname = Path(ref_dec).name
        used_images.append((ref_dec, fname))
        return '![' + alt + '](' + SITE_BASE + '/' + img_rel_dir + '/' + urllib.parse.quote(fname) + ')'

    body = IMG_REF_RE.sub(repl, body)
    cover = ''
    if used_images:
        cover = img_rel_dir + '/' + used_images[0][1]
    fm_lines = [
        '---',
        'layout: post',
        'title: "' + title + '"',
        'date: ' + date,
    ]
    if cover:
        fm_lines.append('img: ' + cover + ' # Add image post (optional)')
    fm_lines += [
        'fig-caption: # Add figcaption (optional)',
        'tags: [' + ', '.join(tags) + ']',
        'description: ' + desc,
        '---',
    ]
    new_text = '\n'.join(fm_lines) + '\n' + body
    post_dir = site_root / '_posts' / cat
    if year:
        post_dir = post_dir / year
    post_path = post_dir / (date + '-' + slug + '.md')
    img_dir = site_root / 'assets' / 'img' / Path(*[x for x in [cat, year, slug] if x])
    return {
        'source': str(source), 'title': title, 'slug': slug, 'category': cat,
        'year': year, 'date': date, 'tags': tags, 'description': desc,
        'post_path': str(post_path), 'img_dir': str(img_dir),
        'assets_dir': str(assets_dir), 'used_images': [u[1] for u in used_images],
        'cover': cover,
    }


def write_output(plan, new_text, compress):
    post_path = Path(plan['post_path'])
    post_path.parent.mkdir(parents=True, exist_ok=True)
    post_path.write_text(new_text, encoding='utf-8')
    import shutil
    sys.path.insert(0, str(Path(__file__).parent))
    from compress_assets import compress_one
    img_dir = Path(plan['img_dir'])
    img_dir.mkdir(parents=True, exist_ok=True)
    src_map = plan.get('img_src_map') or {}
    copied = 0
    for fname in plan['used_images']:
        src_img = Path(src_map.get(fname) or (Path(plan['assets_dir']) / fname))
        if not src_img.exists():
            # 回退：尝试源目录下其他 assets 目录（H1 同名等）
            fallbacks = list(Path(plan['assets_dir']).parent.glob('*.assets'))
            found = False
            for d in fallbacks:
                cand = d / fname
                if cand.exists():
                    src_img = cand
                    found = True
                    break
            if not found:
                print(json.dumps({'warning': 'image not found: ' + fname}, ensure_ascii=False))
                continue
        dst_img = img_dir / fname
        if compress:
            compress_one(src_img, dst_img, 1600, 300 * 1024)
        else:
            shutil.copy2(src_img, dst_img)
        copied += 1
    return copied


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--source', required=True)
    ap.add_argument('--site-root', default=r'G:\Gerigory.github.io')
    ap.add_argument('--publish', action='store_true')
    ap.add_argument('--compress', action='store_true')
    ap.add_argument('--date')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--emit-text', action='store_true', help='dry-run 时输出转换后全文')
    args = ap.parse_args()
    source = Path(args.source)
    site_root = Path(args.site_root)

    # convert 需要完整文本，重新组装
    text = source.read_text(encoding='utf-8', errors='replace')
    sfm, body = parse_source_fm(text)
    cat, year = detect_category(source.stem, sfm)
    h1 = re.search(r'^#\s+(.+)$', body, re.M)
    title = h1.group(1).strip() if h1 else source.stem
    if cat in ('GDC', 'Siggraph') and year and not title.startswith('【'):
        title = '【' + cat + ' ' + year + '】' + title
    elif cat == 'UnrealFest' and not title.startswith('【'):
        m = re.search(r'(?:Unreal\s*Fest|UFSH)\D*(\d{4})', source.stem, re.I)
        if m:
            title = '【Unreal Fest ' + m.group(1) + '】' + title
    title = clean_title_prefix(title)
    date = args.date or sfm.get('date') or '2026-10-09'
    date = re.sub(r'\s+.*$', '', date)
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', date):
        date = '2026-10-09'
    slug = slugify(title) or slugify(source.stem)
    tags = derive_tags(source.stem, sfm, cat, year)
    desc = gen_description(sfm, body, title)
    body2 = re.sub(r'^#\s+.+?\n', '', body, count=1)
    assets_dir = source.parent / (source.stem + '.assets')
    img_rel_dir = '/'.join(x for x in [cat, year, slug] if x)
    used_images = []

    def repl(m):
        alt, ref = m.group(1), m.group(2)
        ref = ref.strip()
        if ref.startswith('<') and ref.endswith('>'):
            ref_clean = ref[1:-1]  # 尖括号包裹：内部空格是文件名的一部分
        else:
            ref_clean = ref.split(' ')[0]
        ref_dec = urllib.parse.unquote(ref_clean)
        fname = Path(ref_dec).name
        used_images.append((ref_dec, fname))
        return '![' + alt + '](' + SITE_BASE + '/' + img_rel_dir + '/' + urllib.parse.quote(fname) + ')'

    body2 = IMG_REF_RE.sub(repl, body2)
    cover = ''
    if used_images:
        cover = img_rel_dir + '/' + used_images[0][1]
    fm_lines = [
        '---', 'layout: post', 'title: "' + title + '"', 'date: ' + date,
    ]
    if cover:
        fm_lines.append('img: ' + cover + ' # Add image post (optional)')
    fm_lines += [
        'fig-caption: # Add figcaption (optional)',
        'tags: [' + ', '.join(tags) + ']',
        'description: ' + desc,
        '---',
    ]
    new_text = '\n'.join(fm_lines) + '\n' + body2
    plan = {
        'source': str(source), 'title': title, 'slug': slug, 'category': cat,
        'year': year, 'date': date, 'tags': tags, 'description': desc,
        'post_path': str(site_root / '_posts' / cat / (year or '') / (date + '-' + slug + '.md')),
        'img_dir': str(site_root / 'assets' / 'img' / Path(*[x for x in [cat, year, slug] if x])),
        'assets_dir': str(assets_dir), 'used_images': [u[1] for u in used_images],
        'cover': cover,
    }
    print(json.dumps(plan, ensure_ascii=False, indent=2))
    if args.emit_text:
        print('=====CONVERTED_TEXT=====')
        print(new_text)
    if args.dry_run:
        return
    copied = write_output(plan, new_text, args.compress)
    print(json.dumps({'written': plan['post_path'], 'images_copied': copied}, ensure_ascii=False))
    if args.publish:
        r = subprocess.run(['git', 'add', '_posts', 'assets/img', 'skills', '_config.yml'],
                           cwd=site_root, capture_output=True, text=True)
        msg = 'publish: ' + plan['title']
        r2 = subprocess.run(['git', 'commit', '-m', msg], cwd=site_root, capture_output=True, text=True)
        r3 = subprocess.run(['git', 'push'], cwd=site_root, capture_output=True, text=True)
        print(json.dumps({'git_add': r.returncode, 'git_commit': r2.returncode,
                          'git_push': r3.returncode,
                          'commit_out': (r2.stdout + r2.stderr)[-300:],
                          'push_out': (r3.stdout + r3.stderr)[-300:]},
                         ensure_ascii=False, indent=2))
        if r3.returncode != 0:
            sys.exit(2)


if __name__ == '__main__':
    main()
