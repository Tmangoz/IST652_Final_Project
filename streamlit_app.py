import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import yfinance as yf
import csv
csv_file = "15 Years Stock Data of NVDA AAPL MSFT GOOGL and AMZN.csv"
# Load the CSV file into a DataFrame    
csvread = pd.read_csv(csv_file)
StocksDF = pd.DataFrame(csvread)

st.title('Team Alpha Stock Final Project')

print(StocksDF.head())


