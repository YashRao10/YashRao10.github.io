# YR Hub

Live at **[yashrao10.github.io](https://yashrao10.github.io)**

Built and maintain a public portfolio site that brings every live tool and finished project
I've shipped into one place. The site has an editorial dark-theme design and a live stock
ticker that pulls real sector and market data every 30 minutes, along with project tiles
that link out to specific case studies. I kept one strict rule throughout: no dollar amounts
or position sizes shown anywhere. I owned the full build myself, from the design system to
deployment to ongoing maintenance, including a real performance investigation where I traced
a rendering slowdown back to a specific browser behavior instead of the more obvious
suspects like animation count or speed.

## What's hosted here

- `index.html` — the hub
- `causal-toolkit/` — synthetic-control event-study case studies (rendered reports)
- `factor-decomposition/` — per-holding market / sector / rate factor breakdowns
- `fred-nowcast/` — GDP bridge-equation nowcast
- `scripts/`, `data/` — the ticker-data refresh pipeline

Static site, deployed on GitHub Pages.
