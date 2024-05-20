# Bankruptcy Risk Prediction with Data Integration and Prompt Engineering

## Project Description

Bankruptcy risk is a critical factor in evaluating the stability of a company, attracting the attention of investors and researchers. This project aims to enhance current bankruptcy risk prediction approaches by leveraging natural language in company filings using large language models (LLMs) like GPT-3.5. Our innovative approach utilizes prompt engineering methods on GPT-3.5 to analyze quarterly SEC 10-Q filings and earnings call transcripts, combined with Benzinga news headlines, to predict bankruptcy risk levels (low, medium, high).

We contrast our results with FinBERT, a smaller language model fine-tuned on financial data. Both models are evaluated using the Altman Z-score as a ground truth label.

## Goals

- Demonstrate the financial understanding capabilities of LLMs such as GPT-3.5 using advanced prompt engineering methods.
- Compare the evaluations of GPT-3.5 and FinBERT to provide evidence for or against using larger, general-purpose models for financial prediction tasks.
- Evaluate Altman Z-Score as an effective ground truth label by performing sector-by-sector analysis and evaluating overall trends.
- Create an end-user tool to visualize model outputs for each ticker symbol and access other quarter trends, risk networks, and sector-by-sector risk confusion matrix.

## Intended Audience

This project targets institutional investors, asset managers, potential creditors, and academic researchers. The end-user tool developed will help in identifying and explaining bankruptcy risk, while the academic research aspect investigates whether large language models can adapt to domain-specific tasks without explicit training.

## Datasets

We collect data through the following methods:

- **10-Q Filings:** SEC API is used to collect filings for around 600 companies. The Management’s Discussion and Analysis (MD&A) sections are extracted and analyzed.
- **Z-Score Financials:** Altman Z-scores are calculated using data from Yahoo Finance API.
- **Benzinga News Headlines:** Historical news headlines provide an unbiased view of a company’s state.
- **Earnings Call Transcripts:** These are fetched using the Seeking Alpha API.

## Technical Challenges

### Data Integration
We designed a data loader script to consolidate data from multiple sources (SEC, Yahoo Finance, Kaggle). This involves handling unstructured data and merging it into a single dataframe.

### Prompt Engineering
Prompt engineering for GPT-3.5 involves creating an effective prompt to perform bankruptcy risk prediction. Techniques such as Chain of Thought reasoning and few-shot learning are applied to improve model performance.

## Approach

### Prompt Engineered GPT-3.5
- **Feature Set:** MD&A text, Benzinga headlines, earnings call transcripts.
- **Method:** Using OpenAI API with a system prompt outlining the task, chain of thought reasoning, and custom heuristics to guide the model’s predictions.

### FinBERT Logistic Regression
- **Feature Set:** Same as GPT-3.5.
- **Method:** Using FinBERT embeddings as input to a logistic regression model to classify bankruptcy risk.

## Evaluation

We evaluate both models using a confusion matrix and calculate precision, recall, F1-score, and other metrics. The evaluation shows that GPT-3.5 achieves slightly better performance compared to FinBERT.

## Results

- **Precision:** GPT-3.5: 0.82, FinBERT: 0.79
- **Recall:** GPT-3.5: 0.83, FinBERT: 0.79
- **F1-Score:** GPT-3.5: 0.83, FinBERT: 0.79
- **Overall Accuracy:** GPT-3.5: 83%, FinBERT: 79%

### Z-score Sector Comparison
Sector-by-sector analysis indicates that Altman Z-score is a reliable proxy for bankruptcy risk, aligning with human perception of risk.

## Team

- **Vatsal Baherwani:** Data scraping, prompt engineering, dataset creation.
- **Rishabh Sinha:** Earnings call retrieval, data pipeline, demo dashboard, evaluation scripts.
- **Amol Menon:** 10-Q filing parser, AWS Sagemaker implementations, prompt engineering script.
- **Kushal Kapoor:** Project documentation, UI for demo dashboard, synthesis model outputs.

## Links

- **Dashboard:** [https://blooming-river-80042-cd6fb12eaf4d.herokuapp.com/](https://blooming-river-80042-cd6fb12eaf4d.herokuapp.com/)
- **Dataset:** [Google Drive](https://drive.google.com/file/d/1Fi_oKpR0H8hzhqo55DM6Yho5ujmG2GXk/view?usp=sharing)

## References

- Altman, E. I. (1968). Financial ratios, discriminant analysis and the prediction of corporate bankruptcy. The journal of finance, 23(4), 589-609.
- Barden, Jeffrey. “The Impact of a Competitor’s Chapter 11 Bankruptcy on Firm Risk-Taking - Yohan Choi, Jeffrey Barden, Jonathan Arthurs, Sam Yul Cho, 2023.” Australian Journal of Management, 2023.
- Baranchuk, Nina, and Michael J. Rebello. “Spillovers from Good-News and Other Bankruptcies: Real Effects and Price Responses.” Journal of Financial Economics, 2018.
- Additional references provided in the project documentation.
