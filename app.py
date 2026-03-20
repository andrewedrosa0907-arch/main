import streamlit as st
import pandas as pd
from datetime import datetime

# -----------------------
# Functions
# -----------------------
def fetch_news():
    """
    Replace this with your actual news source or API.
    For demo, we return dummy news data.
    """
    news_data = [
        {"time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
         "headline": "EUR/JPY hits 5-year high", 
         "details": "Momentum is strong; technical breakout expected. Watch resistance at 163.50."},
        {"time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
         "headline": "USD/JPY weakens on inflation report", 
         "details": "Traders are cautious due to weak CPI data. Support around 133.20."},
        {"time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
         "headline": "BoJ announces interest rate decision", 
         "details": "No change in rates. Yen remains stable; market reaction muted."}
    ]
    return pd.DataFrame(news_data)

# -----------------------
# Streamlit Layout
# -----------------------
st.set_page_config(page_title="Macro News Dashboard", layout="wide")
st.title("Macro News Dashboard 📊")

# Sidebar
st.sidebar.header("News Details / Analysis")
st.sidebar.write("Click on a news headline to see detailed explanation here.")

# Main: Button to fetch news
if st.button("Fetch Latest News"):
    st.info("Fetching latest news...")
    news_df = fetch_news()
    st.success("News fetched successfully!")
    
    # Show headlines as clickable
    for idx, row in news_df.iterrows():
        if st.button(row['headline'], key=idx):
            st.sidebar.subheader("Selected News")
            st.sidebar.write(f"**Time:** {row['time']}")
            st.sidebar.write(f"**Headline:** {row['headline']}")
            st.sidebar.write(f"**Details / Analysis:** {row['details']}")
else:
    st.write("Press the button above to fetch the latest news.")
