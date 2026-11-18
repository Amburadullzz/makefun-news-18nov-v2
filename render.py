#!/usr/bin/env python3
"""Draw the 18 November 2026 front poster: six stories, all first reported that day."""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (12, 16, 28)
CARD = (20, 26, 42)
EDGE = (44, 56, 82)
WHITE = (246, 248, 252)
MUTED = (170, 184, 206)
ACCENT = (250, 204, 21)
RED = (239, 68, 68)
ORANGE = (249, 115, 22)
CYAN = (56, 189, 248)
STEEL = (203, 213, 225)
SEA = (30, 64, 108)
GOLD = (245, 196, 81)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def fit(d, xy, s, f, fill, maxw):
    """Draw s, shrinking the size until it fits maxw."""
    while f.size > 10 and d.textlength(s, font=f) > maxw:
        f = font(f.path, f.size - 1)
    d.text(xy, s, font=f, fill=fill)
    return f


def icon_flags(d, x, y):
    """Three flags on poles: the Shenzhen summit."""
    for kind, px in (("us", x + 12), ("cn", x + 48), ("ru", x + 84)):
        d.rectangle([px, y + 12, px + 3, y + 104], fill=(122, 136, 160))
        if kind == "us":
            d.rectangle([px + 3, y + 16, px + 33, y + 44], fill=(255, 255, 255))
            for i in range(4):
                d.rectangle([px + 3, y + 16 + i * 7, px + 33, y + 19 + i * 7], fill=RED)
            d.rectangle([px + 3, y + 16, px + 15, y + 30], fill=(37, 64, 143))
        elif kind == "cn":
            d.rectangle([px + 3, y + 16, px + 33, y + 44], fill=(206, 17, 38))
            d.ellipse([px + 7, y + 20, px + 15, y + 28], fill=(255, 214, 0))
        else:
            d.rectangle([px + 3, y + 16, px + 33, y + 44], fill=(255, 255, 255))
            d.rectangle([px + 3, y + 25, px + 33, y + 34], fill=(0, 57, 166))
            d.rectangle([px + 3, y + 34, px + 33, y + 44], fill=(213, 43, 30))


def icon_rescue(d, x, y):
    """A struck building with rescue workers: the double-tap strike."""
    d.rectangle([x + 10, y + 44, x + 78, y + 98], fill=(120, 134, 158))
    d.rectangle([x + 20, y + 56, x + 34, y + 70], fill=(30, 40, 58))
    d.rectangle([x + 46, y + 56, x + 60, y + 70], fill=(30, 40, 58))
    d.rectangle([x + 20, y + 78, x + 34, y + 92], fill=(30, 40, 58))
    d.polygon([(x + 44, y + 20), (x + 66, y + 46), (x + 54, y + 58), (x + 36, y + 54),
               (x + 30, y + 34)], fill=ORANGE)
    d.polygon([(x + 44, y + 30), (x + 54, y + 46), (x + 42, y + 50)], fill=(253, 224, 71))
    d.rectangle([x + 84, y + 74, x + 114, y + 80], fill=(226, 232, 240))
    d.rectangle([x + 96, y + 62, x + 104, y + 74], fill=RED)
    d.rectangle([x + 88, y + 96, x + 112, y + 102], fill=(51, 65, 85))


def icon_voyager(d, x, y):
    """The probe and its trail to a star."""
    d.ellipse([x + 28, y + 34, x + 96, y + 94], outline=STEEL, width=4)
    d.line([(x + 62, y + 30), (x + 62, y + 98)], fill=STEEL, width=3)
    d.ellipse([x + 42, y + 48, x + 82, y + 80], outline=(148, 163, 184), width=3)
    d.line([(x + 62, y + 64), (x + 96, y + 76)], fill=(148, 163, 184), width=4)
    for i in range(6):
        d.ellipse([x + 2 + i * 8, y + 98 - i * 3, x + 5 + i * 8, y + 101 - i * 3], fill=CYAN)
    d.ellipse([x + 2, y + 10, x + 12, y + 20], fill=(253, 224, 71))


