"""Copy the 20 November 2026 world-news image to the output path.

The image is entry.png beside this file: a 1024x1024 original drawing
summarising six stories reported on 20 November 2026 -- Kyiv, the ICJ
Myanmar ruling, the Shenzhen summit, the EU-UK deal, Anthropic's fall,
and the Riyadh tower strike. The program writes it to
/output/entry.png, or to $MAKEFUN_OUTPUT_DIR/entry.png when that is set.
Standard library only, no network, deterministic: the same bytes every run.
"""
import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT = OUTPUT_DIR / "entry.png"


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)


if __name__ == "__main__":
    main()
