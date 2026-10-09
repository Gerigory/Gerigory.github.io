#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""图片压缩：长边>1600px 等比缩小；PNG 尝试量化 256 色，效果差则 optimize 无损压缩。

用法：
  python compress_assets.py --src <源图片目录> --dst <目标目录> [--max-side 1600] [--max-bytes 307200]

输出压缩报告 JSON。
"""
import argparse
import json
import shutil
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print(json.dumps({'error': 'Pillow not installed'}))
    sys.exit(1)


def compress_one(src: Path, dst: Path, max_side: int, max_bytes: int):
    """压缩单张图片，返回统计。JPG/GIF 保持原样拷贝（已足够小）。"""
    ext = src.suffix.lower()
    if ext in ('.jpg', '.jpeg', '.gif'):
        shutil.copy2(src, dst)
        return {'file': dst.name, 'action': 'copy', 'src_bytes': src.stat().st_size,
                'dst_bytes': dst.stat().st_size}
    orig_bytes = src.stat().st_size
    try:
        img = Image.open(src)
        img.load()
    except Exception as e:
        shutil.copy2(src, dst)
        return {'file': dst.name, 'action': 'copy-error', 'error': str(e),
                'src_bytes': orig_bytes, 'dst_bytes': dst.stat().st_size}
    # 缩放
    w, h = img.size
    scale = min(1.0, max_side / max(w, h))
    if scale < 1.0:
        img = img.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.LANCZOS)
    mode = img.mode
    # 先尝试量化（调色板 256 色 + 抖动）
    best = None
    if mode in ('RGB', 'RGBA', 'P'):
        try:
            q = img.quantize(colors=256, method=Image.FASTOCTREE, dither=Image.FLOYDSTEINBERG)
            q.save(dst, 'PNG', optimize=True)
            if best is None or dst.stat().st_size < best:
                best = dst.stat().st_size
        except Exception:
            pass
    # 无损 optimize（保持全色深）
    try:
        tmp = dst.with_suffix('.tmp.png')
        img.save(tmp, 'PNG', optimize=True)
        tmp_size = tmp.stat().st_size
        if best is None or tmp_size < best:
            tmp.replace(dst)
            best = tmp_size
        else:
            tmp.unlink(missing_ok=True)
    except Exception:
        pass
    if best is None:
        shutil.copy2(src, dst)
        return {'file': dst.name, 'action': 'copy-fallback', 'src_bytes': orig_bytes,
                'dst_bytes': dst.stat().st_size}
    # 若压缩后反而更大（罕见），用原文件
    if dst.stat().st_size >= orig_bytes:
        shutil.copy2(src, dst)
        return {'file': dst.name, 'action': 'copy-bigger', 'src_bytes': orig_bytes,
                'dst_bytes': orig_bytes}
    return {'file': dst.name, 'action': 'compress', 'src_bytes': orig_bytes,
            'dst_bytes': dst.stat().st_size}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--src', required=True)
    ap.add_argument('--dst', required=True)
    ap.add_argument('--max-side', type=int, default=1600)
    ap.add_argument('--max-bytes', type=int, default=300 * 1024)
    args = ap.parse_args()
    src, dst = Path(args.src), Path(args.dst)
    dst.mkdir(parents=True, exist_ok=True)
    report = []
    total_src = total_dst = 0
    for f in sorted(src.iterdir()):
        if not f.is_file() or f.suffix.lower() not in ('.png', '.jpg', '.jpeg', '.gif'):
            continue
        r = compress_one(f, dst / f.name, args.max_side, args.max_bytes)
        report.append(r)
        total_src += r['src_bytes']
        total_dst += r['dst_bytes']
    out = {
        'src_dir': str(src), 'dst_dir': str(dst), 'files': report,
        'total_src_mb': round(total_src / 1048576, 2),
        'total_dst_mb': round(total_dst / 1048576, 2),
        'ratio': round(total_dst / total_src, 3) if total_src else 0,
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
