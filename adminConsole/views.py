from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from wokesdlPages.models import Payment
from django.contrib.auth.decorators import login_required
from .forms import DeliveryStatusUpdateForm

# Create your views here.


def adminLogin(request): #pass the login form in the admin login page
    if request.method == 'POST':
        username =  request.POST.get('username')
        password  = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/orders/list')
        else:
            messages.error(request,'Error Login in')
            return redirect(adminLogin)

        
            
    return render(request,'html/adminLogin.html')

@login_required(login_url='/')
def orderList(request):
    payments = Payment.objects.all().filter(verified=True)
    context = {
        'payments':payments,
    
    }
    print(payments)
    return render(request,'html/list.html',context)

def orderDetails(request,ref):
    payment = Payment.objects.get(ref=ref)
    DeliveryStatusUpdateFormCreator = DeliveryStatusUpdateForm(instance=payment)

    if request.method == 'POST':
        if 'updateDeliveryStatus' in request.POST:
            DeliveryStatusUpdateFormCreator = DeliveryStatusUpdateForm(request.POST, instance=payment)
            if DeliveryStatusUpdateFormCreator.is_valid():
                DeliveryStatusUpdateFormCreator.save()
                return redirect(f'/orders/list/')
            else:
                print('Form errors:', DeliveryStatusUpdateFormCreator.errors) 
            

    context = {
        'payment':payment,
        'DeliveryStatusUpdateFormCreator':DeliveryStatusUpdateFormCreator,

    }
    print(payment)
    return render(request,'html/orderDetails.html',context)