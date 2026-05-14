#!/usr/bin/env python3
"""Parses survey.md → docs/index.html + docs/details/"""

import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent
SURVEY_PATH = ROOT / "survey.md"
DETAIL_DIR = ROOT / "detailed_survey"
DOCS_DIR = ROOT / "docs"
OUTPUT_PATH = DOCS_DIR / "index.html"
DETAILS_OUT = DOCS_DIR / "details"

CHECK = '<span class="badge badge-yes"><svg width="16" height="16" viewBox="0 0 16 16"><circle cx="8" cy="8" r="7.5" fill="currentColor" opacity="0.12"/><path d="M4.5 8.5L7 11l4.5-5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg></span>'
CROSS = '<span class="badge badge-no"><svg width="16" height="16" viewBox="0 0 16 16"><circle cx="8" cy="8" r="7.5" fill="currentColor" opacity="0.12"/><path d="M5.25 5.25l5.5 5.5M10.75 5.25l-5.5 5.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" fill="none"/></svg></span>'
DETAIL_BTN = '<svg width="13" height="13" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="2" y="1.5" width="12" height="13" rx="2"/><path d="M5 5.5h6M5 8h6M5 10.5h4"/></svg>'


def norm(name: str) -> str:
    name = re.sub(r"(\d+)\.\d+", r"\1", name)
    return re.sub(r"[^a-z0-9]", "", name.lower())


# ── Detail file scanning ──────────────────────────────────────────────

def scan_details() -> dict[str, str]:
    mapping: dict[str, str] = {}
    if not DETAIL_DIR.exists():
        return mapping
    for sec_dir in sorted(DETAIL_DIR.iterdir()):
        if not sec_dir.is_dir():
            continue
        for md_file in sec_dir.glob("*.md"):
            if md_file.name.startswith("_"):
                continue
            first = md_file.read_text(encoding="utf-8", errors="replace").split("\n")[0]
            title = re.sub(r"^#+\s*(\d+(\.\d+)?\s+)?", "", first).strip()
            n = norm(title)
            if n:
                mapping[n] = f"{sec_dir.name}/{md_file.stem}"
            fn = norm(md_file.stem)
            if fn and fn not in mapping:
                mapping[fn] = f"{sec_dir.name}/{md_file.stem}"
    return mapping


def render_detail_md(md_text: str) -> str:
    lines = md_text.split("\n")
    parts: list[str] = []
    in_ul = False
    in_tbl = False

    def close_ul():
        nonlocal in_ul
        if in_ul:
            parts.append("</ul>")
            in_ul = False

    def close_tbl():
        nonlocal in_tbl
        if in_tbl:
            parts.append("</tbody></table></div>")
            in_tbl = False

    for line in lines:
        s = line.strip()
        if not s:
            close_ul()
            close_tbl()
            continue
        if s == "---":
            close_ul()
            close_tbl()
            parts.append("<hr>")
            continue
        if s.startswith("### "):
            close_ul(); close_tbl()
            parts.append(f'<h3 class="dp-h3">{render_inline(s[4:])}</h3>')
            continue
        if s.startswith("## "):
            close_ul(); close_tbl()
            parts.append(f'<h2 class="dp-h2">{render_inline(s[3:])}</h2>')
            continue
        if s.startswith("> "):
            close_ul(); close_tbl()
            parts.append(f'<blockquote class="dp-quote">{render_inline(s[2:])}</blockquote>')
            continue
        if s.startswith("- "):
            close_tbl()
            if not in_ul:
                parts.append('<ul class="dp-list">')
                in_ul = True
            parts.append(f"<li>{render_inline(s[2:])}</li>")
            continue
        if s.startswith("|") and "|" in s[1:]:
            close_ul()
            if re.match(r"^\|[\s\-:|]+\|$", s):
                continue
            cells = [c.strip() for c in s.strip("|").split("|")]
            if not in_tbl:
                in_tbl = True
                parts.append('<div class="dp-tbl-wrap"><table class="dp-tbl"><thead><tr>')
                for c in cells:
                    parts.append(f"<th>{render_inline(c)}</th>")
                parts.append("</tr></thead><tbody>")
            else:
                parts.append("<tr>")
                for c in cells:
                    parts.append(f"<td>{render_inline(c)}</td>")
                parts.append("</tr>")
            continue
        close_ul(); close_tbl()
        parts.append(f'<p class="dp-p">{render_inline(s)}</p>')

    close_ul(); close_tbl()
    return "\n".join(parts)


