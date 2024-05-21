# Financial Management Discussion Analysis

## Overview
This project utilizes the FinBERT model, a transformer-based model pre-trained on financial texts, to perform sentiment analysis on management discussions. The objective is to analyze the sentiments expressed in financial management discussions and categorize them into predefined classes based on their sentiment scores. This analysis can help in understanding the sentiment trends in financial management narratives.

## Prerequisites
Before running this script, ensure you have the following installed:
- Python 3.8 or higher
- Pandas
- NumPy
- scikit-learn
- PyTorch
- Transformers library
- CUDA (optional, for GPU support)

## Dataset
The dataset, should contain at least the following columns:
- `Management Discussion`: Text of the management discussion.
- `score`: Numerical score indicating the sentiment of the discussion.
You can use the full_feature_datas

## Installation
To set up your environment to run this code, follow these steps:

1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Install the required Python packages:
   ```bash
   pip install pandas numpy torch scikit-learn transformers
   ```

## Usage
Run the script using the following command:
```bash
python sentiment_analysis.py
```

This will execute the data loading, preprocessing, model training, and evaluation steps, and print the classification report at the end.

## Features
- Data cleaning and preprocessing.
- Data splitting for training and testing.
- Text tokenization using FinBERT tokenizer.
- Embedding extraction using FinBERT model.
- Training a logistic regression model on extracted embeddings.
- Evaluation of the model using classification metrics.

## Output
The output of the script includes:
- The shapes of the initial and cleaned datasets.
- Confirmation of successful data splitting.
- Notification of DataLoader preparation.
- Device configuration for model operations.
- Extraction and display of embeddings.
- Training status of the logistic regression model.
- Detailed classification report showing precision, recall, and F1-score for each category.
