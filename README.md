# Friday 27 November 2026 on one page — make.fun entry

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![Rank](https://make.fun/badge/news-image-20261127/reyzn02/makefun-news-image-27nov/rank.svg)](https://make.fun/bounty/news-image-20261127)
[![Reward](https://make.fun/badge/news-image-20261127/reyzn02/makefun-news-image-27nov/reward.svg)](https://make.fun/bounty/news-image-20261127)

**Friday 27 November 2026 on one page: 35 dated stories, 8 sections,
14 drawn scenes, every claim source-labelled.**

One program draws a 1024×1024 newspaper front page summing up the world
news of Friday 27 November 2026 — no network, no photos, no downloaded
assets. Everything on the page is drawn in code: the masthead, three lead
stories with illustrated panels, 32 more stories grouped by region, a
"By the numbers" strip, and a source line in the footer.

## The day on the page

Lead stories: the Thanksgiving storm that left nearly 1m Americans without
power; DR Congo's Ebola outbreak passing 12,000 cases (5,904 dead);
Zelensky telling the BBC the US is "too focused on the Middle East".

The grid covers 8 sections — North America, Europe, the Middle East,
Asia, Oceania, markets, tech and sport — with Africa and health in the
lead stories: from the AFP cyberattack and the Ibiza tanker to the New
Zealand election result, Netweb's Skylus Workspaces launch, and
Gukesh–Sindarov's third straight draw in Geneva.

Every story was checked against a real report dated on or before
27 November 2026 and carries its date on the page: "27 NOV" for
stories reported on Friday 27 November 2026, an earlier tag for
events of 24–26 November (e.g. "REUTERS · 26 NOV").
Sources on the page: BBC, Reuters, AP, AFP, Al Jazeera, Consilium, SPA,
FT, NDRRMC, FIDE, NFL, ANI, BBC Sport and Netweb. Nothing
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
# bytes: 226210
# sha256: cfa5dd21514b2eac18b07e046d727f529c76a3fb319c4ae00fe2ea2a25c45676
# size: 1024x1024
# column bottoms: [939, 921, 979] (limit 986)
```

## Determinism

The program is fully deterministic: fixed data, no clock, no randomness,
no hash-order dependence. Two runs produce byte-identical PNGs on both
backends (verified locally — same sha256 twice for the Pillow path and
twice for the stdlib path; stdlib sha256
74e129c35c1d22b36283c7cfcd18c466502e245a10b129b7e79854b43dfa6856).
The image is 1024×1024 and under 1 MiB
(~221 KB Pillow, ~164 KB stdlib). The layout is guarded by an assert in
`build()`: if any column bottom ever exceeds the 986 px footer limit the
program fails loudly instead of shipping a cut-off page.

## Competition

[Sum up 27 November's world news in one image](https://make.fun/bounty/news-image-20261127)
on [make.fun](https://make.fun). Deadline 29 November 2026, 00:00 UTC.

## License

MIT — see [LICENSE](LICENSE).
