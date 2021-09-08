import boto3

# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'https://sqs.ap-south-1.amazonaws.com/675270067251/SgnSendingSecretMail'

# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=10,
    MessageAttributes={
        'email': {
            'DataType': 'String',
            'StringValue': 'SGN'
        },
        'Secret': {
            'DataType': 'String',
            'StringValue': 'ONS'
        },
        'Ddate': {
            'DataType': 'Number',
            'StringValue': '108'
        }
    },
    MessageBody=(
        'Sgnons jkh jam jbm jkh jcs jjb jam jom jsm jsm jgb jlm jkb jjb jgb jhd jd jd jmp jg'
        'week of 12/11/2016.'
        'sgnons11@gmail.com'
        'anilprajapati18@gnu.ac.in'
    )
)

print(response['MessageId'])


"""
import json

def lambda_handler(event, context):
    # TODO implement
    print(event['Records'][0]['messageAttributes']['Secret']['stringValue'])
    print(event['Records'][0]['messageAttributes']['email']['stringValue'])
    print(event['Records'][0]['messageAttributes']['Ddate']['stringValue'])
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


"""