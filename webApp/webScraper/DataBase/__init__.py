import boto3, os

AWS_PUB = str(os.getenv('AWS_PUB'))
AWS_PRIV = str(os.getenv('AWS_PRIV'))

dynamoDB = boto3.client(
    'dynamodb', aws_access_key_id=AWS_PUB,
    aws_secret_access_key=AWS_PRIV, region_name='us-east-2'
)

dynamo_db = boto3.resource(
    'dynamodb', aws_access_key_id=AWS_PUB,
    aws_secret_access_key=AWS_PRIV, region_name='us-east-2'
)
