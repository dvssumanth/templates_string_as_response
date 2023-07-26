from django.urls import path
from app1.views import *

app_name='hii'
urlpatterns=[
    path('new/',new,name='new'),
    path('dvs/',dvs,name='dvs'),
    path('ind/',ind,name='ind'),
]