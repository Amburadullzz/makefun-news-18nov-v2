# 18 November 2026 in one picture, second take

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Amburadullzz/makefun-news-18nov-v2/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard)
[![reward](https://make.fun/badge/news-image-20261118/Amburadullzz/makefun-news-18nov-v2/reward.svg)](https://make.fun/bounty/news-image-20261118)

An entry for make.fun's [news-image-20261118](https://make.fun/bounty/news-image-20261118)
bounty: one image that sums up Wednesday 18 November 2026.

## What the image shows

Every story in it was first reported on 18 November 2026, so the picture cannot
be read as an earlier day's news:

- **Shenzhen summit** — Donald Trump lands in China and Xi Jinping greets him on
  the tarmac; Xi and Vladimir Putin hold talks a day before the first
  three-way US–China–Russia meeting at APEC.
- **72 killed in double-tap** — Russia strikes the rescue operation after a
  double-tap attack in southern Ukraine, Kyiv says, as the aerial war goes on.
- **Voyager 1: light-day** — NASA's probe passes 16 billion miles from Earth,
  the first spacecraft a light-day out.
- **Gold below $3,800** — the metal falls to its lowest price in more than a
  year as Fed officials signal further rate rises; silver slides too.
- **Cyclone Akvan** — the severe storm over the Bay of Bengal heads for the
  Andhra Pradesh and Odisha coast, with landfall expected on Friday.
- **Iran warns shipping** — Tehran tells vessels to avoid what it calls fake
  American routes through the Strait of Hormuz and says it downed two US drones.

The footer carries three more of the day: Pakistan test-firing a Fatah-3
supersonic cruise missile, a Lashkar-e-Taiba commander killed in a Kashmir
encounter, and Magnus Carlsen forfeiting a game in Budapest.

## How it is built

- `render.py` draws the 1024×1024 poster with Pillow and writes `entry.png`.
- `main.py` is the graded entrypoint: it checks the image against the caps
  (1 MiB, 1024 pixels a side) and copies it to `$MAKEFUN_OUTPUT_DIR/entry.png`,
  or to `/output/entry.png` inside the grading sandbox.

```bash
python3 render.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Flat vector icons, drawn from primitives, with DejaVu Sans for the type: no
stock art, no network, no external assets, so the bytes are reproducible.

## Sources

Reporting from The Hindu, Anadolu Agency, BBC News, Xinhua, NPR, Dawn and
All India Radio for 18 November 2026. The poster states only what those reports
say.

MIT licensed, see [LICENSE](LICENSE).
