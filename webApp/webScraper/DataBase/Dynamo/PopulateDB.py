import boto3
from boto3.dynamodb.conditions import Key, Attr
import random
import json

dynamoDB = boto3.client(
    'dynamodb', aws_access_key_id='AKIA5KVCCTT2WXS2FYS3',
    aws_secret_access_key='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', region_name='us-east-2'
)

dynamo_db = boto3.resource(
    'dynamodb', aws_access_key_id='AKIA5KVCCTT2WXS2FYS3',
    aws_secret_access_key='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', region_name='us-east-2'
)


# f = open('webApp/usajob_data.json')
# t = open('webapp/github_data.jason')


def pop_git_table():
    for job in f:
        dynamoDB.put_item(
            TableName='GitHubJobs',
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
                    'SS': [job['Skills']]
                },
                'Technology': {
                    'SS': [job['Technology']]
                },
                'URL': {
                    'S': job['URL']
                }
            }
        )


def pop_usa_jobs_table():
    for job in t:
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
                    'SS': [job['Skills']]
                },
                'Technology': {
                    'SS': [job['Technology']]
                },
                'URL': {
                    'S': job['URL']
                }
            }
        )


# TODO query with param state, role ie. entry level or junior, top 2 tech

def query_usa(state, role, tech1, tech2):
    table = dynamo_db.Table('USAJobs')
    print(table)
    data = table.scan(
        TableName='GitHubJobs',
        FilterExpression=Attr('State').eq(state) & Attr('JobRole').contains(role)
        & Attr('Technology').contains(tech1)
        & Attr('Technology').contains(tech2)
    )
    return data['Items']


def query_github(state, role, tech1, tech2):
    table = dynamo_db.Table('GitHubJobs')
    print(table)
    data = table.scan(
        TableName='GitHubJobs',
        FilterExpression=Attr('State').eq(state) & Attr('JobRole').contains(role)
        & Attr('Technology').contains(tech1)
        & Attr('Technology').contains(tech2)
    )
    return data['Items']


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
            TableName='GitHubJobs',
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


def query_test(state, role, tech1, tech2):
    table = dynamo_db.Table('GitHubJobs')
    data = table.scan(
        TableName='GitHubJobs',
        FilterExpression=Attr('State').eq(state) & Attr('JobRole').contains(role)
        & Attr('Technology').contains(tech1)
        & Attr('Technology').contains(tech2)
    )
    print(data['Count'])
    for x in data['Items']:
        print(x)


# pop_test()
# query_test('IL', 'entry level', 'red', 'green')

