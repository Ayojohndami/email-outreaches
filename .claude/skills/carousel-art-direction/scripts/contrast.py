#!/usr/bin/env python3
"""Report WCAG relative-luminance contrast for two opaque sRGB hex colors."""
import argparse
import re


def color(value):
    value = value.lstrip('#')
    if not re.fullmatch(r'(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})', value):
        raise argparse.ArgumentTypeError('Use a 3- or 6-digit opaque hex color.')
    if len(value) == 3:
        value = ''.join(c * 2 for c in value)
    return value.upper()


def luminance(value):
    channels = [int(value[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return sum(c * w for c, w in zip(linear, (0.2126, 0.7152, 0.0722)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('foreground', type=color)
    parser.add_argument('background', type=color)
    args = parser.parse_args()
    low, high = sorted((luminance(args.foreground), luminance(args.background)))
    ratio = (high + 0.05) / (low + 0.05)
    print(f'#{args.foreground} on #{args.background}: {ratio:.2f}:1')
    print(f'Body copy target (4.5:1): {"PASS" if ratio >= 4.5 else "FAIL"}')
    print(f'Large display target (3:1): {"PASS" if ratio >= 3 else "FAIL"}')
    print('Opaque solid colors only; does not assess image backgrounds, type size, or the whole design.')


if __name__ == '__main__':
    main()
