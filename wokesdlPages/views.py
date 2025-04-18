import ast

from django.shortcuts import render,redirect
from django.views import View
from .models import ImageSet, Product, Payment, Cart, CartObject
# Create your views here.


class MainHome(View):

    def get(self,request):
        return render(request,'wokesdlPages/mainHome.html')

class WokeSdlHome(View):
    
    def get(self,request):
        return render(request,'wokesdlPages/wokesdlHome.html')

class Store(View):

    def get(self,request):
        products = Product.objects.all()
        context ={
            'products':products,
        }
        return render(request,'wokesdlPages/store.html',context)


class LookBook(View):

    def get(self,request,accessCode):
        imageset = ImageSet.objects.get(accessCode=accessCode)
        countRange = list(range(1,imageset.count_number))
        imageSets = ImageSet.objects.all()
        context ={
            'imageset':imageset,
            'countRange':countRange,
            'accessCode':accessCode,
            'imageSets':imageSets,
        }
        return render(request,'wokesdlPages/lookBook.html',context)
    
class AboutWokeSdl(View):

    def get(self,request):
        return render(request,'wokesdlPages/about.html')
    
class MakePayment(View):
    def get(self,request,unique_id):
        payment = Payment.objects.get(ref=unique_id)
        context ={
            'payment':payment
        }

        return render(request,'wokesdlPages/makePayment.html',context)
    
class OrderSuccess(View):
    def get(self, request, unique_id):
        payment = Payment.objects.get(ref=unique_id)
        context = {
            'payment':payment,
        }
        return render(request,'wokesdlPages/orderSuccess.html',context)

class Checkout(View):

    def get(self,request):
        return render(request,'wokesdlPages/checkout.html')

    def post(self,request):
        if 'checkout' in request.POST:
            cartData = request.POST.get('cartData')
            cartData =ast.literal_eval(cartData)

            

            # delivery info 
            firstName = request.POST.get('fname')
            lastName = request.POST.get('lname')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            orderNotes = request.POST.get('orderNotes')
            street_address_1 = request.POST.get('street_address_1')
            street_address_2 = request.POST.get('street_address_2')
            city = request.POST.get('city')
            state = request.POST.get('state')
            zip_code = request.POST.get('zip')
            destination_country = request.POST.get('destination_country')
            deliveryInfo = request.POST.get('deliveryInfo')
            cart_total = request.POST.get('cart-total')
          

            payment = Payment(first_name=firstName,last_name=lastName,email=email,phone=phone,street_address_1=street_address_1,street_address_2=street_address_2,city=city,state=state,zip_code=zip_code,destination_country=destination_country,amount=float(cart_total))
            payment.save()
            
            # on payment save create cart for payment
            cart = Cart.objects.get_or_create(payment=payment) # create cart for payment
            cart[0].save()

            # loop through cart object list to append to cart
            for obj in cartData:
                product = Product.objects.get(unique_id=obj['product_id'])
                cartObj = CartObject(cart=cart[0],product=product,size=obj['selectedSize'],quantity=obj['quantity'] )
                cartObj.save()


            return redirect(f'/makePayment/{payment.ref}')


    
class Contact(View):
    
    def get(self,request):
        return render(request,'wokesdlPages/contact.html')

class ProductDetail(View):

    def get(self, request,unique_id):
        product = Product.objects.get(unique_id=unique_id)
        context = {
            'product':product,
        }
        return render(request,'wokesdlPages/productDetail.html',context)