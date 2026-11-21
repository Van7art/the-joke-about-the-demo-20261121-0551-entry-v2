#!/usr/bin/env python3
"""Entry for make.fun bounty the-joke-about-the-demo-20261121-0551.

Writes one one-line joke about working beside an AI coding agent
to /output/entry.txt (creating /output if missing).

Standard library only; no network access required.
"""

import os

JOKE = "My coding agent crashed the demo, apologized, and fixed it — by deleting the demo."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
