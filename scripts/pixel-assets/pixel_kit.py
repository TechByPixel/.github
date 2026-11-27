"""Shared pixel-art SVG toolkit for the TechByPixel profile READMEs.

Everything renders as self-contained SVG: text is drawn as pixel rects (GitHub
blocks external fonts inside <img>), motion is pure CSS so it runs when GitHub
shows the SVG as an image, and prefers-reduced-motion turns all motion off.
Builders (gen_org_assets.py, gen_personal_assets.py) call set_out() then write().
"""
import os
import random

OUT = "."

# Palette sampled from the TechByPixel avatar (blue "T", red "P", near-black ground).
BLUE, BLUE_L = "#1F7BFF", "#5CC8FF"
RED, RED_L = "#FF2D3D", "#FF7A85"
PURPLE = "#9B4DFF"
YELLOW = "#FFC93C"
BG, INK, MUTED = "#0B0E1A", "#F4F7FF", "#9AA8CC"

REDUCED = "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"


def set_out(path, seed=1337):
    """Choose the output folder and reset the RNG so output is reproducible."""
    global OUT
    OUT = path
    os.makedirs(OUT, exist_ok=True)
    random.seed(seed)


# ---------------------------------------------------------------- pixel font
# Cap height 7 rows, descenders use rows 7-8. "#" = lit pixel.
FONT = {
    "A": [".###.", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"],
    "B": ["####.", "#...#", "#...#", "####.", "#...#", "#...#", "####."],
    "C": [".###.", "#...#", "#....", "#....", "#....", "#...#", ".###."],
    "D": ["####.", "#...#", "#...#", "#...#", "#...#", "#...#", "####."],
    "E": ["#####", "#....", "#....", "####.", "#....", "#....", "#####"],
    "F": ["#####", "#....", "#....", "####.", "#....", "#....", "#...."],
    "G": [".###.", "#...#", "#....", "#.###", "#...#", "#...#", ".####"],
    "H": ["#...#", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"],
    "I": ["###", ".#.", ".#.", ".#.", ".#.", ".#.", "###"],
    "J": ["..###", "...#.", "...#.", "...#.", "...#.", "#..#.", ".##.."],
    "K": ["#...#", "#..#.", "#.#..", "##...", "#.#..", "#..#.", "#...#"],
    "L": ["#....", "#....", "#....", "#....", "#....", "#....", "#####"],
    "M": ["#...#", "##.##", "#.#.#", "#.#.#", "#...#", "#...#", "#...#"],
    "N": ["#...#", "#...#", "##..#", "#.#.#", "#..##", "#...#", "#...#"],
    "O": [".###.", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."],
    "P": ["####.", "#...#", "#...#", "####.", "#....", "#....", "#...."],
    "Q": [".###.", "#...#", "#...#", "#...#", "#.#.#", "#..#.", ".##.#"],
    "R": ["####.", "#...#", "#...#", "####.", "#.#..", "#..#.", "#...#"],
    "S": [".####", "#....", "#....", ".###.", "....#", "....#", "####."],
    "T": ["#####", "..#..", "..#..", "..#..", "..#..", "..#..", "..#.."],
    "U": ["#...#", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."],
    "V": ["#...#", "#...#", "#...#", "#...#", "#...#", ".#.#.", "..#.."],
    "W": ["#...#", "#...#", "#...#", "#.#.#", "#.#.#", "#.#.#", ".#.#."],
    "X": ["#...#", "#...#", ".#.#.", "..#..", ".#.#.", "#...#", "#...#"],
    "Y": ["#...#", "#...#", ".#.#.", "..#..", "..#..", "..#..", "..#.."],
    "Z": ["#####", "....#", "...#.", "..#..", ".#...", "#....", "#####"],
    "a": [".....", ".....", ".###.", "....#", ".####", "#...#", ".####"],
    "b": ["#....", "#....", "####.", "#...#", "#...#", "#...#", "####."],
    "c": [".....", ".....", ".####", "#....", "#....", "#....", ".####"],
    "d": ["....#", "....#", ".####", "#...#", "#...#", "#...#", ".####"],
    "e": [".....", ".....", ".###.", "#...#", "#####", "#....", ".####"],
    "f": ["..##", ".#..", "####", ".#..", ".#..", ".#..", ".#.."],
    "g": [".....", ".....", ".####", "#...#", "#...#", "#...#", ".####", "....#", ".###."],
    "h": ["#....", "#....", "####.", "#...#", "#...#", "#...#", "#...#"],
    "i": ["#", ".", "#", "#", "#", "#", "#"],
    "j": ["..#", "...", "..#", "..#", "..#", "..#", "..#", "#.#", ".#."],
    "k": ["#...", "#...", "#..#", "#.#.", "##..", "#.#.", "#..#"],
    "l": ["#.", "#.", "#.", "#.", "#.", "#.", ".#"],
    "m": [".....", ".....", "##.#.", "#.#.#", "#.#.#", "#.#.#", "#.#.#"],
    "n": [".....", ".....", "####.", "#...#", "#...#", "#...#", "#...#"],
    "o": [".....", ".....", ".###.", "#...#", "#...#", "#...#", ".###."],
    "p": [".....", ".....", "####.", "#...#", "#...#", "#...#", "####.", "#....", "#...."],
    "q": [".....", ".....", ".####", "#...#", "#...#", "#...#", ".####", "....#", "....#"],
    "r": ["....", "....", "#.##", "##..", "#...", "#...", "#..."],
    "s": [".....", ".....", ".####", "#....", ".###.", "....#", "####."],
    "t": [".#..", ".#..", "####", ".#..", ".#..", ".#..", "..##"],
    "u": [".....", ".....", "#...#", "#...#", "#...#", "#...#", ".####"],
    "v": [".....", ".....", "#...#", "#...#", "#...#", ".#.#.", "..#.."],
    "w": [".....", ".....", "#...#", "#...#", "#.#.#", "#.#.#", ".#.#."],
    "x": [".....", ".....", "#...#", ".#.#.", "..#..", ".#.#.", "#...#"],
    "y": [".....", ".....", "#...#", "#...#", "#...#", "#...#", ".####", "....#", ".###."],
    "z": [".....", ".....", "#####", "...#.", "..#..", ".#...", "#####"],
    "0": [".###.", "#...#", "#..##", "#.#.#", "##..#", "#...#", ".###."],
    "1": ["..#..", ".##..", "..#..", "..#..", "..#..", "..#..", ".###."],
    "2": [".###.", "#...#", "....#", "...#.", "..#..", ".#...", "#####"],
    "3": ["####.", "....#", "....#", ".###.", "....#", "....#", "####."],
    "4": ["...#.", "..##.", ".#.#.", "#..#.", "#####", "...#.", "...#."],
    "5": ["#####", "#....", "####.", "....#", "....#", "#...#", ".###."],
    "6": [".###.", "#....", "#....", "####.", "#...#", "#...#", ".###."],
    "7": ["#####", "....#", "...#.", "..#..", ".#...", ".#...", ".#..."],
    "8": [".###.", "#...#", "#...#", ".###.", "#...#", "#...#", ".###."],
    "9": [".###.", "#...#", "#...#", ".####", "....#", "....#", ".###."],
    ".": [".", ".", ".", ".", ".", ".", "#"],
    ",": ["..", "..", "..", "..", "..", ".#", ".#", "#."],
    ";": ["..", "..", ".#", "..", "..", ".#", ".#", "#."],
    ":": [".", ".", "#", ".", ".", "#", "."],
    "!": ["#", "#", "#", "#", "#", ".", "#"],
    "'": ["#", "#", ".", ".", ".", ".", "."],
    '"': ["#.#", "#.#", "...", "...", "...", "...", "..."],
    "@": [".###.", "#...#", "#.###", "#.#.#", "#.###", "#....", ".####"],
    "-": ["...", "...", "...", "###", "...", "...", "..."],
    "—": [".....", ".....", ".....", "#####", ".....", ".....", "....."],
    "·": ["..", "..", "..", "##", "##", "..", ".."],
    "→": [".....", "..#..", "...#.", "#####", "...#.", "..#..", "....."],
    "&": [".##..", "#..#.", "#.#..", ".#...", "#.#.#", "#..#.", ".##.#"],
    ">": ["#....", ".#...", "..#..", "...#.", "..#..", ".#...", "#...."],
    "/": ["....#", "...#.", "...#.", "..#..", ".#...", ".#...", "#...."],
    "+": [".....", "..#..", "..#..", "#####", "..#..", "..#..", "....."],
    "=": [".....", ".....", "#####", ".....", "#####", ".....", "....."],
    "(": [".#", "#.", "#.", "#.", "#.", "#.", ".#"],
    ")": ["#.", ".#", ".#", ".#", ".#", ".#", "#."],
    "[": ["##", "#.", "#.", "#.", "#.", "#.", "##"],
    "]": ["##", ".#", ".#", ".#", ".#", ".#", "##"],
    "{": ["..##", ".#..", ".#..", "#...", ".#..", ".#..", "..##"],
    "}": ["##..", "..#.", "..#.", "...#", "..#.", "..#.", "##.."],
    " ": ["...", "...", "...", "...", "...", "...", "..."],
}
ROWS = 9


def glyph(ch):
    rows = FONT[ch]
    return rows + ["." * len(rows[0])] * (ROWS - len(rows))


def advance(ch, mono=False):
    return (5 if mono else len(FONT[ch][0])) + 1


def layout(text, mono=False):
    """Return ([(x, y, char_index)], width_in_cells). mono pads glyphs to 5 wide."""
    cells, x = [], 0
    for i, ch in enumerate(text):
        rows = glyph(ch)
        w = len(rows[0])
        cw = 5 if mono else w
        off = (cw - w) // 2 if mono else 0
        for y, row in enumerate(rows):
            for gx, c in enumerate(row):
                if c == "#":
                    cells.append((x + off + gx, y, i))
        x += cw + 1
    return cells, x - 1


PLAIN, STRONG, EMPH = 0, 1, 2


def wrap_rich(text, max_cells, mono=False):
    """Word-wrap Markdown-ish text: **strong** and *emphasis*.
    Returns lines of (char, style) pairs with style PLAIN / STRONG / EMPH."""
    chars, strong, emph, i = [], False, False, 0
    while i < len(text):
        if text.startswith("**", i):
            strong, i = not strong, i + 2
            continue
        if text[i] == "*":
            emph, i = not emph, i + 1
            continue
        chars.append((text[i], STRONG if strong else EMPH if emph else PLAIN))
        i += 1
    words, cur = [], []
    for ch, b in chars:
        if ch == " ":
            if cur:
                words.append(cur)
                cur = []
        else:
            cur.append((ch, b))
    if cur:
        words.append(cur)
    lines, line, width = [], [], 0
    space = advance(" ", mono)
    for w in words:
        ww = sum(advance(c, mono) for c, _ in w)
        if line and width + space + ww - 1 > max_cells:
            lines.append(line)
            line, width = [], 0
        if line:
            line.append((" ", PLAIN))
            width += space
        line.extend(w)
        width += ww
    if line:
        lines.append(line)
    return lines


# ---------------------------------------------------------------- helpers
def hex2rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def lerp(a, b, t):
    ra, rb = hex2rgb(a), hex2rgb(b)
    return "#%02X%02X%02X" % tuple(round(ra[i] + (rb[i] - ra[i]) * t) for i in range(3))


def grad3(t):
    """Brand gradient: blue -> purple -> red."""
    return lerp(BLUE, PURPLE, t * 2) if t < 0.5 else lerp(PURPLE, RED, (t - 0.5) * 2)


def f(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


def cells_path(cells, s, ox=0, oy=0):
    """Merge lit cells into horizontal runs and emit one compact path."""
    rows = {}
    for x, y in cells:
        rows.setdefault(y, set()).add(x)
    d = []
    for y in sorted(rows):
        xs = sorted(rows[y])
        i = 0
        while i < len(xs):
            j = i
            while j + 1 < len(xs) and xs[j + 1] == xs[j] + 1:
                j += 1
            w = (j - i + 1) * s
            d.append(f"M{f(ox + xs[i] * s)} {f(oy + y * s)}h{f(w)}v{f(s)}h-{f(w)}z")
            i = j + 1
    return "".join(d)


def text_path(text, s, ox, oy, mono=False):
    cells, _ = layout(text, mono)
    return cells_path([(x, y) for x, y, _ in cells], s, ox, oy)


def text_width(text, s, mono=False):
    return layout(text, mono)[1] * s


def grid_paths(grid, colors, s, ox, oy, cls=None, style=""):
    """Paint a letter grid (one letter per colour key) as one path per colour."""
    out = ""
    for key, col in colors.items():
        pts = [(x, y) for y, r in enumerate(grid) for x, c in enumerate(r) if c == key]
        if pts:
            c_attr = f' class="{cls}"' if cls else ""
            st = f' style="{style}"' if style else ""
            out += f'<path{c_attr}{st} fill="{col}" d="{cells_path(pts, s, ox, oy)}"/>'
    return out


def notched(x, y, w, h, n):
    """Rectangle with two-step pixel corners."""
    p = [
        (x + 2 * n, y), (x + w - 2 * n, y), (x + w - 2 * n, y + n), (x + w - n, y + n),
        (x + w - n, y + 2 * n), (x + w, y + 2 * n), (x + w, y + h - 2 * n), (x + w - n, y + h - 2 * n),
        (x + w - n, y + h - n), (x + w - 2 * n, y + h - n), (x + w - 2 * n, y + h), (x + 2 * n, y + h),
        (x + 2 * n, y + h - n), (x + n, y + h - n), (x + n, y + h - 2 * n), (x, y + h - 2 * n),
        (x, y + 2 * n), (x + n, y + 2 * n), (x + n, y + n), (x + 2 * n, y + n),
    ]
    return "M" + "L".join(f"{f(a)} {f(b)}" for a, b in p) + "Z"


def svg(w, h, title, css, body):
    title = title.replace("&", "&amp;").replace('"', "&quot;")
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
        f'role="img" aria-label="{title}" shape-rendering="crispEdges">'
        f"<title>{title}</title><style>{css}{REDUCED}</style>{body}</svg>\n"
    )


def write(name, content):
    path = os.path.join(OUT, name)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(content)
    print(f"{name}: {len(content.encode()) / 1024:.1f} KB")


# ---------------------------------------------------------------- shared motion
TWINKLE_CSS = ".tw{animation:tw 3s ease-in-out infinite}@keyframes tw{0%,100%{opacity:.12}50%{opacity:1}}"
COMET_CSS = (".cm{opacity:.28;animation:cm 4s linear infinite}"
             "@keyframes cm{0%,16%,100%{opacity:.28}5%{opacity:1}}")
BLINK_CSS = ".bl{animation:bl .9s steps(1,end) infinite}@keyframes bl{0%{opacity:1}50%{opacity:0}}"


def rise_css(dist):
    return (f".rs{{animation:rs 8s linear infinite}}@keyframes rs{{0%{{transform:translateY(0);opacity:0}}"
            f"15%{{opacity:.5}}100%{{transform:translateY(-{dist}px);opacity:0}}}}")


def cluster(x0, x1, y0, y1, left, colors, dens=0.55, step=12, size=8):
    """Pixel dust that thins out away from one edge; every pixel twinkles."""
    out = []
    for gx in range(x0, x1, step):
        d = (gx - x0) / (x1 - x0) if left else (x1 - step - gx) / (x1 - x0)
        for gy in range(y0, y1, step):
            if random.random() < dens * max(0.0, 1 - d) ** 2.2:
                dur, delay = random.uniform(2, 5), -random.uniform(0, 5)
                out.append(f'<rect class="tw" x="{gx}" y="{gy}" width="{size}" height="{size}" '
                           f'fill="{random.choice(colors)}" '
                           f'style="animation-duration:{f(dur)}s;animation-delay:{f(delay)}s"/>')
    return "".join(out)


def particles(n, x0, x1, ybase, colors):
    out = []
    for _ in range(n):
        x = random.randrange(x0 // 10, x1 // 10) * 10
        size = random.choice([4, 6, 8])
        dur = random.uniform(6, 11)
        out.append(f'<rect class="rs" x="{x}" y="{ybase - random.randint(0, 30)}" width="{size}" '
                   f'height="{size}" fill="{random.choice(colors)}" '
                   f'style="animation-duration:{f(dur)}s;animation-delay:{f(-random.uniform(0, dur))}s"/>')
    return "".join(out)


def comet_strip(x0, x1, y, size=10, gap=6, period=4.0):
    """Row of gradient squares with a light pulse travelling left to right."""
    n = (x1 - x0 + gap) // (size + gap)
    start = x0 + ((x1 - x0) - (n * (size + gap) - gap)) / 2
    out = []
    for i in range(n):
        out.append(f'<rect class="cm" x="{f(start + i * (size + gap))}" y="{y}" width="{size}" height="{size}" '
                   f'fill="{grad3(i / max(1, n - 1))}" style="animation-delay:{f(i * period / n * 0.6)}s"/>')
    return "".join(out)


def hud_corners(w, h, inset, s, color):
    arm = [(0, 0), (1, 0), (2, 0), (0, 1), (0, 2)]
    out = []
    for cx, cy, sx, sy in [(inset, inset, 1, 1), (w - inset - s, inset, -1, 1),
                           (inset, h - inset - s, 1, -1), (w - inset - s, h - inset - s, -1, -1)]:
        for ax, ay in arm:
            out.append(f'<rect x="{cx + sx * ax * s}" y="{cy + sy * ay * s}" width="{s}" height="{s}"/>')
    return f'<g fill="{color}" opacity=".55">{"".join(out)}</g>'


def card_bg(w, h, notch, gid):
    """Dark notched card with blue/red side glows and a dot grid. Leaves a clip <g> open."""
    return (
        f'<defs><radialGradient id="{gid}b" cx="0" cy=".5" r=".55"><stop offset="0" stop-color="{BLUE}" '
        f'stop-opacity=".28"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/></radialGradient>'
        f'<radialGradient id="{gid}r" cx="1" cy=".5" r=".55"><stop offset="0" stop-color="{RED}" '
        f'stop-opacity=".24"/><stop offset="1" stop-color="{RED}" stop-opacity="0"/></radialGradient>'
        f'<pattern id="{gid}g" width="20" height="20" patternUnits="userSpaceOnUse">'
        f'<rect width="2" height="2" fill="#FFFFFF" opacity=".07"/></pattern>'
        f'<clipPath id="{gid}c"><path d="{notched(2, 2, w - 4, h - 4, notch)}"/></clipPath></defs>'
        # thin outline so the card still separates from GitHub's near-identical dark page
        f'<path d="{notched(0, 0, w, h, notch)}" fill="#232C52"/>'
        f'<path d="{notched(2, 2, w - 4, h - 4, notch)}" fill="{BG}"/>'
        f'<g clip-path="url(#{gid}c)"><rect width="{w}" height="{h}" fill="url(#{gid}b)"/>'
        f'<rect width="{w}" height="{h}" fill="url(#{gid}r)"/><rect width="{w}" height="{h}" fill="url(#{gid}g)"/>'
    )


def wordmark(word, s, ox, oy):
    """Big pixel wordmark: pixels pop in left to right, then a blue/red shine sweeps
    across on a loop while red/blue ghost layers glitch every few seconds."""
    cells, _ = layout(word)
    plain = [(x, y) for x, y, _ in cells]
    css = (
        f".w{{fill:{INK};animation:pop .55s cubic-bezier(.2,1.6,.4,1) both,sh 6s linear infinite}}"
        "@keyframes pop{0%{opacity:0;transform:translateY(-26px)}100%{opacity:1;transform:translateY(0)}}"
        f"@keyframes sh{{0%,12%,100%{{fill:{INK}}}4%{{fill:{BLUE_L}}}8%{{fill:{RED_L}}}}}"
        ".gl{animation:fi .8s .9s both}@keyframes fi{0%{opacity:0}100%{opacity:1}}"
        ".gr{animation:gr 5s steps(1,end) 2s infinite}"
        "@keyframes gr{0%,94%,100%{transform:translate(0,0)}90%{transform:translate(-10px,4px)}92%{transform:translate(12px,-3px)}}"
        ".gb{animation:gb 5s steps(1,end) 2s infinite}"
        "@keyframes gb{0%,94%,100%{transform:translate(0,0)}90%{transform:translate(10px,-3px)}92%{transform:translate(-12px,2px)}}"
    )
    whites = []
    for x, y, _ in cells:
        d1 = 0.15 + x * 0.018 + random.uniform(0, 0.12)
        d2 = 1.8 + x * 0.03
        whites.append(f'<rect class="w" x="{f(ox + x * s)}" y="{f(oy + y * s)}" width="{s}" height="{s}" '
                      f'style="animation-delay:{f(d1)}s,{f(d2)}s"/>')
    ghosts = (
        f'<g class="gl"><g transform="translate(-5 0)"><path class="gr" fill="{RED}" d="{cells_path(plain, s, ox, oy)}"/></g>'
        f'<g transform="translate(5 0)"><path class="gb" fill="{BLUE}" d="{cells_path(plain, s, ox, oy)}"/></g></g>'
    )
    return css, whites, ghosts


# ---------------------------------------------------------------- reusable assets
def divider():
    W, H = 1200, 28
    write("divider.svg", svg(W, H, "", COMET_CSS, comet_strip(0, W, 9, size=10, gap=6, period=4.0)))


ICONS = {
    "website": ["AAAAAAAAAAA", "A.R.B.W...A", "AAAAAAAAAAA", "A.........A", "A.WWWWW...A",
                "A.........A", "A.WWW.....A", "AAAAAAAAAAA"],
    "medium": [".WWW...W...", "WWWWW.WWW.W", "WWWWW.WWW.W", "WWWWW.WWW.W", ".WWW...W..."],
    "youtube": [".RRRRRRRRR.", "RRRRWRRRRRR", "RRRRWWRRRRR", "RRRRWWWRRRR", "RRRRWWRRRRR",
                "RRRRWRRRRRR", ".RRRRRRRRR."],
    "email": ["AAAAAAAAAAA", "AA.......AA", "A.A.....A.A", "A..A...A..A", "A...A.A...A",
              "A....A....A", "A.........A", "AAAAAAAAAAA"],
    "github": [".W.......W.", ".WW.....WW.", ".WWWWWWWWW.", "WWWWWWWWWWW", "WW..WWW..WW",
               "WW..WWW..WW", "WWWWWWWWWWW", ".WWWWWWWWW.", "..WWW.WWW..", "..W.....W.."],
}


def button(name, label, accent, delay, file_name=None):
    """Pixel button with an icon, a pixel label and a light sweep."""
    s, H, pad, gap, border = 3, 56, 20, 12, 3
    icon = ICONS[name]
    iw, ih = len(icon[0]), len(icon)
    cells, lw = layout(label)
    W = pad + iw * s + gap + lw * s + pad
    ix, iy = pad, (H - ih * s) / 2
    lx, ly = ix + iw * s + gap, (H - 7 * s) / 2
    icon_layers = grid_paths(icon, {"A": accent, "R": RED, "B": BLUE_L, "W": INK}, s, ix, iy)
    css = (
        f".sn{{animation:sn 4.5s ease-in-out {f(delay)}s infinite}}"
        f"@keyframes sn{{0%{{transform:translateX(-120px)}}35%,100%{{transform:translateX({W + 60}px)}}}}"
    )
    body = (
        f'<defs><clipPath id="c"><path d="{notched(border, border, W - 2 * border, H - 2 * border, 4)}"/></clipPath></defs>'
        f'<path d="{notched(0, 0, W, H, 4)}" fill="{accent}"/>'
        f'<path d="{notched(border, border, W - 2 * border, H - 2 * border, 4)}" fill="{BG}"/>'
        + icon_layers
        + f'<path fill="{INK}" d="{cells_path([(x, y) for x, y, _ in cells], s, lx, ly)}"/>'
        + f'<g clip-path="url(#c)"><path class="sn" d="M0 0h28l-24 {H}h-28z" fill="#FFFFFF" opacity=".16"/></g>'
    )
    write(file_name or f"btn-{name}.svg", svg(W, H, label, css, body))
