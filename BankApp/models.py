from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Banks(models.Model):
    Bcity = models.CharField(max_length=100)
    BState = models.CharField(max_length=100)
    def __str__(self):
        return self.Bcity

class DonnerModel(models.Model):
    fullname = models.CharField(max_length=100)
    Did = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_no = models.IntegerField()
    BloodGrp = models.CharField(max_length=20)
    Age = models.IntegerField()
    is_diabitic =  models.BooleanField()
    Bid = models.ForeignKey(Banks, on_delete=models.CASCADE)    
    donnate_date = models.DateField()
    is_recived_by_bank = models.BooleanField(default=False)
    Secret = models.CharField(max_length=100,default="SGN1ONS")    
    
    def __str__(self):
        return self.fullname
    
    
class Blood(models.Model):
    Did = models.ForeignKey(User, on_delete=models.CASCADE)    
    Bid = models.ForeignKey(Banks, on_delete=models.CASCADE)  
    BloodGrp = models.CharField(max_length=20) 
    Secret = models.CharField(max_length=100)    
    is_available = models.BooleanField(default=True)     
    
class RequesterModel(models.Model):
    fullname = models.CharField(max_length=100)
    Rid = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_no = models.IntegerField()
    BloodGrp = models.CharField(max_length=20)
    Age = models.IntegerField()
    is_diabitic =  models.BooleanField()
    def __str__(self):
        return self.fullname

class RequestNoBlood(models.Model):
    RNid = models.ForeignKey(User, on_delete=models.CASCADE)


class RequestedBlood(models.Model):
    Rqid = models.ForeignKey(User, on_delete=models.CASCADE)
    Dnid = models.IntegerField()     
    Bid = models.ForeignKey(Banks, on_delete=models.CASCADE)   
    Bloodid = models.ForeignKey(Blood, on_delete=models.CASCADE)
    Secret = models.CharField(max_length=100) 