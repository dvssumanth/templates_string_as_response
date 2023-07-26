from django.urls import path
from app2.views import *

app_name='hiii'
urlpatterns=[
    path('sai/',sai,name='sai'),
    path('new2/',new2,name='new2'),
    path('ind2/',ind2,name='ind2'),
]