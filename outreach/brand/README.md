# Brand, the global event, co-branded with Waipapa Taumata Rau

Two families to honour, and they cooperate better than they had any right to.

**The global event** supplies the palette, the typography and the overall feel, our collateral
should read as *part of* the OSI Hackathon, not adjacent to it. Tokens read from
[llmhackathon.github.io](https://llmhackathon.github.io/) on 2026-09-19 and recorded verbatim in
[`tokens.css`](tokens.css).

**The University of Auckland** supplies the institutional identity: the Waipapa Taumata Rau
wordmark and crest, and the cyan motif used as a lead-in or separator.

The happy accident:

| | UoA | Global event | |
| --- | --- | --- | --- |
| Deep navy | `#0C0C48` | `#0D1226` (`--void-deep`) | A shade apart |
| Bright cyan | `#00D3F6` | `#5EC9E8` (`--sp-cyan`) | Same hue, different saturation |

So we use **OSI's palette for surfaces and type, and UoA's marks and cyan for identity**, and have
aligned our `--south` accent to the UoA cyan so there is one accent rather than two competing.

---

## What we inherited

| Role | Token | Value |
| --- | --- | --- |
| Deep background | `--void` / `--void-deep` | `#141C36` / `#0D1226` |
| Panel on dark | `--void-panel` | `#1D2A4F` |
| Light backgrounds | `--bg-top` → `--bg-bot` | `#F6F6F2` → `#DFE3EE` |
| Body ink | `--ink` | `#1E2A4A` |
| **Action** | `--action` | `#3F5FBC`, indigo. Buttons, links, primary emphasis |
| Accent | `--gold` | `#C79A4D`, used sparingly by them, sparingly by us |
| Text on dark | `--on-void` | `#EEF1FB` |
| Display type | `--font-display` | **Inter**, 800 weight for headings, tight tracking |
| Mono | `--font-mono` | Martian Mono |
| Radius | `--radius-sm/md` | 4px / 8px, restrained, not pill-shaped |

The overall feel is **dark navy, indigo action, Inter at heavy weight, tight letter-spacing, small
radii.** Serious, modern, not playful.

## The OSI Hackathon's marks

The global event has an identity of its own, and where we point at them we use **theirs**, not our
interpretation of it. All of it is reproduced from
[llmhackathon.github.io](https://llmhackathon.github.io/) at their own proportions and colour
values.

| Mark | What it is |
| --- | --- |
| **The lockup** | Five spectral bars at a `10:16:7:18:12` height ratio, aligned to a baseline, then the wordmark **OSI Hackathon** in Inter 700 |
| **The emission spectrum** | Seven lines at fixed wavelengths — the hydrogen Balmer series (α, β, γ, δ), magnesium, and the sodium D doublet. It opens the global-event panel on the landing page and the [`osi-band.png`](osi-band.png) strip |
| **The edition tile** | A periodic-table tile: `26` / `Oct`, the symbol **Osi**, the name, the dates. Paper white in every context, so its ink is fixed rather than themed |

Their spectral palette, used **only** for their marks:

| Token | Value |
| --- | --- |
| `--sp-violet` | `#8B7CF6` |
| `--sp-blue` | `#8AA0E6` |
| `--sp-cyan` | `#5EC9E8` |
| `--sp-green` | `#3FA3C4` |
| `--sp-amber` | `#C79A4D` |
| `--sp-red` | `#A66F44` |

Three rules, and they are the same ones we apply to the University's lockup:

1. **Never recoloured.** The bars are violet-to-red because that is what they are. The poster arch
   used to carry three ascending bars in our cyan, which was us inventing a mark they already had.
2. **Never invented.** If a surface needs something of theirs that is not here, take it from their
   site rather than drawing something in the spirit of it.
3. **Their section, their palette.** The global-event panel is the one place on the landing page
   that uses a palette other than ours, and that is the point of it.

[`osi-band.html`](osi-band.html) → [`osi-band.png`](osi-band.png), rebuilt with `make osi`, carries
the lockup, the spectrum and the tile on their own dark ground, so one file reads correctly on
either GitHub theme. It is rendered to PNG rather than shipped as SVG because GitHub will not load
a webfont inside an `<img>`, and the wordmark is Inter.

**Check these against their site before a release.** They are someone else's marks and can change
without us hearing about it.

## What we added, two tokens, and that is the limit

| Token | Value | Use |
| --- | --- | --- |
| `--south` | `#00D3F6` | The Auckland accent, the UoA cyan. Southern Cross, the one highlighted atom in the pocket diagram, the odd badge. Little else |
| `--south-soft` | `#5EC9E8` | OSI's cyan, for small text on dark where the full-saturation cyan glares |
| `--target` / `--counter` | `#8AA0E6` / `#8B7CF6` | The two pockets in our diagrams, deliberately close in hue, because telling them apart is the whole problem |

`--target`/`--counter` are promoted from OSI's own `--sp-*` spectrum, so they are in-family by
construction. `--south` is UoA's cyan, which lands within a few degrees of hue of OSI's.

**Resist adding more.** The point of adopting their palette is that we look like the same event.

## University of Auckland assets

| File | What | Use |
| --- | --- | --- |
| [`uoa-logo-navy.png`](uoa-logo-navy.png) | Waipapa Taumata Rau · University of Auckland, navy | Light surfaces |
| [`uoa-logo-white.png`](uoa-logo-white.png) | The same lockup, reversed | Dark surfaces |
| [`uoa-motif.png`](uoa-motif.png) | The cyan motif, as supplied (36 × 18) | The canonical asset |
| [`uoa-motif.svg`](uoa-motif.svg) | Faithful redraw of the same geometry | Inline and scalable use; the raster is 36 px wide and will not enlarge |

## The favicon

| File | What | Rebuild |
| --- | --- | --- |
| [`favicon.svg`](favicon.svg) | The crest, navy on light and reversed on dark | Hand-edited; see below |
| `favicon-{16,32}.png` · `apple-touch-icon.png` | Flat navy tiles with the reversed crest | `make icons` |

**A favicon is one of the three places the brand rules allow the crest to leave the wordmark**, so
this is the exception rather than a liberty. The University's own site serves the crest in navy on
transparent, and that is the source this is adapted from — at 16 px in a dark tab strip it is navy
on near-black, so the SVG here carries the same light/dark switch as the lockup and the raster
fallbacks sit on a solid navy tile. Both are approved treatments of the mark; neither invents one.

If UoA reissue their favicon, re-fetch it and reapply the `.crest` class and the `<style>` block.

## Rendered cards

| File | Size | Rebuild | Where it goes |
| --- | --- | --- | --- |
| [`readme-banner.png`](readme-banner.png) | 1200 × 500 | `make banner` | The top of [README.md](../../README.md) |
| [`social-preview.png`](social-preview.png) | 1280 × 640 | `make social` | **Settings → General → Social preview.** It cannot be set through the API, so it is uploaded by hand |

Both are rendered from the `.html` beside them rather than shipped as SVG, because Inter has to be
guaranteed wherever the image is unfurled and nothing loads a webfont inside an `<img>`.

The social card keeps everything that matters inside a **40 px border**, since every service that
unfurls a link crops it differently. The padding is 64 px, which leaves room to spare.

Both are the supplied files at half resolution, 1000 × 474, **with their transparent margin left
on**. That margin is the clear space: nothing else goes inside it, and nothing here crops it out.

### Placement

**Top left of the page, with the title or key message left-aligned under it.** That is the rule for
standard applications, and everything here follows it: the landing page hero, the README banner, the
poster, the one-pager. A designer may place it differently for a specific reason; absent that
reason, top left.

### One UoA

Faculties, service divisions, departments, schools and research centres **are not sub-brands and do
not get their own lock-ups.** An internal division name can appear as content, in type, when it adds
something for the reader. Where space is short, the University logo alone is the identifier.

### The crest stays with the wordmark

Do not decouple them. The only exceptions are a favicon, a social-media profile picture, and
merchandise approved case by case by the Brand Manager. Nothing in this repo qualifies.

### Light and dark

The mark is never recoloured, so a change of surface is a change of file. Where the surface is dark
in every mode — the site hero, the poster, the banner — use `uoa-logo-white.png` directly. Where the
surface follows the reader's theme, switch:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="brand/uoa-logo-white.png">
  <img src="brand/uoa-logo-navy.png" width="230" alt="Waipapa Taumata Rau, University of Auckland">
</picture>
```

GitHub honours that in a README. The landing page carries the CSS equivalent as `.uoa-logo-swap`.

### Using the motif

Six sheared bars in two opposed rows. It reads as a woven pattern, and it's small by design: a
lead-in before a heading, or a separator between sections.

**It sits on its own line, with clear air above and below it.** Nothing inline beside it, no text on
the same line, no other decorative element next to it. It offsets the text that follows, and that's
all it does.

```html
<img src="brand/uoa-motif.svg" alt="" width="36" height="18">
<h2>The heading it offsets</h2>
```

Not a background, not a texture, not scaled up to hero size, and not more than one per section.

**Where it appears:** before every section heading on the landing page, and between sections in the
README. It is not on the poster or the banner, because those have no section structure for it to
lead, and their one top-left slot now carries the lockup.

### What was removed on 22 Sep

The small linked-dot Southern Cross that sat in front of "Auckland site" on the landing page. It
read as a molecule rather than a constellation, and the lockup now opens the page instead.
`mark-southern-cross.svg` stays in here as an event mark, unused on the public page.

### [`mark-pocket-pair.svg`](mark-pocket-pair.svg), the topic

Two near-identical pocket graphs side by side, differing at exactly one position, highlighted in
`--south`. It is a literal picture of the problem: same shape, same ligand, one atom of difference,
and the entire project is about whether that difference is detectable.

Uses `currentColor`, so it inherits the surrounding text colour and works on light or dark.

### [`mark-southern-cross.svg`](mark-southern-cross.svg), the place

Crux. Four bright stars and the faint fifth, on the two crossing lines. Simple, geometric, and it
sits comfortably beside the pocket diagram. Used sparingly, and never next to the UoA motif.

### A note on the imagery we did not use

We deliberately avoided koru, fern and other Māori visual forms. They carry cultural meaning that
is not ours to borrow for a poster, and using them casually would be worse than using nothing. If
we later want visual identity that genuinely speaks to Aotearoa, that is a conversation to have
properly with the right people, not a design decision to make in an afternoon.

The Southern Cross is a constellation and it is what we can honestly claim: where we are, and why
we go first.

## Applying it

```html
<link rel="stylesheet" href="brand/tokens.css">
<style> body{ background:var(--void); color:var(--on-void); font-family:var(--font-display); } </style>
```

Inter is on Google Fonts; Martian Mono too. Both degrade acceptably to Helvetica/Menlo, and the
poster is built to print correctly either way.

**Applied in:** `../poster.html` · [`../site/index.html`](../site/index.html)

## Rules of thumb

1. **Dark for impact, light for reading.** Posters and hero sections on `--void`; anything with more
   than a paragraph of text on `--bg-top`.
2. **One accent per surface.** `--action` for what people should click; `--south` (the UoA cyan) for
   what makes us the Auckland hub. Not both competing.
3. **Heavy headings, tight tracking.** Inter 800, `letter-spacing:-.02em`. Matches theirs.
4. **Small radii.** 4px, 8px. Nothing rounder, it reads as a different product.
5. **No gradients or glows in the chrome, and no stock photography.** Buttons, panels, rules and type stay flat, the way the global event's do. The generated imagery in [`../imagery/`](../imagery/) is the exception and is full of both — it sits behind things rather than being one of them.
6. **The UoA motif gets clear air.** Own line, nothing inline beside it, one per section at most.

## Type weight

**Headings run light, not bold.** The inherited OSI spec sets headings in Inter 800. We use
**Inter 300 at a larger size** instead, so the words carry rather than the weight.

Small caps labels — eyebrows, scale labels, section heads — stay at 700 or 800, where the weight is
doing legibility work at 11–12px.

The font link has to load 200 and 300 or the browser synthesises a fake light and it looks wrong.
