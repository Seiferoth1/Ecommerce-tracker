import streamlit as st
import pandas as pd
from datetime import datetime

# --- CONFIG ---
st.set_page_config(page_title="Resell Pro 2026", layout="wide", initial_sidebar_state="expanded")

# --- STYLE ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_value=True)

# --- IN-MEMORY DATABASE (Simulated) ---
if 'inventory' not in st.session_state:
    st.session_state.inventory = []

# --- SIDEBAR: NEW PURCHASE LOG ---
with st.sidebar:
    st.header("📸 Quick Log Item")
    # This uses the phone's camera if opened on mobile!
    picture = st.camera_input("Take a photo of the tag")
    
    item_name = st.text_input("Item Name")
    cost = st.number_input("What did you pay?", min_value=0.0, step=1.0)
    est_sell = st.number_input("Est. Sell Price", min_value=0.0, step=1.0)
    
    if st.button("✅ Save to Inventory"):
        new_item = {
            "Date": datetime.now().strftime("%Y-%m-%d"),
            "Item": item_name,
            "Cost": cost,
            "Est. Sell": est_sell,
            "Potential Profit": est_sell - cost - (est_sell * 0.13) # Minus 13% eBay fee
        }
        st.session_state.inventory.append(new_item)
        st.success("Item Saved!")

# --- MAIN DASHBOARD ---
st.title("🚀 Resell Partner Dashboard")

# Top Level Stats
if st.session_state.inventory:
    df_inv = pd.DataFrame(st.session_state.inventory)
    col1, col2, col3 = st.columns(3)
    col1.metric("Items Sourced Today", len(df_inv))
    col2.metric("Total Capital Spent", f"${df_inv['Cost'].sum():.2f}")
    col3.metric("Projected Profit", f"${df_inv['Potential Profit'].sum():.2f}", delta_color="normal")

# Comp Search Section
st.divider()
st.subheader("🔍 Market Research")
search_query = st.text_input("Search Market Comps (eBay Simulation)", placeholder="e.g. Vintage 90s Disney Shirt")

if search_query:
    # Mock Market Data logic (will be replaced by eBay API tomorrow)
    st.info(f"Showing simulated results for '{search_query}'")
    mock_comps = pd.DataFrame({
        "Date Sold": ["Today", "Yesterday", "2 days ago"],
        "Price": [45.0, 32.0, 38.5],
        "Condition": ["Used", "New", "Used"]
    })
    st.table(mock_comps)

# Inventory List
st.divider()
st.subheader("📋 Sourcing Log (Current Session)")
if st.session_state.inventory:
    st.dataframe(pd.DataFrame(st.session_state.inventory), use_container_width=True)
else:
    st.write("No items logged yet. Use the sidebar to add your first find!")