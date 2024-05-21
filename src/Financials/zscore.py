import pandas as pd
import yfinance as yf

"""
This script conducts a financial analysis of A company using data from Yahoo Finance to evaluate its credit risk and stability. 
The analysis involves several steps:

1. Data Retrieval: The script fetches historical share data and financial statements from Yahoo Finance, 
   focusing on market capitalization, balance sheet, and income statement metrics.

2. Market Capitalization Calculation: It calculates the market cap by combining share price with the number of outstanding shares, 
   providing a snapshot of the company's perceived value in the financial market.

3. Altman Z-score Computation: 
   - The Z-score is derived from five financial ratios that are crucial indicators of financial health:
     a. X1 (Working Capital / Total Assets): Measures liquidity, indicating the ability to cover short-term obligations.
     b. X2 (Retained Earnings / Total Assets): Assesses profitability over time, reflecting accumulated profits and losses.
     c. X3 (EBIT / Total Assets): Evaluates operational efficiency, showing earnings before interest and taxes relative to total assets.
     d. X4 (Market Cap / Total Liabilities): Gauges leverage, comparing the company's market valuation against its liabilities.
     e. X5 (Sales / Total Assets): Indicates asset utilization efficiency, measuring how effectively a company uses its assets to generate sales.
   - These ratios collectively assess different aspects of a company's financial stability, such as liquidity, profitability, operational efficiency, leverage, and activity.

4. Application: The Altman Z-score serves as a ground truth for predicting bankruptcy risk, making it a critical metric in determining a company's long-term viability.
"""


def get_financial_data(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    total_shares = ticker.get_shares_full(start='2019-01-01', end='2023-12-31')
    total_shares.index = pd.to_datetime(total_shares.index.date)
    share_price = ticker.history(start='2020-01-01', end='2023-12-31').Close
    share_price.index = pd.to_datetime(share_price.index.date)
    
    total_shares = pd.DataFrame(total_shares.values, columns=['Total Shares'], index=total_shares.index).drop_duplicates(keep='last')
    share_price = pd.DataFrame(share_price.values, columns=['Share Price'], index=share_price.index)
    
    total_share_price = pd.merge_asof(share_price, total_shares, left_index=True, right_index=True)
    total_share_price['Market Cap'] = total_share_price['Share Price'] * total_share_price['Total Shares']
    
    return ticker, total_share_price

def get_combined_financials(ticker):
    balance_sheet = ticker.balance_sheet.T
    income_statement = ticker.income_stmt.T
    financials = pd.merge(balance_sheet, income_statement, left_index=True, right_index=True).sort_index()
    return financials

def calculate_z_score(financials, market_cap):
    financials = pd.merge_asof(financials, market_cap, left_index=True, right_index=True)
    
    X1 = financials['Working Capital'] / financials['Total Assets']
    X2 = financials['Retained Earnings'] / financials['Total Assets']
    X3 = financials['EBIT'] / financials['Total Assets']
    X4 = financials['Market Cap'] / financials['Total Liabilities Net Minority Interest']
    X5 = financials['Total Revenue'] / financials['Total Assets']
    
    return 1.2*X1 + 1.4*X2 + 3.3*X3 + 0.6*X4 + 1.0*X5

def main():
    ticker_symbol = 'AAPL'
    ticker, market_cap = get_financial_data(ticker_symbol)
    financials = get_combined_financials(ticker)
    z_score = calculate_z_score(financials, market_cap)
    print(z_score)
