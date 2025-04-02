# Bybit Market Data Fetcher

## Overview
This Python script fetches market data and order book information from Bybit using the PyBit library.
The data is saved in CSV format for further analysis.

## Features
- Fetches market ticker data for `NEARUSDT`
- Retrieves order book information
- Saves results in CSV files
- Uses environment variables for API authentication

## Prerequisites
- Python 3.9+
- Bybit API credentials
- A `.env` file containing your API keys

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/bybit-data-fetcher.git
   cd bybit-data-fetcher
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your API credentials:
   ```ini
   api_key=your_api_key_here
   api_secret=your_api_secret_here
   ```

## Usage
Run the script to fetch market data and save it to CSV files:
```sh
python bybit_data_fetch.py
```

## Output
- `ticker.csv` - Contains market ticker information
- `order_book.csv` - Contains order book data

## Notes
- The script runs in Bybit **testnet** mode. Modify `testnet=False` to use the live API.
- Ensure your API key has the correct permissions.

## License
MIT License

