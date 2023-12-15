# from .serializers import UserSerializers
from .serializers import UserSerializers, UserLoginSerializer

from .models import *
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.decorators import api_view
import random
import math
from addmin.models import *
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class AuthUserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'email': serializer.data['email'],
                'role': serializer.data['role']
            }

            return Response(response, status=status_code)
import requests
def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]

    return OTP
def generatingOTP(number):
    OTP = generateOTP()

    return OTP
url = "https://www.fast2sms.com/dev/bulkV2"
@api_view(['GET', 'POST'])
def otpGeneration(request):
    number = request.data['number']
    print(number)
    generatedOTP = generatingOTP(number)
    print(generatedOTP)
    s=OTPVerifiaction.objects.filter(phone_number=number).delete()
    print("end")
    querystring = {"authorization":"FlksSDzg13vfLoUreKH9xh6CbXIA42OVynQduMPG0Bm7Ja5c8qdaBRD5fUS4lT0EX2HzV9rtAcInkZxK","variables_values":generatedOTP,"route":"otp","numbers":number}
    headers = {
    'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print("start")
    print(response.text)
    if generatedOTP:
        data = OTPVerifiaction(phone_number=number, otp=generatedOTP)
        data.save()
        print(generatedOTP)
        return Response({"OTPSent": True})
    else:
        return Response({"OTPSent": False})


@api_view(['PUT'])
def checkOTP(request):
    number = request.data['number']
    otp = request.data['otp']
    print("checking time",number,otp)
    generatedOTP = OTPVerifiaction.objects.filter(
        phone_number=number).values_list('otp')
    print(generatedOTP)
    if generatedOTP[0][0] == otp:
        data = OTPVerifiaction.objects.get(phone_number=number)
        data.is_verfied = True
        data.save()
        return Response({"status": True})

    else:
        return Response({"status": False})




from rest_framework import generics, status, viewsets, response

from django.conf import settings
# from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from . import serializers


class PasswordReset(generics.GenericAPIView):
    """
    Request for Password Reset Link.
    """

    serializer_class = serializers.EmailSerializer

    def post(self, request):
        """
        Create token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data["email"]
        user = User.objects.filter(email=email).first()
        if user:
            encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)
            reset_url = reverse(
                "reset-password",
                kwargs={"encoded_pk": encoded_pk, "token": token},
            )
            reset_link = f"localhost:8000{reset_url}"

            # send the rest_link as mail to the user.

            return response.Response(
                {
                    "message":
                    f"Your password rest link: {reset_link}"
                },
                status=status.HTTP_200_OK,
            )
        else:
            return response.Response(
                {"message": "User doesn't exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ResetPasswordAPI(generics.GenericAPIView):
    """
    Verify and Reset Password Token View.
    """

    serializer_class = serializers.ResetPasswordSerializer

    def patch(self, request, *args, **kwargs):
        """
        Verify token & encoded_pk and then reset the password.
        """
        serializer = self.serializer_class(
            data=request.data, context={"kwargs": kwargs}
        )
        serializer.is_valid(raise_exception=True)
        return response.Response(
            {"message": "Password reset complete"},
            status=status.HTTP_200_OK,
        )
from django.http import HttpResponse
from django.core import serializers
class PendingRequest(APIView):
    def post(self, request, format=None):
        userEmail=request.data.get("userEmail")
        user=User.objects.get(email=userEmail)
        user.is_active=True
        user.save()
        return HttpResponse("sucess", content_type='application/json')
    def get(self, request, format=None):
        data=User.objects.all()
        s1 = serializers.serialize('json', data)
        return HttpResponse(s1, content_type='application/json')

class ChatSheet(APIView):
    def post(self, request, format=None):
        userEmail=request.data.get("userEmail")
        userData=Sheet.objects.filter(Email=userEmail)
        s1 = serializers.serialize('json', userData)
        return HttpResponse("sucess", content_type='application/json')

class UserAmountStatus(APIView):
    def post(self, request, format=None):
        userEmail=request.data.get("userEmail")
        userData=AmountAccount.objects.filter(user_email=userEmail)
        s1 = serializers.serialize('json', userData)
        return HttpResponse(s1, content_type='application/json')



class UpdateAmountStatus(APIView):
    def post(self, request, format=None):
        date=request.data.get("date")
        price=request.data.get("price")
        loss=request.data.get("loss")
        profit=request.data.get("profit")
        user_email=request.data.get("user_email")
        idValue=request.data.get("idValue")
        userData=AmountAccount.objects.get(pk=idValue)
        userData.date=date
        userData.price=price
        userData.loss=loss
        userData.profit=profit
        userData.save()
        # s1 = serializers.serialize('json', userData)
        return HttpResponse("success", content_type='application/json')
    def get(self, request, format=None):
        userData=AmountAccount.objects.all()
        s1 = serializers.serialize('json', userData)
        return HttpResponse(s1, content_type='application/json')


class UploadProfile(APIView):
    def post(self, request, format=None):
        userEmail=request.data.get("userEmail")
        image=request.data.get("image")
        if image :
            print("image is calling")
            s=User.objects.get(email=userEmail)
            s.Image=image
            s.save()
        s=User.objects.filter(email=userEmail)
        s1 = serializers.serialize('json', s)
        # userData=AmountAccount.objects.filter(user_email=userEmail)
        # s1 = serializers.serialize('json', userData)
        return HttpResponse(s1, content_type='application/json')
    def get(self, request, format=None):
        userEmail=request.data.get("userEmail")
        s=User.objects.filter(email=userEmail)
        s1 = serializers.serialize('json', s)
        return HttpResponse(s1, content_type='application/json')



from django.conf import settings
from django.core.mail import EmailMessage
from rest_framework.views import APIView
from rest_framework.response import Response





class Sendmail(APIView):
    def post(self, request):
        email = request.data.get('to')
        
        if not email or not getattr(PasswordUpdate, 'password', None):
            return Response({'status': False, 'message': 'Incomplete data for sending email'})

        password = PasswordUpdate.password
          
        if not email:
            return Response({'status': False, 'message': 'Email address is missing'})

        email_message = EmailMessage(
            'Confirmation for Registration',
            f'Thank you for registering with Trading!\n\n'
            f'Your email: {email}\n' 
            f'Your password: {password}\n\n' 
            'We appreciate your trust. Your account is in process and will be confirmed shortly.\n'
            f'For any assistance, please contact our support team at support@growwcapitals.com.\n\n'
            'Best regards,\nThe Trading Team ',
            settings.EMAIL_HOST_USER,
            [email]
        )

        try:
            email_message.send()
            return Response({'status': True, 'message': 'Email sent successfully'})
        except Exception as e:
            return Response({'status': False, 'message': 'Failed to send email', 'error': str(e)})


class UserData(APIView):
    def post(self, request):
        Email=request.data.get("userEmail")
        s=User.objects.filter(email=Email)
        s1 = serializers.serialize('json', s)
        return HttpResponse(s1, content_type='application/json')
    def get(self, request, format=None):
        s=EmployeeData.objects.all()
        s1 = serializers.serialize('json', s)
        return HttpResponse(s1, content_type='application/json')


class PasswordUpdate(APIView):
    def post(self, request):
        Email=request.data.get("email")
        password=request.data.get("password")
        s=EmployeeData.objects.create(Email=Email,Password=password)
        s.save()
        return HttpResponse(s1, content_type='application/json')
    def get(self, request, format=None):
        s=EmployeeData.objects.all()
        s1 = serializers.serialize('json', s)
        return HttpResponse(s1, content_type='application/json')

class DeleteFund(APIView):
    def post(self, request):
        Email=request.data.get("idvalue")
        s=AmountAccount.objects.get(pk=Email).delete()
        s.save()
        return HttpResponse("success", content_type='application/json')
    def get(self, request, format=None):
        s=EmployeeData.objects.all()
        s1 = serializers.serialize('json', s)
        return HttpResponse(s1, content_type='application/json')

class Reject(APIView):
    def post(self, request):
        Email=request.data.get("email")
        s=User.objects.get(email=Email)
        s.is_active=False
        s.save()
        return HttpResponse("success", content_type='application/json')

class AccountUpdate(APIView):
    def post(self, request):
        data=request.data
        email=data["email"]
        bankaccount=data["bankaccount"]
        pancar=data["pancard"]
        phone_number=data["phone_number"]
        aadhaarCardNumber=data["aadhaarCardNumber"]
        first_name=data["first_name"]
        last_name=data["last_name"]
        s=User.objects.get(email=email)
        s.bankaccount=bankaccount
        s.pancar=pancar
        s.phone_number=phone_number
        s.aadhaarCardNumber=aadhaarCardNumber
        s.first_name=first_name
        s.last_name=last_name
        s.save()
        return HttpResponse("success", content_type='application/json')



import json
class AccountDetailss(APIView):
    def post(self, request, format=None):
        s=request.data
        s1=AccountDetails.objects.create(Name=s["name"],AccountNO=s["accountNo"],IfscCode=s["ifscCode"],QRcodeImage=s["qrcodeImage"],UPIid=s["upiId"],BankName=s["bankName"],mobileNumber=s["mobileNumber"])
        s1.save()
        print(s)
        return HttpResponse("ss", content_type='application/json')
    def get(self, request, format=None):
        s = AccountDetails.objects.all()
        print(s)
        s1 = serializers.serialize('json', s)

        last_record = json.loads(s1)[-1]  # Deserialize the JSON and retrieve the last record

        return HttpResponse(json.dumps(last_record), content_type='application/json')

class UpdateNewAmount(APIView):
    def post(self, request):
        s=AmountAccount.objects.create(date=request.data.get('date'),price=request.data.get('amount'),loss=request.data.get('losss'),profit=request.data.get('profit'),user_email=request.data.get('userEmail'))
        s.save()
        return HttpResponse("this", content_type='application/json')
    def get(self, request, format=None):
        s=EmployeeData.objects.all()
        s1 = serializers.serialize('json', s)
        return HttpResponse(s1, content_type='application/json')

# views.py in your Django app
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
import pytesseract
from PIL import Image
import os
import re
@api_view(['POST'])
def ocr_extract(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']

        # Using OCR.space API
        url = "https://api.ocr.space/parse/image"
        payload = {
            'isOverlayRequired': False,
            'apikey': 'K86122232388957',
            'language': 'eng',
        }
        files = [('image', image_file)]

        response = requests.post(url, data=payload, files=files)
        result = response.json()

        extracted_text = result['ParsedResults'][0]['ParsedText'] if result.get('ParsedResults') else ''

        # Extract PAN and Aadhaar numbers using regex (example patterns below)
        pan_pattern = re.compile(r'[A-Z]{5}[0-9]{4}[A-Z]{1}')
        aadhaar_pattern = re.compile(r'\d{4}\s\d{4}\s\d{4}')

        pan_number = pan_pattern.search(extracted_text)
        aadhaar_number = aadhaar_pattern.search(extracted_text)

        return Response({
            'panNumber': pan_number.group() if pan_number else '',
            'aadhaarNumber': aadhaar_number.group() if aadhaar_number else ''
        })

    return Response({'error': 'No image provided'}, status=400)
from django.views.decorators.http import require_http_methods
class TotalUserOneData(APIView):
    def post(self, request):
        Email=request.data.get("userEmail")
        user=User.objects.filter(email=Email)
        user1 = serializers.serialize('json', user)
        AmountData=AmountAccount.objects.filter(user_email=Email)
        AmountData1 = serializers.serialize('json', AmountData)
        StockForm=Stock_form.objects.filter(user_email=Email)
        StockForm1 = serializers.serialize('json', StockForm)
        widraw=StockFunds.objects.filter(user_email=Email)
        widraw1 = serializers.serialize('json', widraw)
        Diposit=Deposit.objects.filter(Email=Email)
        Diposit1 = serializers.serialize('json', Diposit)
        print(user)
        s={
            "user":user,"Amount":AmountData1,"StockForm":StockForm1,"widraw":widraw1,"Diposit":Diposit1
        }
       
        return JsonResponse(s)
    def get(self, request, format=None):
        s=EmployeeData.objects.all()
        s1 = serializers.serialize('json', s)
        return HttpResponse(s1, content_type='application/json')

@require_http_methods(["GET"])
def get_transaction_by_email(request, email):
    try:
        # Get the transaction from the database
        transactions = Transaction.objects.filter(email=email).values()
        # Convert the transactions to a list
        transactions_list = list(transactions)
        return JsonResponse(transactions_list, safe=False)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Transaction not found'}, status=404)

# View to post a transaction
@csrf_exempt
@require_http_methods(["POST"])
def post_transaction(request):
    try:
        # Parse the JSON data from the request
        data = json.loads(request.body)
        # Create a new transaction object
        transaction = Transaction(
            name=data['name'],
            email=data['email'],
            type=data['type'],
            amount=data['amount']
        )
        # Save the transaction to the database
        transaction.save()
        return JsonResponse({'message': 'Transaction saved successfully'}, status=201)
    except (ValueError, KeyError):
        return JsonResponse({'error': 'Invalid data'}, status=400)
    

@require_http_methods(["GET"])
def get_messages_by_email(request, email):
    try:
        # Get the messages from the database
        messages = Message.objects.all()
        # Convert the messages to a list
        messages_list = list(messages)
        return JsonResponse(messages_list, safe=False)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Messages not found'}, status=404)

# View to post a message
@csrf_exempt
@require_http_methods(["POST"])
def post_message(request):
    try:
        # Parse the JSON data from the request
        data = json.loads(request.body)
        # Create a new message object
        message = Message(
            subject=data['subject'],
            email=data['email'],
            message=data['message']
        )
        # Save the message to the database
        message.save()
        return JsonResponse({'message': 'Message saved successfully'}, status=201)
    except (ValueError, KeyError):
        return JsonResponse({'error': 'Invalid data'}, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def update_or_create_contact_info(request):
    try:
        # Parse the JSON data from the request
        data = json.loads(request.body)

        # Update or create contact information
        contact_info, created = ContactInformation.objects.update_or_create(
            email=data['email'],  # Email is used as the identifier
            defaults={
                'address': data.get('address', ''),
                'phone': data.get('phone', ''),
                'social_media_facebook': data.get('social_media_facebook', ''),
                'social_media_instagram': data.get('social_media_instagram', ''),
                'social_media_linkedin': data.get('social_media_linkedin', ''),
                'social_media_twitter': data.get('social_media_twitter', '')
            }
        )

        if created:
            message = 'Contact information created successfully.'
        else:
            message = 'Contact information updated successfully.'

        return JsonResponse({'message': message}, status=201)
    except (ValueError, KeyError):
        return JsonResponse({'error': 'Invalid data'}, status=400)