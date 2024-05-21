# OpenAI GPT for MD&A Analysis Toolkit

This repository contains a suite of Python scripts designed to leverage OpenAI's GPT models for analyzing Management's Discussion and Analysis (MD&A) sections from SEC 10-Q filings. The toolkit includes three main scripts, each tailored for different aspects and scales of data processing and analysis.

## Overview of Scripts

### 1. `gpt_single_inference.py`

This script is designed for performing single inference tasks using OpenAI's GPT models. It processes individual MD&A texts, evaluating the bankruptcy risk based on structured prompts that guide the model to analyze the text's sentiment, financial metrics, and overall business outlook.

#### Key Features:
- Detailed interaction with the GPT model to perform focused analysis on MD&A sections.
- Structured prompts to ensure consistent and comprehensive analysis.
- Outputs include a risk rating and a detailed reasoning breakdown.

### 2. `gpt_batch_inference.py`

Aimed at processing multiple MD&A sections in batch, this script automates the evaluation of bankruptcy risk for several companies at once, efficiently handling larger datasets typically encountered in financial analysis.

#### Key Features:
- Batch processing capabilities for handling multiple filings simultaneously.
- Utilizes structured prompts similar to `gpt_single_inference.py` but optimized for batch operations.
- Provides comprehensive output files that capture the risk assessments and detailed analyses for each MD&A section processed.

### 3. `gpt_fewshot_inference.py`

This script employs few-shot learning techniques with OpenAI's GPT models to enhance the accuracy and relevance of the bankruptcy risk evaluations. By providing examples within the prompt, the model leverages prior inferences to refine its predictions and reasoning for new MD&A texts.

#### Key Features:
- Few-shot learning approach to improve model performance on new MD&A texts.
- Detailed output that includes both the risk rating and a step-by-step analysis based on the model's learning from previous examples.
- Ideal for scenarios where enhanced accuracy and contextual understanding are crucial.

## Installation

Before running these scripts, ensure you have Python and the necessary libraries installed:

```bash
pip install openai pandas
```

## Usage

Each script can be run from the command line or integrated into larger Python projects. Ensure your OpenAI API key is configured correctly in your environment:

```bash
export OPENAI_API_KEY='your-api-key-here'
```

### Example Command

```bash
python gpt_single_inference.py
```