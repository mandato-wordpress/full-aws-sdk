#!/usr/bin/env python3
"""
Generate .wordpress-org/screenshot-1.png
Version and release date are read from env vars so the workflow can inject
current values at build time:
  AWS_SDK_VERSION=3.373.8 AWS_SDK_RELEASE_DATE=2026-03-23 python3 scripts/generate_screenshot.py
"""
import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

VERSION      = os.environ.get('AWS_SDK_VERSION',      '3.373.8')
RELEASE_DATE = os.environ.get('AWS_SDK_RELEASE_DATE', '2026-03-23')
OUT          = Path(__file__).parent.parent / '.wordpress-org' / 'screenshot-2.png'

W, H = 1280, 720

img  = Image.new('RGB', (W, H), '#1d2327')
draw = ImageDraw.Draw(img)

def font(name, size):
    faces = [
        f'/usr/share/fonts/truetype/dejavu/{name}.ttf',
        f'/usr/share/fonts/truetype/liberation/Liberation{name.replace("DejaVu","").replace("Sans","Sans-").strip("-")}.ttf',
    ]
    for f in faces:
        try:
            return ImageFont.truetype(f, size)
        except OSError:
            pass
    return ImageFont.load_default()

f_title  = font('DejaVuSans-Bold',  30)
f_label  = font('DejaVuSans-Bold',  18)
f_small  = font('DejaVuSans',       14)
f_code   = font('DejaVuSansMono',   13)

# ── Top bar ──────────────────────────────────────────────────────────────────
draw.rectangle([0, 0, W, 64], fill='#ff9900')
draw.text((24, 16), 'Full AWS SDK —  WordPress Plugin', font=f_title, fill='#1d2327')

# ── Stat cards ───────────────────────────────────────────────────────────────
cards = [
    ('SDK VERSION',  VERSION,       '#f0f0f1'),
    ('RELEASE DATE', RELEASE_DATE,  '#f0f0f1'),
    ('AUTOLOADER',   'Active',      '#00a32a'),
]
cx = 24
for label, value, col in cards:
    draw.rounded_rectangle([cx, 90, cx + 260, 190], radius=8, fill='#2c3338', outline='#3c434a')
    draw.text((cx + 16, 102), label, font=f_small, fill='#8c8f94')
    draw.text((cx + 16, 130), value, font=f_label, fill=col)
    cx += 280

# ── Service tiles ─────────────────────────────────────────────────────────────
services = [
    ('EC2',         '#ff9900', 'Elastic Compute'),
    ('S3',          '#569a31', 'Simple Storage'),
    ('CloudFront',  '#8c4fff', 'CDN / Delivery'),
    ('Lambda',      '#e67e22', 'Serverless'),
    ('DynamoDB',    '#3f88c5', 'NoSQL Database'),
    ('SES',         '#d63638', 'Email Service'),
    ('SQS',         '#00b9e4', 'Queue Service'),
    ('Rekognition', '#c0392b', 'Image Analysis'),
]
tw, th, cols = 136, 100, 4
sx, sy = 24, 220
for i, (name, color, desc) in enumerate(services):
    x = sx + (i % cols) * (tw + 16)
    y = sy + (i // cols) * (th + 12)
    draw.rounded_rectangle([x, y, x + tw, y + th], radius=8, fill='#2c3338', outline=color)
    draw.rounded_rectangle([x, y, x + tw, y + 6],  radius=4, fill=color)
    draw.text((x + 10, y + 18), name, font=f_label, fill=color)
    draw.text((x + 10, y + 58), desc, font=f_small, fill='#8c8f94')

# ── Code panel ───────────────────────────────────────────────────────────────
px = sx + cols * (tw + 16) + 8
py, pw, ph = 220, W - (sx + cols * (tw + 16) + 8) - 24, 240
draw.rounded_rectangle([px, py, px + pw, py + ph], radius=8, fill='#0d1117', outline='#30363d')
draw.text((px + 14, py + 12), 'Usage Example', font=f_small, fill='#8c8f94')

code = [
    ("if ( defined( 'FULL_AWS_SDK_VERSION' ) ) {", '#ff7b72'),
    ('',                                          '#e6edf3'),
    ("    $s3 = new Aws\\S3\\S3Client([",         '#79c0ff'),
    ("        'region'  => 'us-east-1',",         '#a5d6ff'),
    ("        'version' => 'latest',",            '#a5d6ff'),
    ("    ]);",                                    '#e6edf3'),
    ('',                                          '#e6edf3'),
    ("    $cf = new Aws\\CloudFront\\CloudFrontClient([", '#79c0ff'),
    ("        'region'  => 'us-east-1',",         '#a5d6ff'),
    ("        'version' => 'latest',",            '#a5d6ff'),
    ("    ]);",                                    '#e6edf3'),
    ("}",                                         '#ff7b72'),
]
ly = py + 38
for line, col in code:
    draw.text((px + 14, ly), line, font=f_code, fill=col)
    ly += 16

# ── Footer ────────────────────────────────────────────────────────────────────
draw.rectangle([0, H - 40, W, H], fill='#2c3338')
draw.text((24,       H - 28), 'Tools -> Full AWS SDK  |  mandato-wordpress/full-aws-sdk', font=f_small, fill='#8c8f94')
draw.text((W - 370,  H - 28), 'github.com/mandato-wordpress/full-aws-sdk',           font=f_small, fill='#8c8f94')

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT)
print(f'Saved {OUT}')
