import boto3
def getAuthenticateEmail(email1):
    # Create SES client
    ses = boto3.client('ses')
    response = ses.verify_email_identity(
    EmailAddress = email1
    )
    print(response)	
    response = ses.list_identities(
    IdentityType = 'EmailAddress',
    )
    print(response)	
    if email1 not in response:
        print("no sgn")

getAuthenticateEmail("kevinpandya18@gnu.ac.in")        