# Binance Price Analysis Tool

## Overview

This Python script leverages the Binance API to retrieve historical price data for a specified cryptocurrency symbol within a user-defined date range. It analyzes the data to determine the maximum and minimum prices during that period, along with the percentage change.

## Prerequisites

- Python 3.x
- Binance API key and secret

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Abenchioui/binance-price-analysis.git
    cd binance-price-analysis
    ```

2. **Install required packages:**

    ```bash
    pip install pandas
    ```

## Usage

1. **Run the script:**

    ```bash
    python binance_price_analysis.py
    ```

2. **Enter your Binance API key, secret key, and the cryptocurrency symbol when prompted.**

3. **Choose the date format for input (DD-MM-YYYY or MM-DD-YYYY) and enter the start and end dates accordingly.**

4. **The script will fetch historical data and display the maximum price, minimum price, and percentage change.**

## Example

```bash
Enter Your Binance API key: YOUR_API_KEY
Enter Your Binance SECRET key: YOUR_SECRET_KEY
Enter the symbol (e.g., BTCUSDT): BTCUSDT

Choose the date format:
1. DD-MM-YYYY
2. MM-DD-YYYY
Enter the number of your choice: 1

Enter the start date (e.g., "DD-MM-YYYY"): 01-01-2022
Enter the end date (e.g., "DD-MM-YYYY"): 10-01-2022

Max Price: 50000.0
Low Price: 30000.0
Percentage Change: 66.67%
