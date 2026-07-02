#!/usr/bin/env python3
"""Convert the Berwick Saga markdown guide into a static HTML site under html/."""
import os
import re
import html

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "html")

# ---------------------------------------------------------------- inline
_CODE = []


def _stash_code(m):
    _CODE.append(html.escape(m.group(1)))
    return f"\x00CODE{len(_CODE) - 1}\x00"


def rewrite_link(url):
    # leave external / anchor links alone; rewrite .md -> .html
    if re.match(r"^[a-z]+://", url) or url.startswith("#") or url.startswith("mailto:"):
        return url
    base, _, frag = url.partition("#")
    if base.endswith(".md"):
        base = base[:-3] + ".html"
    return base + (("#" + frag) if frag else "")


def inline(text):
    _CODE.clear()
    # pull code spans out first so their contents aren't further parsed
    text = re.sub(r"`([^`]+)`", _stash_code, text)
    text = html.escape(text, quote=False)
    # images (wrapped in a link so clicking opens the full-size image)
    text = re.sub(
        r"!\[([^\]]*)\]\(([^)]+)\)",
        lambda m: (
            f'<a href="{rewrite_link(m.group(2))}" target="_blank">'
            f'<img src="{rewrite_link(m.group(2))}" alt="{m.group(1)}"></a>'
        ),
        text,
    )
    # links
    text = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: f'<a href="{rewrite_link(m.group(2))}">{m.group(1)}</a>',
        text,
    )
    # bold then italic
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    # restore code
    text = re.sub(r"\x00CODE(\d+)\x00", lambda m: f"<code>{_CODE[int(m.group(1))]}</code>", text)
    return text


# ---------------------------------------------------------------- table
def parse_alignments(sep_cells):
    aligns = []
    for c in sep_cells:
        c = c.strip()
        left, right = c.startswith(":"), c.endswith(":")
        if left and right:
            aligns.append("center")
        elif right:
            aligns.append("right")
        elif left:
            aligns.append("left")
        else:
            aligns.append("")
    return aligns


def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def render_table(lines):
    header = split_row(lines[0])
    aligns = parse_alignments(split_row(lines[1]))
    out = ['<div class="table-wrap"><table>', "<thead><tr>"]
    for i, h in enumerate(header):
        a = aligns[i] if i < len(aligns) else ""
        style = f' style="text-align:{a}"' if a else ""
        out.append(f"<th{style}>{inline(h)}</th>")
    out.append("</tr></thead><tbody>")
    for row in lines[2:]:
        cells = split_row(row)
        out.append("<tr>")
        for i, c in enumerate(cells):
            a = aligns[i] if i < len(aligns) else ""
            style = f' style="text-align:{a}"' if a else ""
            out.append(f"<td{style}>{inline(c)}</td>")
        out.append("</tr>")
    out.append("</tbody></table></div>")
    return "\n".join(out)


