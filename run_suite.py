#!/usr/bin/env python3
"""
Run the thermostat eval against a suite of models served by OpenRouter.

Requires OPENROUTER_API_KEY in your environment.

Run:
    python run_suite.py --suite popular
    python run_suite.py --suite free --max-tasks 1
    python run_suite.py --suite all
"""

import argparse
import os
import sys

from inspect_ai import eval

from eval.suites import SUITES
from eval.task import thermostat_control


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--suite",
        choices=sorted(SUITES),
        default="all",
        help="Which model suite to run (default: all).",
    )
    parser.add_argument(
        "--max-tasks",
        type=int,
        default=4,
        help="Models to evaluate in parallel (default: 4). Lower this for free tiers.",
    )
    args = parser.parse_args()

    if not os.environ.get("OPENROUTER_API_KEY"):
        sys.exit("OPENROUTER_API_KEY is not set.")

    models = [f"openrouter/{model}" for model in SUITES[args.suite]]
    print(f"Running suite '{args.suite}' with {len(models)} model(s)...\n")

    logs = eval(thermostat_control(), model=models, max_tasks=args.max_tasks)

    print("\nSummary:")
    for log in logs:
        print(f"  {log.eval.model:<70} {log.status}")


if __name__ == "__main__":
    main()
