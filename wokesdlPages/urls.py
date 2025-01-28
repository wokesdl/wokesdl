from django.urls import path
from .views import MainHome, Store

urlpatterns =[
path('',MainHome.as_view(),name='mainHome'),
path('store/',Store.as_view(),name='store')
]