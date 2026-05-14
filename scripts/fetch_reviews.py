#!/usr/bin/env python3
"""Fetch OpenReview scores and brief summaries for surveyed papers."""

import json
import re
import time
import urllib.request
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).parent.parent
DETAIL_DIR = ROOT / "content" / "detailed"
REVIEWS_PATH = ROOT / "reviews" / "data.json"
API = "https://api2.openreview.net"


def api_get(endpoint: str, params: dict) -> dict | None:
    qs = urllib.parse.urlencode(params)
    url = f"{API}{endpoint}?{qs}"
    req = urllib.request.Request(url, headers={"User-Agent": "survey-bot/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except Exception as e:
        print(f"    API error: {e}")
        return None


def search_paper(title: str) -> dict | None:
    clean = re.sub(r"[^\w\s]", "", title).strip()
    data = api_get("/notes/search", {"query": clean, "limit": 5})
    if not data or not data.get("notes"):
        return None
    for note in data["notes"]:
        ct = note.get("content", {})
        nt = ct.get("title", {}).get("value", "")
        if nt.lower().strip() == title.lower().strip():
            venue = ct.get("venue", {}).get("value", "")
            return {"id": note["id"], "forum": note.get("forum", note["id"]), "venue": venue}
        if title.lower()[:30] in nt.lower():
            venue = ct.get("venue", {}).get("value", "")
            return {"id": note["id"], "forum": note.get("forum", note["id"]), "venue": venue}
    return None


def get_reviews(forum_id: str) -> list[dict]:
    data = api_get("/notes", {"forum": forum_id, "limit": 50})
    if not data or not data.get("notes"):
        return []
    reviews = []
    for note in data["notes"]:
        invs = note.get("invitations", [])
        if not any("Official_Review" in inv for inv in invs):
            continue
        ct = note.get("content", {})
        rating = ct.get("rating", {}).get("value")
        confidence = ct.get("confidence", {}).get("value")
        summary = ct.get("summary", {}).get("value", "")
        strengths = ct.get("strengths", {}).get("value", "")
        if not strengths:
            strengths = ct.get("strengths_and_weaknesses", {}).get("value", "")
        if not summary:
            summary = ct.get("main_review", {}).get("value", "")

        r: dict = {}
        if rating is not None:
            r["rating"] = rating if isinstance(rating, (int, float)) else _extract_num(str(rating))
        if confidence is not None:
            r["confidence"] = confidence if isinstance(confidence, (int, float)) else _extract_num(str(confidence))
        if summary:
            r["summary"] = summary[:300].split("\n")[0]
        elif strengths:
            r["summary"] = strengths[:300].split("\n")[0]
        if r.get("rating") is not None or r.get("summary"):
            reviews.append(r)
    return reviews


def _extract_num(s: str) -> float | None:
    m = re.search(r"(\d+\.?\d*)", s)
    return float(m.group(1)) if m else None


def collect_papers() -> list[dict]:
    papers = []
    if not DETAIL_DIR.exists():
        return papers
    for sec_dir in sorted(DETAIL_DIR.iterdir()):
        if not sec_dir.is_dir():
            continue
        for md_file in sorted(sec_dir.glob("*.md")):
            if md_file.name.startswith("_"):
                continue
            text = md_file.read_text(encoding="utf-8", errors="replace")
            first = text.split("\n")[0]
            title = re.sub(r"^#+\s*(\d+(\.\d+)?\s+)?", "", first).strip()
            ft_match = re.search(r"\*\*Full [Tt]itle:\*\*\s*(.+)", text)
            full_title = ft_match.group(1).strip() if ft_match else ""
            key = re.sub(r"[^a-z0-9]", "", title.lower())
            papers.append({"key": key, "title": title, "full_title": full_title, "file": str(md_file.relative_to(ROOT))})
    return papers


def main():
    REVIEWS_PATH.parent.mkdir(exist_ok=True)
    existing: dict = {}
    if REVIEWS_PATH.exists():
        existing = json.loads(REVIEWS_PATH.read_text(encoding="utf-8"))

    papers = collect_papers()
    print(f"Found {len(papers)} papers in detailed_survey/")
    new_count = 0

    for i, p in enumerate(papers):
        key = p["key"]
        if key in existing:
            continue

        search_title = p["full_title"] or p["title"]
        print(f"[{i+1}/{len(papers)}] Searching: {p['title']}")

        result = search_paper(search_title)
        if not result:
            if p["full_title"] and p["full_title"] != p["title"]:
                result = search_paper(p["title"])
            if not result:
                existing[key] = {"found": False}
                time.sleep(1.5)
                continue

        forum_id = result["forum"]
        url = f"https://openreview.net/forum?id={forum_id}"
        print(f"  Found: {url}")

        time.sleep(1.5)
        reviews = get_reviews(forum_id)

        if reviews:
            ratings = [r["rating"] for r in reviews if r.get("rating") is not None]
            avg = round(sum(ratings) / len(ratings), 1) if ratings else None
            existing[key] = {
                "found": True,
                "url": url,
                "venue": result.get("venue", ""),
                "avg_rating": avg,
                "num_reviews": len(reviews),
                "reviews": reviews,
            }
            print(f"  {len(reviews)} reviews, avg rating: {avg}")
            new_count += 1
        else:
            existing[key] = {"found": True, "url": url, "venue": result.get("venue", ""), "reviews": []}
            print(f"  No reviews found (may be preprint)")
            new_count += 1

        REVIEWS_PATH.write_text(json.dumps(existing, indent=2, ensure_ascii=False), encoding="utf-8")
        time.sleep(2.0)

    print(f"\nDone. {new_count} new entries. Total: {len(existing)} papers in {REVIEWS_PATH}")


if __name__ == "__main__":
    main()
