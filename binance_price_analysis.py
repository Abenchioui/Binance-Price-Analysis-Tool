import pandas as pd
from binance.client import Client
from binance.exceptions import BinanceAPIException
from datetime import datetime

def main():
    client = None

    while client is None:
        try:
            Pkey = get_user_input("Enter Your Binance API key")
            Skey = get_user_input("Enter Your Binance SECRET key")
            client = Client(api_key=Pkey, api_secret=Skey)
        except BinanceAPIException as e:
            print(f"Binance API Error: {e}")
            print("Invalid API key or secret key. Please try again.")

    symbol = None

    while symbol is None:
        try:
            symbol = get_user_input("Enter the symbol (e.g., BTCUSDT)")
            # Check if the symbol is valid
            client.get_symbol_info(symbol)
        except BinanceAPIException as e:
            print(f"Binance API Error: {e}")
            print("Invalid symbol. Please try again.")

    start_date, end_date = None, None

    while start_date is None or end_date is None or end_date < start_date:
        try:
            start_date = get_date_input('Enter the start date (e.g., "YYYY-MM-DD")')
            end_date = get_date_input('Enter the end date (e.g., "YYYY-MM-DD")')

            if end_date < start_date:
                print("End date cannot be earlier than start date. Please try again.")
                end_date = get_date_input('Enter the end date (e.g., "YYYY-MM-DD")')  # Allow the user to modify only the end date
        except ValueError as e:
            print(f"Error: {e}")
            print("Invalid date format. Please try again.")

    try:
        klines = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1DAY, start_date, end_date)

        if klines:
            columns = [
                "open_time",
                "open",
                "high",
                "low",
                "close",
                "volume",
                "close_time",
                "quote_vol",
                "num_trades",
                "taker_buy_base_vol",
                "taker_buy_quote_vol",
                "ignore",
            ]
            df = pd.DataFrame(klines, columns=columns)

            # Convert relevant columns to numeric
            numeric_columns = ["open", "high", "low", "close", "volume", "quote_vol"]
            df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors="coerce")

            max_price = max(df["high"])
            low_price = min(df["low"])
            pct_change = round((max_price - low_price) / low_price * 100, 2)
            pct_change = abs(pct_change)  # Make sure it's positive for display purposes

            print(f"Max Price: {max_price} $")
            print(f"Low Price: {low_price} $")
            print("Percentage Change:", pct_change, "%")
        else:
            print(f"No data available for symbol '{symbol}' in the specified period.")
    except BinanceAPIException as e:
        print(f"Binance API Error: {e}")
        print("Invalid symbol. Please try again.")

def get_user_input(prompt):
    return input(f"{prompt}: ")

def get_date_input(prompt):
    date_str = input(f"{prompt}: ")
    date_format = "%Y-%m-%d"

    try:
        date_obj = datetime.strptime(date_str, date_format).strftime(date_format)
        return date_obj
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == "__main__":
    main()
