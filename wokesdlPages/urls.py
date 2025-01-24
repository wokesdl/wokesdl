from django.urls import path
from .views import MainHome

urlpatterns =[
path('',MainHome.as_view(),name='mainHome')
]