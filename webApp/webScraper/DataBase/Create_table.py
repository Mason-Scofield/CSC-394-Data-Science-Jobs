import boto3
import os

dynamoDB = boto3.client(
    'dynamodb', aws_access_key_id=os.getenv('AWS_PUB'),
    aws_secret_access_key=os.getenv('AWS_PRIV'), region_name='us-east-2'
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
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
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
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )



