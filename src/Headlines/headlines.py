import pandas as pd

headlines = pd.read_csv('/Users/Vatsal/Downloads/analyst_ratings_processed.csv')
headlines['date'] = pd.to_datetime(headlines.date, errors='coerce')

another_df = pd.read_csv('/path/to/another_dataframe.csv')

another_df['concatenated_headlines'] = ''

def get_headlines(ticker, year, quarter):
    data = headlines[
        (headlines.stock == ticker) &
        (headlines.date.dt.year == year) &
        (headlines.date.dt.quarter == quarter)
    ]
    return '\n\n'.join(data.sample(min(20, len(data))).title)

for index, row in another_df.iterrows():
    ticker = row['Ticker']
    year = row['Year']
    quarter = row['Quarter']
    another_df.at[index, 'concatenated_headlines'] = get_headlines(ticker, year, quarter)

output_file_path = '/path/to/another_dataframe_modified.csv'
another_df.to_csv(output_file_path, index=False)
print(f"Modified CSV file saved to {output_file_path}")
