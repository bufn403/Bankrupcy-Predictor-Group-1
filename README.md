# Bankruptcy Risk Prediction with Data Integration and Prompt Engineering

## Project Description
This project advances bankruptcy risk prediction by integrating natural language processing with large language models like GPT-3.5 and FinBERT. We utilize a novel approach by analyzing quarterly SEC 10-Q filings and earnings call transcripts, alongside news headlines, to predict bankruptcy risk. The innovative aspect of our project lies in the use of prompt engineering techniques with GPT-3.5 to interpret complex financial narratives and derive meaningful insights, which are then contrasted with the financial understanding capabilities of FinBERT, a model fine-tuned on financial data.

Our results are benchmarked against the traditional Altman Z-score, providing a dual perspective that combines both cutting-edge AI technologies and established financial analysis methodologies. This dual approach allows us to validate the Altman Z-Score as an effective indicator while exploring the potential of LLMs to revolutionize financial risk prediction.

## Goals
- Showcase the capability of LLMs to understand and analyze financial narratives using advanced prompt engineering.
- Compare the performance of GPT-3.5 and FinBERT in financial prediction tasks.
- Evaluate the reliability of the Altman Z-Score within modern predictive frameworks.

## File Structure
```
Financials/
└── zscore.py                  # Calculates the Altman Z-score, a critical metric for assessing company solvency.
Data Acquisition/
├── extractor.py               # Automates the extraction of financial data and news articles from various sources.
├── sec_10q_parser.py          # Parses SEC 10-Q filings to extract key financial data and narratives.
└── dataloader.py              # Prepares and preprocesses data for analysis, ensuring accuracy and compatibility.
Finbert/
└── embedding-extraction-logistic-regression-training.py  # Utilizes FinBERT embeddings to train a logistic regression model for predicting bankruptcy risks.
Prompt Engineering/
├── gpt_single_inference.py    # Executes inference on single data points using GPT-3.5 for detailed prompt analysis.
├── gpt_batch_inference.py     # Facilitates efficient batch processing of data for prompt-based inference using GPT-3.5.
└── gpt_fewshot_inference.py   # Implements few-shot learning techniques with GPT-3.5 to adapt to new data scenarios quickly.
```

## Installation and Setup
To explore this archived project:
1. **Clone the repository:**
   ```
   git clone https://github.com/bufn403/Bankrupcy-Predictor-Group-2.git
   ```
2. **Install required dependencies:**
   - Ensure Python 3.6+ is installed.
   - Install Python libraries, as indicated in each file. 
     
3. **Set up each component:**
   - Navigate to the script directory.
   - Follow the detailed setup instructions in the header comments of each script.

## Intended Audience
This project targets researchers, institutional investors, and anyone interested in applying advanced NLP techniques to financial risk assessment.

## Usage
Refer to individual scripts for detailed usage instructions. Each component can be executed independently, tailored to specific data and analysis needs.

## Project Insights
### Methodology
We employed a mix of qualitative and quantitative approaches. The qualitative data from SEC filings and news articles were processed using NLP techniques to identify semantic similarities and patterns related to financial risks.

### Results
Our models demonstrated the ability to accurately predict bankruptcy risks, with precision and recall metrics showing robust performance against traditional models. The detailed sector-by-sector analysis provided new insights into risk factors across different industries.

## Evaluation
The models were evaluated using precision, recall, and F1-score metrics, affirming the practical viability of LLMs in complex financial applications.

## Team
- **Vatsal Baherwani:** Led the data scraping and prompt engineering initiatives.
- **Rishabh Sinha:** Managed the data pipeline and earnings call data integration.
- **Amol Menon:** Specialized in SEC filings parsing and cloud implementations.
- **Kushal Kapoor:** Oversaw documentation and UI development for model outputs.

## Links
- **Dashboard:** [https://blooming-river-80042-cd6fb12eaf4d.herokuapp.com/](https://blooming-river-80042-cd6fb12eaf4d.herokuapp.com/)
- **Final Dataset as a CSV:** [Google Drive](https://drive.google.com/file/d/1UjToxyC71yFfZUb1-liqyIG86VwEZOD_/view)
