from . import dynamo_db
from boto3.dynamodb.conditions import Attr

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

# function to give count of items in database

def count():
    cnt= 0
    git_table = dynamo_db.Table('GitHubJobs')
    usa_table = dynamo_db.Table('USAJobs')
    table1 = git_table.scan()
    table2 = usa_table.scan()
    data1 = table1['Items']
    data2 = table2['Items']
    while 'LastEvaluatedKey' in table1:
        table1 = git_table.scan(ExclusiveStartKey=table1['LastEvaluatedKey'])
        data1.extend(table1['Items'])

    while 'LastEvaluatedKey' in table2:
        table2 = usa_table.scan(ExclusiveStartKey=table2['LastEvaluatedKey'])
        data2.extend(table2['Items'])
    cnt = len(data1) + len(data2)

    return cnt
