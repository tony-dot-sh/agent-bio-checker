# bio_checker.py
import requests
from bs4 import BeautifulSoup
from difflib import SequenceMatcher
from config import PLATFORM_RULES

HEADERS = {"User-Agent": "Mozilla/5.0"}

def extract_bio(url):
    domain = next((d for d in PLATFORM_RULES if d in url), None)
    if not domain:
        return None, f"No rule for {url}"

    rule = PLATFORM_RULES[domain]
    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        tag = soup.find(rule["tag"], class_=rule["class"])
        return (tag.get_text(strip=True) if tag else None), None
    except Exception as e:
        return None, str(e)

def compare_bios(master, target):
    return SequenceMatcher(None, master, target).ratio()

def scrape_and_compare(urls, master_bio):
    results = []
    for url in urls:
        bio, error = extract_bio(url)
        if error:
            results.append({
                "url": url,
                "bio": None,
                "match_score": 0.0,
                "status": "⚠️ Error",
                "error": error
            })
        elif bio:
            score = round(compare_bios(master_bio, bio), 2)
            results.append({
                "url": url,
                "bio": bio,
                "match_score": score,
                "status": "✅ Match" if score > 0.9 else "❌ Mismatch",
                "error": None
            })
        else:
            results.append({
                "url": url,
                "bio": None,
                "match_score": 0.0,
                "status": "⚠️ Not Found",
                "error": "No bio tag found"
            })
    return results
