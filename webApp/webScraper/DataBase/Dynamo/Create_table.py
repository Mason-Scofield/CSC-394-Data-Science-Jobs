import boto3
import os

dynamoDB = boto3.client(
   'dynamodb', aws_access_key_id='AKIA5KVCCTT2WXS2FYS3', aws_secret_access_key='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', region_name='us-east-2'
 )


def create_tables():

    table = dynamoDB.create_table(
        TableName='USAJobs',
        KeySchema=[
            {
                'AttributeName': 'ID',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'ID',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 8000,
            'WriteCapacityUnits': 8000
        }
    )

    table = dynamoDB.create_table(
        TableName='GitHubJobs',
        KeySchema=[
            {
                'AttributeName': 'ID',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'ID',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 8000,
            'WriteCapacityUnits': 8000
        }
    )
