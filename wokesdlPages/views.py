from django.shortcuts import render
from django.views import View
from .models import ImageSet
# Create your views here.


class MainHome(View):

    def get(self,request):
        return render(request,'wokesdlPages/mainHome.html')

class WokeSdlHome(View):
    
    def get(self,request):
        return render(request,'wokesdlPages/wokesdlHome.html')

class Store(View):

    def get(self,request):
        return render(request,'wokesdlPages/store.html')


class LookBook(View):

    def get(self,request,accessCode):
        imageset = ImageSet.objects.get(accessCode=accessCode)
        countRange = list(range(1,imageset.count_number))
        context ={
            'imageset':imageset,
            'countRange':countRange,
        }
        return render(request,'wokesdlPages/lookBook.html',context)
    
class AboutWokeSdl(View):

    def get(self,request):
        return render(request,'wokesdlPages/about.html')