def icon_gold(d, x, y):
    """Two ingots and a red arrow falling past them."""
    for i, by in enumerate((y + 60, y + 82)):
        d.polygon([(x + 16, by), (x + 60, by), (x + 72, by + 14), (x + 28, by + 14)],
                  fill=GOLD if i == 0 else (212, 166, 58))
        d.polygon([(x + 16, by), (x + 28, by + 14), (x + 28, by + 18), (x + 16, by + 4)],
                  fill=(255, 228, 132))
    d.line([(x + 92, y + 20), (x + 92, y + 72)], fill=RED, width=6)
    d.polygon([(x + 80, y + 58), (x + 104, y + 58), (x + 92, y + 80)], fill=RED)


def icon_cyclone(d, x, y):
    """A spiral storm over a coastline."""
    cx, cy = x + 58, y + 56
    for i, r in enumerate((46, 36, 26, 16, 7)):
        d.arc([cx - r, cy - r, cx + r, cy + r], 200 + i * 40, 340 + i * 40,
              fill=(226, 232, 240) if i % 2 == 0 else CYAN, width=5)
    d.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=(226, 232, 240))
    d.rectangle([x + 2, y + 98, x + 114, y + 104], fill=SEA)


def icon_hormuz(d, x, y):
    """A tanker in the strait, a drone above it."""
    d.rectangle([x + 2, y + 84, x + 114, y + 94], fill=SEA)
    d.polygon([(x + 16, y + 62), (x + 94, y + 62), (x + 102, y + 84), (x + 10, y + 84)],
              fill=(148, 163, 184))
    d.rectangle([x + 42, y + 44, x + 72, y + 62], fill=STEEL)
    d.rectangle([x + 66, y + 32, x + 82, y + 44], fill=(226, 232, 240))
    d.line([(x + 16, y + 24), (x + 40, y + 24)], fill=STEEL, width=3)
    d.line([(x + 22, y + 18), (x + 34, y + 18)], fill=STEEL, width=3)
    d.ellipse([x + 18, y + 12, x + 28, y + 20], fill=RED)


CARDS = [
    ("SHENZHEN SUMMIT", ["Trump lands, Xi greets him;", "Putin talks first before", "Thursday's trilateral"], icon_flags),
    ("72 KILLED IN DOUBLE-TAP", ["Russia hits rescuers in", "southern Ukraine, says Kyiv,", "as the strikes go on"], icon_rescue),
    ("VOYAGER 1: LIGHT-DAY", ["NASA probe passes 16", "billion miles, the first a", "light-day from Earth"], icon_voyager),
    ("GOLD BELOW $3,800", ["Lowest in over a year as", "the Fed signals more rate", "rises; silver slides too"], icon_gold),
    ("CYCLONE AKVAN", ["Severe storm heads for", "Andhra and Odisha, landfall", "expected on Friday"], icon_cyclone),
    ("IRAN WARNS SHIPPING", ["Tehran tells ships to avoid", "'fake' US routes and says it", "downed two US drones"], icon_hormuz),
]


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 8], fill=ACCENT)
    d.text((36, 40), "WEDNESDAY", font=font(BOLD, 26), fill=ACCENT)
    d.text((34, 74), "18 NOVEMBER 2026", font=font(BOLD, 76), fill=WHITE)
    d.text((36, 162), "THE WORLD IN ONE DAY", font=font(BOLD, 22), fill=MUTED)
    d.line([(36, 200), (W - 36, 200)], fill=EDGE, width=2)

    cw, ch, gap = 470, 216, 18
    left, top = 32, 214
    for i, (title, lines, icon) in enumerate(CARDS):
        x = left + (i % 2) * (cw + gap)
        y = top + (i // 2) * (ch + gap)
        d.rounded_rectangle([x, y, x + cw, y + ch], radius=18, fill=CARD, outline=EDGE, width=2)
        icon(d, x + 26, y + 52)
        tf = fit(d, (x + 152, y + 34), title, font(BOLD, 30), WHITE, cw - 176)
        ty = y + 34 + tf.size + 12
        for line in lines:
            fit(d, (x + 152, ty), line, font(REG, 21), MUTED, cw - 172)
            ty += 28

    fy = top + 3 * (ch + gap) + 12
    d.rounded_rectangle([left, fy, W - left, fy + 66], radius=14, fill=(17, 23, 38), outline=EDGE, width=2)
    d.text((left + 20, fy + 20), "Also today: Pakistan test-fires a Fatah-3 cruise missile,",
           font=font(REG, 20), fill=MUTED)
    d.text((left + 20, fy + 42), "a Kashmir commander is killed, Carlsen forfeits a game",
           font=font(REG, 20), fill=MUTED)

    img.save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
