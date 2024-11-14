import requests
import time
from crypto_symbols import symbol_to_name  # Import the dictionary from crypto_symbols.py
from colorama import Fore, Style, init
# Initialize colorama
init(autoreset=True)

def format_price(price_value):
    if price_value >= 1:
        # For prices >= 1, use commas for thousands and limit to 2 decimal places
        return f"${price_value:,.2f}"
    elif price_value < 0.0001:
        # For small values, use up to 8 decimal places
        return f"${price_value:,.8f}"
    else:
        # For very tiny values, format without scientific notation (up to 4 decimals)
        return f"${price_value:.4f}"

# Function to get prices from CoinGecko API
def get_prices(crypto_symbols):
    url = "https://api.coingecko.com/api/v3/simple/price"
    
    # Convert input symbols to CoinGecko names
    names = [symbol_to_name.get(symbol.lower()) for symbol in crypto_symbols]
    names = [name for name in names if name]  # Filter out None values if invalid symbols were input

    if not names:
        print(Fore.RED + "No valid cryptocurrency symbols entered. Exiting.")
        return False

    # Prepare the symbols to be sent to the API
    symbols = ','.join(names)
    
    # Make the API request
    params = {
        'ids': symbols,  # Crypto ids are needed, e.g., 'bitcoin', 'ethereum'
        'vs_currencies': 'usd'  # Get prices in USD
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Check if the request was successful
        
        # Parse the JSON response
        data = response.json()
        
        # Display the prices for the valid cryptocurrencies
        for symbol in crypto_symbols:
            coingecko_name = symbol_to_name.get(symbol.lower())
            if coingecko_name and coingecko_name in data:
                # Format price
                price = format_price(data[coingecko_name]['usd'])

                # Display the price in green
                print(f"{Style.BRIGHT}{Fore.GREEN}{symbol.upper()}: {price}")
            else:
                # If the coin is not found, print in red
                print(Fore.RED + f"Invalid coin symbol: {symbol.upper()}")
        
        return True
        
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error fetching data: {e}")
        return False

def main():
    # Step 1: Ask user to input a comma separated list of crypto symbols
    crypto_input = input("Enter cryptocurrency symbols (comma separated, e.g., BTC,ETH): ").strip()
    crypto_symbols = [symbol.strip() for symbol in crypto_input.split(',')]

    # Step 2: If no valid cryptocurrencies, exit
    if not crypto_symbols:
        print(Fore.RED + "No symbols entered. Exiting.")
        return

    # Step 3: Get prices for valid cryptocurrencies and exit if none are valid
    if not get_prices(crypto_symbols):
        return

    # Step 4: Start polling every 30 seconds for valid cryptocurrencies
    print(Fore.CYAN + "\nPrices will now be fetched every 30 seconds...")
    while True:
        time.sleep(30)  # Wait for 30 seconds before fetching prices again
        print(Fore.YELLOW + "\nFetching prices...")
        get_prices(crypto_symbols)

# Run the program
if __name__ == "__main__":
    main()
