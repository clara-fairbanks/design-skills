---
name: design-brief
description: Read a repo, a branch, a PR, or the current agent session and produce a design brief — the design decisions that were made, the rationale, what was considered and rejected, open questions, and how to review it — packaged as a shareable document with the link to the running prototype or PR. Use this whenever a designer needs to "write this up for stakeholders", "get sign-off", "share what we decided", "document the design rationale", "prep for design review", or at the end of a prototyping session before handing work to engineering or leadership.
---

# Design brief

When design happens in code, the reasoning lives in commits, comments, and a long agent transcript that nobody else will read. A brief pulls it back out so a stakeholder can approve the *decisions*, not squint at a diff.

## Step 1 · Gather

Depending on what you're given:

- **The current session** — you already have it. Reread it for the moments where a choice was made: "let's go with," "actually, instead," "the reason is." Those are the brief.
- **A branch or PR** — read the diff, the commit messages, and the PR description. Then run the app or open the preview so you can see what shipped, not just what changed.
- **A repo** — look for `DESIGN.md`, ADRs, a `docs/` folder, recent commits touching UI, and the component tree. Ask which area to brief; a whole repo is not a brief.

Collect, for each decision: **what** was decided, **why**, **what else was considered**, and **what it costs** (the trade-off). If you can only find the what, say the rationale is undocumented rather than inventing one — stakeholders can smell a retrofitted reason.

Capture screenshots of the current state. A brief without pictures gets skimmed; a brief with the actual screens gets approved or corrected.

## Step 2 · Write

Keep it to one screen of reading before the details. Structure:

```
# <Project or feature> — design brief
<date> · <author> · <status: draft / for review / approved>
Prototype: <url> · Code: <PR or branch link>

## In one paragraph
What this is, who it's for, and the single most important design decision.

## Decisions
### 1. <Decision, as a statement — "Show the plan before generating code">
**Why:** …
**Considered:** … (and why not)
**Trade-off:** …
<screenshot>

### 2. …

## Open questions
Things the reviewer needs to answer, each with a recommended default.

## What's not in scope
So nobody reviews the wrong thing.

## How to review
Where to click, what to look at first, how long it takes. Ten minutes is a good target.

## Next steps if approved
```

Write for the busiest reader. Decisions as headlines; rationale as one or two sentences each. No process narrative ("first we explored…") — that's what the prototype is for.

## Step 3 · Package

Produce whatever the team actually shares:
- A Markdown file in the repo (`docs/design/<feature>-brief.md`) so the rationale lives with the code, **and**
- A shareable version if one is needed — a doc, an HTML page, a PR description, a Slack-ready summary. If the environment has an artifact or docs tool, use it and hand back the link.

Include the screenshots inline. Link the prototype at the top; if there isn't a running one, say what a reviewer should run.

## Step 4 · Ask for the approval you actually need

End with the exact question: *"Approve decisions 1–4 as described? Decision 5 is the open one — I recommend option A."* A brief that ends with "let me know your thoughts" never gets approved.

## Guardrails

- Don't overstate certainty. A prototype decision is provisional; mark it that way.
- Don't hide the ugly trade-off. Stakeholders trust briefs that name what got worse.
- Keep the agent transcript out of it. Nobody needs the journey; they need the decisions.
