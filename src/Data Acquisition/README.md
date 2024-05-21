# SEC Filings Analysis Toolkit

This repository contains Python modules specifically designed for parsing, loading, and extracting data from SEC filings, particularly focusing on the Management's Discussion and Analysis (MD&A) sections from 10-Q filings. The toolkit includes `sec_10q_parser.py` for parsing the documents, `dataloader.py` for managing data retrieval and processing, and `extractor.py` for automating the data retrieval process across a wide range of tickers.

## Overview of Modules

### 1. `sec_10q_parser.py`

This module provides a parser specifically designed for extracting structured data from the 10-Q filings' MD&A sections. It employs a combination of text processing techniques and financial domain knowledge to identify and extract relevant information from these complex documents.

#### Key Features:
- Advanced parsing techniques to handle the unique structure of SEC filings.
- Outputs structured data that can be easily analyzed for financial insights.
- Customizable to focus on different sections of the filings as required.

### 2. `dataloader.py`

The `dataloader.py` module handles the loading and initial processing of data from various sources, including local files and web APIs. It is particularly tailored to work with financial data related to SEC filings, ensuring that data is loaded efficiently and ready for analysis.

#### Key Features:
- Efficient loading of large datasets typically associated with SEC filings.
- Integration with web APIs to fetch real-time data when necessary.
- Works in tandem with `sec_10q_parser.py` to streamline the data processing workflow.

### 3. `extractor.py`

The `extractor.py` script automates the retrieval and storage of management discussion sections from quarterly reports (10-Q) for a large list of company tickers. It handles exceptions gracefully, logs skipped tickers due to failures, and includes a delay between requests to manage API usage limits.

#### Key Features:
- Automated retrieval of management discussions for numerous tickers.
- Saves each management discussion in a separate text file for further analysis.
- Gracefully handles network and parsing exceptions, logging issues for skipped tickers.

## Installation

Ensure Python is installed on your machine along with the required libraries. You can install the necessary dependencies via pip:

```bash
pip install pandas requests beautifulsoup4 lxml
```

## Usage

Import the modules in your Python scripts or Jupyter notebooks to start parsing and loading SEC filings:

```python
from dataloader import DataLoader
from sec_10q_parser import parse_management_discussion
from extractor import automate_data_retrieval

# Example of loading and parsing data
data_loader = DataLoader()
mdna_text = data_loader.load_management_discussion('AAPL', 2021, 2)
parsed_data = parse_management_discussion(mdna_text)

# Example of automating data retrieval
automate_data_retrieval()
```
