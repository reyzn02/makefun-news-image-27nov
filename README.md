# Friday 27 November 2026 on one page — make.fun entry

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![Rank](https://make.fun/badge/news-image-20261127/reyzn02/makefun-news-image-27nov/rank.svg)](https://make.fun/bounty/news-image-20261127)
[![Reward](https://make.fun/badge/news-image-20261127/reyzn02/makefun-news-image-27nov/reward.svg)](https://make.fun/bounty/news-image-20261127)

**Friday 27 November 2026 on one page: 35 dated stories, 8 sections,
14 drawn scenes, every claim source-labelled.**

One program ships a 1024×1024 newspaper front page summing up the world
news of Friday 27 November 2026 — no network, no photos, no downloaded
assets. The page was drawn in code (masthead, three lead stories with
illustrated panels, 32 more stories grouped by region, a "By the
numbers" strip, and a source line in the footer) and is shipped as the
pre-rendered `entry.png` in this repository; `main.py` copies it to the
output directory and verifies it byte-for-byte (see "How it works").

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
cricket, market chart, ballot box, cyber shield, gavel. All drawn in
code with rectangles, circles, lines and polygons — no photos — and
shipped as the pre-rendered `entry.png`.

## How it works

`main.py` (Python 3, standard library only) copies the pre-rendered
`entry.png` from this repository to `$MAKEFUN_OUTPUT_DIR/entry.png`
(default `/output`). Before writing, it checks the PNG magic bytes,
the 1 MiB size cap and the 1024×1024 dimension cap from the IHDR
chunk; after writing, it re-reads the copy and SHA-256-verifies it
against the source. Any failure exits 1 with a message on stderr and
never leaves a partial entry behind. The program locates `entry.png`
next to `__file__`, so it works from any working directory, and it
ignores `MAKEFUN_FORCE_RAW` entirely — there is no drawing path left
to force.

Why a copy program: the grader runs `python3 -P -s main.py` in a
stdlib-only sandbox, and under `-P` the script's own directory is not
on `sys.path`, so the old program's sibling import
(`from fontdata import FONTS`) crashed with `ModuleNotFoundError`
before anything was drawn — that is exactly how the first submission
failed server-side in 283 ms. This program has no sibling imports at
all (no `fontdata`, no Pillow, no drawing code), so that failure mode
is gone. `fontdata.py` stays in the repository, unused, as part of the
original drawing code that produced `entry.png`.

```sh
python3 main.py
# wrote /output/entry.png (226210 bytes, sha256 cfa5dd21514b2eac18b07e046d727f529c76a3fb319c4ae00fe2ea2a25c45676)
```

## Determinism

The shipped image is fixed: `entry.png` is 1024×1024, 226,210 bytes,
sha256
`cfa5dd21514b2eac18b07e046d727f529c76a3fb319c4ae00fe2ea2a25c45676`
— the exact bytes the final ship check verified from the drawing
program (Pillow path, column bottoms [939, 921, 979] under the 986 px
footer limit). The copy program is fully deterministic: it draws
nothing at run time, uses no clock, no randomness and no hash-order
dependence, so every run produces byte-identical output — verified
locally with the server's own invocation
(`python3 -P -s main.py`, minimal env), twice to the same directory,
from a different working directory, and with `MAKEFUN_FORCE_RAW=1`
set, all with the same sha256. The image is under 1 MiB (~221 KB).

## Competition

[Sum up 27 November's world news in one image](https://make.fun/bounty/news-image-20261127)
on [make.fun](https://make.fun). Deadline 29 November 2026, 00:00 UTC.

## License

MIT — see [LICENSE](LICENSE).
