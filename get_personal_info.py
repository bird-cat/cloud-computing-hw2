import json
import boto3
from boto3 import Session
from boto3.dynamodb.conditions import Attr, Key

def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource('dynamodb')
    client = boto3.resource('dynamodb')
    table = dynamodb.Table('personal_info')
    
    response = table.query(
        KeyConditionExpression=Key('name').eq(event['name'])
    )
    return {
        'statusCode': 200,
        'body': response['Items']
    }
    
