import streamlit as st
import pandas as pd
from datetime import datetime
import requests

# -----------------------
# Functions
# -----------------------
def fetch_news():
    """
    Replace this with your actual news source or API.
    For demo, we return dummy news data.
    """
    news_data = [
        {"time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "headline": "EUR/JPY hits 5-year high", "details": "Momentum strong, breakout expected."},
        {"time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "headline": "USD/JPY weakens on inflation report", "details": "Traders cautious, volatility expected."}
    ]
    return pd.DataFrame(news_data)

# -----------------------
# Streamlit Layout
# -----------------------
st.set_page_config(page_title="Macro News Dashboard", layout="wide")
st.title("Macro News Dashboard 📈")

# Sidebar for explanations
st.sidebar.header("Explanation / Analysis")
st.sidebar.write("""
This panel explains what’s happening with the news data.
- You can add your trading commentary here.
- Highlight key events or important news releases.
""")

# Main: Button to fetch news
if st.button("Fetch Latest News"):
    st.info("Fetching latest news...")
    news_df = fetch_news()
    st.success("News fetched successfully!")
    st.dataframe(news_df)
else:
    st.write("Press the button above to fetch the latest news.")
