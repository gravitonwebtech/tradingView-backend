
from django.urls import path
# from .views import UserList
from .views import *


urlpatterns = [
    path("register/", UserList.as_view(), name = "register"),
    path("email/", Sendmail.as_view(), name = "email"),

    path('login/', AuthUserLoginView.as_view(), name = "login"),
    path('pendingRequest/', PendingRequest.as_view(), name = "pendingRequest"),
    path('UserAmountStatus/', UserAmountStatus.as_view(), name = "UserAmountStatus"),
    path('UpdateAmountStatus/', UpdateAmountStatus.as_view(), name = "UpdateAmountStatus"),
    path('accountUpdate/', AccountUpdate.as_view(), name = "accountUpdate"),
    path('chatSheet/', ChatSheet.as_view(), name = "ChatSheet"),
    path('uploadProfile/', UploadProfile.as_view(), name = "UploadProfile"),
    path('PasswordUpdate/', PasswordUpdate.as_view(), name = "PasswordUpdate"),
    path('deleteFund/', DeleteFund.as_view(), name = "deleteFund"),
    path('reject/', Reject.as_view(), name = "Reject"),
    path('userData/', UserData.as_view(), name = "userData"),
    path('checkOTP/', checkOTP ),
    path('sendOTP/',otpGeneration),
    path('AccountDetails/', AccountDetailss.as_view(), name = "AccountDetails"),
     path(
        "",
       PasswordReset.as_view(),
        name="request-password-reset",
    ),
    path(
        "password-reset/<str:encoded_pk>/<str:token>/",
      ResetPasswordAPI.as_view(),
        name="reset-password",
    ),
]