import pandas as pd
import json
import requests
import os

from sec_10q_parser import parse_management_discussion

"""
This Python module defines a DataLoader class that facilitates the extraction and processing of financial data from multiple sources, specifically tailored for analyzing analyst ratings and SEC filings. The DataLoader class initializes by loading analyst rating headlines from a CSV file and mapping stock ticker symbols to their corresponding CIK codes using a JSON file. It includes methods to:
- Load management's discussion and analysis from a company's 10-Q filings using the SEC's data API, filtered by ticker, year, and quarter.
- Retrieve random sample headlines related to a specific ticker and time period from the pre-loaded CSV.
- A placeholder for a method to compute the z-score which is not implemented yet.

The class handles HTTP requests to the SEC's website using a predefined user agent for identification. It also handles potential errors that might arise during the retrieval and parsing of the 10-Q documents, such as missing documents or issues within the parsed content. This tool is particularly useful for financial analysts and researchers looking to automate and streamline the process of data collection for financial analysis.
"""


#Replace yourUID in this field
headers = {'User-Agent': 'Mozilla/5.0 (UMD yourUID@umd.edu)'}

class DataLoader():
  def __init__(self):
    self.headlines = pd.read_csv('/Users/Vatsal/Downloads/analyst_ratings_processed.csv')

    with open('../data/company_tickers.json', 'r') as f:
      company_tickers = json.loads(f.read())
    self.ticker2cik = dict([(entry['ticker'], entry['cik_str']) for _, entry in company_tickers.items()])

  def load_management_discussion(self, ticker, year, quarter):
    cik = self.ticker2cik[ticker]

    data_url = f'https://data.sec.gov/submissions/CIK{cik:010d}.json'
    res = requests.get(data_url, headers=headers)
    recent = res.json()['filings']['recent']

    filings = [dict((key, recent[key][i]) for key in recent.keys()) for i in range(len(list(recent.values())[0]))]
    filings_10q = [filing for filing in filings if filing['primaryDocDescription'] == '10-Q']

    try:
      filing = sorted(
        [filing_10q for filing_10q in filings_10q if pd.to_datetime(filing_10q['reportDate']).year == year], 
        key=lambda filing: filing['reportDate']
      )[quarter - 1]
    except IndexError:
      raise IndexError(f'No filing found for {ticker} in Q{quarter} {year} at {data_url}:\n{filings_10q}')

    document = filing['primaryDocument']
    accession_number = filing['accessionNumber'].replace('-', '')

    document_url = f'https://www.sec.gov/Archives/edgar/data/{cik}/{accession_number}/{document}'
    document_res = requests.get(document_url, headers=headers)
    try:
      return parse_management_discussion(document_res.text)
    except AssertionError as e:
      raise KeyError(f'No management\'s discussion found in filing {document_url}')
      
    # raise KeyError(f'No filing found for {ticker} in Q{quarter} {year} at {data_url}')

  def load_headlines(self, ticker, year, quarter):
    data = self.headlines[
      (self.headlines.stock == ticker) & 
      (self.headlines.date.dt.year == year) & 
      (self.headlines.date.dt.quarter == quarter)
    ]
    return '\n\n'.join(data.sample(20).title)
  
  def load_zscore(self, ticker, year, quarter):
    raise NotImplementedError