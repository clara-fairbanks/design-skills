---
name: iterate
description: Take a design concept, wireframe, screenshot, Figma export, or an existing screen/component in the codebase and iterate on it in structured rounds until it meets a stated bar. Use this whenever a designer asks to "iterate", "push this further", "explore variations", "make this better", "give me options", or shares a screen and asks what's wrong with it — even if they don't say "iterate". Works on images and on live code.
---

# Iterate

Design iteration with an agent goes wrong in two predictable ways: it produces one polished-looking answer with no alternatives, or it produces five superficial variants that change the color and call it exploration. This skill is a loop that avoids both — critique honestly, diverge on the thing that matters, converge on evidence, repeat.

## Inputs

You'll get one or more of:
- An image (screenshot, wireframe, Figma export, sketch photo)
- A path to a component or page in a repo
- A description of a concept with no artifact yet

And, ideally, a **bar**: what "done" looks like. If it isn't stated, ask one question to get it — "what should this be better at when we're finished?" — and propose a default if they shrug (usually: clearer primary action, less to read, works at phone width).

## The loop

Each round has four steps. Run them in order; don't skip the critique because you already have ideas.

### 1. Critique

Look at the artifact as the user would, not as a designer would. Say what the screen is *for*, then say what gets in the way. Be specific to the pixel: "the secondary button has the same visual weight as the primary" is useful; "the hierarchy could be stronger" isn't. Limit to the 3–5 problems that matter most. Rank them.

If you're working from an image, describe what you see before critiquing so the designer can correct a misread.

### 2. Diverge on the top problem

Pick the highest-ranked problem and generate **three genuinely different** solutions to it. Different means different mechanisms, not different styling — e.g. for "too much to read": progressive disclosure, a summary-first layout, or cutting half the content. Name each direction in a few words and say what it trades away.

If working in code, build each as a real variant (a prop, a sibling component, or a branch), so it can be seen and clicked, not imagined. If working from images, describe each precisely enough to sketch, or render a quick HTML mock when that's faster than words.

### 3. Recommend and converge

Recommend one, with the reason. Then apply it and re-render. Now this is the new artifact.

### 4. Check against the bar

Re-read the bar from the inputs. Is it met? If yes, stop and summarize what changed and why. If not, go back to step 1 with the new artifact — the top problem has probably changed.

Cap at four rounds unless asked to continue. Past that, diminishing returns almost always mean the bar is wrong, not the design; say so.

## Working in code

- Keep the original intact until the designer picks. Variants live beside it, not over it.
- Reuse the project's tokens, components, and patterns. A variant that ignores the design system isn't a real option — it can't ship.
- Use the running app or a preview to look at your own work before presenting it. If you can't see it, say so.
- When the designer picks a variant, remove the others and leave one clean diff.

## Output per round

```
## Round N

**Critique** — ranked list, 3–5 items
**Exploring:** <top problem>
- A · <name> — <mechanism> · trades away <x>
- B · <name> — …
- C · <name> — …
**Recommendation:** <letter>, because <reason>
**Applied.** <what changed>
**Bar:** met / not yet — <why>
```

## Tone

Direct and specific. The designer wants a sharp collaborator, not encouragement. Say when something is already good so the critique has credibility when it isn't.
