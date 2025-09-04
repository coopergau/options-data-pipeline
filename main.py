import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd
from dotenv import load_dotenv
import os

def get_expiration_dates(expiration_dates, days_out=31):
    # Returns expiration dates that fall within the next 'days_out' days
    current_date = datetime.now()
    last_date = current_date + timedelta(days=days_out)
    dates = []
    for date_string in expiration_dates:
        date_object = datetime.strptime(date_string, '%Y-%m-%d')
        if date_object <= last_date:
            dates.append(date_string)
    return dates

def get_chain_df(ticker, exp_date, option_type, stock_price):
    # Returns options chain dataframe from yfinance
    if option_type == 'call':
        chain = ticker.option_chain(exp_date).calls
    elif option_type == 'put':
        chain = ticker.option_chain(exp_date).puts
    else:
        raise ValueError(f'Invalid option type: "{option_type}". Must be "call" or "put"')
        
    chain['ticker'] = ticker.ticker
    chain['exp_date'] = exp_date
    chain['option_types'] = option_type
    chain['stock_price'] = stock_price
    return chain


def main():
    option_types = ['call', 'put']
    all_ticker_names = open('nasdaq100.txt').read().splitlines()

    for option_type in option_types:
        df_list = []
        
        for ticker_name in all_ticker_names:
            ticker = yf.Ticker(ticker_name)
            all_exp_dates = ticker.options
            exp_dates = get_expiration_dates(all_exp_dates)
            stock_price = ticker.fast_info['lastPrice']
            
            for exp_date in exp_dates:
                chain = get_chain_df(ticker, exp_date, option_type, stock_price)
                df_list.append(chain)
            
        combined_df = pd.concat(df_list, ignore_index=True)

if __name__ == '__main__':
    main()