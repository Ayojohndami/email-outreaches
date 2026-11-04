---
name: carousel-art-direction
description: Create or upgrade Instagram and LinkedIn carousel designs using Pinterest-informed art direction, brand-color adaptation, expressive typography, and varied slide composition. Use for carousel design briefs, image-generation prompts, rendered carousels, or the visual-design layer of a carousel master prompt; not website image sliders.
---

# Carousel art direction

Turn researched content into a recognizable visual campaign. Build on six studied references without copying their finished artwork. Read [the reference study](references/pinterest-study.md) when choosing a direction; it is the source of this skill's visual taste.

## Work with the existing prompt

Act as a design layer, not a replacement for the user's research or content workflow. Preserve audience, language, approved claims, slide count, exact copy when locked, and requested deliverable. Honor the user's brand rules and chosen production tools. Do not impose an extra approval gate. Ask only for information that blocks a correct result; state reversible assumptions and proceed otherwise.

Route to the requested output:
- **Design direction:** supply a usable art-direction brief and slide specifications.
- **Image prompts:** supply a shared style block and one self-contained prompt per slide. Follow any existing image-generation workflow.
- **Rendered carousel:** create the actual requested slide files using available tools, then inspect them. A prompt list is not a rendered carousel.
- **Design upgrade:** identify specific weaknesses in the provided slides, preserve what works, and revise the composition rather than merely adding decoration.

This skill supplies judgment, not an image engine, font library, browser, or export tool. If a capability is unavailable, finish the useful design work and name the remaining production step accurately.

## 1. Resolve the brand

Use this priority: supplied brand guidelines/assets → verified first-party brand site or brand kit → the user's existing research → clearly labeled provisional design choices. Research the business through available authorized tools when needed. Inspect source artwork or first-party styles when available; a screenshot color estimate is not an exact official hex value. Never guess official colors, fonts, logos, audience demographics, or business results from a name.

Record a compact brand brief: audience and intended action; character of the brand; verified palette and fonts with sources; logo/assets available; constraints; provisional choices. Use the user's objective to decide whether the work should feel playful, cinematic, technical, editorial, or restrained.

Define these roles before composing slides:

| Token | Function |
|---|---|
| `canvas-light` / `canvas-dark` | Readable light and dark environments; choose only those needed |
| `ink-on-light` / `ink-on-dark` | Primary reading text on the respective canvas |
| `brand-primary` | The recognizable brand hue |
| `brand-accent` | A supplied secondary hue, or an approved/provisional derivative |
| `surface` | Supporting panel, comparison, or evidence field |
| `muted-ink` | Secondary information that still needs to be readable |

Roles may alias existing colors or remain unused; a brand with one hue does not need an invented secondary color. Omit the dark environment if it is unnecessary. A small brand signature is optional when no logo is supplied or locked copy excludes additional text; type, palette, and visual logic can establish identity.

Translate relationships, not literal colors: forest + lime becomes the client's dark field + high-contrast emphasis; cobalt + pale blue becomes the client's primary hue + compatible tint. Preserve a mandated logo's colors. If a bright brand hue cannot carry readable text, use it as a field, marker, border, or object and use dark ink for reading. Do not darken the official color silently; label a darker derivative separately. Match photographic lighting and 3D material accents to the palette without turning skin or product colors unnatural.

Use measured solid-color contrast as an aid: target at least 4.5:1 for explanatory copy and 3:1 for large display type. Run `python3 scripts/contrast.py FOREGROUND BACKGROUND` when a Python runtime is available. On photography, test the actual text region and add a controlled scrim or panel if necessary. A solid-color ratio alone does not validate text over an image. Do not claim whole-carousel accessibility from this check.

## 2. Choose one primary direction

Select from the study according to brand and message, not whichever effect is most dramatic:

| Direction | Visual mechanism | Good fit |
|---|---|---|
| Character-led list | Huge numeral, original recurring character, deep field and sharp accent | Playful education, creator brands, mistakes/checklists |
| Photographic depth | One hero subject, selective floating panels, oversized type | Personal brands, workflows, launches |
| Editorial photo stack | Central anchor image, receding frames, condensed side title, quiet metadata | Culture, fashion, storytelling, portfolios |
| Sculptural brand campaign | One dimensional metaphor, related materials and lighting, open space | Technology, agencies, services, product systems |
| Bold comparison | Clear opposing examples, heavy type, selective accent labels | Teardowns, before/after explanations, practical teaching |
| Cinematic type poster | Condensed headline, cropped hero, one accent word or stamp | Punchy covers, font showcases, creative announcements |

Use a secondary direction only when it solves a content need, such as a comparison inside a photo-led sequence. Keep the same palette roles, type system, and treatment of assets. Do not combine all six directions into one deck. A restrained adaptation can be stronger for a serious business than characters or luminous objects.

For brands that need a plain typographic treatment, translate only the references' scale hierarchy, disciplined alignment, and pacing into flat type and simple rules. Name this a restrained typographic adaptation; do not force it into a 3D or photographic recipe. The six directions are options, not a closed template catalog.

