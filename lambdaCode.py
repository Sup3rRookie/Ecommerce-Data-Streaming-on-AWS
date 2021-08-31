## Import Dependencies
import json
import boto3

def lambda_handler(event, context):
    print('My Event:')
    print(event)

my_context = event.get('context')
method = my_context.get('http-method')
method = event['context']['http-method']

if method == 'GET':
    dynamo_client = boto3.client('dynamodb')

