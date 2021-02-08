import requests
import time
import math

STOCKS = ['GME', 'AMC']
ENDPOINT = 'https://query1.finance.yahoo.com/v7/finance/download/{symbol}?period1={start}&period2={end}&interval={interval}&events={events}&includeAdjustedClose=true'

for stock in STOCKS:
    today = math.floor(time.time())
    url = ENDPOINT.format(
        symbol=stock, start=0, end=today, interval='1d', events='historical'
    )

    response = requests.get(url)
    raw_data = response.text.split('\n')

    for i in range(0, len(raw_data)):
        row = raw_data[i].split(',')
        print(row)
