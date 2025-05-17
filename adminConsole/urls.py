from django.urls import path
from .views import adminLogin, orderList, orderDetails

urlpatterns =[
    path('orders/',adminLogin,name='adminLogin'), #set login of admin to orders
    path('orders/list/',orderList,name='orderList'),
    path('orderDetails/<str:ref>/',orderDetails,name='order_details')
]