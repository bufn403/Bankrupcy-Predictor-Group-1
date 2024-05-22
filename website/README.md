# Stock Data Viewer

This project is a Stock Data Viewer built with Flask for the backend and HTML/CSS/JavaScript for the frontend. It allows users to input a stock ticker symbol and retrieve related data from a CSV file. The data is displayed in a structured format along with various visualizations.

## Folder Structure

```
BUFN403_Capstone_UI_Prod
├── frontend
│   ├── high_risk_network_graph.html
│   ├── index.html
│   ├── low_risk_network_graph.html
│   ├── medium_risk_network_graph.html
│   ├── script.js
│   ├── sector_confusion_matrix.html
│   ├── sector_confusion_matrix.png
│   └── style.css
├── node_modules
├── venv
│   ├── bin
│   ├── include
│   └── lib
├── .gitattributes
├── app.py
├── final_dataframe.csv
├── package.json
├── package-lock.json
├── Procfile
└── requirements.txt
```

## Prerequisites

- Python 3.x
- Pip (Python package installer)
- Node.js (for frontend dependencies, if any)

## Setup Instructions

1. **Clone the Repository**

    ```sh
    git clone https://github.com/bufn403/Bankrupcy-Predictor-Group-1.git
    cd Bankrupcy-Predictor-Group-1/website
    ```

2. **Download the CSV File**

    Download the CSV file from [this Google Drive link](https://drive.google.com/file/d/1Kqpi_ihIbcDym24caprNe6tvtDwiEoCV/view?usp=sharing) and place it in the project directory as `final_dataframe.csv`.

3. **Set Up Virtual Environment**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install Backend Dependencies**

    ```sh
    pip install -r requirements.txt
    ```

5. **Set Up Frontend (if required)**

    If your project uses Node.js for frontend dependencies, install them:

    ```sh
    cd frontend
    npm install
    cd ..
    ```

6. **Run the Application Locally**

    ```sh
    python app.py
    ```

7. **Access the Application**

    Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Project Details

### Backend

- **Framework**: Flask
- **Main File**: `app.py`
- **Data Source**: `final_dataframe.csv`

### Frontend

- **HTML**: `index.html` and other related HTML files in the `frontend` directory.
- **CSS**: `style.css`
- **JavaScript**: `script.js`

### Routes

- **`/`**: Serves the main page.
- **`/data/<ticker>`**: API endpoint to get data for the specified ticker symbol.

### How It Works

1. The user enters a stock ticker symbol in the input field.
2. The JavaScript function `fetchData` makes an API call to the backend with the ticker symbol.
3. The backend filters the CSV data based on the ticker symbol and returns the relevant data as JSON.
4. The frontend displays the data in a structured format along with visualizations.

## Troubleshooting

### Common Issues

1. **Large File Detected Error**

    If you encounter an error regarding large files when pushing to GitHub, consider using Git LFS (Large File Storage).

    ```sh
    git lfs install
    git lfs track "*.csv"
    git add .gitattributes
    git add final_dataframe.csv
    git commit -m "Track large CSV file with Git LFS"
    git push origin main
    ```

2. **Virtual Environment Activation**

    Ensure you have activated the virtual environment before running the application.

    ```sh
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

---
