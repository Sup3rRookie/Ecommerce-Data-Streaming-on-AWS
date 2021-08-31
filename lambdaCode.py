## Import Dependencies
import json
import boto3

def lambda_handler(event, context):
    print('My Event:')
    print(event)

# my_context = event.get('context')
# method = my_context.get('http-method')
    method = event['context']['http-method']

    if method == "GET":

        im_customer_ID = event['params']['querystring']['CustomerID']
        print(im_customer_ID)

        response = dynamo_client.get_itme(TableName = 'Customers', Key = {'CustomerID':{'N':im_customer_ID}})
        print(response['Item'])

        return {
            'statusCode' :200,
            'body' : json.dumps(response['Item'])
        }

