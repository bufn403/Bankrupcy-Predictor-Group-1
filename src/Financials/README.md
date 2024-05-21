# Financial Analysis Script

This Python script performs a detailed financial analysis of a company (Apple Inc. as default) using data fetched from Yahoo Finance. It evaluates credit risk and stability by calculating the Altman Z-score, a predictor of bankruptcy risk.

## Overview

The script is designed to:
1. Retrieve historical share data and financial statements for a company.
2. Calculate the market capitalization by combining share price with the number of outstanding shares.
3. Compute the Altman Z-score using five key financial ratios to assess aspects of financial stability such as liquidity, profitability, operational efficiency, leverage, and activity.

## Prerequisites

- Python 3.6 or newer
- Pandas library
- yfinance library

To install the necessary Python libraries, you can use pip:

```bash
pip install pandas yfinance
```

## Usage

To run this script, simply execute the `main` function defined in the script. You can modify the `ticker_symbol` in the `main()` function to analyze different companies listed on stock exchanges.

Example of running the script:

```bash
python financial_analysis.py
```

## Components

- **get_financial_data(ticker_symbol)**: Fetches the total shares and share prices over specified dates and calculates the market capitalization.
- **get_combined_financials(ticker)**: Retrieves and merges balance sheet and income statement data.
- **calculate_z_score(financials, market_cap)**: Calculates the Altman Z-score using financial data.

## Output

The script will print the Altman Z-score for the specified company, providing an insight into the company's financial health and the likelihood of financial distress.
