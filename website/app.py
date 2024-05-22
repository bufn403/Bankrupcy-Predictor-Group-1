from flask import Flask, jsonify, request, send_from_directory
import pandas as pd

app = Flask(__name__, static_folder='frontend')

# Load the CSV data into a DataFrame
df = pd.read_csv('final_dataframe copy.csv')

@app.route('/data/<ticker>', methods=['GET'])
def get_data(ticker):
    # Filter the data based on the ticker
    data = df[df['Ticker'].str.upper() == ticker.upper()].to_dict(orient='records')
    return jsonify(data)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(debug=True)
