"""Fetch current price + daily change for the hub's ticker tape.

Tied to tickers already named elsewhere on the site: SPY (market benchmark)
and the 11 GICS sector SPDRs from Regime Classifier, plus GOOGL/TSLA/BE from
Causal Toolkit's case studies. No API key needed (yfinance scrapes Yahoo's
public quote endpoints). Run on a schedule via .github/workflows/update-ticker.yml,
not continuously — this is a periodic snapshot, not a real-time feed.
"""
import json
import sys
from datetime import datetime, timezone

import yfinance as yf

TICKERS = [
    "SPY",
    "XLK", "XLF", "XLV", "XLE", "XLI", "XLY", "XLP", "XLU", "XLB", "XLRE", "XLC",
    "GOOGL", "TSLA", "BE",
]

OUT_PATH = "data/ticker.json"


def main():
    quotes = []
    for sym in TICKERS:
        try:
            info = yf.Ticker(sym).fast_info
            last = float(info["last_price"])
            prev = float(info["previous_close"])
            chg = (last - prev) / prev * 100
            quotes.append({"symbol": sym, "price": round(last, 2), "change_pct": round(chg, 2)})
        except Exception as e:
            print(f"skip {sym}: {e}", file=sys.stderr)

    if not quotes:
        print("no quotes fetched, leaving existing data/ticker.json untouched", file=sys.stderr)
        sys.exit(1)

    out = {
        "updated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "quotes": quotes,
    }
    with open(OUT_PATH, "w") as f:
        json.dump(out, f, indent=2)
    print(f"wrote {len(quotes)} quotes to {OUT_PATH}")


if __name__ == "__main__":
    main()
