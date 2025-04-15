
import streamlit as st
from utils.phishing_checker import check_link_safety
from utils.db import create_table, log_url_check, get_recent_logs

st.set_page_config(page_title="Cyber Guardian", layout="wide")
st.title("🛡️ Cyber Guardian - Phishing Link Checker")

# Initialize DB table
create_table()

st.markdown("### Paste a suspicious link to check for phishing:")
url = st.text_input("Enter URL")

if url:
    result = check_link_safety(url)
    st.write(f"**Verdict:** {result['verdict']}")
    st.write(f"**Reason:** {result['reason']}")
    log_url_check(url, result['verdict'], result['reason'])

    st.markdown("---")
    st.subheader("🕓 Recent URL Checks")
    logs = get_recent_logs()
    for row in logs:
        st.write(f"{row[3]} | {row[0]} → {row[1]} ({row[2]})")
