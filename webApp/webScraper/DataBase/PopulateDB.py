import boto3
from boto3.dynamodb.conditions import Key, Attr
import random
import json
import time
import os

dynamoDB = boto3.client(
    'dynamodb', aws_access_key_id=os.getenv('AWS_PUB'),
    aws_secret_access_key=os.getenv('AWS_PRIV'), region_name='us-east-2'
)

dynamo_db = boto3.resource(
    'dynamodb', aws_access_key_id=os.getenv('AWS_PUB'),
    aws_secret_access_key=os.getenv('AWS_PRIV'), region_name='us-east-2'
)


# f = open('webApp/usajob_data.json')
t = json.loads(open('github_data.json').read())
cnt = 0
cnt_p = 0
for jobs in t:
    if jobs.get('Technology') == ['']:
        jobs['Technology'] = ['none']
    if jobs.get('Skills') == ['']:
        jobs['Skills'] = ['none']
    if jobs.get('Pay') == '':
        jobs['Pay'] = '0'
        cnt_p = cnt_p + 1

    cnt = cnt+1



def pop_git_table():
    c_nter = 0

    for job in t:
        if c_nter % 10 == 0:
            print(c_nter)
            time.sleep(1)
        dynamoDB.put_item(
            TableName='GitHubJobs',
            Item={
                'ID': {
                    'S': job.get('ID')
                },
                'JobRole': {
                    'S': job.get('JobRole')
                },
                'CompanyName': {
                    'S': job.get('CompanyName')
                },
                'JobType': {
                    'S': job.get('JobType')
                },
                'Pay': {
                    'S': job.get('Pay')
                },
                'City': {
                    'S': job.get('City')
                },
                'State': {
                    'S': job.get('State')
                },
                'Skills': {
                   'SS': job['Skills']
                },
                'Technology': {
                   'SS': job['Technology']
                },
                'URL': {
                    'S': job.get('URL')
                }
            }
        )
        c_nter= c_nter+1


def pop_usa_jobs_table():
    c_nter= 0
    for job in t:
        if c_nter % 10 == 0:

            time.sleep(1)
        dynamoDB.put_item(
            TableName='USAJobs',
            Item={
                'ID': {
                    'S': job['ID']
                },
                'JobRole': {
                    'S': job['JobRole']
                },
                'CompanyName': {
                    'S': job['CompanyName']
                },
                'JobType': {
                    'S': job['JobType']
                },
                'Pay': {
                    'S': job['Pay']
                },
                'City': {
                    'S': job['City']
                },
                'State': {
                    'S': job['State']
                },
                'Skills': {
                   'SS': job['Skills']
                },
                'Technology': {
                   'SS': job['Technology']
                },
                'URL': {
                    'S': job['URL']
                }
            }
        )
        c_nter= c_nter+1


# query with param state, role ie. entry level or junior, top 2 tech

def query_usa(state, role, tech1):
    table = dynamo_db.Table('USAJobs')

    a = Attr('State').eq(state) & Attr('JobRole').contains(role)

    for tech in tech1.split(','):
        a = a & Attr('Technology').contains(tech1)

    data = table.scan(
        TableName='USAJobs',
        FilterExpression=a
    )
    return data['Items']


def query_github(state, role, tech):
    table = dynamo_db.Table('GitHubJobs')

    a = Attr('State').eq(state) & Attr('JobRole').contains(role)

    for tech1 in tech.split(','):
        a = a & Attr('Technology').contains(tech1)

    data = table.scan(
        TableName='GitHubJobs',
        FilterExpression=a
    )
    return data['Items']


# functions to test above functions

def pop_test():
    count = 0
    skills1 = ['red', 'blue', 'yellow']
    skills2 = ['purple']
    skills3 = ['green', 'gold']
    tech1 = ['purple', 'green', 'red']
    tech2 = ['gold', 'purple']

    while count < 10:
        skill = random.choice([skills1, skills2, skills3])
        tech = random.choice([tech1, tech2])

        dynamoDB.put_item(
            TableName='USAJobs',
            Item={
                'ID': {
                    'S': 's' + str(count)
                },
                'JobRole': {
                    'S': 'entry level'
                },
                'CompanyName': {
                    'S': 'company'
                },
                'JobType': {
                    'S': 'engineer'
                },
                'Pay': {
                    'S': 'not enough'
                },
                'City': {
                    'S': 'chicago'
                },
                'State': {
                    'S': 'IL'
                },
                'Skills': {
                    'SS': skill
                },
                'Technology': {
                    'SS': tech
                },
                'URL': {
                    'S': 'to long not typing'
                }
            }
        )
        count = count + 1


def query_test(state, role, tech):
    table = dynamo_db.Table('GitHubJobs')

    a = Attr('State').eq(state) & Attr('JobRole').contains(role)

    for tech1 in tech.split(','):
        a = a & Attr('Technology').contains(tech1)

    data = table.scan(
        TableName='GitHubJobs',
        FilterExpression=a
    )
    print(data['Count'])
    for x in data['Items']:
        print(x)


# function to give count of items in database


def count():
    t = dynamo_db.Table('GitHubJobs')
    t2 = dynamo_db.Table('USAJobs')
    table1 = t.scan()
    table2 = t2.scan()
    cnt = int(table1['Count']) + int(table2['Count'])

    return cnt


# pop_test()

# query_test('IL', 'entry level', 'red')

# pop_git_table()
