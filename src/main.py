import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv()

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

def connect_to_database():
    try:
        database_url = f'postgresql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}'
        engine = create_engine(database_url)

        # Test connection
        with engine.connect() as connect:
            print(f'Connected to Database')
        return engine
    except Exception as e:
        print(f'Error connecting to database: {e}')
        raise
   

def save_to_database(df, table_name, engine):
    try:
        df.to_sql(table_name, engine, if_exists='append', index=False)
        print(f'Successfuly saved {len(df)} rows to {table_name} table')
    except Exception as e:
        print(f'Error saving to database: {e}')
        raise

def main():

    engine = connect_to_database()

    ticker_file = os.path.join(os.path.dirname(__file__), 'nasdaq100.txt')
    all_ticker_names = open(ticker_file).read().splitlines()

    option_tables = {'call': 'call_options', 'put': 'put_options'}
    
    for option_type, table_name in option_tables.items():
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
        save_to_database(combined_df, table_name, engine)

if __name__ == '__main__':
    main()