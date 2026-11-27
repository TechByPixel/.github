#!/usr/bin/env python3
"""Generate the TechByPixel org profile assets (.github/profile/assets).

Usage, from the root of the .github repo:
    python scripts/pixel-assets/gen_org_assets.py profile/assets
"""
import sys

from pixel_kit import (BG, BLINK_CSS, BLUE, BLUE_L, COMET_CSS, INK, MUTED, PURPLE, RED, RED_L, ROWS,
                       TWINKLE_CSS, YELLOW, button, card_bg, cells_path, cluster, comet_strip, divider, f,
                       grad3, grid_paths, hud_corners, layout, notched, particles, rise_css, set_out, svg,
                       wordmark, write)


def banner():
    W, H = 1200, 330
    s = 15
    word = "TechByPixel"
    _, wc = layout(word)
    ox, oy = (W - wc * s) / 2, 58

    tag = "Technology, One Pixel at a Time."
    s2 = 4
    tcells, _ = layout(tag, mono=True)
    n = len(tag)
    tw = n * 6 * s2  # each mono glyph advances exactly 6 cells
    tx, ty = (W - tw) / 2, 228

    wm_css, whites, ghosts = wordmark(word, s, ox, oy)
    css = (
        TWINKLE_CSS + COMET_CSS + rise_css(260) + wm_css + BLINK_CSS +
        ".sc{animation:sc 7s linear infinite}@keyframes sc{0%{transform:translateY(-80px)}100%{transform:translateY(420px)}}"
        f".ty{{transform-box:fill-box;transform-origin:0 0;animation:ty 8s steps({n},end) 1.6s infinite both}}"
        "@keyframes ty{0%{transform:scaleX(0)}45%,100%{transform:scaleX(1)}}"
        f".cu{{animation:cu 8s steps({n},end) 1.6s infinite both}}"
        f"@keyframes cu{{0%{{transform:translateX(-{tw}px)}}45%,100%{{transform:translateX(0)}}}}"
    )
    body = (
        card_bg(W, H, 8, "bn")
        + '<rect class="sc" width="1200" height="70" fill="#FFFFFF" opacity=".035"/>'
        + particles(16, 160, 1040, H - 40, [BLUE_L, RED_L, PURPLE, INK])
        + cluster(14, 190, 18, H - 50, True, [BLUE, BLUE_L, BLUE, PURPLE, INK])
        + cluster(1010, 1188, 18, H - 50, False, [RED, RED_L, RED, PURPLE, INK])
        + ghosts
        + "".join(whites)
        + f'<defs><clipPath id="tyc"><rect class="ty" x="{f(tx)}" y="{ty - 2}" width="{tw}" height="{ROWS * s2 + 4}"/></clipPath></defs>'
        + f'<path clip-path="url(#tyc)" fill="{MUTED}" d="{cells_path([(x, y) for x, y, _ in tcells], s2, tx, ty)}"/>'
        + f'<g class="cu"><rect class="bl" x="{f(tx + tw)}" y="{ty}" width="{3 * s2}" height="{7 * s2}" fill="{RED}"/></g>'
        + comet_strip(30, W - 30, H - 34, size=10, gap=6, period=4.0)
        + hud_corners(W, H, 22, 5, MUTED)
        + "</g>"
    )
    write("banner.svg", svg(W, H, "TechByPixel - Technology, One Pixel at a Time.", css, body))


