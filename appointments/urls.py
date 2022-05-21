from django.urls import path
from .views import *

app_name = 'appointments'

urlpatterns = [
    path('', appointment_view, name='appointment_list'),
    path('<uuid:uuid>/', appointment_detail, name='appointment_detail'),
]
