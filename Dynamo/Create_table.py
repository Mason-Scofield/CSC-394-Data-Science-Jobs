import boto3
dynamoDB = boto3.client(
   'dynamodb', aws_access_key_id="AKIA5KVCCTT2T4RRCDF7",aws_secret_access_key="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", region_name='us-east-2'
 )
dynamo = boto3.resource('dynamodb', region_name='us-west-2')
table = dynamo.create_table(
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

print("Table status:", table.table_status)