from django.shortcuts import render
from django.views import View


# This is the sounds by sdl home page
class SbsHome(View):
    def get(self,request):
        return render(request,'sbsPages/home.html')
    
class ArtistPage(View):
    def get(self,request):
        return render(request,'sbsPages/artistsPage.html')
    

class Kwelit(View):
    def get(self,request):
        return render(request,'sbsPages/kwelit.html')

class Santana(View):
    def get(self,request):
        return render(request,'sbsPages/santana.html')

class Montana(View):
    def get(self,request):
        return render(request,'sbsPages/montana.html')

class Videos(View):
    def get(self,request):
        return render(request,'sbsPages/videos.html')