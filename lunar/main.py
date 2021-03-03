import argparse
import os
from dotenv import load_dotenv
import boto3
from botocore.exceptions import ClientError

load_dotenv(dotenv_path='../.env')

RAW_DIR = '../raw-data'
BUCKET_NAME = 'dss2021'
SYMBOLS = open('../targets.txt') # Open symbol list

s3 = boto3.client('s3',
    aws_access_key_id=os.getenv('ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('SECRET_ACCESS_KEY')
)

parser = argparse.ArgumentParser(description='Commandline utility to upload/download raw data to the moon (AWS)')
subparsers = parser.add_subparsers(dest='command', required=True)
parser_upload = subparsers.add_parser('upload', help='Upload data to AWS')
parser_download = subparsers.add_parser('download', help='Download data from AWS')

args = parser.parse_args()

def upload_stock(symbol):
    try:
        response = s3.upload_file(
            '{raw_dir}/{symbol}.csv'.format(raw_dir=RAW_DIR, symbol=symbol),
            BUCKET_NAME,
            '{symbol}.csv'.format(symbol=symbol)
        )
    except ClientError as e:
        print(e)
        return False

    return True


if args.command == 'upload':
    for symbol in SYMBOLS:
        print('Uploading {}'.format(symbol.strip()))
        result = upload_stock(symbol.strip())
        if result == False:
            break
elif args.command == 'download':
    print('Unsupported atm - check back later')
