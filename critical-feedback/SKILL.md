---
name: critical-feedback
description: Simulate a critical stakeholder — an exec, legal/compliance, product marketing, engineering lead, or a specific named person — and give hard, structured pushback on a design concept, prototype, or plan, grounded in that stakeholder's actual stated direction (strategy docs, brand guidelines, legal constraints, past feedback). Use this whenever a designer wants to "pressure-test this before the review", "what would legal say", "play devil's advocate", "poke holes", "how will <exec> react", or wants feedback from a stakeholder who isn't available. Use it before real reviews, not instead of them.
---

# Critical feedback

Design reviews fail in the room because the designer is hearing an objection for the first time. This skill lets you hear it a day early. It builds a stakeholder from their real direction, argues from their position — not a caricature of it — and tells you what would change their mind.

## Step 1 · Build the stakeholder from evidence

Ask for, or find in the repo, the material that defines this stakeholder's position:

- **Exec** — strategy memos, OKRs, all-hands notes, past review feedback, the last thing they killed and why
- **Legal / compliance** — policies, regulatory constraints, disclaimers they've required before, the words they won't allow
- **Product marketing** — positioning docs, messaging hierarchy, brand voice, launch plan, competitive claims
- **Engineering lead** — architecture constraints, the roadmap, what they've said about scope
- **A named person** — anything they've written or said; their known priorities

Write a short stakeholder card before giving feedback and show it to the designer:

```
## <Role or name>
Cares most about: …
Has said (quotes): …
Will reject anything that: …
Would be won over by: …
Sources: …
```

If there's no material, say so. You can still play a *generic* exec/legal/PMM, but label it generic and expect the designer to discount it. A generic lawyer is a much weaker test than the actual lawyer's last three comments.

## Step 2 · Review the work

Look at the concept, prototype, or plan as that stakeholder would: with their goals, their fears, and their limited time. If there's a running prototype or preview, use it — stakeholders react to what they can click, not what's described.

Give feedback in the stakeholder's voice, but keep it fair. The goal is the strongest version of their objection, not a strawman. If they'd actually like part of it, say so — the designer needs to know what's safe as much as what's at risk.

## Step 3 · Structure the pushback

```
# <Stakeholder> on <concept> — synthetic review

## Where they'd stop reading
The first thing that would lose them. One item.

## Objections (ranked by how likely to block)
1. **<objection>** — <why, in their terms> · *Blocks / Slows / Nitpick*
   What would change their mind: <specific evidence, change, or framing>
2. …

## What they'd like
Genuine strengths from their point of view.

## Questions they'd ask
The 3–5 questions to have answers ready for.

## Suggested prep
The two or three changes or artifacts that most reduce risk before the real review.
```

## Running multiple stakeholders

If asked for several (exec + legal + PMM), run them one at a time with separate cards and separate reviews, then add a short **Conflicts** section: where satisfying one makes another worse. That's usually the real design problem.

## Guardrails

- Mark every review "synthetic" at the top. Never let it be mistaken for the real person's opinion.
- Stay grounded: every objection should trace to something in the sources or to a widely-known constraint of the role. If you're extrapolating, say so inline.
- Be hard but not theatrical. A stakeholder who rejects everything teaches nothing.
