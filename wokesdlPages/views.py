from django.shortcuts import render
from django.views import View
# Create your views here.


class MainHome(View):

    def get(self,request):
        return render(request,'wokesdlPages/mainHome.html')


class Store(View):

    def get(self,request):
        return render(request,'wokesdlPages/store.html')