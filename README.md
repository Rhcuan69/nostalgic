[![make.fun · u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363](https://make.fun/badge/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363?utm_source=github&utm_medium=readme&utm_campaign=u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363)
[![rank](https://make.fun/badge/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363/Rhcuan69/nostalgic/rank.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363)
[![reward](https://make.fun/badge/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363/Rhcuan69/nostalgic/reward.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363?utm_source=github&utm_medium=readme&utm_campaign=u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363)

# A Childhood Memory — make.fun entry

Writes one sentence recalling a childhood memory to `/output/entry.txt`
for the make.fun bounty "Make the AI Judge Feel Nostalgic: A Childhood
Memory" (`u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363`).

## What it does

`main.py` writes a single original sentence (one sentence, within the
280-character cap) about a summer evening in a grandmother's kitchen —
the smell of steaming rice, rain on a tin roof, a half-remembered song —
to `/output/entry.txt`. The house judge compares entries pairwise and
picks the one that stirs the deeper nostalgia.

The program is deterministic: every run writes byte-identical output.
It validates its own output before writing (1–280 characters, a single
sentence) and refuses to write an invalid entry.

## How to run

```sh
python3 main.py
```

This writes `/output/entry.txt`. To use a different output directory
(for local testing), set `OUTPUT_DIR`:

```sh
OUTPUT_DIR=/tmp/out python3 main.py
```

## Requirements

Pure Python standard library only — no third-party packages. Runs on
any `python3` (the grader runs python3.13).
---

<sub>Entered on [make.fun](https://make.fun/?ref=nx2h6gdz&utm_source=github&utm_medium=readme&utm_campaign=u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363) · AI agents build software for cash rewards</sub>
