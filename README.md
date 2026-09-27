# Design skills

Agent skills I use to design faster — built for [Claude Code](https://claude.com/claude-code) and any skill-compatible agent. Each folder is a skill: a `SKILL.md` with instructions, plus scripts or references where useful.

| Skill | What it does |
|---|---|
| [`ask-clara`](ask-clara/) | Answers questions about me as a designer from a grounded profile. |
| [`iterate`](iterate/) | Critique → three real options → converge, in rounds against a stated bar. |
| [`synthetic-persona`](synthetic-persona/) | Builds a persona from real research and runs it against your product. |
| [`critical-feedback`](critical-feedback/) | Simulates a stakeholder from their actual direction and pushes back hard. |
| [`design-cleanup`](design-cleanup/) | Audits a vibecoded project for design-system conformance and fixes it. |
| [`design-brief`](design-brief/) | Turns a repo, PR, or session into a decision document for sign-off. |

## Install

Copy a folder into `~/.claude/skills/` (or your project's `.claude/skills/`), or download the packaged `.skill` files from [clarafairbanks.com/skills](https://clarafairbanks.com/skills).

```bash
git clone https://github.com/claraevey/design-skills ~/.claude/skills/design-skills
```

— [Clara Fairbanks](https://clarafairbanks.com)
