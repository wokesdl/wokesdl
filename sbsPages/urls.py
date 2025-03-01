from django.urls import path
from .views import SbsHome
urlpatterns = [
    path('home/',SbsHome.as_view(),name='sbsHome'),
    

]