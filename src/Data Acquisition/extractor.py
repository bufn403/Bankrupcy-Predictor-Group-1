import time
import sys
from dataloader import DataLoader

"""
This script automates the retrieval and storage of management discussion sections from quarterly reports (10-Q)
for a large list of company tickers. It utilizes the Yahoo Finance API via a custom DataLoader class to fetch the
data for the specified year and quarter. Each management discussion is saved into a separate text file for further
analysis. The script handles errors gracefully, logs skipped tickers due to failures, and includes a delay between
requests to manage API usage limits and ensure compliance with service rate limits. This automation aids in financial
analysis by providing a systematic approach to collecting management insights from publicly traded companies.
"""


# List of tickers for which to fetch management discussions
tickers = [
    "MMM", "AOS", "ABT", "ABBV", "ACN", "ADBE", "AMD", "AES", "A", "APD", "ABNB", "AKAM", "ALB", "ARE", "ALGN", "ALLE", 
    "LNT", "GOOGL", "GOOG", "MO", "AMZN", "AMCR", "AEE", "AAL", "AEP", "AMT", "AWK", "AME", "AMGN", "APH", "ADI", "ANSS",
    "APA", "AAPL", "AMAT", "APTV", "ADM", "ANET", "T", "ATO", "ADSK", "ADP", "AZO", "AVB", "AVY", "AXON", "BKR", "BALL",
    "BBWI", "BAX", "BDX", "BBY", "BIO", "TECH", "BIIB", "BA", "BKNG", "BWA", "BXP", "BSX", "BMY", "AVGO", "BR", "BF.B",
    "BLDR", "BG", "CDNS", "CZR", "CPT", "CPB", "CAH", "KMX", "CCL", "CARR", "CTLT", "CAT", "CBRE", "CDW", "CE", "COR",
    "CNC", "CNP", "CF", "CHRW", "CRL", "CHTR", "CVX", "CMG", "CHD", "CI", "CTAS", "CSCO", "C", "CFG", "CLX", "CME", "CMS",
    "KO", "CTSH", "CL", "CMCSA", "CMA", "CAG", "COP", "ED", "STZ", "CEG", "COO", "CPRT", "GLW", "CPAY", "CTVA", "CSGP",
    "COST", "CTRA", "CCI", "CSX", "CMI", "CVS", "DHR", "DRI", "DVA", "DAY", "DECK", "DE", "DAL", "DVN", "DXCM", "FANG",
    "DLR", "DFS", "DG", "DLTR", "D", "DPZ", "DOV", "DOW", "DHI", "DTE", "DUK", "DD", "EMN", "ETN", "EBAY", "ECL", "EIX",
    "EW", "EA", "ELV", "LLY", "EMR", "ENPH", "ETR", "EOG", "EPAM", "EQT", "EFX", "EQIX", "EQR", "ESS", "EL", "ETSY", "EG",
    "EVRG", "ES", "EXC", "EXPE", "EXPD", "EXR", "XOM", "FFIV", "FDS", "FICO", "FAST", "FRT", "FDX", "FIS", "FITB", "FSLR",
    "FE", "FI", "FMC", "F", "FTNT", "FTV", "FOXA", "FOX", "BEN", "FCX", "GRMN", "IT", "GE", "GEHC", "GEV", "GEN", "GNRC",
    "GD", "GIS", "GM", "GPC", "GILD", "GPN", "GL", "GS", "HAL", "HIG", "HAS", "HCA", "DOC", "HSIC", "HSY", "HES", "HPE",
    "HLT", "HOLX", "HD", "HON", "HRL", "HST", "HWM", "HPQ", "HUBB", "HUM", "HBAN", "HII", "IBM", "IEX", "IDXX", "ITW",
    "ILMN", "INCY", "IR", "PODD", "INTC", "ICE", "IFF", "IP", "IPG", "INTU", "ISRG", "IVZ", "INVH", "IQV", "IRM", "JBHT",
    "JBL", "JKHY", "J", "JNJ", "JCI", "JPM", "JNPR", "K", "KVUE", "KDP", "KEY", "KEYS", "KMB", "KIM", "KMI", "KLAC", "KHC",
    "KR", "LHX", "LH", "LRCX", "LW", "LVS", "LDOS", "LEN", "LIN", "LYV", "LKQ", "LMT", "L", "LOW", "LULU", "LYB", "MTB",
    "MRO", "MPC", "MKTX", "MAR", "MMC", "MLM", "MAS", "MA", "MTCH", "MKC", "MCD", "MCK", "MDT", "MRK", "META", "MET", "MTD",
    "MGM", "MCHP", "MU", "MSFT", "MAA", "MRNA", "MHK", "MOH", "TAP", "MDLZ", "MPWR", "MNST", "MCO", "MS", "MOS", "MSI",
    "MSCI", "NDAQ", "NTAP", "NFLX", "NEM", "NWSA", "NWS", "NEE", "NKE", "NI", "NDSN", "NSC", "NTRS", "NOC", "NCLH", "NRG",
    "NUE", "NVDA", "NVR", "NXPI", "ORLY", "OXY", "ODFL", "OMC", "ON", "OKE", "ORCL", "OTIS", "PCAR", "PKG", "PANW", "PARA",
    "PH", "PAYX", "PAYC", "PYPL", "PNR", "PEP", "PFE", "PCG", "PM", "PSX", "PNW", "PXD", "PNC", "POOL", "PPG", "PPL", "PFG",
    "PG", "PGR", "PLD", "PRU", "PEG", "PTC", "PSA", "PHM", "QRVO", "PWR", "QCOM", "DGX", "RL", "RJF", "RTX", "O", "REG",
    "REGN", "RF", "RSG", "RMD", "RVTY", "RHI", "ROK", "ROL", "ROP", "ROST", "RCL", "SPGI", "CRM", "SBAC", "SLB", "STX",
    "SRE", "NOW", "SHW", "SPG", "SWKS", "SJM", "SNA", "SOLV", "SO", "LUV", "SWK", "SBUX", "STT", "STLD", "STE", "SYK",
    "SMCI", "SYF", "SNPS", "SYY", "TMUS", "TROW", "TTWO", "TPR", "TRGP", "TGT", "TEL", "TDY", "TFX", "TER", "TSLA", "TXN",
    "TXT", "TMO", "TJX", "TSCO", "TT", "TDG", "TRV", "TRMB", "TFC", "TYL", "TSN", "USB", "UBER", "UDR", "ULTA", "UNP", "UAL",
    "UPS", "URI", "UNH", "UHS", "VLO", "VTR", "VLTO", "VRSN", "VRSK", "VZ", "VRTX", "VTRS", "VICI", "V", "VMC", "WRB", "WAB",
    "WBA", "WMT", "DIS", "WBD", "WM", "WAT", "WEC", "WFC", "WELL", "WST", "WDC", "WRK", "WY", "WMB", "WTW", "GWW", "WYNN",
    "XEL", "XYL", "YUM", "ZBRA", "ZBH", "ZTS"
]

# Adding directory to system path for importing custom modules
sys.path.append('../src')

# Load data using DataLoader class
data_loader = DataLoader()
year = 2023
quarter = 1

# Track skipped tickers due to errors
skipped = []

# Process each ticker to download and save its management discussion
for ticker in tickers:
    try:
        management_discussion = data_loader.load_management_discussion(ticker, year, quarter)
        with open(f'../data/10q/{ticker}_management_discussion_{year}Q{quarter}.txt', 'w') as f:
            f.write(management_discussion)
            print(f'Saved {f.name}')
    except Exception as e:
        print(f'Skipping ticker {ticker}: {e}')
        skipped.append(ticker)
    
    # Pause between requests to avoid overloading the server
    time.sleep(0.2)

# Print skipped tickers and their count
print(skipped)
print(f'Number of skipped tickers: {len(skipped)}')
