# Crypto Price Fetcher

This Python script fetches and displays real-time cryptocurrency prices in USD using the CoinGecko API. The prices are formatted nicely, with thousands separators for larger values and appropriate decimal places for smaller values (e.g., SHIB, DOGE).

### Features:

- Fetches real-time cryptocurrency prices.
- Supports multiple cryptocurrencies via symbols (e.g., BTC, ETH, DOGE).
- Formats prices for better readability (commas for thousands, correct decimal places).
- Polls the CoinGecko API every 30 seconds for updated prices.
- Handles invalid cryptocurrency symbols gracefully.

---

## Requirements

To run this script, you need to have the following Python libraries installed:

- `requests`: For making HTTP requests to the CoinGecko API.
- `colorama`: For colored terminal output.

You can install the required libraries by running:

```bash
pip install requests colorama
```

## How to Use

- Clone or download the repository to your local machine.
- Make sure you have the required dependencies installed.
- Run the script:

```bash
python crypto_price_fetcher.py
```

- Enter a comma-separated list of cryptocurrency symbols when prompted (e.g., BTC, ETH, DOGE).

- _Example input: BTC,ETH,DOGE,SHIB_

The script will display the prices in USD and continue to update every 30 seconds until stopped manually.

## Example Output

When running the script, you will see output similar to this:

```bash
Enter cryptocurrency symbols (comma separated, e.g., BTC,ETH): BTC,ETH,SHIB
BTC: $89,784.00
ETH: $3,175.06
SHIB: $0.00002535

Prices will now be fetched every 30 seconds...
Fetching prices...
BTC: $89,785.00
ETH: $3,176.10
SHIB: $0.00002530
```

- BTC: Formatted with commas for thousands and two decimal places.
- SHIB: Displayed with up to 8 decimal places for small values.
- Prices will continue updating every 30 seconds.

## Script Breakdown

1. format_price(price_value): This function formats the price according to the value. If the price is larger than 1, it shows two decimal places and adds commas for thousands. If it's smaller than 1, it adjusts the decimal places based on the value.
2. get_prices(crypto_symbols): This function takes a list of cryptocurrency symbols, queries the CoinGecko API, and displays the prices for valid cryptocurrencies. Invalid symbols are handled with an error message.
3. main(): This function runs the script, allowing the user to input cryptocurrency symbols and then fetching and displaying the prices. It also continuously polls the CoinGecko API every 30 seconds.

# Notes

- Ensure you have internet access to fetch prices from the CoinGecko API.
- Invalid cryptocurrency symbols (not in the crypto_symbols.py file) will be reported as errors.
- The script is designed to run in the terminal, and it uses colorama for colored outputs (e.g., green for valid prices, red for errors).
