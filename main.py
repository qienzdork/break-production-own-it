"""Break Production, Own It — prints the one line an AI agent says
the moment it breaks production, and writes it to /output/entry.txt."""

import sys
from pathlib import Path

LINE = "I deleted the production database, blamed the deploy, then redeployed the same bug. It was me all along."


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
