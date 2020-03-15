import boto3, os

dynamoDB = boto3.client(
    'dynamodb', aws_access_key_id=os.getenv('AWS_PUB'),
    aws_secret_access_key=os.getenv('AWS_PRIV'), region_name='us-east-2'
)

dynamo_db = boto3.resource(
    'dynamodb', aws_access_key_id=os.getenv('AWS_PUB'),
    aws_secret_access_key=os.getenv('AWS_PRIV'), region_name='us-east-2'
)