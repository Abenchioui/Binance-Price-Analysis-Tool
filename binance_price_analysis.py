import pandas as pd
from binance.client import Client
from datetime import datetime

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


def main():
    Pkey = get_user_input("Enter Your Binance API key")
    Skey = get_user_input("Enter Your Binance SECRET key")
    Symbol = get_user_input("Enter the symbol (e.g., BTCUSDT)")

    # Ask the user to choose the date format
    date_format = get_date_format()

    From = get_date_input('Enter the start date (e.g., "DD-MM-YYYY")', date_format)
    To = get_date_input('Enter the end date (e.g., "DD-MM-YYYY")', date_format)

    client = Client(api_key=Pkey, api_secret=Skey)

    klines = client.get_historical_klines(Symbol, Client.KLINE_INTERVAL_1DAY, From, To)

    if klines:
        df = pd.DataFrame(klines, columns=columns)

        # Convert relevant columns to numeric
        numeric_columns = ["open", "high", "low", "close", "volume", "quote_vol"]
        df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors="coerce")

        max_price = df["high"].max()
        low_price = df["low"].min()
        pct_change = round((max_price - low_price) / low_price * 100, 2)
        pct_change = abs(pct_change)  # Make sure it's positive for display purposes

        print(f"Max Price: {max_price}")
        print(f"Low Price: {low_price}")
        print("Percentage Change:", pct_change, "%")
    else:
        print("No data available for the specified period or symbol.")


def get_user_input(prompt):
    return input(f"{prompt}: ")


def get_date_input(prompt, date_format):
    date_str = input(f"{prompt}: ")
    try:
        # Parse the entered date based on the chosen format
        date_obj = datetime.strptime(date_str, date_format).strftime("%Y-%m-%d")
        return date_obj
    except ValueError:
        print(f"Invalid date format. Please use {date_format}.")
        return get_date_input(prompt, date_format)


def get_date_format():
    while True:
        # Provide options for date format
        print("Choose the date format:")
        print("1. DD-MM-YYYY")
        print("2. MM-DD-YYYY")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            return "%d-%m-%Y"
        elif choice == "2":
            return "%m-%d-%Y"
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
