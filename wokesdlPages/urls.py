from django.urls import path
from .views import MainHome, Store, LookBook, AboutWokeSdl

urlpatterns =[
path('',MainHome.as_view(),name='mainHome'),
path('store/',Store.as_view(),name='store'),
path('lookbook/<str:accessCode>/',LookBook.as_view(),name='lookbook'),
path('about/',AboutWokeSdl.as_view(),name='about'),
]