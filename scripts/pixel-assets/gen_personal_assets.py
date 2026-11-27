#!/usr/bin/env python3
"""Generate the austinhoang8386 personal profile assets (austinhoang8386/assets).

All copy comes verbatim from the existing profile README; only the presentation
changes to the TechByPixel animated pixel style.

Usage, from the root of the .github repo (the profile repo cloned alongside):
    python scripts/pixel-assets/gen_personal_assets.py ../austinhoang8386/assets
"""
import re
import sys

from gen_org_assets import EXPLORE, ICON_ANIM_CSS, ICON_PHASE
from pixel_kit import (BG, BLINK_CSS, BLUE, BLUE_L, COMET_CSS, EMPH, INK, MUTED, PURPLE, RED, RED_L, ROWS,
                       STRONG, TWINKLE_CSS, YELLOW, button, card_bg, cells_path, cluster, comet_strip, divider,
                       f, grad3, grid_paths, hud_corners, layout, notched, particles, rise_css, set_out, svg,
                       text_path, text_width, wordmark, wrap_rich, write)

DIM = "#4A557A"
KEYWORD = "#B98CFF"

# --------------------------------------------------------------------- banner
HAND = ["...Y.Y.Y....", "...Y.Y.Y.Y..", "...Y.Y.Y.Y..", ".Y.YYYYYYY..", ".YYYYYYYYY..",
        ".YYYYYYYYY..", "..YYYYYYYY..", "..YYYYYYY...", "...YYYYYY...", "....YYYY...."]
PHRASES = ["Senior Software Engineer", "Fintech · Crypto · Distributed Systems",
           "AI-Augmented Development"]


def banner():
    W, H = 1200, 360
    greet, gs = "Hi there, I'm", 4
    hand_s = 3
    gw = text_width(greet, gs) + 14 + len(HAND[0]) * hand_s
    gx, gy = (W - gw) / 2, 44

    word, s = "Austin Hoang", 14
    _, wc = layout(word)
    ox, oy = (W - wc * s) / 2, 90

    wm_css, whites, ghosts = wordmark(word, s, ox, oy)

    # rotating typed tagline: each phrase owns one window of the cycle
    s2, win, ty = 4, 4.5, 254
    cycle = win * len(PHRASES)
    vis_end = 100 / len(PHRASES)
    css = (
        TWINKLE_CSS + COMET_CSS + rise_css(280) + wm_css + BLINK_CSS
        + ".sc{animation:sc 7s linear infinite}@keyframes sc{0%{transform:translateY(-80px)}100%{transform:translateY(440px)}}"
        + ".hd{transform-box:fill-box;transform-origin:50% 100%;animation:hd 2.4s ease-in-out infinite}"
        + "@keyframes hd{0%,60%,100%{transform:rotate(0)}10%,30%{transform:rotate(18deg)}20%,40%{transform:rotate(-10deg)}}"
        + f".vs{{animation:vs {f(cycle)}s steps(1,end) infinite}}@keyframes vs{{0%{{opacity:1}}{f(vis_end)}%,100%{{opacity:0}}}}"
    )
    phrases = ""
    for k, text in enumerate(PHRASES):
        n = len(text)
        tw = n * 6 * s2
        tx = (W - tw) / 2
        typed = f(n * 0.07 / cycle * 100)
        css += (
            f".t{k}{{transform-box:fill-box;transform-origin:0 0;animation:t{k} {f(cycle)}s steps({n},end) infinite}}"
            f"@keyframes t{k}{{0%{{transform:scaleX(0)}}{typed}%,100%{{transform:scaleX(1)}}}}"
            f".c{k}{{animation:c{k} {f(cycle)}s steps({n},end) infinite}}"
            f"@keyframes c{k}{{0%{{transform:translateX(-{tw}px)}}{typed}%,100%{{transform:translateX(0)}}}}"
        )
        # negative delay keeps every phrase on the shared clock from the first frame
        delay = f"animation-delay:{f(k * win - cycle)}s"
        phrases += (
            f'<g class="vs" style="{delay}">'
            f'<defs><clipPath id="p{k}"><rect class="t{k}" style="{delay}" x="{f(tx)}" y="{ty - 2}" '
            f'width="{tw}" height="{ROWS * s2 + 4}"/></clipPath></defs>'
            f'<path clip-path="url(#p{k})" fill="{MUTED}" d="{text_path(text, s2, tx, ty, mono=True)}"/>'
            f'<g class="c{k}" style="{delay}"><rect class="bl" x="{f(tx + tw)}" y="{ty}" width="{3 * s2}" '
            f'height="{7 * s2}" fill="{RED}"/></g></g>'
        )

    hx = gx + text_width(greet, gs) + 14
    body = (
        card_bg(W, H, 8, "bn")
        + '<rect class="sc" width="1200" height="70" fill="#FFFFFF" opacity=".035"/>'
        + particles(16, 160, 1040, H - 40, [BLUE_L, RED_L, PURPLE, INK])
        + cluster(14, 160, 18, H - 50, True, [BLUE, BLUE_L, BLUE, PURPLE, INK])
        + cluster(1040, 1188, 18, H - 50, False, [RED, RED_L, RED, PURPLE, INK])
        + f'<path fill="{MUTED}" d="{text_path(greet, gs, gx, gy)}"/>'
        + f'<g class="hd">{grid_paths(HAND, {"Y": YELLOW}, hand_s, hx, gy - 4)}</g>'
        + ghosts
        + "".join(whites)
        + phrases
        + comet_strip(30, W - 30, H - 34, size=10, gap=6, period=4.0)
        + hud_corners(W, H, 22, 5, MUTED)
        + "</g>"
    )
    title = "Hi there, I'm Austin Hoang - " + " | ".join(PHRASES)
    write("banner.svg", svg(W, H, title, css, body))


