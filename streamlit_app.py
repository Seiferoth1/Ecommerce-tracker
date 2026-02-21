import streamlit as st
import pandas as pd
import time

# --- APP CONFIG ---
st.set_page_config(page_title="Resell Hero 2026", layout="wide")

# --- SIDEBAR: PROFIT CALCULATOR ---
st.sidebar.header("💰 Quick Profit Calc")
buy_price = st.sidebar.number_input("Buy Price ($)", value=10.0)
sell_price = st.sidebar.number_input("Target Sell Price ($)", value=50.0)
platform_fee = st.sidebar.slider("Platform Fee %", 0, 20, 13) # eBay avg is ~13%

profit = sell_price - buy_price - (sell_price * (platform_fee/100))
st.sidebar.metric("Estimated Profit", f"${profit:.2f}")

# --- MAIN INTERFACE ---
st.title("🚀 Resell Market Analyzer")
st.subheader("Partner View: Comp Search & Market Health")

query = st.text_input("Enter Item Name (e.g. Vintage Nike Windbreaker)", "")

if query:
    with st.spinner(f"Searching marketplaces for '{query}'..."):
        time.sleep(1.5) # Simulating API call speed
        
        # Mock Data (This is where the eBay API will plug in next)
        data = {
            "Item Title": [f"{query} - Excellent", f"{query} Blue", f"{query} Used"],
            "Price Sold": [45.00, 38.50, 29.00],
            "Date Sold": ["2026-02-15", "2026-02-12", "2026-02-10"],
            "Seller": ["PowerSeller99", "ThriftKing", "GarageSaleGuy"]
        }
        df = pd.DataFrame(data)
        
        # --- MARKET HEALTH METRICS ---
        col1, col2, col3 = st.columns(3)
        col1.metric("Avg Sold Price", f"${df['Price Sold'].mean():.2f}")
        col2.metric("Market Demand", "High 🔥")
        col3.metric("Sell-Through Rate", "65%")

        st.write("### Recent Sold Listings")
        st.dataframe(df, use_container_width=True)
        
        st.success("Analysis Complete. This looks like a 'Buy'!")
else:
    st.info("👋 Hey partner! Enter an item above to see if it's worth picking up.")

# --- FOOTER ---
st.divider()
st.caption("2026 Resell App v1.0 | Connected to Cloud Engine")