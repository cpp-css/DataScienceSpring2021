from datetime import date
import math
import os
import time
import requests

ENDPOINT = 'https://query1.finance.yahoo.com/v7/finance/download/{symbol}?period1={start}&period2={end}&interval={interval}&events={events}&includeAdjustedClose=true'
OUTPUT_DIR = '../raw-data/'

os.makedirs(OUTPUT_DIR, exist_ok=True) # Ensure output directory is created
SYMBOLS = open('../targets.txt') # Open symbol list

today = math.floor(time.time())

for symbol in SYMBOLS:
    symbol = symbol.strip()
    url = ENDPOINT.format(
        symbol=symbol, start=0, end=today, interval='1d', events='historical'
    )
    print('Attempting to load stock {}...'.format(symbol))
    print('URL: {}'.format(url))
    response = requests.get(url)
    if response.status_code != 200:
        print('Rate limit hit!')
        break

    raw_data = response.text
    output = open(OUTPUT_DIR + '{}.csv'.format(symbol), 'w')
    output.write(raw_data)