# --------------------------------------------------------------------- about me
ROBOT = EXPLORE[0][1]
ABOUT = [
    ("**Senior Software Engineer** with **5+ years** building scalable distributed systems", {
        "base": ["..AAAAAAAA..", "..A......A..", "..A.WW...A..", "..A......A..", "..A.WWWW.A..",
                 "..A......A..", "..AAAAAAAA..", ".AAAAAAAAAA.", "AAAAAAAAAAAA"],
        "anim": [("bk", ["............", "............", ".......B...."])],
    }),
    ("Deep **fintech/crypto** domain experience: OTC & P2P trading platforms, crypto deposit/withdraw "
     "(BTC, ETH, USDT, TRX), NFT marketplaces, payment systems", {
         "base": ["...AAAAAA...", "..AYYYYYYA..", ".AYYWWWYYYA.", "AYYYWYYWYYYA", "AYYYWWWYYYYA",
                  "AYYYWYYWYYYA", "AYYYWYYWYYYA", "AYYYWWWYYYYA", ".AYYYYYYYYA.", "..AYYYYYYA..",
                  "...AAAAAA..."],
         "anim": [],
         "flip": True,
     }),
    ("Early production adopter of **AI-augmented engineering** — shipping features end-to-end through "
     "agentic workflows: *brainstorm → plan → implement → verify*", ROBOT),
    ("Growing toward a **Tech Lead** role", {
        "base": ["....AAAA....", "..AA....AA..", ".A..RRRR..A.", ".A.R....R.A.", "A.R......R.A",
                 "A.R......R.A", "A.R......R.A", "A.R......R.A", ".A.R....R.A.", ".A..RRRR..A.",
                 "..AA....AA..", "....AAAA...."],
        "anim": [("pu", ["............", "............", "............", "............", ".....WW.....",
                         "....WWWW....", "....WWWW....", ".....WW....."])],
    }),
    ("Reach me at **austinhoang8386@gmail.com**", {
        "base": ["AAAAAAAAAAA.", "AA.......AA.", "A.A.....A.A.", "A..A...A..A.", "A...A.A...A.",
                 "A....A....A.", "A.........A.", "AAAAAAAAAAA."],
        "anim": [("bk", ["..........RR", "..........RR"])],
    }),
]