Write one sentence naming the concept and why it supports this message. Example: “A sculptural bridge motif makes the migration process tangible; navy structure and coral waypoints follow the client's palette.” Avoid art direction made only of adjectives such as “premium, modern, stunning.”

## 3. Build the sequence as a system

Use the user's dimensions. If absent, state a working default of 1080 × 1350 px. Do not change aspect ratio across slides. At that width, start around 64–88 px outer margins, 80–128 px headlines, 32–44 px body text, and 24–30 px secondary labels. These are starting values, not measurements of the pins. Give essential labels the readability of body text. Use a 16–24 px internal spacing rhythm and adjust to the typeface.

Choose up to two font families unless an existing identity needs more. Use the brand font when available; if substituting, name a real available alternative and disclose it. Give display type a distinct role: a numeral as an anchor, a condensed headline to create a tall rhythm, or a few enlarged words for emphasis. Keep body copy out of decorative display faces. Do not distort letters to make copy fit.

Storyboard each slide's job and visual mechanism before rendering. Work with the approved narrative; when no structure exists, start with a specific promise, deliver a useful first insight on slide 2, develop the argument with examples, and close with the relevant action. Do not guarantee virality or engagement from visual choices.

Maintain common anchors: margins/grid, type roles, small brand signature, progress marker if useful, image treatment, and lighting/material language. Vary **composition**: cover → focused explanation → comparison/evidence → visual pause → takeaway/CTA, adapted to the actual slide count. A three-slide deck needs fewer variants than a ten-slide deck.

Treat a multi-tile campaign overview as evidence of a shared visual system, not a mandate to squeeze nine miniature designs onto one carousel slide. Use [layout recipes](references/layout-recipes.md) when translating the direction into slide geometry.

Give each slide one dominant reading entry. Direct attention with scale, crop, alignment, and purposeful overlap. A huge number must be a real count or statistic supplied by the content. A 3D object must express the idea, not fill a blank corner. Reuse a character or object through crops and poses rather than pasting the identical picture everywhere.

For fixed copy, reflow it and simplify surrounding graphics first. If it still cannot fit legibly within a locked slide count, explain the conflict and seek permission to shorten it. When copy is editable, prefer one short headline and one concise explanation per content slide; provide a concrete example rather than a wall of text. Avoid treating a decorative word limit as more important than the user's argument.

## 4. Specify assets and produce

Use original, licensed, or user-authorized assets. Study the reference's crop, contrast, pacing, and depth; do not copy its logo, proprietary character, signature artwork, creator identity, or wording. The superhero in one pin teaches silhouette and scale; it is not the default subject for a client's campaign. Do not represent a generated person as an actual customer or founder.

Prefer editable typography composed over generated visual assets when exact text, logos, tables, or screenshots matter. Generate artwork without baked-in text if that gives better reliability. Place real supplied logos and verified screenshots as assets. If all-in-one image generation is requested, specify exact copy and line breaks, then inspect for spelling and layout errors. Never invent an interface or chart and present it as evidence.

Before handoff, provide common tokens once and for each slide specify:
1. Slide number, purpose, and exact copy with intended line breaks.
2. Layout: focal point, normalized positions or pixel regions, reading order, and intentional crop/overlap.
3. Type: family, weight, approximate size, alignment, and emphasis.
4. Color: token assignments for background, text, and accents.
5. Asset brief: subject, crop, lighting/material, source or generation requirement, and clear text-safe areas.
6. Continuity: what repeats and what changes from adjacent slides.

For image prompts, repeat indispensable shared tokens and composition instructions inside each slide prompt so it can work independently. Keep text/canvas/palette instructions unambiguous; avoid contradictory camera or layout instructions. Include exclusions that address actual risks: illegible text, extra logos, unrelated objects, or a reference's branded character. Do not add a long generic negative-prompt list.

## 5. Review the actual result

Inspect all rendered slides at full size and at about 360 px display width, plus a sequence contact sheet. Check:
- Cover: clear promise, one dominant entry point, recognizable brand, no decorative overload.
- Content: readable essential text, intact exact copy, sufficient contrast, diagrams that communicate the actual claim.
- Composition: deliberate crops, aligned baselines, no collisions or stray tangencies, believable depth, repeated motifs with a purpose.
- Sequence: coherent type/palette/assets, meaningful changes in composition, useful slide 2, clear final action.
- Production: correct dimensions/order, clean exports, complete deliverables, no placeholder assets or invented evidence.

Repair concrete defects and inspect again. Do not call text clean based only on a generation tool returning success. If rendering or visual inspection is unavailable, label the work “design specification; visual QA pending.” Do not invent a quality score or claim an unperformed test.

For revisions, state a few specific changes: “Reduced three competing focal points to one, enlarged body copy, and moved the brand accent to the comparison labels.” Deliver the requested files/prompts first; keep rationale brief.
