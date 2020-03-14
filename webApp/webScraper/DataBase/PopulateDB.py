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


f1 = json.loads(open('Artificial_intelligence_usajob_data.json').read())
t1 = json.loads(open('artificial_intelligience_github_data.json').read())
f2 = json.loads(open('Computer_engineering_usajob_data.json').read())
t2 = json.loads(open('computer_engineering_github_data.json').read())
f3 = json.loads(open('Deep_learning_usajob_data.json').read())
t3 = json.loads(open('deep_learning_github_data.json').read())
f4 = json.loads(open('Machine_learning_usajob_data.json').read())
t4 = json.loads(open('machine_learning_github_data.json').read())
f_all = [f1, f2, f3, f4]
t_all = [t1, t2, t3, t4]


for x in f_all:
    for jobs in x:
        if jobs.get('Technology') == ['']:
            jobs['Technology'] = ['none']
        if jobs.get('Skills') == ['']:
            jobs['Skills'] = ['none']
        if jobs.get('Pay') == '':
            jobs['Pay'] = '0'


for x in t_all:
    for jobs in x:
        if jobs.get('Technology') == ['']:
            jobs['Technology'] = ['none']
        if jobs.get('Skills') == ['']:
            jobs['Skills'] = ['none']
        if jobs.get('Pay') == '':
            jobs['Pay'] = '0'


def pop_git_table():
    c_nter = 0
    for y in t_all:
        for job in y:
            if c_nter % 10 ==0:
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
            c_nter = c_nter + 1


def pop_usa_jobs_table():
    c_nter= 0
    for y in f_all:
        for job in y:
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
            c_nter = c_nter + 1


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
    cnt= 0
    git_table = dynamo_db.Table('GitHubJobs')
    usa_table = dynamo_db.Table('USAJobs')
    table1 = git_table.scan()
    table2 = usa_table.scan()
    data1 = table1['Items']
    data2 = table2['Items']
    print(table1['Count'])
    print(table2['Count'])
    while 'LastEvaluatedKey' in table1:
        table1 = git_table.scan(ExclusiveStartKey=table1['LastEvaluatedKey'])
        data1.extend(table1['Items'])

    while 'LastEvaluatedKey' in table2:
        table2 = usa_table.scan(ExclusiveStartKey=table2['LastEvaluatedKey'])
        data2.extend(table2['Items'])
    cnt = len(data1) + len(data2)

    return cnt


pop_git_table()

