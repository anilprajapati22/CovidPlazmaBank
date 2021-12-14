from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,RequesterForm,DonnerForm
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse, request
from .models import Banks, Blood, RequesterModel , DonnerModel ,RequestedBlood
import string
import random
import datetime
from dateutil.relativedelta import relativedelta
import boto3
from html2image import Html2Image
from bs4 import BeautifulSoup as bs
import re
from django.contrib.auth.models import User
queue_url = 'https://sqs.ap-south-1.amazonaws.com/663274486810/sgnCovidPlazmaBankSQS'

#name@#0123

def index(request):
    return HttpResponse("Hello, world. Site is under Cunstruction")
    
def home(request):
    return render(request,'home.html')
    
def GetSecret():
	return ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = 7))

def getAuthenticateEmail(email):
	sqs = boto3.client('sqs',region_name='ap-south-1')
	


	# Send message to SQS queue
	response = sqs.send_message(
		QueueUrl=queue_url,
		DelaySeconds=10,
		MessageAttributes={
			'email': {
				'DataType': 'String',
				'StringValue': email
			},
			'is_secret': {
				'DataType': 'String',
				'StringValue': "no"
			}					
		},
		MessageBody=(
			'sgnons'
		)
	)
	print("\n\n\n\n\n")
	print(response['MessageId'])


def register(request):
	if request.method == "POST":
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			getAuthenticateEmail(request.POST['email'])
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = UserRegistrationForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})    

def getBankList():
    l=[]
    bobj = Banks.objects.all()
    for i in bobj:
        l.append([i.id,i.Bcity])
    return l    

def callSQS(Secret,email,Ddate,Baddress):
	sqs = boto3.client('sqs',region_name='ap-south-1')

	#queue_url = 'https://sqs.ap-south-1.amazonaws.com/675270067251/SgnCovidPlazmaSQS'

	# Send message to SQS queue
	response = sqs.send_message(
		QueueUrl=queue_url,
		DelaySeconds=10,
		MessageAttributes={
			'Secret': {
				'DataType': 'String',
				'StringValue': Secret
			},
			'email': {
				'DataType': 'String',
				'StringValue': email
			},
			'Ddate': {
				'DataType': 'String',
				'StringValue': str(Ddate)
			},
			'is_secret': {
				'DataType': 'String',
				'StringValue': "yes"
			},
			'Baddress':{
				'DataType': 'String',
				'StringValue': str(Baddress)

			}			
		},
		MessageBody=(
			'sgnons'
		)
	)

	print(response['MessageId'])




def Donner(request):
	if request.method == "POST":
		print("\n\n\n sgn 0")			        
		form = DonnerForm(request.POST)	
		if int(request.POST['Age']) < 18:
			return render (request=request, template_name="Donner.html", context={"register_form":form,
																	"isShow":False,
																	"Blist":getBankList(),
																	"SecVal":GetSecret(),
																	"Emess":"you can't Donnate Blood"})    
		donnatedate = request.POST['donnate_date']
		donnatedate = donnatedate.split('-')
		newdate = datetime.date(int(donnatedate[0]),int(donnatedate[1]),int(donnatedate[2]))
		print("\n\n",donnatedate)           
		newdate=relativedelta( newdate , datetime.datetime.today())
		print(newdate.years ,"   ",newdate.days)            
		if  newdate.years < -1 or newdate.months < -1 or newdate.days < -1:
			return render (request=request, template_name="Donner.html", context={"register_form":form,
																	"isShow":False,
																	"Blist":getBankList(),
																	"SecVal":GetSecret(),
																	"Emess":"Please choose date correctly"})    

		print("for save")
		if form.is_valid():
			print("\n\n\n sgn 1")
			form.save()
			#email secret values to user.            
			callSQS(request.POST['Secret'],request.user.email,request.POST['donnate_date'],request.POST['Bid'])
			messages.success(request, "Registration successful." )
			return render(request,'home.html',context={"text":"Thank You for Donation",
                                                        "SecVal":request.POST['Secret']})            
#			B=Blood(BloodGrp=request.POST['BloodGrp'],
#					Bid_id=request.POST['Bid'],
#					Did=request.user,
#					Secret=GetSecret(),
#					is_available=True)
#			print("\n\n\n sgn 2")	
#			B.save()
	donner1 = DonnerModel.objects.filter(Did_id=request.user.id)
	if len(donner1) == 1:
		return redirect(is_donner_already_donated)        
	print("\n\n\n sgn 5")	
	form = DonnerForm()
	return render (request=request, template_name="Donner.html", context={"register_form":form,
                                                                            "isShow":False,
                                                                            "Blist":getBankList(),
                                                                            "SecVal":GetSecret(),
																			"form":form},
																			)    


