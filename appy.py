import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Financial Market Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Financial Market Dashboard")
st.write("Crypto, Oil & Stock Market Analysis")

bitcoin = pd.read_csv("bitcoin_prices.csv")
ethereum = pd.read_csv("ethereum_prices.csv")
tether = pd.read_csv("tether_prices.csv")
oil = pd.read_csv("oil_prices.csv")
stock = pd.read_csv("stock_prices.csv")

bitcoin["date"] = pd.to_datetime(bitcoin["date"])
ethereum["date"] = pd.to_datetime(ethereum["date"])
tether["date"] = pd.to_datetime(tether["date"])
oil["date"] = pd.to_datetime(oil["date"])
stock["Date"] = pd.to_datetime(stock["Date"])

market = st.sidebar.selectbox(
    "Choose a market:",
    ["Bitcoin", "Ethereum", "Tether", "Oil", "Stocks"]
)

if market == "Bitcoin":
    st.header("₿ Bitcoin Price Analysis")
    c1, c2, c3 = st.columns(3)
    c1.metric("Average Price", f"₹{bitcoin['price_inr'].mean():,.2f}")
    c2.metric("Highest Price", f"₹{bitcoin['price_inr'].max():,.2f}")
    c3.metric("Lowest Price", f"₹{bitcoin['price_inr'].min():,.2f}")
    st.line_chart(bitcoin.set_index("date")["price_inr"])

elif market == "Ethereum":
    st.header("Ξ Ethereum Price Analysis")
    c1, c2, c3 = st.columns(3)
    c1.metric("Average Price", f"₹{ethereum['price_inr'].mean():,.2f}")
    c2.metric("Highest Price", f"₹{ethereum['price_inr'].max():,.2f}")
    c3.metric("Lowest Price", f"₹{ethereum['price_inr'].min():,.2f}")
    st.line_chart(ethereum.set_index("date")["price_inr"])

elif market == "Tether":
    st.header("₮ Tether Price Analysis")
    c1, c2, c3 = st.columns(3)
    c1.metric("Average Price", f"₹{tether['price_inr'].mean():,.2f}")
    c2.metric("Highest Price", f"₹{tether['price_inr'].max():,.2f}")
    c3.metric("Lowest Price", f"₹{tether['price_inr'].min():,.2f}")
    st.line_chart(tether.set_index("date")["price_inr"])

elif market == "Oil":
    st.header("🛢️ WTI Crude Oil Analysis")
    c1, c2, c3 = st.columns(3)
    c1.metric("Average Price", f"${oil['price_usd'].mean():,.2f}")
    c2.metric("Highest Price", f"${oil['price_usd'].max():,.2f}")
    c3.metric("Lowest Price", f"${oil['price_usd'].min():,.2f}")
    st.line_chart(oil.set_index("date")["price_usd"])

elif market == "Stocks":
    st.header("📈 Stock Market Analysis")
    ticker = st.selectbox("Select Index:", stock["ticker"].unique())
    selected = stock[stock["ticker"] == ticker]

    c1, c2, c3 = st.columns(3)
    c1.metric("Average Close", f"{selected['close_price'].mean():,.2f}")
    c2.metric("Highest Close", f"{selected['close_price'].max():,.2f}")
    c3.metric("Lowest Close", f"{selected['close_price'].min():,.2f}")

    st.line_chart(selected.set_index("Date")["close_price"])
