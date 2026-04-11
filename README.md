# Foundations

Active learning system for CS fundamentals. Claude acts as primary tutor — tracking progress, running spaced repetition, and adapting the curriculum based on performance.

**Goal**: Competitive at big tech / AI companies within 9–12 months.
**Start date**: April 14, 2026

---

## Schedule

| Day | Focus | Time |
|-----|-------|------|
| Tuesday | DSA + SQL | Post-2pm |
| Wednesday | Systems (DDIA) | Post-2pm |
| Thursday | DSA + SQL | Post-2pm |
| Saturday | Optional build session | Morning |

---

## How This Works

1. At the start of each session, Claude checks `review-queue/queue.json` for due problems (Anki-style)
2. Due reviews surface first, then the next new problem in curriculum order
3. You attempt the problem on LeetCode/Neetcode, then explain your approach and paste your code here
4. Claude asks probing questions and critiques your reasoning
5. Claude rates you (0–3) and updates the queue with the next review date
6. Session is logged in `session-logs/`

**Core rule: You always attempt first. Claude never gives the solution unprompted.**

---

## Curriculum

- **DSA**: [Neetcode 150](curriculum/dsa.md) — in order, no skipping
- **SQL**: [LeetCode SQL 50 → DataLemur](curriculum/sql.md) — in order, Postgres + SQL Server both
- **Systems**: DDIA by Martin Kleppmann — half chapter per week, Wednesdays

---

## Progress

See [progress.md](progress.md) for current status across all topics.

---

## Spaced Repetition Tool

```bash
# Check what's due today
python3 review-queue/srs.py due

# Log a review (Claude does this after each problem)
python3 review-queue/srs.py review two-sum 2 --notes "got hashmap but missed edge case"

# Add a problem to the queue
python3 review-queue/srs.py add two-sum "Two Sum" dsa arrays easy --url "https://leetcode.com/problems/two-sum/"

# Overall stats
python3 review-queue/srs.py stats
```

Rating scale: `0` gave up · `1` hard · `2` okay · `3` easy

---

## Repo Structure

```
foundations/
├── CLAUDE.md                  # Tutor instructions for Claude
├── curriculum/
│   ├── dsa.md                 # Neetcode 150 ordered list
│   └── sql.md                 # SQL 50 + DataLemur ordered list
├── review-queue/
│   ├── queue.json             # SRS state (ground truth)
│   └── srs.py                 # SM-2 spaced repetition calculator
├── session-logs/              # One file per session
├── notes/
│   ├── dsa/                   # Concept notes per topic
│   ├── sql/                   # SQL concept notes
│   └── systems/               # DDIA notes
└── progress.md                # Dashboard
```
