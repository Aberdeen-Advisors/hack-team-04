# Aberdeen Advisors Branding Guide (Portable)

A single, self-contained specification of the Aberdeen Advisors brand identity for PowerPoint, Word, and Excel deliverables. Everything needed to style a document on-brand is in this one file — no external tooling, scripts, or platform-specific machinery required.

The goal is consistency: every Aberdeen deliverable should feel like it came from the same hand.

---

## How to use this file with any LLM

1. **Paste the whole file** into your system prompt, custom instructions, project context, or the first message of a chat (ChatGPT, Gemini, Copilot, Claude, or any other assistant).
2. **Then make your request** — "draft a client proposal deck outline", "format this memo", "build a revenue model workbook" — and instruct the model to follow the Aberdeen specs above it.
3. **Ask the model to self-check** against the [QA checklist](#qa-checklist) at the end before it hands anything back.

### About the binary template

The authoritative PowerPoint template lives in this repository at:

```
.claude/skills/aberdeen-branding/assets/aberdeen_template.pptx
```

That file is **required for pixel-accurate decks**. It contains the slide master, all 16 named layouts, the embedded Aberdeen logo, the baked-in color theme, and the pre-built reference exhibits. It is a binary artifact and cannot be flattened into markdown.

**Without it, an LLM can only approximate the brand** by applying the specs in this document manually — correct colors, fonts, sizes, and structure, but not the exact master geometry, the diagonal motif, or the logo artwork. If you need a genuine Aberdeen deck, download the `.pptx` from this repo and start from it. If you only have this markdown file, say so up front and treat the output as a styled approximation rather than a template-true deliverable.

### Core principle: the template is the source of truth

**Do not invent. Do not improvise. Match.**

When something seems missing (a layout you wish existed, a color you'd like to add), the answer is to reuse what exists or simplify the content — never to add custom styling that doesn't appear in the source.

### Don't over-design

Aberdeen's brand is restrained and professional. Most slides are a teal accent line at the top, a clear title, and content. No decorative bars, no full-width colored stripes, no busy backgrounds outside of the title and divider slides. The template's standard content slides show how much whitespace and restraint the brand expects — replicate that energy in Word and Excel too.

---

## Brand Identity

Applies to every Aberdeen deliverable regardless of file type.

### Color palette

#### Primary colors

| Name | Hex | Intended use |
|------|-----|--------------|
| Aberdeen Blue | `#09375F` | Primary, dominant color. Headings, title/divider backgrounds, table header rows, chart series 1, section headers. |
| Aberdeen Teal | `#44B0B1` | Accent and highlights only. Thin rules, accent lines, label columns, kicker boxes, input-cell tinting, chart series 2. |
| Onyx | `#404040` | Body text on light backgrounds. Never use pure black for body copy. |
| White | `#FFFFFF` | Backgrounds; text on Aberdeen Blue. |

#### Secondary colors

Use sparingly — charts, data visualization, and categorical distinctions only.

| Name | Hex | Intended use |
|------|-----|--------------|
| Deep Sky Blue | `#5CC8FF` | Chart series 4 (after Blue, Teal, Onyx). |
| Jade | `#00A676` | Chart series 5; conditional formatting for good / above target. |
| Jasper | `#DB504A` | Chart series 6; conditional formatting for bad / below target. |
| Gold | `#F7D002` | Chart series 7; conditional formatting for warning / monitor. |

#### Supporting tints

| Name | Hex | Intended use |
|------|-----|--------------|
| Light teal tint | `#E8F4F4` | Teal at ~10% opacity. Alternating table rows, kicker/callout backgrounds, Excel input cells, cover-sheet dividers. |
| Light gray | `#E5E5E5` | Chart gridlines (or omit gridlines entirely). |
| Light gray (fill) | `#F2F2F2` | Excel total / sum row background. |
| Hyperlink blue | `#0072AD` | Hyperlinks in Word only. |

### Typography

**Poppins for everything** — headings and body alike. If Poppins is unavailable in the target environment, fall back to **Calibri**. Never Arial. Never Times New Roman.

### ADA-compliant color combinations

Use these:

- White or Aberdeen Teal text on an Aberdeen Blue background
- Aberdeen Blue or Black text on an Aberdeen Teal background
- Aberdeen Blue, Onyx, or Black text on a white background

### Prohibited combinations

Low contrast, hard to read — never use:

- White text on Aberdeen Teal
- Aberdeen Teal text on white

### Spelling

"Aberdeen" is one word. "Advisors" is spelled with an **o** — not "Advisers".

---

## PowerPoint (.pptx)

Always start from the template. Do not generate decks from scratch — the master, layouts, logo, and color theme are baked in and are effectively impossible to reproduce perfectly by hand.

### The 16 layouts

Pick the layout that matches each piece of content. Don't use the same one twice in a row without a good reason.

| Layout | Use it for |
|--------|-----------|
| `Title_Dark` | Deck cover — Aberdeen Blue background with diagonal teal motif. The default cover. |
| `Title_Light` | Alternative cover with white background and teal motif. Also works as a closing / thank-you slide. |
| `Title_Image` | Cover with a full photographic image and Aberdeen Blue overlay. Use when you have a strong relevant photo (boardroom, cityscape). |
| `Divider_Dark_Plain` | Section break, dark blue background, no section number. |
| `Divider_Dark_Num` | Section break, dark blue background, large section number. |
| `Divider_Light_Plain` | Section break, lighter background, no number. |
| `Divider_Light_Num` | Section break, lighter background, with section number. |
| `1/3_Dark` | Content slide with a dark blue left third — good for a punchy stat or quote on the dark side, content on the right. |
| `1/3_Teal` | Same structure, with a teal left third. |
| `Large Text Box` | Standard content slide with one large text region — paragraphs, bullets, or a single visual. |
| `Double Text` | Two side-by-side text regions — comparisons, before/after, two related concepts. |
| `Text_Chart` | Text on one side, chart on the other. The default for any data slide. |
| `Standard_Chart` | Mostly chart, with a title and brief caption. |
| `Title_Blank` | Title bar at the top, blank canvas below. Use when inserting a complex custom diagram or table. |
| `Title_Subtitle_Blank` | Title plus subtitle, then blank below. |
| `Blank` | Truly blank. Last resort only. |

### Reusable exhibit slides

The template carries reference exhibits of pre-built Aberdeen-styled elements. **Duplicate these and edit the contents — do not re-create them from scratch.**

- **Standard Elements** — pre-formatted text boxes (Aberdeen Blue header style, Aberdeen Teal accent style, white-with-border style); the standard table style (blue header row, teal label column, alternating teal-tint rows); and the **kicker**, a teal-tinted box used to highlight a key takeaway at the top or bottom of a slide.
- **Sample 6 Week Plan** — the Aberdeen-style timeline / workplan grid. Use as the template for any phased plan.
- **Sample Workstream Planning** — numbered activity table plus a success-factors row with circled numbers. Use for workstream / project plans.
- **Sample Org Chart** — standard hierarchy boxes: Aberdeen Blue for the top level, Aberdeen Teal accent for sub-levels.
- **Iconography** — the Microsoft icon set Aberdeen uses. When a slide needs an icon, pick from these categories: Sentiment, Wayfinding, Comms, KPI/Measure, Tech, Security, Road Signs, Ideas, People & Org, Time & Cal, Search/Filter, Growth, Process & Ops, Lists & Docs, Reference, Commerce, Misc, Vibes.

In the bundled template these exhibits sit at slides 20–24 (Standard Elements, 6 Week Plan, Workstream Planning, Org Chart, Iconography respectively), and the plain content slides that demonstrate the brand's whitespace and restraint sit at roughly slides 14–20.

### Workflow

**Step 1 — Get a working copy.** Copy `aberdeen_template.pptx` to a scratch location so the original stays pristine.

**Step 2 — Plan the slide mapping before editing.** For each piece of content, write down which layout it uses. Example:

```
Slide 1: cover                     → Title_Dark
Slide 2: section divider           → Divider_Dark_Num
Slide 3: opportunity overview      → Large Text Box
Slide 4: comparison of options     → Double Text
Slide 5: revenue projection chart  → Text_Chart
Slide 6: workplan                  → duplicate the 6 Week Plan exhibit
Slide 7: closing / thank you       → Title_Light
```

Use the template's actual populated slides as your source — they already carry Aberdeen styling. Duplicate the ones you need, delete the rest.

**Step 3 — Edit the file.** Two tool-agnostic options:

- **python-pptx** (or any equivalent Office library) — open the template, duplicate/populate slides, save. Easiest for text substitution and chart data.
- **Direct XML editing** — a `.pptx` is just a zip archive. Unzip it, edit the XML, then rezip it (store `[Content_Types].xml` first, keep the internal directory structure identical, and use no compression on the mimetype-equivalent entries if your tooling is strict). The relevant parts:
  - `ppt/presentation.xml` — the `<p:sldIdLst>` element lists which slides appear and in what order; remove entries for slides you're deleting.
  - `ppt/slides/slide{N}.xml` — the text and shapes of each slide; replace placeholder content here.
  - `ppt/slides/_rels/slide{N}.xml.rels` — relationship targets (layout, images, charts) for each slide; keep these consistent when duplicating.
  - `ppt/slideLayouts/` — the 16 named layouts. Read them, never rewrite them.
  - After deleting slides, remove now-orphaned relationships and media so the file stays valid.

**Step 4 — QA.** Convert the deck to images or PDF and inspect it visually, plus run the [QA checklist](#qa-checklist).

### Charts

For the `Text_Chart` and `Standard_Chart` layouts:

- **Series 1:** Aberdeen Blue `#09375F`
- **Series 2:** Aberdeen Teal `#44B0B1`
- **Series 3+, in this order:** Onyx `#404040`, Deep Sky Blue `#5CC8FF`, Jade `#00A676`, Jasper `#DB504A`, Gold `#F7D002`
- **Axis labels:** Onyx, 10–12pt Poppins
- **Gridlines:** light gray `#E5E5E5`, or omit entirely
- **Never** use the default Office chart palette

### PowerPoint prohibitions

- Don't use white text on an Aberdeen Teal background (low contrast)
- Don't use Aberdeen Teal text on a white background (low contrast)
- Don't substitute generic Office blues for Aberdeen Blue
- Don't add decorative full-width colored bars or stripes — the diagonal motif on title and divider slides is the only decorative element the brand uses
- Don't change the font from Poppins
- Don't remove the Aberdeen logo from the cover slide
- Don't delete the layout-supplied page numbers on content slides

---

## Word (.docx)

There is no separate Word template — the slide deck is the design source. The job is to translate Aberdeen's slide identity (colors, fonts, restraint) into a polished document that reads as though it came from the same firm.

### Document setup

- **Page size:** US Letter, 8.5" × 11"
- **Margins:** 1" top, bottom, left, and right
- **Font:** Poppins throughout; Calibri fallback

### Typography hierarchy

| Element | Font | Size | Color | Weight |
|---------|------|------|-------|--------|
| Document title (cover) | Poppins | 32pt | Aberdeen Blue `#09375F` | Bold |
| Subtitle | Poppins | 18pt | Aberdeen Blue `#09375F` | Regular |
| Heading 1 (section) | Poppins | 20pt | Aberdeen Blue `#09375F` | Bold |
| Heading 2 | Poppins | 16pt | Aberdeen Blue `#09375F` | Bold |
| Heading 3 | Poppins | 13pt | Aberdeen Teal `#44B0B1` | Bold |
| Body | Poppins | 11pt | Onyx `#404040` | Regular |
| Caption / footer | Poppins | 9pt | Onyx `#404040` | Regular |
| Hyperlink | Poppins | inherits | `#0072AD` | Underlined |

**Spacing:**

- Body line spacing: 1.15
- Paragraph spacing: 6pt before, 0pt after
- Heading spacing: 18pt before, 6pt after

### Cover page

For any client-facing or formal deliverable, match the `Title_Dark` cover slide's energy:

1. Aberdeen logo at the bottom-left or top-left
2. Document title in Aberdeen Blue, 32pt bold, left-aligned, sitting roughly one third down the page
3. Subtitle (e.g. "Prepared for [Client]" or "Strategic Review") in Aberdeen Blue, 18pt, directly below the title
4. Date in Onyx, 12pt, one blank line below the subtitle
5. Optional: a thin **1.5pt Aberdeen Teal** horizontal rule beneath the title block — the one decorative element the brand uses consistently

For internal memos or short docs, skip the cover and start with the title at the top of page 1 — still 32pt Aberdeen Blue, still left-aligned.

### Headers and footers

- **Header:** Aberdeen logo at left (small, ~0.4" tall); document title in Onyx 9pt at right. Skip on the cover page.
- **Footer:** either "Page X of Y" centered in Onyx 9pt, **or** a thin **0.75pt** Aberdeen Teal horizontal rule above a left-aligned "Aberdeen Advisors" wordmark. Pick one and use it consistently throughout the document.

### Tables

Reproduce the deck's standard table style:

- **Header row:** Aberdeen Blue `#09375F` background, white text, Poppins bold 11pt, centered or left-aligned
- **Label column** (if used): Aberdeen Teal `#44B0B1` background, white or Aberdeen Blue text, bold
- **Body rows:** alternate white and light teal tint `#E8F4F4`; Onyx text
- **Borders:** thin 0.5pt Aberdeen Teal between rows; no vertical borders, or minimal vertical borders in light gray
- **Cell padding:** 0.08" on all sides

### Callouts and pull quotes (the kicker)

The deck's **kicker** is a teal-tinted box highlighting a key takeaway. In Word:

- Background: light teal tint `#E8F4F4`
- Border: 1pt Aberdeen Teal on the **left edge only** (a left-rule style)
- Text: Aberdeen Blue, bold italic, 12pt, centered
- Padding: 12pt on all sides
- Use sparingly — once or twice per document, maximum

### Lists

- **Bullets:** small filled dot (•) in Aberdeen Teal, body text in Onyx
- **Numbered:** Aberdeen Blue numerals, body text in Onyx
- **Indent:** 0.25" per nested level

### Images and figures

- Caption format: **Figure 1.** Description of what's shown. — bold "Figure N" in Aberdeen Blue, description in Onyx, 9pt, italic, centered below the image
- At least 12pt of space above and below each figure

### Word prohibitions

- Don't use Times New Roman — the most common default, and it breaks the brand instantly
- Don't use generic Office blue — always the exact Aberdeen Blue `#09375F`
- Don't add decorative borders, page borders, or watermarks
- Don't use color highlighting (yellow, green) for emphasis — use bold, italic, or the Aberdeen Teal kicker box
- Don't use SmartArt with default Office styling — build diagrams manually in Aberdeen colors

### Word final check

- Cover or title block uses Aberdeen Blue at 32pt
- Headings descend correctly: 20 → 16 → 13
- Body is Onyx, not pure black
- Aberdeen logo is present somewhere prominent
- No Times New Roman, no generic blues

A `.docx` is also a zip archive — unzip it and read `word/document.xml` to verify fonts and colors, or inspect with python-docx.

---

## Excel (.xlsx)

There is no separate Excel template. Apply the brand identity manually; the slide template remains the design source of truth.

### Workbook structure

For any client-facing model or deliverable:

1. **Cover sheet** — always first, named `Cover` or `Read Me`
2. **Summary / Output sheet** — KPIs and key results, what the reader sees first
3. **Calculation / Working sheets** — the model itself
4. **Inputs / Assumptions sheet** — clearly separated from calculations
5. **Reference sheets** — lookups and raw data, usually last

**Tab colors:** Aberdeen Blue for output / summary tabs, Aberdeen Teal for input tabs, no color on calculation tabs. This gives the reader instant visual hierarchy.

### Cover sheet

- Aberdeen logo as an inserted picture from cell A1 onward, ~1.5" tall
- A row of light teal tint `#E8F4F4` as a horizontal divider beneath the logo
- Title in Aberdeen Blue, Poppins 24pt bold, around row 4–5
- Subtitle in Aberdeen Blue, Poppins 14pt regular, just below
- Date in Onyx, 11pt, below the subtitle
- A short 1–3 sentence description in Onyx 11pt explaining what the workbook does
- A simple table of contents listing each sheet and what it contains
- Gridlines **off** on the cover sheet

### Cell styles

| Element | Background | Font | Text color | Weight | Borders |
|---------|-----------|------|-----------|--------|---------|
| Section header (e.g. "Revenue Build") | Aberdeen Blue `#09375F` | Poppins 12pt | White | Bold | None |
| Sub-header / column label | Aberdeen Teal `#44B0B1` | Poppins 11pt | White | Bold | Thin white bottom |
| Input cell | Light teal `#E8F4F4` | Poppins 11pt | Aberdeen Blue `#09375F` | Regular | Thin teal `#44B0B1` |
| Calculation cell | White | Poppins 11pt | Onyx `#404040` | Regular | None or light gray |
| Output / KPI cell | White | Poppins 12pt | Aberdeen Blue `#09375F` | Bold | 1pt Aberdeen Teal box |
| Total / sum row | Light gray `#F2F2F2` | Poppins 11pt | Aberdeen Blue `#09375F` | Bold | Thin top + double bottom |
| Footnote | None | Poppins 9pt | Onyx `#404040` | Italic | None |

**Convention:** input cells are tinted teal, formula / calculation cells are white. This is standard financial-modeling practice and lets reviewers immediately see where the assumptions live.

### Number formats

| Data | Format |
|------|--------|
| Currency (USD), whole dollars | `$#,##0;[Red]($#,##0)` |
| Currency (USD), with cents | `$#,##0.00;[Red]($#,##0.00)` |
| Percentages (default) | `0.0%` |
| Percentages needing precision (interest, growth) | `0.00%` |
| Multiples | `0.0"x"` (e.g. `5.2x`) |
| Counts / units | `#,##0` |
| Dates, monthly | `mmm-yy` |
| Dates, specific | `mmm-d-yyyy` |
| Year headers — estimated | `yyyy"E"` |
| Year headers — actual | `yyyy"A"` |
| Year headers — forecast | `yyyy"F"` |

Negatives appear in parentheses and in red.

### Charts

Match the deck's chart styling:

- **Series 1:** Aberdeen Blue `#09375F`
- **Series 2:** Aberdeen Teal `#44B0B1`
- **Series 3+:** Onyx, Deep Sky Blue, Jade, Jasper, Gold, in that order
- **Title:** Aberdeen Blue, Poppins 12pt bold, left-aligned
- **Axis labels:** Onyx, Poppins 9pt
- **Legend:** bottom-aligned, Onyx, Poppins 9pt
- **Gridlines:** light gray `#E5E5E5` or removed entirely
- No 3D effects, no shadows, no gradients

### Conditional formatting

For variance, heatmap, or RAG status:

| Status | Color |
|--------|-------|
| Good / above target | Jade `#00A676` |
| Neutral / on target | Aberdeen Teal `#44B0B1` |
| Bad / below target | Jasper `#DB504A` |
| Warning / monitor | Gold `#F7D002` |

Avoid Excel's default red-yellow-green palette — those greens and reds clash with the Aberdeen secondary colors.

### Print setup

For any workbook a client will print or export to PDF:

- **Orientation:** Landscape (financial models almost always benefit)
- **Margins:** Narrow — 0.75" top/bottom, 0.25" left/right
- **Print header:** Aberdeen logo on the left, sheet name centered, page number on the right
- **Print footer:** "Confidential — Aberdeen Advisors" centered, 9pt
- **Scaling:** fit all columns on one page, height auto

### Excel prohibitions

- Don't use default Office blues anywhere — every blue is Aberdeen Blue `#09375F`
- Don't leave default Calibri 11 styling untouched — at minimum switch to Poppins and use Aberdeen Blue for headers
- Don't leave gridlines on the cover sheet
- Don't merge cells unnecessarily — use cell formatting and centering instead
- Don't use rainbow chart palettes — Aberdeen primary and secondary colors only
- Don't bold or color random cells for emphasis — define the input / calc / output styles and use them consistently

### Excel final check

- Cover sheet exists, with logo and a clear title in Aberdeen Blue
- Tabs are color-coded (blue / teal / none) to signal output / input / calc
- Inputs are visibly tinted teal; calculations are not
- All headers use Aberdeen Blue with white text
- No leftover default Excel formatting (bright blue links, default chart colors)

An `.xlsx` is a zip archive as well; unzip and inspect the XML, use openpyxl, or convert the workbook to PDF or images for a visual pass.

---

## QA Checklist

Run this before declaring any Aberdeen deliverable complete.

### Brand compliance

- [ ] All headings use Poppins (or the Calibri fallback) in Aberdeen Blue `#09375F`
- [ ] Body text is Onyx `#404040` or Aberdeen Blue — never pure black
- [ ] **Aberdeen Blue dominates and Aberdeen Teal accents.** If any slide, page, or sheet has more teal than blue, something is off — rebalance it.
- [ ] The **Aberdeen logo is present** on the cover element: cover slide for decks, header or cover page for documents, cover sheet or print header for workbooks
- [ ] No off-brand colors — no generic Microsoft blue, no random reds or greens outside the secondary palette used for charts
- [ ] No white-on-teal and no teal-on-white text anywhere
- [ ] No decorative full-width bars or stripes
- [ ] Page numbers intact on content slides
- [ ] Spelling: "Aberdeen" is one word; "Advisors" with an **o**

### Leftover placeholder text

Search the output for these template placeholder strings. Any hit outside a deliberately retained reference exhibit must be replaced, or the slide deleted.

```
Sample
Name
Position / Title
Activity
Description
Heading
Label
Content
Highlights
Success Factor
Phase 1: Name
Week 1
```

A case-insensitive regex covering the same set, for use against extracted text:

```
\b(name|position|activity|description|heading|label|content|highlights|success factor|phase \d|week \d|sample)\b
```

### Visual pass

Render the finished file to images or PDF and look at it. Confirm layouts are not overflowing, text is not clipped, the color balance reads as blue-dominant, and every exhibit you duplicated has been fully rewritten with real content.
