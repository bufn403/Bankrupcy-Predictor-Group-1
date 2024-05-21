import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from transformers import BertTokenizer, BertModel
import numpy as np

"""
This script is designed to perform sentiment analysis on financial management discussions by leveraging a pre-trained FinBERT model, a BERT-based model specifically fine-tuned for financial texts. The main steps involved in the script are:

1. Data Preparation:
   - Loads a dataset of management discussions from a CSV file.
   - Drops rows with missing values in crucial columns ('Management Discussion', 'score').
   - Transforms the 'score' into categorical labels suitable for classification.

2. Text and Label Preparation:
   - Splits the data into training and testing sets.
   - Prepares the text data for processing by resetting the indices, ensuring data integrity post-split.

3. Tokenization:
   - Utilizes a tokenizer from the 'transformers' library, specifically designed for the FinBERT model, to convert text data into a format suitable for BERT models (token IDs, attention masks).

4. Dataset and DataLoader Setup:
   - Creates custom PyTorch datasets for both training and testing text data.
   - Sets up DataLoaders to handle batching and shuffling of the dataset during the model training and evaluation phases.

5. Model Preparation and Embedding Extraction:
   - Loads the FinBERT model and configures it for running on available hardware (GPU/CPU).
   - Extracts embeddings for each text in the dataset using the FinBERT model, capturing the contextual relationships in the texts.

6. Model Training:
   - Trains a logistic regression model using the extracted embeddings from the training set to predict the categorical labels.

7. Evaluation:
   - Predicts the categories on the testing set using the trained logistic regression model.
   - Provides a detailed classification report to evaluate the performance of the model in terms of precision, recall, and F1-score for each class.
"""


df = pd.read_csv('/Users/a12345/Desktop/fake_final_management_discussions_2020.csv')
print("Initial DataFrame shape:", df.shape)
df.dropna(subset=['Management Discussion', 'score'], inplace=True)
print("DataFrame shape after dropping NA:", df.shape)

def prepare_labels(z_scores):
    labels = pd.cut(z_scores, bins=[-np.inf, 1.8, 3, np.inf], labels=[0, 1, 2])
    return labels

labels = prepare_labels(df['score'])

train_texts, test_texts, train_labels, test_labels = train_test_split(
    df['Management Discussion'], labels, test_size=0.2, random_state=42)
train_texts.reset_index(drop=True, inplace=True)
train_labels.reset_index(drop=True, inplace=True)
test_texts.reset_index(drop=True, inplace=True)
test_labels.reset_index(drop=True, inplace=True)
print("Train and test data split successfully.")

tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-pretrain')

class FinbertDataset(Dataset):
    def __init__(self, texts, labels):
        self.texts = texts
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        text = self.texts.iloc[idx]
        label = self.labels.iloc[idx]
        inputs = tokenizer(text, padding='max_length', max_length=512, truncation=True, return_tensors="pt")
        inputs = {key: val.squeeze() for key, val in inputs.items()}
        return {'input_ids': inputs['input_ids'], 'attention_mask': inputs['attention_mask'],
                'labels': torch.tensor(int(label))}

train_dataset = FinbertDataset(train_texts, train_labels)
test_dataset = FinbertDataset(test_texts, test_labels)
train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=16, shuffle=False)
print("DataLoaders prepared.")

model = BertModel.from_pretrained('yiyanghkust/finbert-pretrain')
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)
print("Model loaded and sent to device:", device)

def extract_embeddings(dataloader):
    model.eval()
    embeddings = []
    labels = []
    with torch.no_grad():
        for batch in dataloader:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            outputs = model(input_ids, attention_mask=attention_mask)
            embeddings.extend(outputs.pooler_output.detach().cpu().numpy())
            labels.extend(batch['labels'].detach().cpu().numpy())
    return np.array(embeddings), np.array(labels)

train_embeddings, train_labels = extract_embeddings(train_loader)
test_embeddings, test_labels = extract_embeddings(test_loader)
print("Embeddings extracted.")

log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(train_embeddings, train_labels)
print("Logistic regression trained.")
pred_labels = log_reg.predict(test_embeddings)
print(classification_report(test_labels, pred_labels))
print("Model evaluation complete.")