#!/usr/bin/env python3
"""Local, dependency-free helpers; no AI calls, downloads or paid operations."""
import argparse
import hashlib
import json
import math
import shutil
import sys
from pathlib import Path

MEDIA = {'.pdf', '.docx', '.pptx', '.xlsx', '.csv', '.md', '.txt', '.png', '.jpg', '.jpeg', '.webp', '.svg', '.mp4', '.mov', '.webm', '.wav', '.mp3', '.m4a', '.srt', '.vtt', '.glb', '.gltf'}


def save_new(path, data):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('x', encoding='utf-8') as f:
        f.write(data)


def init_project(path):
    root = Path(path).expanduser().resolve()
    if root.exists() and any(root.iterdir()):
        raise ValueError('Use a new or empty project directory; existing content preserved.')
    root.mkdir(parents=True, exist_ok=True)
    for name in ('inputs', 'assets', 'audio', 'captions', 'boards', 'exports'):
        (root / name).mkdir()
    manifest = {'schema_version': 1, 'stage': 'intake', 'requirements': {'narration': True, 'captions': True},
                'stages': {s: 'pending' for s in ('intake', 'direction', 'styleframe', 'storyboard', 'caption_draft', 'narration', 'alignment', 'sample', 'animation', 'composition', 'qa')},
                'artifacts': {}, 'tool_versions': {}}
    save_new(root / 'PROJECT.json', json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    return {'project': str(root), 'hyperframes_initialized': False}


def inventory(path):
    root = Path(path).resolve(strict=True)
    if not root.is_dir():
        raise ValueError('Inventory requires a directory.')
    records = []
    for p in sorted(root.rglob('*')):
        rel = p.relative_to(root)
        if any(part.startswith('.') or part in {'node_modules', '__pycache__'} for part in rel.parts):
            continue
        if p.is_symlink() or any(parent.is_symlink() for parent in p.parents if parent != root and root in parent.parents):
            continue
        if not p.is_file() or p.suffix.lower() not in MEDIA:
            continue
        digest = hashlib.sha256()
        with p.open('rb') as f:
            for block in iter(lambda: f.read(1024 * 1024), b''):
                digest.update(block)
        records.append({'path': rel.as_posix(), 'bytes': p.stat().st_size, 'sha256': digest.hexdigest(), 'extension': p.suffix.lower()})
    return {'schema_version': 1, 'assets': records, 'note': 'Metadata only; provenance and permission require review.'}


def millis(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
        raise ValueError('Times must be finite nonnegative seconds.')
    return round(value * 1000)


def stamp(ms):
    seconds, ms = divmod(ms, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f'{hours:02}:{minutes:02}:{seconds:02},{ms:03}'


def to_srt(data, allow_estimated=False):
    source = data.get('timing_source')
    if source not in {'provider', 'forced-alignment', 'manual', 'estimated'}:
        raise ValueError('Declare timing_source: provider, forced-alignment, manual or estimated.')
    if source == 'estimated' and not allow_estimated:
        raise ValueError('Estimated timing is draft-only; explicitly pass --allow-estimated.')
    duration = millis(data['duration'])
    if duration <= 0 or not data.get('cues'):
        raise ValueError('Positive duration and nonempty cues are required.')
    chunks, previous = [], 0
    for number, cue in enumerate(data['cues'], 1):
        start, end = millis(cue['start']), millis(cue['end'])
        text = cue['text']
        if not isinstance(text, str) or not text.strip() or '\n\n' in text.replace('\r', ''):
            raise ValueError(f'Cue {number}: text must be nonempty with no blank paragraph.')
        if start < previous or end <= start or end > duration:
            raise ValueError(f'Cue {number}: overlap, zero-length or beyond duration after millisecond rounding.')
        chunks.append(f'{number}\n{stamp(start)} --> {stamp(end)}\n{text.strip()}\n')
        previous = end
    return '\n'.join(chunks)


def doctor():
    return {'executables': {name: shutil.which(name) for name in ('node', 'npm', 'ffmpeg', 'ffprobe', 'hyperframes')},
            'python': sys.version.split()[0], 'browser_webgl': 'untested', 'tts': 'untested',
            'alignment': 'untested', 'hyperframes_render': 'untested',
            'note': 'A missing global HyperFrames command does not rule out a project-local installation.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest='command', required=True)
    subs.add_parser('doctor')
    init = subs.add_parser('init'); init.add_argument('path')
    inv = subs.add_parser('inventory'); inv.add_argument('path'); inv.add_argument('--out', required=True)
    cap = subs.add_parser('captions'); cap.add_argument('path'); cap.add_argument('--out', required=True); cap.add_argument('--allow-estimated', action='store_true')
    args = parser.parse_args()
    try:
        if args.command == 'doctor': result = doctor()
        elif args.command == 'init': result = init_project(args.path)
        elif args.command == 'inventory':
            result = inventory(args.path)
            save_new(args.out, json.dumps(result, ensure_ascii=False, indent=2) + '\n')
            result = {'output': args.out, 'assets': len(result['assets'])}
        else:
            data = json.loads(Path(args.path).read_text(encoding='utf-8'))
            save_new(args.out, to_srt(data, args.allow_estimated))
            result = {'output': args.out, 'timing_source': data['timing_source']}
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        parser.exit(1, f'{exc}\n')


if __name__ == '__main__':
    main()
