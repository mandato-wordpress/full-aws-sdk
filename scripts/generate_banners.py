#!/usr/bin/env python3
"""
Generate .wordpress-org/banner-1544x500.png and banner-772x250.png (one-time, static).
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = Path(__file__).parent.parent / '.wordpress-org'
OUT_DIR.mkdir(parents=True, exist_ok=True)

TITLE    = 'Full AWS SDK for WordPress'
TAGLINE  = 'Bundle the full AWS SDK for PHP — shared across all your plugins & themes'

SERVICES = [
    ('EC2',    '#ff9900'),
    ('S3',     '#569a31'),
    ('Lambda', '#e67e22'),
    ('SES',    '#d63638'),
    ('SQS',    '#00b9e4'),
    ('SNS',    '#8c4fff'),
    ('CF',     '#3f88c5'),
    ('DB',     '#c0392b'),
]


def font(name, size):
    faces = [
        f'/usr/share/fonts/truetype/dejavu/{name}.ttf',
    ]
    for f in faces:
        try:
            return ImageFont.truetype(f, size)
        except OSError:
            pass
    return ImageFont.load_default()


def make_banner(W, H):
    img  = Image.new('RGB', (W, H), '#1d2327')
    draw = ImageDraw.Draw(img)

    scale = H / 500  # scale relative to the large banner

    # Orange accent stripe on the left
    stripe_w = int(W * 0.38)
    draw.rectangle([0, 0, stripe_w, H], fill='#ff9900')

    # Dark panel overlapping the stripe (creates a layered look)
    overlap = int(stripe_w * 0.55)
    draw.rectangle([overlap, 0, W, H], fill='#1d2327')

    # AWS "smile" arc decoration on the orange strip
    arc_x = int(stripe_w * 0.12)
    arc_r = int(H * 0.72)
    draw.ellipse(
        [arc_x - arc_r, H // 2 - arc_r, arc_x + arc_r, H // 2 + arc_r],
        outline='#cc7a00', width=max(2, int(6 * scale)),
    )

    # "AWS" large logo text on the orange stripe
    f_aws   = font('DejaVuSans-Bold',  int(90 * scale))
    f_sdk   = font('DejaVuSans',       int(26 * scale))
    f_title = font('DejaVuSans-Bold',  int(38 * scale))
    f_tag   = font('DejaVuSans',       int(18 * scale))
    f_svc   = font('DejaVuSans-Bold',  int(14 * scale))

    aw_x, aw_y = int(stripe_w * 0.08), int(H * 0.18)
    draw.text((aw_x, aw_y),                          'AWS',       font=f_aws, fill='#1d2327')
    draw.text((aw_x, aw_y + int(90 * scale) + 4),   'SDK for',   font=f_sdk, fill='#1d2327')
    draw.text((aw_x, aw_y + int(90 * scale) + 4 + int(30 * scale)), 'PHP', font=f_sdk, fill='#1d2327')

    # Title and tagline on the dark side
    tx = overlap + int(30 * scale)
    ty = int(H * 0.20)
    draw.text((tx, ty),                      TITLE,   font=f_title, fill='#f0f0f1')
    draw.text((tx, ty + int(52 * scale)),    TAGLINE, font=f_tag,   fill='#8c8f94')

    # Service pills
    pill_y = ty + int(52 * scale) + int(46 * scale)
    pill_h = int(28 * scale)
    pill_pad = int(12 * scale)
    pill_gap = int(8 * scale)
    px = tx
    for name, color in SERVICES:
        tw_ = int((len(name) * 9 + pill_pad * 2) * scale)
        if px + tw_ > W - int(20 * scale):
            break
        draw.rounded_rectangle([px, pill_y, px + tw_, pill_y + pill_h],
                                radius=int(4 * scale), fill=color)
        draw.text((px + pill_pad, pill_y + int(5 * scale)), name,
                  font=f_svc, fill='#fff')
        px += tw_ + pill_gap

    # Bottom rule
    draw.rectangle([0, H - int(6 * scale), W, H], fill='#ff9900')

    return img


# Large banner
banner_lg = make_banner(1544, 500)
banner_lg.save(OUT_DIR / 'banner-1544x500.png')
print('Saved banner-1544x500.png')

# Small banner – render at full size then resize for sharpness
banner_sm = make_banner(772, 250)
banner_sm.save(OUT_DIR / 'banner-772x250.png')
print('Saved banner-772x250.png')
