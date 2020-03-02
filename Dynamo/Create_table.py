import boto3
import os

dynamoDB = boto3.client(
   'dynamodb',aws_access_key_id='AKIA5KVCCTT2WXS2FYS3', aws_secret_access_key='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', region_name='us-east-2'
 )

table = dynamoDB.create_table(
    TableName='PhoneBook',
    KeySchema=[
        {
            'AttributeName': 'ID',
            'KeyType': 'HASH'  # Partition key
        },
        {
            'AttributeName': 'Name',
            'KeyType': 'RANGE'  # Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'ID',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'Name',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

# print("Table status:", table.table_status)