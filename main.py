"""Copy entry.png, which sits beside this file, into the output directory."""

import os
import shutil
from pathlib import Path

here = Path(__file__).resolve().parent
output = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
output.mkdir(parents=True, exist_ok=True)
shutil.copyfile(here / "entry.png", output / "entry.png")
