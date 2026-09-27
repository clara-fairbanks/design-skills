---
name: design-cleanup
description: Audit a vibecoded or fast-prototyped front-end project for conformance to its design system and design tokens — hardcoded colors, spacing, type sizes, radii, shadows, one-off components that duplicate system components, inconsistent states — and fix them. Use this whenever a designer or engineer says "clean this up", "make this match the design system", "tokenize this", "this prototype needs to be production-ready", "check for hardcoded values", or before a prototype's front end is merged into a real codebase.
---

# Design cleanup

Prototypes built fast are full of `#3b82f6`, `padding: 13px`, and a third slightly different button. That's fine for a prototype and a problem for a codebase. This skill finds the drift from the design system, explains it, and fixes it in a way the team can review.

## Step 1 · Find the system

Before auditing anything, work out what "conformance" means here. Look for, in this order:

1. **Token definitions** — `tokens.*`, `theme.*`, Tailwind config or `@theme` blocks, CSS custom properties on `:root`, Style Dictionary output, a `design-system/` package
2. **Component library** — `components/ui/`, a package like `@company/ui`, shadcn, Radix wrappers, etc.
3. **Written guidance** — `DESIGN.md`, Storybook docs, Figma links in the README

Summarize what you found in a few lines: the token names for color/space/type/radius/shadow, and the components that exist. If there's no system at all, say so and propose the smallest one that would fit the codebase (usually: extract the 5–8 colors, a 4/8px spacing scale, and 3–4 type sizes already in use) — get agreement before applying it.

## Step 2 · Audit

Run `scripts/find_hardcoded.py <src-dir>` to get the raw list of literal values: hex/rgb/hsl colors, pixel spacing, font sizes, border radii, box shadows, font families, z-indexes. It prints file:line, the value, and the surrounding line so you can judge context.

Then read the components, not just the grep output. The script can't see:
- A custom `<Button>` that duplicates the system button with slightly different padding
- Focus, hover, disabled, and error states that exist on some components and not others
- Dark-mode values hardcoded next to light-mode tokens
- Magic breakpoints
- Inline styles that bypass the styling system entirely
- Accessibility regressions that came with the speed: missing labels, contrast under 4.5:1, click targets under 44px

Group findings by **kind**, not by file. Twenty instances of one problem is one finding with twenty locations.

## Step 3 · Report before fixing

```
# Design cleanup — <project> — <date>

## System found
Tokens: … · Components: … · Guidance: …

## Findings
| # | Kind | Count | Example | Fix |
|---|---|---|---|---|
| 1 | Hardcoded color | 23 | `#3b82f6` in Hero.tsx:41 | → `text-accent` / `var(--color-accent)` |
| 2 | Duplicate button | 3 | `CtaButton.tsx` | → `<Button variant="primary">` |
| … |

## Not going to touch
Things that look like drift but are intentional (with the reason), or are out of scope.

## Plan
Ordered list; mechanical fixes first, judgment calls last.
```

Show this and get a go-ahead. A cleanup that silently changes forty files is hard to review and easy to reject.

## Step 4 · Fix

- Mechanical replacements first (literal → token). Do them per kind, one commit each, so the diff reads as "replace hardcoded colors with tokens," not "touched 40 files."
- Consolidate duplicates second. When replacing a one-off component with the system one, keep behavior identical; if the one-off had a real reason to differ, add a variant to the system component instead of keeping the fork.
- Judgment calls last, and ask when unsure. A 13px padding might be a mistake or might be optical alignment someone fought for.
- Run the app and look at every screen you touched, in light and dark if the project has both. Tokens with the wrong value are worse than literals with the right one.
- Don't refactor logic, rename things for taste, or reformat files you didn't otherwise change. Scope creep is how cleanups get reverted.

## Step 5 · Hand off

Finish with a short summary: what was replaced (counts), what was consolidated, what was deliberately left, and anything the system itself should add (a missing token, a missing variant) so the next prototype doesn't drift the same way.
