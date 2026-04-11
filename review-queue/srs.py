#!/usr/bin/env python3
"""
Spaced Repetition System (SM-2 variant) for DSA and SQL problems.

Usage:
  python3 srs.py due                                    # list due problems
  python3 srs.py review <problem-id> <0|1|2|3>          # log a review
  python3 srs.py review <problem-id> <0|1|2|3> --notes "text"
  python3 srs.py add <id> <name> <type> <topic> <difficulty> [--url URL]
  python3 srs.py stats                                  # summary stats
  python3 srs.py list                                   # all problems

Ratings:
  0 = gave_up  → next review in 1 day
  1 = hard     → next review in 3 days
  2 = okay     → next review in 7 days
  3 = easy     → next review in 14 days
  (subsequent reviews scale by ease factor)
"""

import json
import argparse
import sys
from datetime import date, timedelta
from pathlib import Path

QUEUE_FILE = Path(__file__).parent / "queue.json"

RATING_LABELS = {0: "gave_up", 1: "hard", 2: "okay", 3: "easy"}

# First-time review intervals (days)
INITIAL_INTERVALS = {0: 1, 1: 3, 2: 7, 3: 14}


def load_queue() -> dict:
    if not QUEUE_FILE.exists():
        return {"metadata": {}, "problems": []}
    with open(QUEUE_FILE) as f:
        return json.load(f)


def save_queue(data: dict) -> None:
    with open(QUEUE_FILE, "w") as f:
        json.dump(data, f, indent=2, default=str)


def calculate_next_interval(interval: int, ease_factor: float, rating: int) -> tuple:
    """
    SM-2 variant. Returns (new_interval_days, new_ease_factor).

    EF stays between 1.3 and 2.5.
    - gave_up: reset to 1 day, EF drops
    - hard:    small multiplier, EF drops slightly
    - okay:    standard SM-2 multiplier
    - easy:    boosted multiplier, EF rises slightly
    """
    if rating == 0:  # gave_up
        return 1, max(1.3, ease_factor - 0.2)
    elif rating == 1:  # hard
        return max(1, int(interval * 1.2)), max(1.3, ease_factor - 0.15)
    elif rating == 2:  # okay
        return max(1, int(interval * ease_factor)), ease_factor
    else:  # easy
        return max(1, int(interval * ease_factor * 1.3)), min(2.5, ease_factor + 0.15)


def find_problem(data: dict, problem_id: str) -> dict | None:
    return next((p for p in data["problems"] if p["id"] == problem_id), None)


def cmd_add(args) -> None:
    data = load_queue()

    if find_problem(data, args.problem_id):
        print(f"Problem '{args.problem_id}' already exists.")
        sys.exit(1)

    problem = {
        "id": args.problem_id,
        "name": args.name,
        "type": args.type,       # "dsa" or "sql"
        "topic": args.topic,     # "arrays", "two-pointers", "window-functions", etc.
        "difficulty": args.difficulty,  # "easy", "medium", "hard"
        "url": getattr(args, "url", ""),
        "added": date.today().isoformat(),
        "reviews": [],
        "current_interval": 1,
        "ease_factor": 2.5,
        "next_review": None,
        "last_reviewed": None,
    }

    data["problems"].append(problem)
    save_queue(data)
    print(f"✓ Added '{args.name}' to queue.")


def cmd_review(args) -> None:
    data = load_queue()
    problem = find_problem(data, args.problem_id)

    if not problem:
        print(f"Problem '{args.problem_id}' not found. Add it first with: srs.py add ...")
        sys.exit(1)

    rating = args.rating
    today = date.today().isoformat()
    reviews = problem.get("reviews", [])
    is_first = len(reviews) == 0

    current_interval = problem.get("current_interval", 1)
    ease_factor = problem.get("ease_factor", 2.5)

    if is_first:
        new_interval = INITIAL_INTERVALS[rating]
        new_ef = ease_factor
        # Adjust EF on first review too
        if rating == 0:
            new_ef = max(1.3, ease_factor - 0.2)
        elif rating == 1:
            new_ef = max(1.3, ease_factor - 0.15)
        elif rating == 3:
            new_ef = min(2.5, ease_factor + 0.15)
    else:
        new_interval, new_ef = calculate_next_interval(current_interval, ease_factor, rating)

    next_review = (date.today() + timedelta(days=new_interval)).isoformat()
    notes = getattr(args, "notes", "")

    review_entry = {
        "date": today,
        "rating": rating,
        "rating_label": RATING_LABELS[rating],
        "interval_days": new_interval,
        "next_review": next_review,
        "notes": notes,
    }

    problem["reviews"].append(review_entry)
    problem["current_interval"] = new_interval
    problem["ease_factor"] = round(new_ef, 3)
    problem["next_review"] = next_review
    problem["last_reviewed"] = today

    save_queue(data)

    label = RATING_LABELS[rating].upper()
    print(f"✓ [{label}] '{problem['name']}' — next review in {new_interval} day(s) ({next_review})")


