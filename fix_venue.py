"""Remove years from Venue column in survey table rows."""

import re
from pathlib import Path

ROOT = Path(__file__).parent
VENUES = (
    "CoRL", "ICLR", "NeurIPS", "ICRA", "RSS", "CVPR", "IROS", "ICML",
    "ECCV", "AAAI", "ICCV", "HRI", "IJRR", "RA-L", "IEEE T-RO",
    "Science Robotics", "Info. Fusion", "3DV",
)
VENUE_PAT = "|".join(re.escape(v) for v in VENUES)

for name in ["survey.md", "survey_ko.md"]:
    p = ROOT / name
    if not p.exists():
        continue
    text = p.read_text(encoding="utf-8")
    text = re.sub(
        rf"\| ({VENUE_PAT}) (\d{{4}})(.*?) \|",
        lambda m: f"| {m.group(1)}{' ' + m.group(3).strip() if m.group(3).strip() else ''} |",
        text,
    )
    p.write_text(text, encoding="utf-8")
    print(f"Processed {name}")