def menu_rows(items, W, s_txt=3, slot=1.6):
    """Retro game menu: a selection cursor walks the rows; text wraps inside each row."""
    s_icon, gap = 4, 10
    tx0 = 44 + 12 * s_icon + 24
    max_cells = (W - tx0 - 28) // s_txt
    line_h = ROWS * s_txt + 6
    laid = []
    for text, icon in items:
        lines = wrap_rich(text, max_cells)
        text_h = len(lines) * line_h - 6
        laid.append((lines, icon, max(64, text_h + 30), text_h))
    H = sum(r[2] for r in laid) + gap * (len(laid) - 1)
    cycle = slot * len(items)
    on = 100 / len(items)
    css = (
        f".hl{{opacity:.3;animation:hl {f(cycle)}s steps(1,end) infinite}}"
        f"@keyframes hl{{0%{{opacity:1}}{f(on)}%,100%{{opacity:.3}}}}"
        f".ar{{opacity:0;animation:ar {f(cycle)}s steps(1,end) infinite}}"
        f"@keyframes ar{{0%{{opacity:1}}{f(on)}%,100%{{opacity:0}}}}"
        f".tx{{animation:tx {f(cycle)}s steps(1,end) infinite}}"
        f"@keyframes tx{{0%{{transform:translateX(8px)}}{f(on)}%,100%{{transform:translateX(0)}}}}"
        ".fl{animation:fl 3s ease-in-out infinite}"
        "@keyframes fl{0%,60%,100%{transform:scaleX(1)}70%{transform:scaleX(.15)}80%{transform:scaleX(1)}}"
        + ICON_ANIM_CSS
    )
    arrow = ["#....", "##...", "###..", "####.", "###..", "##...", "#...."]
    acells = [(x, yy) for yy, r in enumerate(arrow) for x, c in enumerate(r) if c == "#"]
    out, y = [], 0
    for i, (lines, icon, rh, text_h) in enumerate(laid):
        accent = grad3(i / max(1, len(items) - 1))
        delay = f"animation-delay:{f(i * slot - cycle)}s"
        colors = {"A": accent, "W": INK, "B": BLUE_L, "R": RED, "P": PURPLE, "Y": YELLOW}
        ih = len(icon["base"])
        ix, iy = 44, y + (rh - ih * s_icon) / 2
        icon_svg = grid_paths(icon["base"], colors, s_icon, ix, iy)
        for cls, grid in icon["anim"]:
            icon_svg += grid_paths(grid, colors, s_icon, ix, iy, cls,
                                   f"animation-delay:{f(-(i * 0.37 + ICON_PHASE.get(cls, 0)))}s")
        if icon.get("flip"):
            icon_svg = (f'<g class="fl" style="transform-origin:{f(ix + 6 * s_icon)}px {f(iy + ih * s_icon / 2)}px">'
                        f"{icon_svg}</g>")
        ty = y + (rh - text_h) / 2
        text_svg = ""
        for li, line in enumerate(lines):
            cells, _ = layout("".join(c for c, _ in line))
            by_style = {}
            for x, yy, ci in cells:
                by_style.setdefault(line[ci][1], []).append((x, yy))
            for style, pts in by_style.items():
                col = INK if style == STRONG else BLUE_L if style == EMPH else MUTED
                text_svg += f'<path fill="{col}" d="{cells_path(pts, s_txt, tx0, ty + li * line_h)}"/>'
        out.append(
            f'<path class="hl" style="{delay}" d="{notched(0, y, W, rh, 4)}" fill="{accent}"/>'
            f'<path d="{notched(2, y + 2, W - 4, rh - 4, 4)}" fill="{BG}"/>'
            f'<path class="ar" style="{delay}" fill="{accent}" d="{cells_path(acells, s_txt, 16, y + (rh - 7 * s_txt) / 2)}"/>'
            + icon_svg
            + f'<g class="tx" style="{delay}">{text_svg}</g>'
        )
        y += rh + gap
    return W, H, css, "".join(out)


def about():
    W, H, css, body = menu_rows(ABOUT, 1000)
    title = " | ".join(re.sub(r"\*+", "", t) for t, _ in ABOUT)
    write("about.svg", svg(W, H, title, css, body))


# --------------------------------------------------------------------- code card
CODE = [
    "const austin = {",
    '  role: "Senior Software Engineer",',
    '  domain: ["Fintech", "Crypto Exchange", "OTC/P2P Trading"],',
    '  code: ["TypeScript", "JavaScript", "Python", "SQL"],',
    '  architecture: ["Microservices", "Event-Driven", "gRPC", "GraphQL", "REST"],',
    '  aiWorkflow: ["Claude Code", "ClaudeKit", "OpenAI Codex", "Cursor"],',
    '  motto: "AI amplifies a strong engineer — fundamentals first.",',
    "};",
]
TOKEN = re.compile(r'"[^"]*"|\bconst\b|[A-Za-z_]\w*(?=:)|[A-Za-z_]\w*|\s+|.')


