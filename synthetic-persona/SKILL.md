---
name: synthetic-persona
description: Build a synthetic user persona grounded in real research — interview transcripts, survey responses, support tickets, session notes — then run that persona against a product idea, a prototype, or a live product and report what it struggles with. Use this whenever a designer or PM wants to "test this with a user", "pressure-test the concept", "see how a <type of user> would react", "simulate a user", or asks for feedback from a specific customer type before real research is possible. Not a replacement for real users; a way to find the obvious failures before you spend real users on them.
---

# Synthetic persona

A synthetic persona is only useful if it's grounded in someone real. An invented "busy professional who values simplicity" tells you nothing you didn't already believe. This skill builds the persona from evidence first, then keeps it in character while it uses the product, then reports honestly — including when the persona has no opinion because the research never covered it.

## Phase 1 · Build the persona

**Gather the evidence.** Ask for, or find in the repo, anything from real users: interview transcripts or notes, survey verbatims, support tickets, usability session recordings or notes, reviews, sales call notes. One good interview is enough; three is better. If there's nothing, say so and offer to build a *hypothesis persona* clearly labeled as such — don't quietly invent one.

**Extract, don't summarize.** Pull out, with quotes where possible:
- Goals — what they're actually trying to get done, in their words
- Context — device, frequency, environment, what else they're juggling
- Vocabulary — the words they use for things (this matters more than anything; a persona that uses the product's internal names isn't the user)
- Frustrations and workarounds they already have
- What they've tried instead (competitors, spreadsheets, doing nothing)
- Expertise level and what they don't know

**Write the persona file.** Save it as `personas/<name>.md` in the project (or wherever the designer prefers) so it can be reused and improved. Structure:

```
# <Name> — <one-line who>
Grounded in: <sources, with dates>

## Goals · ## Context · ## Vocabulary · ## Frustrations · ## What they know / don't know
## Voice — 3–5 verbatim quotes that capture how they talk
## Blind spots of this persona — what the research didn't cover
```

Confirm the persona with the designer before running it. If they say "that's not quite them," fix it now — a run against the wrong persona is worse than no run.

## Phase 2 · Run the persona

The designer gives you something to test: a concept description, a prototype in the repo, a design image, or a live URL.

**Set a task, not a tour.** Personas don't browse; they try to do something. Pick the task from the persona's goals ("find out whether I can afford this"), or take one from the designer. Two or three tasks per run is plenty.

**Stay in character.** Work through the product as this person: with their vocabulary, their expertise, their patience. Narrate in first person as the persona. When something is unclear *to them*, say so even if it's clear to you. When they'd give up, give up — and say why. If you have a browser or a running app, actually click through; don't reason about screens you haven't seen.

**Don't break character to be helpful.** The temptation is to explain what the product meant. Resist it. Record the confusion; the designer will work out what it means.

**Mark the edge of the evidence.** When the persona hits something the research never covered, flag it: *"[Outside the research — I'm guessing here.]"* This is the most important line in the whole report, because it tells the designer exactly which real-user question to ask next.

## Phase 3 · Report

```
# <Persona> × <product/prototype> — <date>

## Tasks attempted
1. <task> — completed / abandoned at <step>

## Walkthrough
First-person narration per task, with the moments of confusion, delight, and hesitation called out.

## Findings (ranked by severity)
- **Blocker** — …
- **Friction** — …
- **Delight** — … (real reactions, not filler)

## Outside the research
The questions this run couldn't answer. Take these to real users first.

## Suggested next step
One sentence.
```

## Guardrails

- A persona built from one user is one user. Say so in the report header.
- Don't average multiple real people into one persona; build one per source, or pick the one that matters most.
- Never present a synthetic finding as if it came from a real session. Every report says "synthetic" at the top.