# Each icon: base rows plus animated layers. Letters map to colours, "A" = row accent.
EXPLORE = [
    ("Artificial Intelligence & AI Agents", {
        "base": [".....AA.....", ".....WW.....", "..AAAAAAAA..", ".AWWWWWWWWA.", ".AWWWWWWWWA.",
                 ".AWWWWWWWWA.", ".AWWWWWWWWA.", ".AWWRRRRWWA.", ".AWWWWWWWWA.", "..AAAAAAAA..",
                 "...A....A...", "..AAA..AAA.."],
        "anim": [("ey", ["............", "............", "............", "............", "...BB..BB...",
                         "...BB..BB...", "............"]),
                 ("bk", ["....RR......"])],
    }),
    ("Software Engineering", {
        "base": ["AAAAAAAAAAAA", "AAAAAAAAAAAA", "A..........A", "A.W........A", "A..W.......A",
                 "A...W......A", "A..W.......A", "A.W........A", "A..........A", "AAAAAAAAAAAA"],
        "anim": [("bk", ["............", "............", "............", "............", "............",
                         "............", "............", ".....WWWW..."])],
    }),
    ("System Design & Architecture", {
        "base": ["....AAAA....", "....A..A....", "....AAAA....", ".....WW.....", "..WWWWWWWW..",
                 "..WW....WW..", ".AAAA..AAAA.", ".A..A..A..A.", ".AAAA..AAAA."],
        "anim": [("pu", ["............", ".....BB....."]),
                 ("pv", ["............", "............", "............", "............", "............",
                         "............", "............", "..RR....RR.."])],
    }),
    ("Game Development", {
        "base": [".AAAAAAAAAA.", "AAAAAAAAAAAA", "AAWAAAAAAAAA", "AWWWAAAAAAAA", "AAWAAAAAAAAA",
                 "AAAAAAAAAAAA", "AAAA....AAAA", ".AA......AA."],
        "anim": [("pu", ["............", "............", ".........R..", "............",
                         ".........R.."]),
                 ("pv", ["............", "............", "............", "........W.W."])],
    }),
    ("Developer Tools", {
        "base": ["............", "............", "....AAAA....", "...AAAAAA...", "..AAA..AAA..",
                 "..AA....AA..", "..AA....AA..", "..AAA..AAA..", "...AAAAAA...", "....AAAA....",
                 "............", "............"],
        "anim": [("fa", [".....AA.....", ".....AA.....", "............", "............", "............",
                         "AA........AA", "AA........AA", "............", "............", "............",
                         ".....AA.....", ".....AA....."]),
                 ("fb", ["............", "..AA....AA..", "..AA....AA..", "............", "............",
                         "............", "............", "............", "............", "..AA....AA..",
                         "..AA....AA..", "............"])],
    }),
    ("Engineering Experiments", {
        "base": ["...AAAAAA...", "....A..A....", "....A..A....", "....A..A....", "...A....A...",
                 "..A......A..", ".APPPPPPPPA.", "APPPPPPPPPPA", "APPPPPPPPPPA", ".AAAAAAAAAA."],
        "anim": [("bu", ["............", "............", "............", "............", "............",
                         "............", "....W.......", ".......W....", "............"])],
    }),
    ("Future Technologies", {
        "base": [".....AA.....", "....AAAA....", "....AWWA....", "....ABBA....", "....ABBA....",
                 "....AWWA....", "....AWWA....", "...AAWWAA...", "..AAAAAAAA..", "..A..AA..A.."],
        "anim": [("fa", ["............"] * 10 + ["....RYYR....", ".....RR....."]),
                 ("fb", ["............"] * 10 + [".....YY.....", "....R..R...."])],
    }),
]

# icon micro-animations shared with the personal profile menu
ICON_ANIM_CSS = (
    ".ey{animation:ey 4s steps(1,end) infinite}@keyframes ey{0%{opacity:1}92%{opacity:0}96%{opacity:1}}"
    ".bk{animation:bk 1s steps(1,end) infinite}@keyframes bk{0%{opacity:1}50%{opacity:0}}"
    ".pu{animation:pu 1.6s steps(1,end) infinite}@keyframes pu{0%{opacity:1}50%{opacity:.2}}"
    ".pv{animation:pu 1.6s steps(1,end) infinite}"
    ".fa{animation:fa .5s steps(1,end) infinite}@keyframes fa{0%{opacity:1}50%{opacity:0}}"
    ".fb{animation:fa .5s steps(1,end) infinite}"
    ".bu{animation:bu 2s linear infinite}@keyframes bu{0%{transform:translateY(0);opacity:1}100%{transform:translateY(-20px);opacity:0}}"
)
# paired layers run half a period apart (two-frame gear/flame, alternating lights);
# the phase lives in the inline delay because inline style overrides class delays
ICON_PHASE = {"fb": 0.25, "pv": 0.8}


