import requests
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.grid import grid

st.title("Money Grower")

def build_sidebar():
    st.image("image/MoneyGrower.png")
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=500&page=1&sparkline=false'
    response = requests.get(url)
    if response.status_code == 200:
        data=response.json()
        ticker_list = [asset['symbol'] for asset in data]
        tickers = st.multiselect(label="Selecione os ativos", options = ticker_list, placeholder="Tokens")
        start_date = st.date_input("De:", format = "DD/MM/YYYY", value=datetime(2022,1,2))
        end_date = st.date_input("Até:", format= "DD/MM/YYYY", value = "today")
        if tickers: 
            url_range = f'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=usd&from={start_date}&to={end_date}'
            prices = requests.get(url_range)
            #prices = {tickers} {start_date} {end_date}
            return tickers, prices
    else:
        st.write("Erro ao acessar CoinGecko")

    


def build_main():
    st.write("principal")
    pass

with st.sidebar:
    build_sidebar()
  
