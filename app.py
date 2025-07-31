# app.py
import streamlit as st
from bio_checker import scrape_and_compare

st.set_page_config(page_title="Agent Bio Checker", layout="wide")

st.title("🕵️ Agent Bio Consistency Checker")
st.markdown("Paste your profile URLs below and compare your bios across platforms.")

default_bio = """Helping West Coast buyers relocate to Boise and thrive in our community through outdoor living, safe neighborhoods, and intentional lifestyle choices."""

master_bio = st.text_area("✍️ Master Bio", value=default_bio, height=150)
urls_input = st.text_area("🔗 Profile URLs (one per line)", height=200)

if st.button("🔍 Check My Bios"):
    urls = [url.strip() for url in urls_input.splitlines() if url.strip()]
    results = scrape_and_compare(urls, master_bio)

    for r in results:
        st.markdown(f"### [{r['url']}]({r['url']})")
        st.markdown(f"**Status:** {r['status']} &nbsp;&nbsp;&nbsp; **Match Score:** `{r['match_score']}`")
        if r['error']:
            st.warning(f"Error: {r['error']}")
        elif r['bio']:
            with st.expander("🔍 View Bio"):
                st.text(r['bio'])
        st.markdown("---")