def cmd_due(args) -> None:
    data = load_queue()
    today = date.today().isoformat()

    due = []
    for p in data["problems"]:
        next_review = p.get("next_review")
        # Due if: never reviewed, or next_review is today or earlier
        if not p.get("reviews") or (next_review and next_review <= today):
            due.append(p)

    if not due:
        print("✓ No problems due today.")
        return

    print(f"\n{'='*50}")
    print(f"  {len(due)} problem(s) due for review")
    print(f"{'='*50}")
    for p in due:
        reviews_done = len(p.get("reviews", []))
        last = p.get("last_reviewed", "never")
        status = "NEW" if reviews_done == 0 else f"review #{reviews_done + 1}"
        print(f"  [{p['type'].upper()} | {p['topic']}] {p['name']} ({p['difficulty']}) — {status}")
        if p.get("url"):
            print(f"    {p['url']}")
    print()


def cmd_stats(args) -> None:
    data = load_queue()
    problems = data["problems"]

    if not problems:
        print("No problems in queue yet.")
        return

    total = len(problems)
    reviewed = [p for p in problems if p.get("reviews")]
    dsa = [p for p in problems if p.get("type") == "dsa"]
    sql = [p for p in problems if p.get("type") == "sql"]

    all_ratings = []
    for p in problems:
        for r in p.get("reviews", []):
            all_ratings.append(r["rating"])

    avg_rating = sum(all_ratings) / len(all_ratings) if all_ratings else 0
    gave_up = all_ratings.count(0)
    easy = all_ratings.count(3)

    print(f"\n{'='*50}")
    print(f"  Study Stats")
    print(f"{'='*50}")
    print(f"  Total problems:  {total} ({len(dsa)} DSA, {len(sql)} SQL)")
    print(f"  Reviewed:        {len(reviewed)}")
    print(f"  Total reviews:   {len(all_ratings)}")
    print(f"  Avg rating:      {avg_rating:.2f} / 3.0")
    print(f"  Gave up:         {gave_up} ({100*gave_up//len(all_ratings) if all_ratings else 0}%)")
    print(f"  Easy:            {easy} ({100*easy//len(all_ratings) if all_ratings else 0}%)")
    print()


def cmd_list(args) -> None:
    data = load_queue()
    problems = data["problems"]

    if not problems:
        print("No problems in queue yet.")
        return

    today = date.today().isoformat()
    print(f"\n{'='*60}")
    print(f"  All Problems")
    print(f"{'='*60}")
    for p in problems:
        reviews = p.get("reviews", [])
        next_review = p.get("next_review", "—")
        status = "NEW" if not reviews else ("DUE" if next_review <= today else f"due {next_review}")
        print(f"  {p['id']:35s} [{p['type'].upper():3s}] {status}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Spaced Repetition System for DSA/SQL problems",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command")

    # due
    subparsers.add_parser("due", help="List problems due for review today")

    # stats
    subparsers.add_parser("stats", help="Show overall study stats")

    # list
    subparsers.add_parser("list", help="List all problems")

    # review
    review_p = subparsers.add_parser("review", help="Log a review for a problem")
    review_p.add_argument("problem_id", help="Problem ID (e.g. 'two-sum')")
    review_p.add_argument("rating", type=int, choices=[0, 1, 2, 3],
                          help="0=gave_up 1=hard 2=okay 3=easy")
    review_p.add_argument("--notes", default="", help="One-line notes about the session")

    # add
    add_p = subparsers.add_parser("add", help="Add a problem to the queue")
    add_p.add_argument("problem_id", help="Unique slug (e.g. 'two-sum')")
    add_p.add_argument("name", help="Full problem name")
    add_p.add_argument("type", choices=["dsa", "sql"], help="Problem type")
    add_p.add_argument("topic", help="Topic (e.g. 'arrays', 'window-functions')")
    add_p.add_argument("difficulty", choices=["easy", "medium", "hard"])
    add_p.add_argument("--url", default="", help="LeetCode or DataLemur URL")

    args = parser.parse_args()

    if args.command == "due":
        cmd_due(args)
    elif args.command == "review":
        cmd_review(args)
    elif args.command == "add":
        cmd_add(args)
    elif args.command == "stats":
        cmd_stats(args)
    elif args.command == "list":
        cmd_list(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
