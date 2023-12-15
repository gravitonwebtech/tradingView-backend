import uuid

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone

from .managers import CustomUserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

    # These fields tie to the roles!
    ADMIN = 1
    STAFF = 2
    USER = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (STAFF, 'Staff'),
        (USER, 'User')
    )
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    # Roles created here
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(unique=True)
    
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)


    phone_number=models.CharField(max_length=200,blank=False, default=True)
    pancard =models.CharField(max_length=200 ,blank=False ,default=True)
    bankaccount=models.CharField(max_length=200,blank=False ,default=True)
    ifsccode=models.CharField(max_length=200,blank=False ,default=True)
    aadhaarCardNumber=models.CharField(max_length=200 ,blank=False ,default=True)
    Image=models.CharField(max_length=2322232222222,null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class OTPVerifiaction(models.Model):
    phone_number = models.IntegerField()
    otp = models.CharField(max_length=4)
    is_verfied = models.BooleanField(default=False)

class Sheet(models.Model):
    Pay_Amount=models.CharField(max_length=100)
    Profit=models.CharField(max_length=100)
    Loss=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)

class EmployeeData(models.Model):
    Email=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)


class AccountDetails(models.Model):
    Name = models.CharField(max_length=255)
    AccountNO = models.CharField(max_length=20)
    IfscCode = models.CharField(max_length=20)
    QRcodeImage = models.ImageField(upload_to='qrcodes/')
    UPIid = models.CharField(max_length=255)
    BankName = models.CharField(max_length=255)
    mobileNumber = models.CharField(max_length=15)

    def __str__(self):
        return self.Name


class Deposit(models.Model):
    Name=models.CharField(max_length=15)
    Email=models.CharField(max_length=15)
    Amount=models.CharField(max_length=15)
class Transaction(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    type = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Message(models.Model):
    subject = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.subject} - {self.email}"


class ContactInformation(models.Model):
    address = models.CharField(max_length=255)
    email = models.EmailField(unique=True)  # Assuming email is the unique identifier for each entry
    phone = models.CharField(max_length=20)
    social_media_facebook = models.CharField(max_length=255, blank=True)
    social_media_instagram = models.CharField(max_length=255, blank=True)
    social_media_linkedin = models.CharField(max_length=255, blank=True)
    social_media_twitter = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.email