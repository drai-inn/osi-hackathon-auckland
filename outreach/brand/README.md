# Brand — aligned with the global event

Our collateral should read as **part of the OSI Hackathon**, not adjacent to it. So we adopt the
global site's palette and typography wholesale and add almost nothing.

Source: [llmhackathon.github.io](https://llmhackathon.github.io/), tokens read from its stylesheet
on 2026-09-19 and recorded verbatim in [`tokens.css`](tokens.css).

---

## What we inherited

| Role | Token | Value |
| --- | --- | --- |
| Deep background | `--void` / `--void-deep` | `#141C36` / `#0D1226` |
| Panel on dark | `--void-panel` | `#1D2A4F` |
| Light backgrounds | `--bg-top` → `--bg-bot` | `#F6F6F2` → `#DFE3EE` |
| Body ink | `--ink` | `#1E2A4A` |
| **Action** | `--action` | `#3F5FBC` — indigo. Buttons, links, primary emphasis |
| Accent | `--gold` | `#C79A4D` — used sparingly by them, sparingly by us |
| Text on dark | `--on-void` | `#EEF1FB` |
| Display type | `--font-display` | **Inter**, 800 weight for headings, tight tracking |
| Mono | `--font-mono` | Martian Mono |
| Radius | `--radius-sm/md` | 4px / 8px — restrained, not pill-shaped |

The overall feel is **dark navy, indigo action, Inter at heavy weight, tight letter-spacing, small
radii.** Serious, modern, not playful.

## What we added — two tokens, and that is the limit

| Token | Value | Use |
| --- | --- | --- |
| `--south` | `#5EC9E8` | The Auckland hub accent. The Southern Cross mark, the "two days ahead" badge. **Nothing else** |
| `--target` / `--counter` | `#8AA0E6` / `#8B7CF6` | The two pockets in our diagrams — deliberately close in hue, because telling them apart is the whole problem |

Both are promoted from their own `--sp-*` spectrum, so they are in-family by construction.

**Resist adding more.** The point of adopting their palette is that we look like the same event.

## Marks

### [`mark-pocket-pair.svg`](mark-pocket-pair.svg) — the topic

Two near-identical pocket graphs side by side, differing at exactly one position, highlighted in
`--south`. It is a literal picture of the problem: same shape, same ligand, one atom of difference,
and the entire project is about whether that difference is detectable.

Uses `currentColor`, so it inherits the surrounding text colour and works on light or dark.

### [`mark-southern-cross.svg`](mark-southern-cross.svg) — the place

Crux. Four bright stars and the faint fifth, on the two crossing lines. Simple, geometric, sits
comfortably beside the pocket motif, and carries the thing that is actually true about us: we are a
southern-hemisphere hub running two days ahead of the world.

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

**Applied in:** [`../poster.html`](../poster.html) · [`../site/index.html`](../site/index.html)

## Rules of thumb

1. **Dark for impact, light for reading.** Posters and hero sections on `--void`; anything with more
   than a paragraph of text on `--bg-top`.
2. **One accent per surface.** `--action` for what people should click; `--south` for the one thing
   that makes us the Auckland hub. Not both competing.
3. **Heavy headings, tight tracking.** Inter 800, `letter-spacing:-.02em`. Matches theirs.
4. **Small radii.** 4px, 8px. Nothing rounder — it reads as a different product.
5. **No gradients, no glows, no stock photography.** Neither do they.
