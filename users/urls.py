from django.urls import path
from .views import RegistrationApiView
from django.contrib import admin

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api_accounts'

urlpatterns = [
    path('register/', RegistrationApiView, name='register-api'),
    path('login/', obtain_auth_token, name='login-api'),
]

# admin.site.site_header('Patient Schedular')
# admin.site.site_title('Patient Schedular')

