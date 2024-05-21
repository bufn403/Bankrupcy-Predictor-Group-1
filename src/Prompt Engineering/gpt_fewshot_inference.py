from openai import OpenAI

"""
This script is designed to analyze the Management's Discussion and Analysis (MD&A) sections from companies' 10-Q filings using OpenAI's GPT-3.5 model. The primary functionality includes:

1. File Reading: The script reads the MD&A texts from specified files. These texts are extracted from real-world 10-Q filings for companies like SVB and Apple. The file reading operation loads these texts into memory for further processing.

2. MD&A Evaluation Function: The `evaluate_mdna` function uses OpenAI's API to send the MD&A text to the GPT-3.5 model. The function is configured to interpret the text with a specific prompt that directs the model to evaluate the bankruptcy risk of the company based on the information provided in the MD&A section. The model's response is expected to follow a structured reasoning process, assessing sentiment, financial indicators, and forward-looking statements to determine the risk level.

3. System and User Roles in API Interaction: In the function, roles are defined for 'system' and 'user' in the context of API interaction. The 'system' provides instructions and expectations to the model, setting up a scenario where the model acts as a financial analyst. The 'user' role is used to feed the actual MD&A text to the model. This structured interaction ensures that the model's responses are focused and relevant to the query.

4. Result Extraction and Handling: The script captures and returns the model's analysis, which includes a risk classification (low, medium, or high) and a detailed step-by-step reasoning process based on the MD&A text.

This tool is invaluable for financial analysts, researchers, and companies who seek to automate the preliminary analysis of financial documents using AI, providing insights into potential bankruptcy risks without manual review.
"""


with open('data/fewshot_mdna/SVB2022Q3.txt') as f:
    SVB_mdna = f.read()

with open('data/fewshot_mdna/AAPL2023Q1.txt') as f:
    AAPL_mdna = f.read()


def evaluate_mdna(mdna_text, openai_client):
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
        {'role': 'system', 'content': '''You are a financial assistant evaluating the bankruptcy risk of companies based on their corporate filings. 
Given input text from a company's management discussion section in their 10-Q filing, you will classify the company as having low, medium, or high risk of bankruptcy. 
Provide the reasoning for your explanation, citing statements in the filing that influenced your decision. 
You will only utilize the 10-Q filing in your reasoning without using any other historical knowledge. 
Your reasoning should follow a step-by-step process:
Step 1: Analyze the overall sentiment of the management's discussion, and whether it is optimistic or pessimistic.
Step 2: Observe relevant numbers and figures provided in the discussion, such as future projections or percentage changes.
Step 3: Determine whether the numbers and figures represent a successful or failed quarter, and if the conditions are likely to improve or worsen.
Step 4: Output your final decision on whether the company has a low, medium, or high risk of bankruptcy in the future, taking the sentiment, numbers, and future outlook into account.
Be skeptical in your decision, as the filings are meant to be sugarcoated and may not reflect the true internal condition of the company.
When in doubt, prioritize your decision based on the numbers in Step 2, even if the sentiment in the filing is optimistic.
Your decision should prioritize current conditions of the company rather than forward looking statements in the filings.
First output your final decision as a single word (indicating low, medium, or high risk), then list out your chain of thought as described by the steps. 
Your first output must only be a single word: low, medium, or high.
In each step, cite at least one quote from the text supporting the decision.'''},
        {'role': 'user', 'content': SVB_mdna},
        {'role': 'system', 'content': '''High

Step 1: The sentiment in the management's discussion seems cautiously optimistic. They highlight overall healthy performance, but mention challenging market conditions, especially a volatile market and high interest rates.

Step 2: There are mentions of specific financial indicators like net interest income growth, solid loan growth, and robust core fee income growth. For instance, "Net interest income grew, with moderating positive impact from high interest rates due to deposit outflows and higher funding costs."

Step 3: The discussion acknowledges challenges in the market, such as prolonged public market volatility and pressure on balance sheet growth. However, it also emphasizes continued strong credit performance and robust fee income growth. There's a focus on adapting to changes, like the LIBOR transition program, indicating proactive measures to mitigate risks.

Step 4: Considering the cautiously optimistic sentiment, positive financial indicators, and proactive measures to address challenges like the LIBOR transition, the company appears to be attempting to manage its risks. However, the acknowledgment of market volatility and challenges suggests a high risk of bankruptcy, as uncertainties in the market could still pose significant threats to the company's financial health.'''},
        {'role': 'user', 'content': AAPL_mdna},
        {'role': 'system', 'content': '''Low

Step 1: The overall sentiment of the management's discussion is cautiously optimistic. While the discussion acknowledges the impact of the COVID-19 pandemic on the company's operations and financial performance, it also highlights the significant increase in total net sales and the successful launch of new products and services. The management believes that the company's existing balances of cash, cash equivalents, and marketable securities will be sufficient to meet its liquidity requirements.

Step 2: 
- Working Capital to Total Assets (X1): The negative value of -0.0049 indicates a slight deficiency in working capital compared to total assets, but it's not extremely concerning.
- Retained Earnings to Total Assets (X2): The negative value of -0.0006 suggests a lower proportion of retained earnings to total assets, which could indicate some level of financial strain.
- EBIT to Total Assets (X3): The positive value of 0.3337 shows a good proportion of earnings before interest and taxes to total assets, indicating operational efficiency.
- Total Revenue to Total Assets (X5): The high value of 1.0871 indicates that the company is generating significant revenue relative to its total assets, reflecting strong asset utilization.

Step 3: The combination of an increase in net sales, successful product launches, and sufficient liquidity buffers from the existing cash, cash equivalents, and marketable securities balance, alongside operational efficiency reflected in EBIT to Total Assets ratio, suggests that the company had a successful quarter despite the challenges posed by the COVID-19 pandemic. The negative Retained Earnings to Total Assets ratio may indicate the need for the company to focus on increasing retained earnings to strengthen its financial position further.

Step 4: Low risk of bankruptcy. The company's strong revenue generation, operational efficiency, and strategic financial management, coupled with the cautiously optimistic sentiment expressed in the management's discussion, indicate a relatively stable financial position, mitigating the risk of bankruptcy in the foreseeable future.'''},
        {'role': 'user', 'content': mdna_text},
        ]
    )

    answer = response.choices[0].message.content

    return answer
