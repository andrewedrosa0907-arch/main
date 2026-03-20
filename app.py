============
st.set_page_config(layout="wide")
st.title("📊 Macro Scalper Dashboard")

# ================= SIDEBAR =================
st.sidebar.header("📰 News / Macro Context")

news_input = st.sidebar.text_area(
    "Paste Latest News (from Forex Factory, etc):",
    height=200
)

if news_input:
    st.sidebar.subheader("🧠 News Breakdown")
    
    # VERY basic interpretation logic (you can upgrade this later)
    if "inflation" in news_input.lower():
        st.sidebar.write("➡️ Inflation mentioned → Hawkish bias (currency strength)")
    elif "rate cut" in news_input.lower():
        st.sidebar.write("➡️ Rate cuts → Bearish currency bias")
    elif "rate hike" in news_input.lower():
        st.sidebar.write("➡️ Rate hikes → Bullish currency bias")
    else:
        st.sidebar.write("➡️ Mixed / unclear macro signal")

# ================= MAIN INPUT =================
st.subheader("🔎 Pair Analysis")

pair = st.text_input("Enter Forex Pair (ex: EURUSD, GBPJPY):")

# Map forex pair to Yahoo Finance format
def format_pair(pair):
    if pair.endswith("JPY"):
        return pair + "=X"
    return pair + "=X"

# ================= BUTTON TRIGGER =================
if st.button("Run Analysis"):

    if pair == "":
        st.warning("Enter a pair first.")
    else:
        ticker = format_pair(pair)

        data = yf.download(ticker, period="1d", interval="1m")

        if data.empty:
            st.error("Could not fetch data.")
        else:
            price = data["Close"].iloc[-1]
            prev_price = data["Close"].iloc[-10]

            # ================= MOMENTUM LOGIC =================
            if price > prev_price:
                momentum = "BULLISH 📈"
            elif price < prev_price:
                momentum = "BEARISH 📉"
            else:
                momentum = "INDECISIVE ⚖️"

            # ================= DISPLAY =================
            col1, col2 = st.columns(2)

            with col1:
                st.metric("Current Price", round(price, 5))
                st.metric("Momentum", momentum)

            with col2:
                st.subheader("📊 Price Data")
                st.line_chart(data["Close"])

            # ================= EXTRA CONTEXT =================
            st.subheader("🧠 Trade Insight")

            if momentum == "BULLISH 📈":
                st.write("Buyers currently in control — look for pullbacks to enter longs.")
            elif momentum == "BEARISH 📉":
                st.write("Sellers in control — look for rallies to enter shorts.")
            else:
                st.write("Market is consolidating — avoid overtrading.")
