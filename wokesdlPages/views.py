from django.shortcuts import render
from django.views import View
# Create your views here.


class MainHome(View):

    def get(self,request):
        return render(request,'wokesdlPages/mainHome.html')

# config for vercel