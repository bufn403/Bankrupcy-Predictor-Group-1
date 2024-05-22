async function fetchData() {
    const ticker = document.getElementById('tickerInput').value;
    if (!ticker) return;

    const response = await fetch(`/data/${ticker}`);
    const data = await response.json();

    const display = document.getElementById('dataDisplay');
    display.innerHTML = ''; // Clear previous data

    if (data.length > 0) {
        data.forEach(item => {
            display.innerHTML += `<div>
                <strong>Ticker:</strong> ${item.Ticker}<br>
                <strong>FinBERT Classification:</strong> ${item.fibert_classification}<br>
                <strong>GPT Classification:</strong> ${item.gpt_classification}<br>
                <strong>Quotes:</strong> ${item.gpt_quote}<br>
                <strong>Reasoning:</strong> ${item.gpt_reason}
            </div>`;
        });
    } else {
        display.innerHTML = '<div>No data found for the entered ticker.</div>';
    }
}
