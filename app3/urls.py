from django.urls import path
from app3.views import *
urlpatterns=[
    path('ind3/',ind3,name='ind3'),
    path('sai/',sai,name='sai'),
    path('new3/',new3,name='new3')
]