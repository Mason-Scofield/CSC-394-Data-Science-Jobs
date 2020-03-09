import boto3
import json
dynamoDB = boto3.client(
   'dynamodb',aws_access_key_id='AKIA5KVCCTT2WXS2FYS3', aws_secret_access_key='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', region_name='us-east-2'
 )

f = open('github_data.json')

def pop_git_table():
    for job in f:
     dynamoDB.put_item(
        TableName='GitHubJobs',
        Item={
            'ID': {
                'S': job['ID']
            },
            'JobRole':{
                'S': job['JobRole']
            },
            'CompanyName'{
                'S': job['CompanyName']
            },
            'JobType':{
                'S':job['JobType']
            },
            'Pay':{
                'S':job['Pay']
            },
            'City':{
                'S':job['City']
            },
            'State':{
                'S':job['State']
            },
            'Skills':{
                'SS':[job['Skills']]
            },
            'Technology': {
                'SS':[job['Technology']]
        }
        }
    )
     return

def pop_usa_jobs_table():
    for job in f:
     dynamoDB.put_item(
        TableName='USAJobs',
        Item={
            'ID': {
                'S': job['ID']
            },
            'JobRole':{
                'S': job['JobRole']
            },
            'CompanyName'{
                'S': job['CompanyName']
            },
            'JobType':{
                'S':job['JobType']
            },
            'Pay':{
                'S':job['Pay']
            },
            'City':{
                'S':job['City']
            },
            'State':{
                'S':job['State']
            },
            'Skills':{
                'SS':[job['Skills']]
            },
            'Technology': {
                'SS':[job['Technology']]
        }
        }
    )
     return

def query():

    return