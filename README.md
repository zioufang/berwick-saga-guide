# Berwick Saga Guide — Build

This repository is a guide written in Markdown that is compiled into a small
static HTML site for comfortable reading in a browser (including on mobile).

## Sources

The information in this guide is drawn from:

- **[Serenes Forest wiki](https://wiki.serenesforest.net/index.php/Berwick_Saga)** —
  data pages for calculations, item creation, item locations, civilian
  requests, and more.
- **"Your Berwick Saga Companion"** by user **OceanGale**, posted in
  [/r/fireemblem](https://www.reddit.com/r/fireemblem/).

## Layout

```
index.md              Home page (table of contents)
character_index.md    Character list
characters/*.md       One page per character
chapters/*.md         One page per map/chapter
chapters/images/*.png Map screenshots
food.md, furniture.md, item_creation.md,
civilian_requests.md, experience.md, calculations.md
                      Reference pages
build_html.py         The Markdown -> HTML converter
html/                 Generated output (do not edit by hand)
```

Edit the Markdown files only. Everything under `html/` is generated.

## Generating the HTML

Run the build script with Python 3 (no third-party packages required):

```
python3 build_html.py
```

This regenerates the entire `html/` directory from scratch. The output is
static — open `html/index.html` directly in a browser, or serve the folder
with any static file server.

## How the conversion works

`build_html.py` is a self-contained Markdown-to-HTML converter (no external
libraries). Each run:

1. **Clears and recreates `html/`**, then writes a single shared stylesheet,
   `html/style.css` (warm light/dark theme, responsive tables, mobile-friendly
   spacing).
2. **Walks the repository** for every `.md` file except this `README.md`, which
   documents the build rather than being guide content.
3. **Converts each file** to HTML, mirroring the source layout — e.g.
   `chapters/ch01-main-a-reason-to-fight.md` becomes
   `html/chapters/ch01-main-a-reason-to-fight.html`. `index.md` becomes
   `html/index.html`, so the site opens on the home page by default.
4. **Rewrites internal links** so `*.md` targets point at the generated
   `*.html` files; external links and anchors are left untouched.
5. **Copies image assets** — any `images/` directory is copied into the
   corresponding location under `html/`.

Supported Markdown features: headings, paragraphs, **bold**/*italic*,
`inline code`, links, images, ordered and unordered lists, and tables with
column alignment. Each page's `<title>` is taken from its first `#` heading.

## Adding or editing content

- To add a page, create a new `.md` file in the appropriate directory, link to
  it from `index.md` (and `character_index.md` for characters), then rerun the
  build.
- Use a relative link ending in `.md`; the build rewrites it to `.html`.
- Start each page with a `# Heading` and a `[← Home](index.md)` (or
  `[← Home](../index.md)` from a subdirectory) back-link, matching the existing
  pages.
