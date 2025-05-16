import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import yfinance as yf
import csv
csv_file = '15 Years Stock Data of NVDA AAPL MSFT GOOGL and AMZN.csv'
# Load the CSV file into a DataFrame    
csvread = pd.read_csv(csv_file)
StocksDF = pd.DataFrame(csvread)

st.title('Team Alpha Stock Final Project')

Answer = str(st.text_input('Please Enter a stock you would like to see(NVDA,AAPL,GOOGL, and AMZN):'))
Answer2 = str(st.text_input('Please enter the date of that stock you would like to view:'))