# ---------------------------------------------------------------- block
def is_table_sep(line):
    return bool(re.match(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)+\|?\s*$", line))


def convert(md):
    lines = md.split("\n")
    out = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # heading
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            level = len(m.group(1))
            out.append(f"<h{level}>{inline(m.group(2).strip())}</h{level}>")
            i += 1
            continue

        # table: current line has a pipe and next line is a separator
        if "|" in line and i + 1 < n and is_table_sep(lines[i + 1]):
            tbl = [line, lines[i + 1]]
            i += 2
            while i < n and "|" in lines[i] and lines[i].strip():
                tbl.append(lines[i])
                i += 1
            out.append(render_table(tbl))
            continue

        # unordered list
        if re.match(r"^\s*[-*]\s+", line):
            out.append("<ul>")
            while i < n and re.match(r"^\s*[-*]\s+", lines[i]):
                item = re.sub(r"^\s*[-*]\s+", "", lines[i])
                out.append(f"<li>{inline(item)}</li>")
                i += 1
            out.append("</ul>")
            continue

        # ordered list
        if re.match(r"^\s*\d+\.\s+", line):
            out.append("<ol>")
            while i < n and re.match(r"^\s*\d+\.\s+", lines[i]):
                item = re.sub(r"^\s*\d+\.\s+", "", lines[i])
                out.append(f"<li>{inline(item)}</li>")
                i += 1
            out.append("</ol>")
            continue

        # horizontal rule
        if re.match(r"^\s*([-*_])(\s*\1){2,}\s*$", line):
            out.append("<hr>")
            i += 1
            continue

        # paragraph: gather consecutive plain lines
        para = [stripped]
        i += 1
        while i < n and lines[i].strip() and not re.match(
            r"^(#{1,6}\s|\s*[-*]\s+|\s*\d+\.\s+)", lines[i]
        ) and not ("|" in lines[i] and i + 1 < n and is_table_sep(lines[i + 1])):
            para.append(lines[i].strip())
            i += 1
        out.append(f"<p>{inline(' '.join(para))}</p>")

    return "\n".join(out)


PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="{css}">
</head>
<body>
<main>
{body}
</main>
</body>
</html>
"""


def title_of(md, fallback):
    m = re.search(r"^#\s+(.*)$", md, re.M)
    return html.unescape(re.sub(r"[*`]", "", m.group(1)).strip()) if m else fallback


def rel_css(rel_path):
    depth = rel_path.count(os.sep)
    return ("../" * depth) + "style.css"


CSS = """:root {
  --bg: #faf8f3;
  --surface: #ffffff;
  --text: #2b2b2b;
  --muted: #6b6257;
  --accent: #8a5a2b;
  --accent-soft: #f0e6d6;
  --border: #e4dccd;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #1a1815;
    --surface: #232019;
    --text: #e8e2d6;
    --muted: #a89f8f;
    --accent: #d9a066;
    --accent-soft: #2e281f;
    --border: #3a352b;
  }
}
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  font-size: 17px;
  line-height: 1.65;
}
main {
  max-width: 780px;
  margin: 0 auto;
  padding: 1.25rem 1.1rem 4rem;
}
h1, h2, h3, h4 { line-height: 1.25; font-weight: 700; }
h1 {
  font-size: 1.75rem;
  margin: 0.4em 0 0.6em;
  color: var(--accent);
}
h2 {
  font-size: 1.3rem;
  margin: 1.8em 0 0.5em;
  padding-bottom: 0.25em;
  border-bottom: 2px solid var(--border);
}
h3 { font-size: 1.12rem; margin: 1.4em 0 0.4em; color: var(--muted); }
p { margin: 0.7em 0; }
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
ul, ol { padding-left: 1.35em; margin: 0.6em 0; }
li { margin: 0.28em 0; }
img {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 1em auto;
  border-radius: 8px;
  border: 1px solid var(--border);
  cursor: zoom-in;
}
code {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.88em;
  background: var(--accent-soft);
  padding: 0.12em 0.38em;
  border-radius: 5px;
}
hr { border: none; border-top: 1px solid var(--border); margin: 2em 0; }
.table-wrap { overflow-x: auto; margin: 1em 0; -webkit-overflow-scrolling: touch; }
table {
  border-collapse: collapse;
  width: 100%;
  font-size: 0.92rem;
}
th, td {
  border: 1px solid var(--border);
  padding: 0.4em 0.6em;
  text-align: left;
}
th { background: var(--accent-soft); font-weight: 700; }
tr:nth-child(even) td { background: color-mix(in srgb, var(--surface) 60%, var(--bg)); }
/* back-to-menu link (first paragraph link) */
main > p:first-of-type a { font-weight: 600; }
@media (max-width: 480px) {
  body { font-size: 16px; }
  main { padding: 1rem 0.85rem 3rem; }
  h1 { font-size: 1.5rem; }
  th, td { padding: 0.35em 0.45em; }
}
"""


def main():
    # Image assets are the one canonical copy and live under html/ (the served
    # tree); they are NOT duplicated in the source. So clean only the files this
    # build generates (stale .html / style.css) and leave everything else — most
    # importantly the images/ folders — untouched.
    os.makedirs(OUT, exist_ok=True)
    for dirpath, _dirnames, filenames in os.walk(OUT):
        for fn in filenames:
            if fn.endswith(".html") or fn == "style.css":
                os.remove(os.path.join(dirpath, fn))

    with open(os.path.join(OUT, "style.css"), "w") as f:
        f.write(CSS)

    md_files = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        if OUT in dirpath:
            continue
        for fn in filenames:
            if fn.endswith(".md"):
                rel = os.path.relpath(os.path.join(dirpath, fn), ROOT)
                # README.md documents the build itself; it is not guide content.
                if rel == "README.md":
                    continue
                md_files.append(rel)

    count = 0
    for rel in md_files:
        with open(os.path.join(ROOT, rel)) as f:
            md = f.read()
        out_rel = rel[:-3] + ".html"
        body = convert(md)
        title = title_of(md, os.path.basename(rel))
        page = PAGE.format(title=html.escape(title), css=rel_css(out_rel), body=body)
        dest = os.path.join(OUT, out_rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w") as f:
            f.write(page)
        count += 1

    # Images are not copied: they already live under html/ as the single
    # canonical copy (see the cleanup note in main()).

    print(f"Converted {count} pages -> {OUT}")


if __name__ == "__main__":
    main()
