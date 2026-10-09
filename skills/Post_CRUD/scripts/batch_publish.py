#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批量发布：遍历源目录全部 md，逐篇调用 publish.py 转换（不推送），
输出汇总报告。分批推送由外部控制。

用法：
  python batch_publish.py --src-dir D:\\MarkdownSpace\\LLMWorkspace\\TechniqueDocs
                          --site-root G:\\Gerigory.github.io --compress
                          [--only name1,name2] [--report out.json]
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import publish as P


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--src-dir', required=True)
    ap.add_argument('--site-root', default=r'G:\Gerigory.github.io')
    ap.add_argument('--compress', action='store_true')
    ap.add_argument('--only', help='只处理指定源文件名（不含扩展名），逗号分隔')
    ap.add_argument('--report', help='报告输出 JSON 路径')
    args = ap.parse_args()
    src_dir = Path(args.src_dir)
    site_root = Path(args.site_root)
    only = set(args.only.split(',')) if args.only else None

    md_files = sorted([f for f in src_dir.glob('*.md') if f.is_file()])
    results = []
    for f in md_files:
        if only and f.stem not in only:
            continue
        try:
            # 复刻 publish.py main 中的转换逻辑
            class A:
                date = None
            text = f.read_text(encoding='utf-8', errors='replace')
            sfm, body = P.parse_source_fm(text)
            cat, year = P.detect_category(f.stem, sfm)
            h1 = re_search_h1 = __import__('re').search(r'^#\s+(.+)$', body, __import__('re').M)
            title = h1.group(1).strip() if h1 else f.stem
            if cat in ('GDC', 'Siggraph') and year and not title.startswith('【'):
                title = '【' + cat + ' ' + year + '】' + title
            elif cat == 'UnrealFest' and not title.startswith('【'):
                m = __import__('re').search(r'(?:Unreal\s*Fest|UFSH)\D*(\d{4})', f.stem, __import__('re').I)
                if m:
                    title = '【Unreal Fest ' + m.group(1) + '】' + title
            date = sfm.get('date') or '2026-10-09'
            date = __import__('re').sub(r'\s+.*$', '', date)
            if not __import__('re').match(r'^\d{4}-\d{2}-\d{2}$', date):
                date = '2026-10-09'
            slug = P.slugify(title) or P.slugify(f.stem)
            tags = P.derive_tags(f.stem, sfm, cat, year)
            desc = P.gen_description(sfm, body, title)
            body2 = __import__('re').sub(r'^#\s+.+?\n', '', body, count=1)
            assets_dir = f.parent / (f.stem + '.assets')
            # 回退：md 引用的 assets 目录名可能与源文件名不一致（如 H1 标题同名目录）
            # 收集所有候选 assets 目录，按引用逐个解析真实位置
            cand_dirs = [assets_dir]
            h1_stem = (h1.group(1).strip() if h1 else f.stem)
            cand_dirs.append(f.parent / (h1_stem + '.assets'))
            cand_dirs.append(f.parent / (title + '.assets'))
            seen_d = set()
            cand_dirs = [d for d in cand_dirs if d and str(d) not in seen_d and not seen_d.add(str(d))]
            img_rel_dir = '/'.join(x for x in [cat, year, slug] if x)
            used_images = []
            img_src_map = {}

            def resolve_src(ref_dec):
                """在候选目录中找到引用图片的真实位置。"""
                fname = Path(ref_dec).name
                for d in cand_dirs:
                    cand = d / fname
                    if cand.exists():
                        return str(cand)
                # 引用路径本身可能含子目录结构，直接相对源目录解析
                direct = f.parent / ref_dec.lstrip('./')
                if direct.exists():
                    return str(direct)
                return None

            def repl(m):
                alt, ref = m.group(1), m.group(2)
                ref = ref.strip()
                if ref.startswith('<') and ref.endswith('>'):
                    ref_clean = ref[1:-1]
                else:
                    ref_clean = ref.split(' ')[0]
                ref_dec = __import__('urllib.parse', fromlist=['parse']).unquote(ref_clean)
                fname = Path(ref_dec).name
                src_real = resolve_src(ref_dec)
                if src_real:
                    img_src_map[fname] = src_real
                used_images.append((ref_dec, fname))
                return '![' + alt + '](' + P.SITE_BASE + '/' + img_rel_dir + '/' + __import__('urllib.parse', fromlist=['parse']).quote(fname) + ')'

            body2 = P.IMG_REF_RE.sub(repl, body2)
            cover = ''
            if used_images:
                cover = img_rel_dir + '/' + used_images[0][1]
            fm_lines = ['---', 'layout: post', 'title: "' + title + '"', 'date: ' + date]
            if cover:
                fm_lines.append('img: ' + cover + ' # Add image post (optional)')
            fm_lines += ['fig-caption: # Add figcaption (optional)',
                         'tags: [' + ', '.join(tags) + ']',
                         'description: ' + desc,
                         '---']
            new_text = '\n'.join(fm_lines) + '\n' + body2
            plan = {
                'source': str(f), 'title': title, 'slug': slug, 'category': cat,
                'year': year, 'date': date, 'tags': tags, 'description': desc,
                'post_path': str(site_root / '_posts' / cat / (year or '') / (date + '-' + slug + '.md')),
                'img_dir': str(site_root / 'assets' / 'img' / Path(*[x for x in [cat, year, slug] if x])),
                'assets_dir': str(assets_dir),
                'used_images': [u[1] for u in used_images],
                'img_src_map': img_src_map,
            }
            copied = P.write_output(plan, new_text, args.compress)
            results.append({**{k: v for k, v in plan.items()}, 'images_copied': copied, 'status': 'ok'})
        except Exception as e:
            results.append({'source': str(f), 'status': 'error', 'error': str(e)})
    report = {'total': len(results),
              'ok': sum(1 for r in results if r['status'] == 'ok'),
              'error': sum(1 for r in results if r['status'] == 'error'),
              'results': results}
    out = json.dumps(report, ensure_ascii=False, indent=2)
    print(out)
    if args.report:
        Path(args.report).write_text(out, encoding='utf-8')


if __name__ == '__main__':
    main()
