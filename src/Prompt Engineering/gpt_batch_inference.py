from openai import OpenAI
from gpt_single_inference import evaluate_mdna
import pandas as pd
import time

"""
This script is designed to automate the process of analyzing the Management's Discussion and Analysis (MD&A) sections from SEC 10-Q filings using OpenAI's GPT models. The primary functionalities of the script include:

1. Data Preparation: It loads MD&A texts from a CSV file containing information about various companies, such as their ticker symbols, the year and quarter of the filing, and the text of the MD&A section.

2. Text Truncation: The script truncates the MD&A text to a manageable size (default is 4096 words) to ensure it fits within the input constraints of the GPT model.

3. GPT Analysis: Utilizes a custom function `evaluate_mdna` from the `gpt_single_inference` module to perform analysis on the truncated MD&A text. This function presumably sends the text to the OpenAI GPT model and retrieves an analysis, which could include sentiment analysis, summarization, or other types of textual interpretation.

4. Output Management: Analysis results are saved into text files named according to the company's ticker, year, and quarter, ensuring organized storage of results for easy reference.

5. Error Handling and Logging: The script logs successes and failures, collecting any tickers for which the analysis failed into a list for potential troubleshooting or re-analysis.

6. Rate Limit Management: Includes a brief sleep interval between API calls to prevent hitting rate limits of the API.

This tool is particularly useful for financial analysts, data scientists, and researchers interested in extracting insights from corporate financial disclosures efficiently.

Prerequisites:
- A valid OpenAI API key set as 'API_KEY'.
- The necessary Python libraries installed (`pandas`, `time`, and the `openai` library from OpenAI).
"""


def truncate_mdna_text(mdna_text, num_words=4096):
    words = mdna_text.split()
    if len(words) > num_words:
        mdna_text = ' '.join(words[:num_words])
    return mdna_text

api_key = "API_KEY"

client = OpenAI(api_key=api_key)

df = pd.read_csv('data/mdna_headline_dataframe/final_management_discussions_2020.csv')
df = df.dropna(subset=['Ticker', 'Year', 'Quarter', 'Management Discussion'])

# Filter df to year 2020 and Quarter 3
df = df[(df['Year'] == 2020) & (df['Quarter'] == 3)]


failed_tickers = []
n = len(df)

for i, row in df.iterrows():
    ticker = row['Ticker']
    year = row['Year']
    quarter = row['Quarter']


    try:
        mdna_text = truncate_mdna_text(row['Management Discussion'])
        answer = evaluate_mdna(mdna_text, client)
        file_name = f'data/gpt_results_v2/{ticker}_{year}_{quarter}.txt'
        with open(file_name, 'w') as f:
            f.write(answer)
        print(f'({i+1}/{n})\tWrote to {file_name}')
    except Exception as e:
        print(f'({i+1}/{n})\tFailed to evaluate {ticker} {year} Q{quarter}: {e}')
        failed_tickers.append((ticker, year, quarter))

    # sleep for 0.2 seconds to avoid rate limiting
    time.sleep(0.2)

print("Total evaluations:", len(df))
print(f'\n\nFailed tickers: {failed_tickers}')
