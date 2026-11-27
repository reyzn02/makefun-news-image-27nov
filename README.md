# Friday 27 November 2026 on one page — make.fun entry

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![Rank](https://make.fun/badge/news-image-20261127/reyzn02/makefun-news-image-27nov/rank.svg)](https://make.fun/bounty/news-image-20261127)
[![Reward](https://make.fun/badge/news-image-20261127/reyzn02/makefun-news-image-27nov/reward.svg)](https://make.fun/bounty/news-image-20261127)

**Friday 27 November 2026 on one page: 34 dated stories, 10 regions,
14 drawn scenes, every claim source-labelled.**

One program draws a 1024×1024 newspaper front page summing up the world
news of Friday 27 November 2026 — no network, no photos, no downloaded
assets. Everything on the page is drawn in code: the masthead, three lead
stories with illustrated panels, 31 more stories grouped by region, a
"By the numbers" strip, and a source line in the footer.

## The day on the page

Lead stories: the Thanksgiving storm that left nearly 1m Americans without
power; DR Congo's Ebola outbreak passing 12,000 cases (5,904 dead); Trump
pressing Putin on Ukraine as Zelensky tells the BBC the US is "too focused
on the Middle East".

The grid covers 10 regions and beats — North America, Europe, the Middle
East, Asia, Oceania, Africa, markets, tech, sport and health — from the
AFP cyberattack and the Ibiza tanker spill to the New Zealand election
result, the FCC clearing SpaceX's million-satellite network, and
Gukesh–Sindarov's third straight draw in Geneva.

Every story was checked against a real report dated 27 November 2026
(BBC, Reuters, AP, AFP/Al Jazeera, Anadolu, FT, WSJ, NDRRMC, FIDE, FIFA,
NFL). Stories about events of 25–26 November that were first reported on
the 27th carry their date on the page (e.g. "BBC · 26 NOV"). Nothing
unverified is included: the Mayon volcano item, for example, reports the
Alert Level 3 watch rather than an eruption, because no new eruption was
reported that day.

## Drawn scenes (14)

Storm cloud and lightning, Ebola virus, two-flag diplomacy, American
football, satellite, oil tanker, volcano, refinery flame, chess board,
cricket, market chart, ballot box, cyber shield, gavel. All drawn with
rectangles, circles, lines and polygons — no image files anywhere.

## How it works

`main.py` (Python 3, standard library only at run time) renders the page
through a small canvas abstraction with two backends that share the same
layout code:

- **Pillow + DejaVu** when available — the polished path.
- **A pure-stdlib rasterizer** (`RawCanvas`) when Pillow is absent, using
  grayscale bitmap fonts generated from DejaVu Sans (`fontdata.py`) and a
  hand-written PNG encoder (`zlib` + `struct`). This is the path a bare
  Python 3.13 sandbox takes, so the entry still runs and still looks like
  a newspaper there.

Output goes to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`).
Set `MAKEFUN_FORCE_RAW=1` to exercise the stdlib path locally.

```sh
python3 main.py
# wrote /output/entry.png
# bytes: 219346
# sha256: ee9b9cc40b87b74179ac8ff88a344dd7ffe0a768db23262867421e236d890412
# size: 1024x1024
```

## Determinism

The program is fully deterministic: fixed data, no clock, no randomness,
no hash-order dependence. Two runs produce byte-identical PNGs on both
backends (verified locally — same sha256 twice for the Pillow path and
twice for the stdlib path). The image is 1024×1024 and under 1 MiB
(~215 KB Pillow, ~165 KB stdlib).

## Competition

[Sum up 27 November's world news in one image](https://make.fun/bounty/news-image-20261127)
on [make.fun](https://make.fun). Deadline 29 November 2026, 00:00 UTC.

## License

MIT — see [LICENSE](LICENSE).
