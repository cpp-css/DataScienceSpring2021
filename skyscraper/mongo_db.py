from pymongo import MongoClient

def fill_database (json_response, ticker):
    conn = MongoClient('localhost', 27017)
    db = conn["stocks"]
    K = 3
    collection = db[ticker]
    response = json_response
    raw_data = response.text.split('\n')

    for i in range(1, len(raw_data)):
        row = raw_data[i].split(',')
        post = {
            '_id': i,
            'date': row[0],
            'open': round(float(row[1]), K),
            'high': round(float(row[2]), K),
            'low': round(float(row[3]), K),
            'close': round(float(row[4]), K),
            'adj close': round(float(row[5]), K),
            'volume': round(float(row[6]), K)
        }
        collection.insert_one(post)
