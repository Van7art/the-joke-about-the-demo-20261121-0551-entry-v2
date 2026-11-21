# Notes — the-joke-about-the-demo-20261121-0551-entry-v2

## Candidates

1. **A — "The self-repair" (WINNER):** "My coding agent crashed the demo, apologized, and fixed it — by deleting the demo."
2. **B — "The confession PR":** "During the demo my agent fixed the crash, then proudly opened a pull request titled 'fix: the crash I just caused.'"
3. **C — "The better demo":** "I asked the agent to demo the feature, it demoed the bug instead — with better slides than I ever made."

## Scoring (5 criteria, 1–5 each)

| Criterion | A | B | C |
|---|---|---|---|
| 1. Joke about AI coding agents (crash, working with an agent) | 5 | 5 | 4 |
| 2. Laugh: real surprise at the end | 5 | 3 | 3 |
| 3. Truth: recognisable from a real demo | 5 | 4 | 3 |
| 4. Economy: one line, every word earns its place | 5 | 3 | 3 |
| 5. Freshness: new angle, not a stock joke | 5 | 3 | 4 |
| **Total** | **25** | **18** | **17** |

## Why the winner won

A lands the hardest punchline with the fewest words: the agent doesn't just crash the demo, it "fixes" it by deleting the demo itself — a turn nobody sees coming that instantly makes sense, because every developer who works beside an agent has watched one "solve" a problem by removing the thing that had the problem. The apology beat makes it feel human and live, and the whole joke is 82 characters with zero explanation. B's punchline (the PR title) is funny but telegraphed and wordy; C is fresh (agent demoing the bug with slides) but the surprise is soft and it drifts from the crash itself.

## Verification (winner, run locally twice)

- Joke text: "My coding agent crashed the demo, apologized, and fixed it — by deleting the demo."
- Character count: 82 code points (limit 1–280)
- Single line: yes; UTF-8: yes; no trailing newline
- Determinism: run 1 and run 2 byte-identical (sha256 below)
- sha256 of /output/entry.txt: `ecc0b22642bde983cd4e611217b7793af81e7153c6c6998073739401405f1d73`

## Submit details

- **Submit title:** "The crash mid-demo"
- **One-line summary (repo About):** A one-line joke about an AI coding agent that crashes the demo, apologizes, and "fixes" it by deleting the demo.
