from django import urls
from .views import *

app_name = 'specialisation'

urlpatterns = [
    urls.path('', specialisation_view, name='specialisation'),
    urls.path('<uuid:uuid>/', specialisation_detail, name='specialisation_detail'),
]