def code_colors(line):
    """Per-character colour for a line of the TypeScript snippet."""
    cols = []
    for m in TOKEN.finditer(line):
        tok = m.group(0)
        if tok.startswith('"'):
            c = YELLOW
        elif tok == "const":
            c = KEYWORD
        elif re.match(r"[A-Za-z_]", tok):
            c = BLUE_L if line[m.end():m.end() + 1] == ":" else INK
        else:
            c = MUTED
        cols.extend([c] * len(tok))
    return cols


def code_card():
    s, adv = 2, 12  # mono glyph advance = 6 cells
    pad, bar, gutter = 26, 42, 3 * adv
    code_x = pad + gutter + 18
    line_h = ROWS * s + 8
    W = code_x + max(len(l) for l in CODE) * adv + pad
    H = bar + 22 + len(CODE) * line_h + 16
    per_char, gap, start, hold, erase = 0.018, 0.15, 0.4, 5.5, 0.6
    t, sched = start, []
    for line in CODE:
        d = len(line) * per_char
        sched.append((t, t + d))
        t += d + gap
    cycle = t + hold + erase
    pct = lambda v: f(v / cycle * 100)
    h_pct = pct(cycle - erase)

    css = BLINK_CSS
    body = (
        f'<path d="{notched(0, 0, W, H, 6)}" fill="#232C52"/>'
        f'<path d="{notched(2, 2, W - 4, H - 4, 6)}" fill="{BG}"/>'
        f'<rect x="2" y="{bar}" width="{W - 4}" height="2" fill="#232C52"/>'
    )
    for k, col in enumerate([RED, PURPLE, BLUE]):
        body += f'<rect x="{pad + k * 22}" y="{bar / 2 - 6}" width="12" height="12" fill="{col}"/>'
    lang = "typescript"
    body += f'<path fill="{DIM}" d="{text_path(lang, s, W - pad - text_width(lang, s), bar / 2 - 7)}"/>'

    for k, line in enumerate(CODE):
        y = bar + 22 + k * line_h
        n = len(line)
        lw = n * adv
        s0, e0 = sched[k]
        nxt = sched[k + 1][0] if k + 1 < len(CODE) else cycle - erase
        css += (
            f".l{k}{{transform-box:fill-box;transform-origin:0 0;animation:l{k} {f(cycle)}s steps({n},end) infinite}}"
            f"@keyframes l{k}{{0%,{pct(s0)}%{{transform:scaleX(0)}}{pct(e0)}%,{h_pct}%{{transform:scaleX(1)}}"
            f"100%{{transform:scaleX(0)}}}}"
            f".m{k}{{animation:m{k} {f(cycle)}s steps({n},end) infinite}}"
            f"@keyframes m{k}{{0%,{pct(s0)}%{{transform:translateX(-{lw}px)}}{pct(e0)}%,100%{{transform:translateX(0)}}}}"
            f".o{k}{{animation:o{k} {f(cycle)}s steps(1,end) infinite}}"
            f"@keyframes o{k}{{0%{{opacity:0}}{pct(s0)}%{{opacity:1}}{pct(nxt)}%,100%{{opacity:0}}}}"
        )
        num = str(k + 1)
        body += f'<path fill="{DIM}" d="{text_path(num, s, pad + gutter - len(num) * adv, y, mono=True)}"/>'
        cells, _ = layout(line, mono=True)
        cols = code_colors(line)
        by_col = {}
        for x, yy, ci in cells:
            by_col.setdefault(cols[ci], []).append((x, yy))
        glyphs = "".join(f'<path fill="{c}" d="{cells_path(p, s, code_x, y)}"/>' for c, p in by_col.items())
        body += (
            f'<defs><clipPath id="k{k}"><rect class="l{k}" x="{code_x}" y="{y - 2}" width="{lw}" '
            f'height="{ROWS * s + 4}"/></clipPath></defs><g clip-path="url(#k{k})">{glyphs}</g>'
            f'<g class="m{k}"><g class="o{k}" opacity="0"><rect class="bl" x="{code_x + lw}" y="{y}" '
            f'width="{3 * s}" height="{7 * s}" fill="{RED}"/></g></g>'
        )
    write("code.svg", svg(W, H, " ".join(l.strip() for l in CODE), css, body))


