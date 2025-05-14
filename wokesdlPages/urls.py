from django.urls import path
from .views import MainHome, Store, LookBook, Shipping, Films,OrderSuccess,AboutWokeSdl, WokeSdlHome, Checkout, Contact, ProductDetail, MakePayment

urlpatterns =[
path('',MainHome.as_view(),name='mainHome'),
path('store/',Store.as_view(),name='store'),
path('lookbook/<str:accessCode>/',LookBook.as_view(),name='lookbook'),
path('about/',AboutWokeSdl.as_view(),name='about'),
path('wokesdlhome/',WokeSdlHome.as_view(),name='wokesdlHome'),
path('checkout/',Checkout.as_view(),name='checkout'),
path('contact/',Contact.as_view(),name='contact'),
path('productDetail/<str:unique_id>/',ProductDetail.as_view(),name='productDetail'),
path('makePayment/<str:unique_id>/',MakePayment.as_view(),name='makePayment'),
path('orderSuccess/<str:unique_id>/',OrderSuccess.as_view(),name='orderSucess'),
path('shipping/',Shipping.as_view(),name='shipping'),
path('films/',Films.as_view(),name='films'),
]