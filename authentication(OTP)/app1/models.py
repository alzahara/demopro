from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

from random import randint
#CustomUserModel definition
class CustomUser(AbstractUser):
    phone=models.IntegerField()
    address=models.TextField()
    role=models.CharField(max_length=20,default=" ")

    is_verified=models.BooleanField(default=False)#After verification it will set to True
    otp=models.CharField(max_length=10,null=True,blank=True)#To store the generated otp in

    def generate_otp(self):
        #for creating random otp number for verification
        otp_number=str(randint(1000,9999))+str(self.id)
        self.otp=otp_number
        self.save()