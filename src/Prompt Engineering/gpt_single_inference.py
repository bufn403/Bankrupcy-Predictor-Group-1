from openai import OpenAI

"""
This script utilizes the OpenAI GPT-3.5 model to evaluate the bankruptcy risk of companies based on the Management's Discussion and Analysis (MD&A) sections from their 10-Q filings. The function `evaluate_mdna` serves as the core component:

1. **Functionality**: The `evaluate_mdna` function is designed to send a block of text, specifically the MD&A section from a company's 10-Q filing, to the GPT-3.5 model. It formulates a structured prompt that guides the model to analyze the text according to predefined steps.

2. **API Interaction**: It leverages OpenAI's `chat.completions.create` method to interact with the model. The function configures the request with a detailed prompt that includes instructions for the AI to:
    - Analyze the overall sentiment of the management's discussion.
    - Review key financial numbers and figures mentioned in the text.
    - Assess the financial health and future outlook based on the observed data.
    - Conclude with a bankruptcy risk rating (low, medium, or high).

3. **Structured Output**: The output from the GPT-3.5 model includes a one-word bankruptcy risk rating followed by a detailed reasoning process that aligns with the steps in the prompt. Each step requires the model to cite specific quotes from the MD&A section to support its analysis.

4. **Use Case**: This tool is particularly useful for financial analysts and investors who need a quick preliminary analysis of a company's financial health as reported in their 10-Q filings. It automates the analysis of complex financial narratives, providing insights that are immediately useful for decision-making.

This script exemplifies how AI can be used to enhance financial analysis, reducing the workload on human analysts and providing rapid assessments based on large volumes of text.
"""


def evaluate_mdna(mdna_text, openai_client):
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
        {'role': 'user', 'content': '''
        You are a helpful assistant evaluating the bankruptcy risk of companies based on their corporate filings. 
        Given input text from a company's management discussion section in their 10-Q filing, you will classify the company as having low, medium, or high risk of bankruptcy. 
        Provide the reasoning for your explanation, citing up to three statements in the filing that influenced your decision. 
        You will only utilize the 10-Q filing in your reasoning without using any other historical knowledge. 
        Your reasoning should follow a step-by-step process:
        Step 1: Analyze the overall sentiment of the management's discussion, and whether it is optimistic or pessimistic.
        Step 2: Observe relevant numbers and figures provided in the discussion, such as future projections or percentage changes.
        Step 3: Determine whether the numbers and figures represent a successful or failed quarter, and if the conditions are likely to improve or worsen.
        Step 4: Output your final decision on whether the company has a low, medium, or high risk of bankruptcy in the future, taking the sentiment, numbers, and future outlook into account.
        First output your final decision as a single word (indicating low, medium, or high risk), then list out your chain of thought as described by the steps. 
        In each step, cite at least one quote verbatim from the text supporting the decision.
        The filing will be provided below.\n\n
         '''+mdna_text},
        ]
    )

    answer = response.choices[0].message.content

    return answer
