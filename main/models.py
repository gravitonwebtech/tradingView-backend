from django.db import models
from django.utils import timezone
# Create your models here.

class MainContact(models.Model):

    
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    message=models.CharField(max_length=200,default=True )
    subject=models.CharField(max_length=200 ,default=True)
    

    def __str__(self):

        return self.firstname or ' '