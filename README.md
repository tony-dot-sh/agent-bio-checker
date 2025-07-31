# 🕵️ Agent Bio Consistency Checker

A tool for real estate agents to audit their online bios across platforms like Zillow, Realtor.com, Homes.com, and Yelp. Built with Python and Streamlit.

## 🚀 Features
- Scrape bios from common agent profile pages
- Compare to a master bio
- Visual red/green status indicators
- Clean Streamlit UI — no coding required for end users

## 🛠 Tech Stack
- Python (requests, BeautifulSoup)
- Streamlit (frontend)
- JSON config for platform rules

## ✅ Getting Started

```bash
git clone https://github.com/tony-dot-sh/agent-bio-checker
cd agent-bio-checker
pip install -r requirements.txt
streamlit run app.py
