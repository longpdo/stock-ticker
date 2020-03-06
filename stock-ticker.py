from colorama import Fore, Back, Style
from datetime import datetime
import json
import os
import pandas
import sys
import time

minutes_between_updates = 5

indices_dict = {
    '^GSPC': 'S&P 500',
    '^DJI': 'DOW 30',
    '^IXIC': 'NASDAQ',
    '^GDAXI': 'DAX',
    '^FTSE': 'FTSE 100',
    '^STOXX50E': 'EURO STOXX 50',
}

currency_dict = {
    'EURUSD=X': 'EUR/USD',
    'EURGBP=X':	'EUR/GBP',
    'EURCHF=X':	'EUR/CHF',
    'EURJPY=X': 'EUR/JPY',
    'GC=F': 'GOLD',
    'BTC-EUR': 'BTC',
    'ETH-EUR': 'ETH'
}

keys_dict = {
    'symbol': 'SYMBOL',
    'shortName': 'NAME',
    'currency': 'CUR',
    'regularMarketPrice': 'PRICE',
    'regularMarketChangePercent': 'CHANGE%',
    'regularMarketDayLow': 'LOW',
    'regularMarketDayHigh': 'HIGH',
    'fiftyTwoWeekLow': 'LOW52',
    'fiftyTwoWeekHigh': 'HIGH52',
    'fiftyTwoWeekLowChangePercent': 'LOW52%',
    'fiftyTwoWeekHighChangePercent': 'HIGH52%',
    'fiftyDayAverage': 'MA50',
    'twoHundredDayAverage': 'MA200',
    'fiftyDayAverageChangePercent': 'MA50%',
    'twoHundredDayAverageChangePercent': 'MA200%',
    'regularMarketTime': 'TIME',
    'fullExchangeName': 'EXCHANGE'
}


def get_ticker_symbols():
    if not os.path.isfile(sys.argv[1]):
        return sys.argv[1:]

    watchlist_path = sys.argv[1]
    file_reader = open(watchlist_path, 'r')
    ticker_symbols = file_reader.read().splitlines()
    file_reader.close()
    return ticker_symbols


def build_headline(symbol_dict):
    headline = ''
    for symbol, name in symbol_dict.items():
        stock_info = _get_stock_info(symbol)
        headline += _color_yellow(name) + ' ' + _color_white(
            stock_info['regularMarketPrice']) + ' ' + _color_red_green(
                stock_info['regularMarketChangePercent']/100) + ' | '
    return headline


def get_all_stocks(symbols):
    stocks = []
    for symbol in symbols:
        stock_info = _get_stock_info(symbol)
        # Filter python objects with list comprehensions
        filtered_d = dict((v, stock_info[k]) for k, v in keys_dict.items())
        stocks.append(filtered_d)
    return stocks


def _get_stock_info(symbol):
    library = "curl --silent "
    link = "https://query1.finance.yahoo.com/v7/finance/quote?symbols="
    cmd = library + link + symbol
    output_string = _run_terminal_cmd(cmd)
    stock_info = json.loads(output_string)
    return stock_info['quoteResponse']['result'][0]


def _run_terminal_cmd(cmd):
    stream = os.popen(cmd)
    output = stream.read()
    return output


def build_dataframe(stocks):
    df = pandas.DataFrame(stocks)
    # Converts epoch into readable time
    df['TIME'] = pandas.to_datetime(df['TIME'], unit='s')
    df['TIME'] = df['TIME'].dt.time

    # Styles negative and positive values with red or green
    df['CHANGE%'] = (df['CHANGE%'].astype(float)/100).apply(_color_red_green)
    df['LOW52%'] = df['LOW52%'].astype(float).apply(_color_red_green)
    df['HIGH52%'] = df['HIGH52%'].astype(float).apply(_color_red_green)
    df['MA50%'] = df['MA50%'].astype(float).apply(_color_red_green)
    df['MA200%'] = df['MA200%'].astype(float).apply(_color_red_green)

    # Adds ansi codes to the rest to offset the TextAdjustment from pandas
    # or: https://github.com/pandas-dev/pandas/issues/18066#issuecomment-522192922
    df['SYMBOL'] = df['SYMBOL'].apply(_color_yellow)
    df['NAME'] = df['NAME'].apply(_color_yellow)
    df['CUR'] = df['CUR'].apply(_color_yellow)
    df['PRICE'] = df['PRICE'].apply(_color_white)
    df['LOW'] = df['LOW'].apply(_color_white)
    df['HIGH'] = df['HIGH'].apply(_color_white)
    df['LOW52'] = df['LOW52'].apply(_color_white)
    df['HIGH52'] = df['HIGH52'].apply(_color_white)
    df['MA50'] = df['MA50'].apply(_color_white)
    df['MA200'] = df['MA200'].apply(_color_white)
    df['TIME'] = df['TIME'].apply(_color_yellow)
    df['EXCHANGE'] = df['EXCHANGE'].apply(_color_yellow)

    colored_headers = dict((v, _color_yellow(v)) for v in keys_dict.values())
    df = df.rename(columns=colored_headers)

    return df.to_string(index=False)


def _color_red_green(val):
    if val >= 0:
        color = Fore.GREEN
    if val < 0:
        color = Fore.RED
    return color + '(' + str('{:.2%}'.format(val)) + ')' + Style.RESET_ALL


def _color_yellow(val):
    return Fore.YELLOW + str(val) + Style.RESET_ALL


def _color_white(val):
    return Fore.RESET + str('{:.2f}'.format(val)) + Style.RESET_ALL


if __name__ == '__main__':
    symbols = get_ticker_symbols()

    while True:
        index_headline = build_headline(indices_dict)
        currency_headline = build_headline(currency_dict)
        stocks = get_all_stocks(symbols)
        dataframe = build_dataframe(stocks)

        os.system('cls||clear')
        print('\n' + index_headline)
        print(currency_headline + '\n')
        print(dataframe)
        print('\n updated: ' + datetime.now().strftime('%H:%M:%S'))

        time.sleep(minutes_between_updates*60)