# --------------------------------------------------------------------- chips
def chip(x, y, label, accent, cls="", style="", h=40, s=3):
    tw = text_width(label, s)
    w = 30 + tw + 16
    return w, (
        f'<path class="{cls}" style="{style}" d="{notched(x, y, w, h, 3)}" fill="{accent}"/>'
        f'<path d="{notched(x + 2, y + 2, w - 4, h - 4, 3)}" fill="{BG}"/>'
        f'<rect x="{x + 14}" y="{y + h / 2 - 3}" width="6" height="6" fill="{accent}"/>'
        f'<path fill="{INK}" d="{text_path(label, s, x + 30, y + (h - 7 * s) / 2)}"/>'
    )


def chip_width(label, s=3):
    return 30 + text_width(label, s) + 16


def flow_rows(labels, W, gap=12, center=False):
    """Greedy left-to-right wrap; returns [(row_y_index, x, label)]."""
    rows, cur, cw = [], [], 0
    for lb in labels:
        w = chip_width(lb)
        if cur and cw + gap + w > W:
            rows.append((cur, cw))
            cur, cw = [], 0
        cw += (gap if cur else 0) + w
        cur.append(lb)
    if cur:
        rows.append((cur, cw))
    out = []
    for r, (items, total) in enumerate(rows):
        x = (W - total) / 2 if center else 0
        for lb in items:
            out.append((r, x, lb))
            x += chip_width(lb) + gap
    return out, len(rows)


CHIP_CSS = (".pc{opacity:.35;animation:pc 4s linear infinite}"
            "@keyframes pc{0%,14%,100%{opacity:.35}5%{opacity:1}}")

STACK = [
    ("Languages", ["TypeScript", "JavaScript", "Node.js", "Python", "Go"]),
    ("Backend & Frameworks", ["NestJS", "Express", "Django", "React", "GraphQL"]),
    ("Databases & Messaging", ["PostgreSQL", "MySQL", "Redis", "MongoDB", "RabbitMQ"]),
    ("DevOps & Cloud", ["Docker", "Kubernetes", "AWS", "Terraform", "Grafana"]),
]


def stack():
    W, s = 1000, 3
    total = sum(len(items) for _, items in STACK)
    body, y, idx = "", 0, 0
    for c, (title, items) in enumerate(STACK):
        accent = grad3(c / (len(STACK) - 1))
        body += f'<rect x="0" y="{y + 4}" width="12" height="12" fill="{accent}"/>'
        body += f'<path fill="{accent}" d="{text_path(title, s, 22, y)}"/>'
        placed, nrows = flow_rows(items, W)
        for r, x, lb in placed:
            delay = f"animation-delay:{f(idx * 4 / total * 0.8)}s"
            _, svg_chip = chip(x, y + 34 + r * 52, lb, accent, "pc", delay)
            body += svg_chip
            idx += 1
        y += 34 + nrows * 52 + 18
    H = y - 18
    title = "; ".join(f"{t}: {', '.join(i)}" for t, i in STACK)
    write("stack.svg", svg(W, H, title, CHIP_CSS, body))


# --------------------------------------------------------------------- AI workflow
AI_TOOLS = ["Claude Code", "ClaudeKit", "OpenAI Codex", "Cursor", "MCP"]
FLOW = ["brainstorm", "plan", "implement", "verify"]
PRACTICES = ["multi-agent code review", "spec-driven development", "prompt & context engineering"]