def explore():
    W, RH, GAP = 900, 64, 10
    H = len(EXPLORE) * RH + (len(EXPLORE) - 1) * GAP
    slot = 1.4
    cycle = slot * len(EXPLORE)
    on = 100 / len(EXPLORE)
    css = (
        # selection cursor walks down the menu, one row per slot
        f".hl{{opacity:.3;animation:hl {f(cycle)}s steps(1,end) infinite}}"
        f"@keyframes hl{{0%{{opacity:1}}{f(on)}%,100%{{opacity:.3}}}}"
        f".ar{{opacity:0;animation:ar {f(cycle)}s steps(1,end) infinite}}"
        f"@keyframes ar{{0%{{opacity:1}}{f(on)}%,100%{{opacity:0}}}}"
        f".lb{{fill:{MUTED};animation:lb {f(cycle)}s steps(1,end) infinite}}"
        f"@keyframes lb{{0%{{fill:{INK};transform:translateX(8px)}}{f(on)}%,100%{{fill:{MUTED};transform:translateX(0)}}}}"
        + ICON_ANIM_CSS
    )
    arrow = ["#....", "##...", "###..", "####.", "###..", "##...", "#...."]
    s_icon, s_txt = 4, 3
    rows = []
    for i, (label, icon) in enumerate(EXPLORE):
        y = i * (RH + GAP)
        accent = grad3(i / (len(EXPLORE) - 1))
        delay = f"animation-delay:{f(i * slot - cycle)}s"
        colors = {"A": accent, "W": INK, "B": BLUE_L, "R": RED, "P": PURPLE, "Y": YELLOW}
        ih = len(icon["base"])
        ix, iy = 44, y + (RH - ih * s_icon) / 2
        icon_svg = grid_paths(icon["base"], colors, s_icon, ix, iy)
        for cls, grid in icon["anim"]:
            icon_svg += grid_paths(grid, colors, s_icon, ix, iy, cls,
                                   f"animation-delay:{f(-(i * 0.37 + ICON_PHASE.get(cls, 0)))}s")
        lcells, _ = layout(label)
        lx, ly = ix + 12 * s_icon + 24, y + (RH - 7 * s_txt) / 2
        acells = [(x, yy) for yy, r in enumerate(arrow) for x, c in enumerate(r) if c == "#"]
        rows.append(
            f'<path class="hl" style="{delay}" d="{notched(0, y, W, RH, 4)}" fill="{accent}"/>'
            f'<path d="{notched(2, y + 2, W - 4, RH - 4, 4)}" fill="{BG}"/>'
            f'<path class="ar" style="{delay}" fill="{accent}" d="{cells_path(acells, s_txt, 16, y + (RH - 7 * s_txt) / 2)}"/>'
            + icon_svg
            + f'<path class="lb" style="{delay}" d="{cells_path([(x, yy) for x, yy, _ in lcells], s_txt, lx, ly)}"/>'
        )
    title = ", ".join(label for label, _ in EXPLORE)
    write("explore.svg", svg(W, H, title, css, "".join(rows)))


def footer():
    W, H = 1200, 170
    text = "Stay curious. Keep building. Think in pixels."
    s = 4
    cells, tw = layout(text, mono=True)
    ox, oy = (W - tw * s) / 2, 62
    css = (
        TWINKLE_CSS + COMET_CSS + rise_css(130) +
        f".ch{{fill:{INK};animation:wv 5s linear infinite}}"
        f"@keyframes wv{{0%,20%,100%{{fill:{INK};transform:translateY(0)}}6%{{fill:{BLUE_L};transform:translateY(-6px)}}"
        f"12%{{fill:{RED_L};transform:translateY(0)}}}}"
    )
    by_char = {}
    for x, y, i in cells:
        by_char.setdefault(i, []).append((x, y))
    glyphs = "".join(
        f'<path class="ch" style="animation-delay:{f(i * 0.06)}s" d="{cells_path(pts, s, ox, oy)}"/>'
        for i, pts in sorted(by_char.items())
    )
    body = (
        card_bg(W, H, 8, "ft")
        + particles(10, 120, 1080, H - 30, [BLUE_L, RED_L, PURPLE])
        + cluster(14, 130, 16, H - 40, True, [BLUE, BLUE_L, PURPLE], dens=0.5)
        + cluster(1070, 1188, 16, H - 40, False, [RED, RED_L, PURPLE], dens=0.5)
        + glyphs
        + comet_strip(30, W - 30, H - 30, size=8, gap=6, period=4.0)
        + hud_corners(W, H, 18, 4, MUTED)
        + "</g>"
    )
    write("footer.svg", svg(W, H, text, css, body))


if __name__ == "__main__":
    set_out(sys.argv[1] if len(sys.argv) > 1 else ".")
    banner()
    divider()
    explore()
    button("website", "Website", BLUE, 0.0)
    button("medium", "Medium", PURPLE, 0.6)
    button("youtube", "YouTube", RED, 1.2)
    button("email", "hello@techbypixel.com", BLUE_L, 1.8)
    footer()
