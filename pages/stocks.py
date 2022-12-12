import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import requests
from pandas import json_normalize
import json
plt.style.use('default')
st.title('Streamlit Interactive Analytics Demo')


symbol = st.text_input('Please enter the ticker symbol for the data you want to analyze', 'IBM')

url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=' + symbol + '&apikey=LDGYT7FTCVVICA6X'
r = requests.get(url)
SEARCHdata = r.json()['bestMatches']
st.json(SEARCHdata)

optionscount = len(SEARCHdata)

names = []
for record in SEARCHdata:
    opt = record['1. symbol']
#     print(opt)
    names.append(opt)

symbol1 = st.radio(
    "Which ticker symbol from the list would you like to use",
    (names))

# print(data)


url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=' + symbol1 + '&apikey=LDGYT7FTCVVICA6X'
r = requests.get(url)
# data = r.json()

data = r.json()['Weekly Time Series']
df = pd.DataFrame(data)
# data
# df = json_normalize(data)
df = df.transpose()
df.reset_index(inplace=True)
cols = df.columns.drop('index')
df[cols] = df[cols].apply(pd.to_numeric)


option = st.selectbox(
    'What data are you interested in',
    ('1. open', '2. high', '3. low', '4. close','5. volume'))


fig1 = px.line(df, x = 'index', y = option, title='Weekly Stock Data')
st.plotly_chart(fig1, use_container_width=True)
