#!/usr/bin/env python3
"""Copy the portable skill without replacing an existing installation."""
import argparse
import shutil
from pathlib import Path


def install(target):
    source = Path(__file__).resolve().parent / 'skills' / 'teaching-video-studio'
    dest = Path(target).expanduser().resolve() / source.name
    if dest.exists():
        raise FileExistsError(f'Existing installation preserved: {dest}')
    shutil.copytree(source, dest, ignore=shutil.ignore_patterns('__pycache__', 'node_modules', 'vendor', '.DS_Store'))
    return dest


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', required=True, help='Agent skills parent directory')
    args = parser.parse_args()
    try:
        print(install(args.target))
    except (OSError, ValueError) as exc:
        parser.exit(1, f'{exc}\n')
