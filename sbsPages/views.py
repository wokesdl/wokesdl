from django.shortcuts import render
from django.views import View


# This is the sounds by sdl home page
class SbsHome(View):
    def get(self,request):
        return render(request,'sbsPages/home.html')