def ai_workflow():
    W, s = 1000, 3
    body, y = "", 0
    placed, nrows = flow_rows(AI_TOOLS, W, center=True)
    for i, (r, x, lb) in enumerate(placed):
        accent = grad3(i / (len(AI_TOOLS) - 1))
        _, c = chip(x, y + r * 52, lb, accent, "pc", f"animation-delay:{f(i * 0.6)}s")
        body += c
    y += nrows * 52 + 26

    label = "Agentic coding workflows"
    body += f'<path fill="{MUTED}" d="{text_path(label, s, (W - text_width(label, s)) / 2, y)}"/>'
    y += 40

    # brainstorm -> plan -> implement -> verify, lit one step at a time
    bh, arrow_w, agap = 52, 5 * 4, 16
    widths = [text_width(t, s) + 44 for t in FLOW]
    total = sum(widths) + (len(FLOW) - 1) * (arrow_w + 2 * agap)
    x = (W - total) / 2
    slot = 0.9
    cycle = slot * len(FLOW)
    on = 100 / len(FLOW)
    css = (
        CHIP_CSS
        + f".st{{opacity:.3;animation:st {f(cycle)}s steps(1,end) infinite}}"
        + f"@keyframes st{{0%{{opacity:1}}{f(on)}%,100%{{opacity:.3}}}}"
        + f".sa{{opacity:.25;animation:st {f(cycle)}s steps(1,end) infinite}}"
    )
    for i, (t, w) in enumerate(zip(FLOW, widths)):
        accent = grad3(i / (len(FLOW) - 1))
        delay = f"animation-delay:{f(i * slot - cycle)}s"
        body += (
            f'<path class="st" style="{delay}" d="{notched(x, y, w, bh, 4)}" fill="{accent}"/>'
            f'<path d="{notched(x + 3, y + 3, w - 6, bh - 6, 4)}" fill="{BG}"/>'
            f'<path fill="{INK}" d="{text_path(t, s, x + 22, y + (bh - 7 * s) / 2 - 2)}"/>'
        )
        x += w
        if i < len(FLOW) - 1:
            # the arrow lights with the step it leads into
            nd = f"animation-delay:{f((i + 1) * slot - cycle)}s"
            body += (f'<path class="sa" style="{nd}" fill="{grad3((i + 1) / (len(FLOW) - 1))}" '
                     f'd="{text_path(chr(0x2192), 4, x + agap, y + (bh - 28) / 2)}"/>')
            x += arrow_w + 2 * agap
    y += bh + 26

    placed, nrows = flow_rows(PRACTICES, W, center=True)
    for r, x, lb in placed:
        _, c = chip(x, y + r * 52, lb, DIM)
        body += c
    H = y + nrows * 52 - 12
    title = (f"{', '.join(AI_TOOLS)}. {label}: {' -> '.join(FLOW)} · " + " · ".join(PRACTICES))
    write("ai.svg", svg(W, H, title, css, body))


# --------------------------------------------------------------------- footer
STAR = ["....Y....", "....Y....", "...YYY...", "YYYYYYYYY", ".YYYYYYY.", "..YYYYY..", "..YY.YY..",
        ".YY...YY."]


def footer():
    W, H = 1200, 170
    text, s = "From austinhoang8386 — thanks for stopping by!", 4
    cells, tw = layout(text)
    star_w = len(STAR[0]) * s
    total = star_w + 18 + tw * s
    sx = (W - total) / 2
    ox, oy = sx + star_w + 18, 64
    css = (
        TWINKLE_CSS + COMET_CSS + rise_css(130)
        + f".ch{{fill:{INK};animation:wv 5s linear infinite}}"
        + f"@keyframes wv{{0%,20%,100%{{fill:{INK};transform:translateY(0)}}6%{{fill:{BLUE_L};transform:translateY(-6px)}}"
        + f"12%{{fill:{RED_L};transform:translateY(0)}}}}"
        + ".sr{transform-box:fill-box;transform-origin:50% 50%;animation:sr 1.8s steps(1,end) infinite}"
        + "@keyframes sr{0%{transform:scale(1)}50%{transform:scale(1.25)}}"
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
        + cluster(14, 110, 16, H - 40, True, [BLUE, BLUE_L, PURPLE], dens=0.5)
        + cluster(1090, 1188, 16, H - 40, False, [RED, RED_L, PURPLE], dens=0.5)
        + f'<g class="sr">{grid_paths(STAR, {"Y": YELLOW}, s, sx, oy - 2)}</g>'
        + glyphs
        + comet_strip(30, W - 30, H - 30, size=8, gap=6, period=4.0)
        + hud_corners(W, H, 18, 4, MUTED)
        + "</g>"
    )
    write("footer.svg", svg(W, H, text, css, body))


if __name__ == "__main__":
    set_out(sys.argv[1] if len(sys.argv) > 1 else ".", seed=8386)
    banner()
    divider()
    about()
    code_card()
    stack()
    ai_workflow()
    button("email", "Gmail", RED, 0.0, "btn-gmail.svg")
    button("github", "GitHub", BLUE, 0.8, "btn-github.svg")
    footer()
