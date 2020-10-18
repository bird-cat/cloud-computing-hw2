import json
import boto3

def lambda_handler(event, context):
        dynamodb = boto3.resource('dynamodb')
            client = boto3.client('dynamodb')
                
                    table = dynamodb.Table('personal_info')
                        table.put_item(
                                        Item = {
                                                        'name': event['name'],
                                                                    'student id': event['student id'],
                                                                                'birthday': event['birthday'],
                                                                                            'cellphone': event['cellphone']
                                                                                                    }    
                                            )
                            return {
                                            'statusCode': 200,
                                                    'body': json.dumps('Successfully insert an info!')
                                                        }
