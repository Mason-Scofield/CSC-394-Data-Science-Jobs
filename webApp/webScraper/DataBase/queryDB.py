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
