#!/usr/bin/env python3
"""Write entry.html: the newspaper front page that is rendered to entry.png."""

STORIES = [
    (
        "RUSSIA AND NATO",
        "Moscow warns of preventive nuclear strike",
        "Medvedev warns of a preventive nuclear attack as NATO vows to defend "
        "space amid reports of a Russian nuclear-armed satellite launch.",
    ),
    (
        "MYANMAR",
        "Court rules Myanmar committed genocide",
        "The International Court of Justice rules Myanmar committed genocide "
        "against the Rohingya.",
    ),
    (
        "RIYADH",
        "Houthi attack hits Riyadh tower, 11 hurt",
        "A Houthi attack on a financial district tower injures 11; Saudi "
        "Arabia condemns a terrorist attack.",
    ),
    (
        "GAZA",
        "Gaza strikes kill Hamas security chief",
        "Israeli strikes kill Hamas security chief Naeem Abu Nahal and six "
        "others despite the ceasefire.",
    ),
    (
        "NVIDIA",
        "Huang returns as Nvidia chief executive",
        "Jensen Huang is reinstated as CEO after Trump intervenes and tells "
        "staff he made terrible mistakes.",
    ),
    (
        "CLIMATE",
        "UN climate summit ends with no deal",
        "The summit closes in failure after a split over fossil fuels and "
        "climate finance.",
    ),
    (
        "CONGO",
        "Fighting traps Ebola teams in Ituri",
        "Heavy fighting traps Ebola responders in eastern DR Congo, the WHO "
        "says.",
    ),
]

FOOT = (
    "All events of Tuesday 24 November 2026. Sources: BBC, Reuters, SCMP, "
    "Arab News, UN News."
)

CSS = """
@page { margin: 0; size: 1024px 1024px; }
html, body { margin: 0; padding: 0; }
body {
  width: 1024px; height: 1024px; box-sizing: border-box; overflow: hidden;
  background: #ffffff; color: #0c1a3a;
  font-family: 'DejaVu Sans', sans-serif;
  padding: 30px 54px 18px;
  display: flex; flex-direction: column;
}
.mast {
  flex: none;
  font-size: 39px; font-weight: bold; letter-spacing: 8px; text-align: center;
  border-top: 6px solid #0c1a3a; border-bottom: 5px solid #0c1a3a;
  padding: 8px 0 11px;
}
.date { flex: none; font-size: 47px; font-weight: bold; text-align: center;
  margin: 11px 0 3px; }
.stand { flex: none; font-size: 23px; font-style: italic; text-align: center;
  margin: 0 0 13px; border-bottom: 2px solid #0c1a3a; padding-bottom: 12px; }
.lead { flex: none; padding-bottom: 10px; border-bottom: 1px solid #b9c0cd; }
.briefs {
  flex: 1; min-height: 0; display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: auto auto auto;
  column-gap: 34px; row-gap: 0;
  align-content: start;
}
.brief.b0 { grid-column: 1; grid-row: 1; }
.brief.b1 { grid-column: 1; grid-row: 2; }
.brief.b2 { grid-column: 1; grid-row: 3; }
.brief.b3 { grid-column: 2; grid-row: 1; }
.brief.b4 { grid-column: 2; grid-row: 2; }
.brief.b5 { grid-column: 2; grid-row: 3; }
.kick { font-size: 17px; font-weight: bold; text-transform: uppercase;
  letter-spacing: 2px; color: #b3121b; margin: 0 0 6px; }
.head { font-size: 31px; font-weight: bold; line-height: 1.1; margin: 0 0 5px; }
.fact { font-size: 20px; line-height: 1.26; margin: 0; }
.lead .head { font-size: 46px; line-height: 1.14; margin-bottom: 8px; }
.lead .fact { font-size: 22px; line-height: 1.34; }
.briefs .story { overflow: hidden; }
.briefs .b0, .briefs .b1 { padding-bottom: 14px; }
.foot { flex: none; font-size: 15px; text-align: center;
  border-top: 2px solid #0c1a3a; padding-top: 10px; margin-top: 10px; }
"""


def block(story, cls):
    kicker, head, fact = story
    return (
        "<div class='story %s'>" % cls
        + "<div class='kick'>%s</div>" % kicker
        + "<div class='head'>%s</div>" % head
        + "<div class='fact'>%s</div>" % fact
        + "</div>"
    )


def main():
    parts = [
        "<!DOCTYPE html>",
        "<html><head><meta charset='utf-8'>",
        "<style>",
        CSS,
        "</style></head><body>",
        "<div class='mast'>THE WORLD IN ONE PAGE</div>",
        "<div class='date'>TUESDAY 24 NOVEMBER 2026</div>",
        "<div class='stand'>The day in seven stories</div>",
        "<div class='lead'>" + block(STORIES[0], "lead-story") + "</div>",
        "<div class='briefs'>",
    ]
    for i, story in enumerate(STORIES[1:]):
        parts.append(block(story, "brief b%d" % i))
    parts.append("</div>")
    parts.append("<div class='foot'>%s</div>" % FOOT)
    parts.append("</body></html>")
    with open("entry.html", "w", encoding="utf-8") as f:
        f.write("".join(parts))


if __name__ == "__main__":
    main()
