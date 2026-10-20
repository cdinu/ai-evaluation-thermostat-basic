from pathlib import Path

from .scenarios import load_scenarios, SCENARIO_DIR


def main():
    """List available scenarios."""
    scenarios = load_scenarios()
    print(f"Found {len(scenarios)} scenario(s) in {SCENARIO_DIR}:\n")
    for scenario in scenarios:
        print(f"  {scenario.id:<40} {scenario.title}")
        print(f"    Attack class: {scenario.attack_class}, Tags: {', '.join(scenario.tags)}\n")


if __name__ == "__main__":
    main()
