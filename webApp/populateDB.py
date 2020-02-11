'''
populateDB.py ultimately receives data from webScraper/Scrape.py
and uploads to the AWS Dynamo DB using the boto3 module
'''
from webScraper import Scrape

if __name__ == '__main__':
    Scrape.usajob('token',
               'email', 'PositionTitle', 'Software%20Developer')

    Scrape.github()