def build_detail_pages(detail_map: dict[str, str]) -> int:
    count = 0
    for key, rel_path in detail_map.items():
        parts = rel_path.split("/")
        src = DETAIL_DIR / parts[0] / f"{parts[1]}.md"
        if not src.exists():
            continue
        md = src.read_text(encoding="utf-8", errors="replace")
        html = render_detail_md(md)
        out_dir = DETAILS_OUT / parts[0]
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{parts[1]}.html"
        if not out_path.exists() or out_path.read_text(encoding="utf-8", errors="replace") != html:
            out_path.write_text(html, encoding="utf-8")
        count += 1
    return count


# ── Inline markdown ───────────────────────────────────────────────────

def render_inline(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r"\[(\*\*(.+?)\*\*)\]\(([^)]+)\)",
                  r'<a href="\3" target="_blank" rel="noopener"><strong>\2</strong></a>', text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
                  r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


# ── Badge rendering ───────────────────────────────────────────────────

def badge(text: str) -> str:
    s = text.strip()
    if s == "—":
        return '<span class="badge badge-na">—</span>'
    has_y = "✅" in s
    has_n = "✗" in s
    if not has_y and not has_n:
        return render_inline(s)
    remaining = s.replace("✅", "").replace("✗", "").strip()
    b = CHECK if has_y else CROSS
    if remaining:
        return b + " " + render_inline(remaining)
    return b


# ── Hand type classification ─────────────────────────────────────────

DEX_KW = ["allegro", "shadow", "leap", "inspire", "xhand", "d'claw", "multi-finger",
          "dexterous", "sharpa", "ability", "oymotion", "wuji", "schunk", "rohand",
          "adroit", "mano", "dex-ee", "anthropomorphic", "5-finger", "dex hand",
          "dclaw", "fourier", "faive", "orca", "isyhand", "ruka", "psyonic"]

def classify_hand(cells: list[str], headers: list[str]) -> list[str]:
    hl = [h.lower() for h in headers]
    hand_txt = ""
    robot_txt = ""
    for i, h in enumerate(hl):
        if i >= len(cells):
            break
        cl = cells[i].lower()
        if any(k in h for k in ("hand", "dex hand", "dof", "target hand")):
            hand_txt += " " + cl
        if "robot" in h:
            robot_txt += " " + cl
    combined = hand_txt + " " + robot_txt
    tags: list[str] = []
    if any(k in combined for k in DEX_KW) or ("✅" in hand_txt):
        tags.append("dex")
    if "gripper" in combined or "parallel" in combined:
        tags.append("gripper")
    if "✗" in hand_txt and "dex" not in tags and "gripper" not in tags:
        tags.append("gripper")
    if any(k in combined for k in ["bimanual", "2x ", "dual", "2×"]):
        tags.append("bimanual")
    if any(k in combined for k in ["humanoid", "unitree", " g1 ", " h1"]):
        tags.append("fullbody")
    return tags


# ── Table parsing & rendering ─────────────────────────────────────────

def parse_row(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]

def is_sep(line: str) -> bool:
    return bool(re.match(r"^\|[\s\-:|]+\|$", line.strip()))

def row_meta(cells: list[str], headers: list[str]) -> dict[str, str]:
    meta: dict[str, str] = {}
    hl = [h.lower() for h in headers]
    for i, h in enumerate(hl):
        if i >= len(cells):
            break
        c = cells[i]
        if h in ("year", "date"):
            m = re.search(r"(20\d{2})", c)
            if m:
                meta["year"] = m.group(1)
        if any(k in h for k in ("code", "open code", "design files", "install")):
            meta["code"] = "true" if ("✅" in c or "github" in c.lower() or "pip" in c.lower()) else "false"
        if any(k in h for k in ("weights", "open weights")):
            meta["weights"] = "true" if ("✅" in c or "ckpt" in c.lower() or "hf" in c.lower() or "apache" in c.lower()) else "false"
        if "download" in h:
            meta["code"] = "true" if "✅" in c else "false"
    hand_tags = classify_hand(cells, headers)
    if hand_tags:
        meta["hand"] = " ".join(hand_tags)
    return meta


def extract_paper_name(cell: str) -> str:
    m = re.search(r"\*\*([^*]+)\*\*", cell)
    return m.group(1) if m else cell.strip()[:30]


def render_table(headers: list[str], rows: list[list[str]], sec_id: str, detail_map: dict[str, str]) -> str:
    n = len(rows)
    h = '<div class="table-card">\n'
    h += '  <div class="table-controls">\n'
    h += '    <div class="table-search-wrap"><svg class="search-icon" viewBox="0 0 20 20" fill="currentColor" width="16" height="16"><path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd"/></svg>'
    h += '<input type="search" class="table-search" placeholder="Search this table..."></div>\n'
    h += f'    <span class="table-count"><span class="count-visible">{n}</span> / {n}</span>\n'
    h += '  </div>\n  <div class="table-scroll">\n'
    h += f'    <table class="survey-table" data-section="{sec_id}" data-total="{n}">\n'
    h += '      <thead><tr>\n'
    for col in headers:
        h += f'        <th class="sortable">{col}</th>\n'
    h += '      </tr></thead>\n      <tbody>\n'

    for row in rows:
        m = row_meta(row, headers)
        attrs = " ".join(f'data-{k}="{v}"' for k, v in m.items())
        h += f'      <tr {attrs}>\n'
        for ci, cell in enumerate(row):
            rendered = badge(cell)
            if ci == 0:
                pname = extract_paper_name(cell)
                nk = norm(pname)
                dp = detail_map.get(nk)
                if dp:
                    rendered += f' <button class="detail-btn" data-detail="details/{dp}.html" data-title="{pname}" title="View details">{DETAIL_BTN}</button>'
            h += f'        <td>{rendered}</td>\n'
        h += '      </tr>\n'
    h += '      </tbody>\n    </table>\n  </div>\n</div>\n'
    return h


# ── Section parsing ───────────────────────────────────────────────────

def parse_md(md: str, detail_map: dict[str, str]) -> tuple[str, list[dict], str]:
    """Return (sidebar_html, sections, date_str)."""
    lines = md.split("\n")
    sections: list[dict] = []
    cur: dict | None = None
    content: list[tuple] = []
    in_table = False
    t_hdr: list[str] | None = None
    t_rows: list[list[str]] = []

    date_match = re.search(r"Last updated:\s*(\d{4}-\d{2}-\d{2})", md)
    if date_match:
        d = datetime.strptime(date_match.group(1), "%Y-%m-%d")
        date_str = d.strftime("%B %d, %Y")
    else:
        date_str = "May 14, 2026"

    def flush_table():
        nonlocal in_table, t_hdr, t_rows
        if t_hdr and t_rows:
            sid = cur["id"] if cur else "intro"
            content.append(("table", render_table(t_hdr, t_rows, sid, detail_map)))
        in_table = False; t_hdr = None; t_rows = []

    def flush_section():
        nonlocal cur, content
        flush_table()
        if cur:
            cur["content"] = content
            sections.append(cur)
            content = []

    for line in lines:
        if line.startswith("## "):
            flush_section()
            title = line[3:].strip()
            m = re.match(r"(\d+(?:\.\d+)?)\.\s*(.*)", title)
            num, ttl = (m.group(1), m.group(2)) if m else ("", title)
            sec_id = f"sec-{num}" if num else re.sub(r"[^a-z0-9]+", "-", ttl.lower()).strip("-")
            cur = {"id": sec_id, "number": num, "title": ttl, "content": []}
            content = []
            continue
        if line.startswith("### "):
            flush_table()
            title = line[4:].strip()
            m = re.match(r"(\d+(?:\.\d+)?)\s*(.*)", title)
            num, ttl = (m.group(1), m.group(2)) if m else ("", title)
            sub_id = re.sub(r"[^a-z0-9]+", "-", ttl.lower()).strip("-")
            content.append(("sub", num, ttl, sub_id))
            continue
        if line.strip().startswith("|") and "|" in line.strip()[1:]:
            if is_sep(line):
                continue
            cells = parse_row(line)
            if not in_table:
                in_table = True; t_hdr = cells
            else:
                t_rows.append(cells)
            continue
        if in_table:
            flush_table()
        if line.strip() in ("---", "") or line.startswith("# ") or line.startswith("> "):
            continue
        if cur:
            content.append(("text", line.strip()))

    flush_section()

    # Sidebar with subsections
    sb = ""
    for sec in sections:
        if sec["number"]:
            n = sec["number"].zfill(2) if len(sec["number"]) == 1 else sec["number"]
            short = sec["title"]
            if len(short) > 32:
                short = short[:30] + "…"
            subs = [it for it in sec["content"] if it[0] == "sub"]
            sb += f'<div class="sb-group" data-section="{sec["id"]}">\n'
            sb += f'  <a href="#{sec["id"]}" class="sb-link" data-target="{sec["id"]}"><span class="sb-num">{n}</span>{short}</a>\n'
            if subs:
                sb += '  <div class="sb-subs">\n'
                for it in subs:
                    _, sn, st, si = it
                    ss = st[:26] + "…" if len(st) > 26 else st
                    sb += f'    <a href="#sub-{si}" class="sb-sub">{sn} {ss}</a>\n'
                sb += '  </div>\n'
            sb += '</div>\n'

    return sb, sections, date_str


def render_sections(sections: list[dict]) -> str:
    bands = ["band-canvas", "band-cloud"]
    out = ""
    for idx, sec in enumerate(sections):
        band = bands[idx % 2]
        out += f'<section class="section {band}" id="{sec["id"]}">\n  <div class="container">\n'
        out += '    <div class="section-header">\n'
        if sec["number"]:
            n = sec["number"].zfill(2) if len(sec["number"]) == 1 else sec["number"]
            out += f'      <span class="section-number">{n}</span>\n'
        out += f'      <h2>{sec["title"]}</h2>\n    </div>\n'
        for item in sec["content"]:
            if item[0] == "text":
                rendered = render_inline(item[1])
                cls = "note" if item[1].startswith("Note:") else "section-text"
                out += f'    <p class="{cls}">{rendered}</p>\n'
            elif item[0] == "sub":
                _, num, title, sub_id = item
                out += f'    <div class="subsection" id="sub-{sub_id}"><h3>'
                if num:
                    out += f'<span class="sub-number">{num}</span> '
                out += f'{title}</h3></div>\n'
            elif item[0] == "table":
                out += f'    {item[1]}\n'
        out += '  </div>\n</section>\n\n'
    return out


def count_stats(md: str) -> dict[str, int]:
    rows = code = 0
    secs = 0
    in_t = False
    is_hdr = True
    for line in md.split("\n"):
        if line.startswith("## "):
            secs += 1
        if line.strip().startswith("|") and "|" in line.strip()[1:]:
            if is_sep(line):
                continue
            if not in_t:
                in_t = True; is_hdr = True
            elif is_hdr:
                is_hdr = False
            else:
                rows += 1
                if "github" in line.lower():
                    code += 1
        else:
            if in_t:
                in_t = False; is_hdr = True
    return {"entries": rows, "sections": secs, "open_source": code}


# ── Page template ─────────────────────────────────────────────────────

def build(md: str) -> str:
    detail_map = scan_details()
    detail_count = build_detail_pages(detail_map)
    sidebar_html, sections, date_str = parse_md(md, detail_map)
    stats = count_stats(md)
    sections_html = render_sections(sections)

    return f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Contact-Rich Dexterous Manipulation Survey</title>
<meta name="description" content="Interactive survey: {stats['entries']}+ papers on dexterous manipulation, force-aware VLAs, impedance learning, and benchmarks (2018-2026).">
<meta property="og:title" content="Contact-Rich Dexterous Manipulation Survey">
<meta property="og:description" content="Interactive survey covering {stats['entries']}+ papers across dexterous manipulation, force-aware VLAs, and impedance control.">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable.min.css">
<link rel="stylesheet" href="style.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🤖</text></svg>">
</head>
<body>

<div class="utility-strip">
  <div class="container utility-inner">
    <span class="utility-label">Research Survey &mdash; Last updated {date_str}</span>
    <div class="utility-actions">
    <button class="font-toggle" id="font-toggle" aria-label="Toggle font size" title="Font size">
      <span id="font-label">A+</span>
    </button>
    <button class="theme-toggle" id="theme-toggle" aria-label="Toggle theme">
      <svg class="icon-sun" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>
      <svg class="icon-moon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"/></svg>
    </button>
    </div>
  </div>
</div>

<nav class="nav-bar" id="nav-bar">
  <div class="container nav-inner">
    <a href="#" class="nav-logo">DexManip Survey</a>
    <div class="nav-actions">
      <div class="global-search-wrap">
        <svg class="search-icon" viewBox="0 0 20 20" fill="currentColor" width="16" height="16"><path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd"/></svg>
        <input type="search" id="global-search" class="global-search" placeholder="Search all tables...">
      </div>
    </div>
  </div>
</nav>

<section class="hero-section">
  <div class="container">
    <div class="hero-card">
      <div class="chevron chevron-left"></div>
      <div class="hero-content">
        <h1>Contact-Rich<br>Dexterous Manipulation</h1>
        <p class="hero-subtitle">A Comprehensive Survey</p>
        <p class="hero-desc">Papers, repos, and datasets for dexterous manipulation, force-aware VLAs, impedance learning, RL policies, and related benchmarks.</p>
        <div class="hero-stats">
          <div class="stat"><span class="stat-number">{stats['entries']}+</span><span class="stat-label">Entries</span></div>
          <div class="stat"><span class="stat-number">{stats['sections']}</span><span class="stat-label">Sections</span></div>
          <div class="stat"><span class="stat-number">{stats['open_source']}+</span><span class="stat-label">Open Source</span></div>
          <div class="stat"><span class="stat-number">{detail_count}</span><span class="stat-label">Detailed Reviews</span></div>
        </div>
      </div>
      <div class="chevron chevron-right"></div>
    </div>
  </div>
</section>

<div class="filter-band band-cloud">
  <div class="container">
    <div class="filter-row">
      <div class="filter-group">
        <span class="filter-label">Filter:</span>
        <button class="chip chip-active" data-filter="all">All</button>
        <button class="chip" data-filter="code">Has Code</button>
        <button class="chip" data-filter="weights">Has Weights</button>
      </div>
      <div class="filter-group">
        <span class="filter-label">Hand:</span>
        <button class="chip chip-toggle" data-hand="dex">Dexterous</button>
        <button class="chip chip-toggle" data-hand="gripper">Gripper</button>
        <button class="chip chip-toggle" data-hand="bimanual">Bimanual</button>
        <button class="chip chip-toggle" data-hand="fullbody">Full Body</button>
      </div>
      <select class="year-select" id="year-filter">
        <option value="">All Years</option>
        <option value="2026">2026</option>
        <option value="2025">2025</option>
        <option value="2024">2024</option>
        <option value="2023">2023</option>
        <option value="older">2022 &amp; earlier</option>
      </select>
    </div>
  </div>
</div>

<div class="layout">
  <aside class="sidebar" id="sidebar">
    <nav class="sb-nav">
      {sidebar_html}
    </nav>
  </aside>
  <div class="main-content">
    {sections_html}
  </div>
</div>

<footer class="footer-dark">
  <div class="container">
    <div class="footer-content">
      <div class="footer-main">
        <h3>Contact-Rich Dexterous Manipulation Survey</h3>
        <p>An interactive survey of dexterous manipulation, force-aware VLAs, impedance learning, and related benchmarks.</p>
      </div>
      <div class="footer-links">
        <h4>Resources</h4>
        <a href="https://github.com/OpenHelix-Team/Awesome-Force-Tactile-VLA" target="_blank" rel="noopener">Awesome-Force-Tactile-VLA</a>
        <a href="https://github.com/Physical-Intelligence/openpi" target="_blank" rel="noopener">OpenPI (pi0)</a>
        <a href="https://github.com/NVIDIA/Isaac-GR00T" target="_blank" rel="noopener">Isaac-GR00T</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>GitHub links and weight availability were checked as of {date_str}; links may become stale.</span>
    </div>
  </div>
</footer>

<div class="detail-panel" id="detail-panel">
  <div class="dp-header">
    <div class="dp-tabs" id="dp-tabs"></div>
    <div class="dp-actions">
      <button class="dp-btn" id="dp-minimize" title="Minimize">
        <svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 8h10"/></svg>
      </button>
      <button class="dp-btn" id="dp-maximize" title="Maximize">
        <svg class="icon-max" width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="3" width="10" height="10" rx="1.5"/></svg>
        <svg class="icon-restore" width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="5" y="1.5" width="9" height="9" rx="1.5"/><rect x="2" y="5.5" width="9" height="9" rx="1.5"/></svg>
      </button>
      <button class="dp-btn" id="dp-close-all" title="Close all">
        <svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4l8 8M12 4l-8 8"/></svg>
      </button>
    </div>
  </div>
  <div class="dp-body" id="dp-body"></div>
</div>

<script src="app.js"></script>
</body>
</html>"""


def main():
    md = SURVEY_PATH.read_text(encoding="utf-8")
    html = build(md)
    DOCS_DIR.mkdir(exist_ok=True)
    OUTPUT_PATH.write_text(html, encoding="utf-8")
    detail_count = len(list(DETAILS_OUT.rglob("*.html"))) if DETAILS_OUT.exists() else 0
    print(f"Built -> {OUTPUT_PATH} ({len(html):,} bytes, {detail_count} detail pages)")


if __name__ == "__main__":
    main()