#if user already created donner id do code here
def is_donner_already_donated(request):
	donner1 = DonnerModel.objects.filter(Did_id=request.user.id)
	dateNow = donner1[0].donnate_date
	a_month = relativedelta(months=6)        
	date_plus_month = dateNow + a_month
	if request.method == "GET":
		return render(request=request, template_name="Donner_already.html",context={
                                    "Ddate":date_plus_month })	
		    
	if request.method == "POST":
		if donner1[0].Did_id==request.user.id:	
			print("\n\n",donner1[0].BloodGrp,"  ",)
			dateNow=donner1[0].donnate_date
			print(request.POST['DonnerData'])            
			donnatedate = request.POST['DonnerData']
			donnatedate = donnatedate.split('-')
			newdate = datetime.date(int(donnatedate[0]),int(donnatedate[1]),int(donnatedate[2]))
			print("\n\n",donnatedate)           
			newdate=relativedelta( newdate , date_plus_month )
			print(newdate.years ,"   ",newdate.months ,"  ",newdate.days)            
			if  newdate.years > -1 and newdate.months > -1 and newdate.days > -1:
				addBlood = DonnerModel.objects.get(Did=request.POST['id1'])
				addBlood.is_recived_by_bank = False
				addBlood.Secret = GetSecret()                
				addBlood.donnate_date = request.POST['DonnerData']                    
				addBlood.save()      
				#call sqs      
				callSQS(addBlood.Secret,request.user.email,request.POST['DonnerData'],addBlood.Bid)
				return render(request,'home.html',context={"text":"Thank You For Donation Please Save Secret" ,
                                                            "Ddate" :addBlood.Secret})
                
			else:
				return render(request,'Donner_already.html',context={"text":"Sorry You have to wait till" ,"Ddate" :date_plus_month})            
			return render(request,'home.html',context={"text":""})	


def Requester(request):
	request.session['Bloodgrp'] = ""	
	if request.method == "POST":
		form = RequesterForm(request.POST)			
		if form.is_valid():
			form.save()
			messages.success(request, "Registration successful." )
			request.session['Bloodgrp'] = request.POST['BloodGrp']
			print("dgn done1")
			return redirect("RequesterBloodIsAvailable")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	req1=RequesterModel.objects.filter(Rid=request.user)	
	if len(req1) == 1:	
		return redirect("RequesterBloodIsAvailable")	
	form = RequesterForm()
	return render (request=request, template_name="Requester.html", context={"register_form":form,"isShow":False})    


# make condition if blood is not present

def RequesterBloodIsAvailable(request):
	print("dgn done2")
	if request.method == "POST":
		print("dgn done3")
		DonnerList = Blood.objects.filter(BloodGrp=request.POST['BloodGrp'],is_available=1)
		if len(DonnerList)>0:
			print("dgn done4")
			#now just give the first blood but after add date and give oldest blood
			print(DonnerList[0].Bid.id,"  ",type(DonnerList[0].Bid),"  ",str(DonnerList[0].Bid))
			BankDetails = Banks.objects.get(id=DonnerList[0].Bid.id) 
			
			DonnerData = [DonnerList[0].BloodGrp,BankDetails.Bcity,BankDetails.BState]
			#add here a data on which date blood will given.
			ReqObj = RequestedBlood(Dnid=DonnerList[0].Did.id,
									Bid=BankDetails,
									Rqid=request.user,
									Secret=GetSecret(),
									Bloodid=DonnerList[0])
			ReqObj.save()
			print("\n\n",DonnerList[0].BloodGrp,"   ",BankDetails.Bcity,"   ",BankDetails.BState,"\n\n")
			BloodD = Blood.objects.get(id=DonnerList[0].id)
			BloodD.is_available = False
			BloodD.save()
			return render (request=request, template_name="RequesterForBlood.html", context={"DonnerData":DonnerData,"is_data":True})			
	return render (request=request, template_name="RequesterForBlood.html", context={"BloodGrp":request.session['Bloodgrp'],"is_show":True})


def SendBankCertificate(fullname,Did):
	u1 = User.objects.get(id=Did)
	email = u1.email
	sqs = boto3.client('sqs',region_name='ap-south-1')

	#queue_url = 'https://sqs.ap-south-1.amazonaws.com/675270067251/SgnCovidPlazmaSQS'

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
	fullname = fullname.replace(" ","_")	
	new_file_name="certi/"+str(fullname)+".html"
	# Alter HTML file to see the changes done
	with open(new_file_name, "wb") as f_output:
		f_output.write(soup.prettify("utf-8"))

#	hti = Html2Image()
#	new_png=fullname+".png"
#	hti.screenshot(
#		html_file=new_file_name,
#		save_as=new_png,
#		size=(750, 563)
#	)            
	response = s3_client.upload_file(new_file_name, "yashtherudra", new_file_name)
	print("\n\nfile uploaded")
	response = sqs.send_message(
		QueueUrl=queue_url,
		DelaySeconds=10,
		MessageAttributes={
			'filename': {
				'DataType': 'String',
				'StringValue': str(new_file_name)
			},
			'email': {
				'DataType': 'String',
				'StringValue': email
			},
			'is_secret': {
				'DataType': 'String',
				'StringValue': "certi"
			}

			},
		MessageBody=(
			'sgnons'
		)
	)

	print(response['MessageId'])


def BankAdminPage(request):
	if request.method == "POST":
		print(request.POST["Secret"],"\n\n\n")
		print(request.POST['id1'])        
		addBlood = DonnerModel.objects.get(id=request.POST['id1'])
		if addBlood.Secret == request.POST['Secret']:
			addBlood.is_recived_by_bank = True
			addBlood.save()            
			SendBankCertificate(request.POST['fullname'],request.POST['Did'])
			#send email to user with certificate.            
			DonnerData = DonnerModel.objects.filter(is_recived_by_bank=0)
			return render (request=request, template_name="BankAdmin.html", context={"DonnerData":DonnerData})    			    
		else:
			DonnerData = DonnerModel.objects.filter(is_recived_by_bank=0)
			return render (request=request, template_name="BankAdmin.html", context={"DonnerData":DonnerData,
                                                            "Perror":"Plase Check Secret and enter again" })			        

	DonnerData = DonnerModel.objects.filter(is_recived_by_bank=0)
	return render (request=request, template_name="BankAdmin.html", context={"DonnerData":DonnerData})    
     
       
