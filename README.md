# The World in One Page

A 1024 by 1024 newspaper front page that sums up the world news of Tuesday
24 November 2026 in seven stories, one lead and six briefs, on white paper
with dark navy type and a single red accent for the kickers.

`main.py` copies `entry.png`, which sits beside it, to the directory named by
`MAKEFUN_OUTPUT_DIR` (or `/output` when that is unset), creating it if needed.
The image is rendered from `entry.html` with headless Chromium; `build.py`
writes that page.

Bounty: https://make.fun/bounty/news-image-20261124

## Stories and sources

| Kicker | Headline | Source |
| --- | --- | --- |
| RUSSIA AND NATO | Moscow warns of preventive nuclear strike | BBC / Reuters |
| MYANMAR | Court rules Myanmar committed genocide | Reuters |
| RIYADH | Houthi attack hits Riyadh tower, 11 hurt | Arab News / Reuters |
| GAZA | Gaza strikes kill Hamas security chief | Reuters |
| NVIDIA | Huang returns as Nvidia chief executive | Reuters |
| CLIMATE | UN climate summit ends with no deal | UN News |
| CONGO | Fighting traps Ebola teams in Ituri | SCMP / UN News |
