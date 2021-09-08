from html2image import Html2Image
from bs4 import BeautifulSoup as bs
import re
import os
import boto3

"""

# Remove the last segment of the path
base = os.path.dirname(os.path.abspath(__file__))

# Open the HTML in which you want to make changes
html = open(os.path.join(base, 'sgncerti.html'))

# Parse HTML file in Beautiful Soup
soup = bs(html, 'html.parser')

# Give location where text is
# stored which you wish to alter
old_text = soup.find("div", {"id": "fullname"})

# Replace the already stored text with
# the new text which you wish to assign
new_text = old_text.find(text=re.compile(
	'sgnons')).replace_with('SGNONS123')

# Alter HTML file to see the changes done
with open("sgncerti"+str(1)+".html", "wb") as f_output:
	f_output.write(soup.prettify("utf-8"))



hti = Html2Image()

hti.screenshot(
    html_file='sgncerti1.html',
    save_as='sgn.png',
    size=(750, 563)
)

"""

def SendBankCertificate(fullname,email):
	#sqs = boto3.client('sqs')

	#queue_url = 'https://sqs.ap-south-1.amazonaws.com/675270067251/sgnVerificationEmail'

	# Send message to SQS queue
	s3_client = boto3.client('s3')
	html = open("certi/sgncerti.html")
	
	# Parse HTML file in Beautiful Soup
	soup = bs(html, 'html.parser')
	
	# Give location where text is
	# stored which you wish to alter
	old_text = soup.find("div", {"id": "fullname"})
	
	# Replace the already stored text with
	# the new text which you wish to assign
	new_text = old_text.find(text=re.compile(
		'sgnons')).replace_with(fullname)
	fullname = fullname.split(" ")[0]	
	new_file_name="certi/"+str(fullname)+".html"
	# Alter HTML file to see the changes done
	with open(new_file_name, "wb") as f_output:
		f_output.write(soup.prettify("utf-8"))

	hti = Html2Image()
	new_png=fullname+".png"
	hti.screenshot(
		html_file=new_file_name,
		save_as="certi/"+new_png,
		size=(750, 563)
	)            
	response = s3_client.upload_file("certi/"+new_png, "s3-prac5-bucket", new_png)
	


SendBankCertificate("sgnons123anil","anilprajapati18@gnu.ac.in")
