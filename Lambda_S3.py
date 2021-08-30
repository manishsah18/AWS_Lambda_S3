import json
import urllib.parse
import boto3

print('Loading function')

s3_client = boto3.client('s3')
#simple storage service
ses_client = boto3.client('ses')
#simple email service

def lambda_handler(event, context):
   
    #Get the object from the event and show its content type
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
   
    
    response = ses_client.send_email(
        Destination={
            'ToAddresses': [
                'manishsah18@gmail.com'
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': 'UTF-8',
                    'Data': '<h1>Hello World</h1><p>This is a pretty mail with HTML formatting</p>',
                },
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': 'We are happy to recive your file we will let u know our decision',
                },
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': 'Your file name'+file_name+ 'has been received',
            },
        },
        Source='premchandrakumar39@gmail.com',
    )

   
