from django.urls import path
from .views import MainHome, Store, LookBook, AboutWokeSdl, WokeSdlHome, Checkout, Contact

urlpatterns =[
path('',MainHome.as_view(),name='mainHome'),
path('store/',Store.as_view(),name='store'),
path('lookbook/<str:accessCode>/',LookBook.as_view(),name='lookbook'),
path('about/',AboutWokeSdl.as_view(),name='about'),
path('wokesdlhome/',WokeSdlHome.as_view(),name='wokesdlHome'),
path('checkout/',Checkout.as_view(),name='checkout'),
path('contact/',Contact.as_view(),name='contact')
]