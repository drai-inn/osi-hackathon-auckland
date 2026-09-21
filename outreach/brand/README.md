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
| [`uoa-logo-light.png`](uoa-logo-light.png) | Waipapa Taumata Rau · University of Auckland, navy on light | Footers, poster base, the site footer |
| `uoa-logo-dark.png` | **Not yet supplied**, reversed version for dark surfaces | Hero sections. Until we have it, dark surfaces carry the motif and the name set in type, not the crest |
| [`uoa-motif.png`](uoa-motif.png) | The cyan motif, as supplied (36 × 18) | The canonical asset |
| [`uoa-motif.svg`](uoa-motif.svg) | Faithful redraw of the same geometry | Inline and scalable use, the raster is 36 px wide and will not enlarge |

### Using the motif

Six sheared bars in two opposed rows. It reads as a woven pattern, and it's small by design: a
lead-in before a heading, or a separator between sections.

**It sits on its own line, with clear air above and below it.** Nothing inline beside it, no text
on the same line, no other decorative element next to it. It offsets the text that follows, and
that's all it does.

```html
<img src="brand/uoa-motif.svg" alt="" width="36" height="18">
<h2>The heading it offsets</h2>
```

Not a background, not a texture, not scaled up to hero size, and not more than one per section.

**Don't restyle it.** Not recoloured, not rearranged, not reproportioned, not animated. It's an
institutional mark with design heritage that isn't ours to reinterpret, and the right way to use it
is exactly as supplied.

The SVG is a redraw only because the supplied raster is 36 px wide and will not scale. Geometry and
colour match. **Replace it with the official vector** from UoA brand resources when we have one.

### On the imagery we invented, and the line between

Earlier in this project we deliberately avoided koru, fern and similar forms: they carry cultural
meaning that is not ours to borrow for a poster, and using them casually would be worse than using
nothing.

That reasoning still holds, and the UoA motif is not an exception to it, it is the other side of
it. It is the University's own mark, supplied to us for use as a University event, and we use it
**unmodified and in its own colour**. Inventing our own variation on it would be exactly the thing
we said we would not do.

Our two invented marks stay deliberately neutral: the Southern Cross is a constellation, and the
paired-pocket diagram is our science drawn literally.

## Marks

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
