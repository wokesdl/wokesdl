from django.urls import path
from .views import SbsHome, ArtistPage, Kwelit,Santana, Montana
urlpatterns = [
    path('home/',SbsHome.as_view(),name='sbsHome'),
    path('artistPage/',ArtistPage.as_view(),name='artistPage'),
    path('kwelit/',Kwelit.as_view(),name='kwelit'),
    path('santana/',Santana.as_view(),name='santana'),
    path('montana/',Montana.as_view(),name='montana'),

]