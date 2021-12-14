import json
import boto3
from botocore.exceptions import ClientError


def lambda_handler(event, context):
    # Create SES client
    email=event['Records'][0]['messageAttributes']['email']['stringValue']
    is_secret=event['Records'][0]['messageAttributes']['is_secret']['stringValue']    

    if is_secret == "no":
        #to send 1st time verification while register user
        ses = boto3.client('ses')
        response = ses.verify_email_identity(
        EmailAddress = email
        )
    
        print(response)	
    
        response = ses.list_identities(
        IdentityType = 'EmailAddress',
        )
        print(response)	
    elif is_secret == "yes":
        #now it's sending code
        Secret=event['Records'][0]['messageAttributes']['Secret']['stringValue']
        email=event['Records'][0]['messageAttributes']['email']['stringValue']
        Ddate=event['Records'][0]['messageAttributes']['Ddate']['stringValue']
        Baddress = event['Records'][0]['messageAttributes']['Baddress']['stringValue']  
        SENDER = "anilprajapati18@gnu.ac.in"
    
        # Replace recipient@example.com with a "To" address. If your account 
        # is still in the sandbox, this address must be verified.
        RECIPIENT = email 
        
        # Specify a configuration set. If you do not want to use a configuration
        # set, comment the following variable, and the 
        # ConfigurationSetName=CONFIGURATION_SET argument below.
        CONFIGURATION_SET = "ConfigSet"
        
        # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
        AWS_REGION = "ap-south-1"
        
        # The subject line for the email.
        SUBJECT = "Amazon SES Test (SDK for Python)"
        
        # The email body for recipients with non-HTML email clients.
        BODY_TEXT = ("Amazon SES Test (Python)\r\n"
                     "This email was sent with Amazon SES using the "
                     "AWS SDK for Python (Boto)."
                    )
                    
        # The HTML body of the email.
        BODY_HTML = """<html>
        <head></head>
        <body>
          <h1>Covid Plamzma Bank </h1>
          <p> your Blood Donnation is Booked on """+ Ddate+""" at  """  + Baddress + """
          <p>Plase Bring this secret with you while donate blood</p>
           <p> """+ Secret +""" </p>
        </body>
        </html>
                    """            
        
        # The character encoding for the email.
        CHARSET = "UTF-8"
        
        # Create a new SES resource and specify a region.
        client = boto3.client('ses',region_name=AWS_REGION)
        
        # Try to send the email.
        try:
            #Provide the contents of the email.
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        RECIPIENT,
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': CHARSET,
                            'Data': BODY_HTML,
                        },
                        'Text': {
                            'Charset': CHARSET,
                            'Data': BODY_TEXT,
                        },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                    },
                },
                Source=SENDER,
                # If you are not using a configuration set, comment or delete the
                # following line
                #ConfigurationSetName=CONFIGURATION_SET,
            )
        # Display an error if something goes wrong.	
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])

    elif is_secret == 'certi':
        print(event)
        filename=event['Records'][0]['messageAttributes']['filename']['stringValue']
        email=event['Records'][0]['messageAttributes']['email']['stringValue']
        SENDER = "anilprajapati18@gnu.ac.in"
        # Replace recipient@example.com with a "To" address. If your account 
        # is still in the sandbox, this address must be verified.
        RECIPIENT = email
        
        # Specify a configuration set. If you do not want to use a configuration
        # set, comment the following variable, and the 
        # ConfigurationSetName=CONFIGURATION_SET argument below.
        CONFIGURATION_SET = "ConfigSet"
        
        # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
        AWS_REGION = "ap-south-1"
        
        # The subject line for the email.
        SUBJECT = "Amazon SES Test (SDK for Python)"
        
        # The email body for recipients with non-HTML email clients.
        BODY_TEXT = ("Amazon SES Test (Python)\r\n"
                     "This email was sent with Amazon SES using the "
                     "AWS SDK for Python (Boto)."
                    )
                    
        filename = "https://yashtherudra.s3.ap-south-1.amazonaws.com/"+filename            
        # The HTML body of the email.
        BODY_HTML = """<html>
        <head></head>
        <body>
          <h1>Covid Plamzma Bank </h1>
          <p> your Blood Donnation Certificate :  </p> <p>"""+ filename+"""
          <p>Plase Bring this secret with you while donate blood</p>
        </body>
        </html>
                    """            
        
        # The character encoding for the email.
        CHARSET = "UTF-8"
        
        # Create a new SES resource and specify a region.
        client = boto3.client('ses',region_name=AWS_REGION)
        
        # Try to send the email.
        try:
            #Provide the contents of the email.
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        RECIPIENT,
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': CHARSET,
                            'Data': BODY_HTML,
                        },
                        'Text': {
                            'Charset': CHARSET,
                            'Data': BODY_TEXT,
                        },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                    },
                },
                Source=SENDER,
                # If you are not using a configuration set, comment or delete the
                # following line
                #ConfigurationSetName=CONFIGURATION_SET,
            )
        # Display an error if something goes wrong.	
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])




    
        
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

