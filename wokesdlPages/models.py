import uuid
from django.db import models


# Create your models here.

class ImageSet(models.Model):
    name = models.CharField(max_length=500)
    accessCode = models.CharField(max_length=500)
    count_number = models.PositiveIntegerField(default=1)
    def __str__(self):
        return self.name
    
class Image(models.Model):
    imageLink = models.CharField(max_length=500)
    imageSet = models.ForeignKey(ImageSet,on_delete=models.CASCADE)

    def __str__(self):
        return self.imageLink
    

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    active = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']  # Ascending order; use ['-order'] for descending



    
class Product(models.Model):   
    name = models.CharField(max_length=255)
    unique_id = models.UUIDField(editable=False,unique=True,default=uuid.uuid4)
    image = models.ImageField(upload_to='productImages/',null=True,blank=True)
    product_category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    color_tag = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    product_ordering = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    is_active = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(default=0)

    
    class Meta:
        ordering = ['product_ordering'] 
    
    def __str__(self):
        color_tag = self.color_tag
        if color_tag:
            return f'{self.name}  {color_tag} Category:{self.product_category}' 
        else:
            return f'{self.name}  {color_tag} Category:{self.product_category}' 
            color_tag = ''
    
    @property
    def stock_actual(self):
        if self.size_set:
            if self.size_set.name == '39 - 46':
                return self.size39to46.size39 + self.size39to46.size40 + self.size39to46.size41 + self.size39to46.size42 + self.size39to46.size43 + self.size39to46.size44 + self.size39to46.size45 + self.size39to46.size46
            elif self.size_set.name == 'Medium Large Xl 2xl 3xl':
                return self.mediumLargeStock.medium + self.mediumLargeStock.large + self.mediumLargeStock.xl + self.mediumLargeStock.xl2 + self.mediumLargeStock.xl3
        else:
            return self.stock
    
    def get_size(self,size):
        get = getattr(self.size_set,size,0)
        if get:
            return get
        else:
            return 0


class SizeSet(models.Model):
    product = models.OneToOneField(Product,on_delete=models.CASCADE)
  

class Size(models.Model):
    size = models.CharField(max_length=255)
    stock = models.CharField(max_length=255,null=True,blank=True)
    sizeSet = models.ForeignKey(SizeSet,on_delete=models.SET_NULL,null=True,blank=True, related_name='sizes')
        
    def __str__(self):
        return f'{self.size}'



class Payment(models.Model):
    # personal details 
    first_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255,blank=True)
    country_code = models.CharField(max_length=255)
    phone = models.CharField(max_length=255,blank=True)
    email = models.EmailField(blank=True)
    order_notes = models.TextField(blank=True)

    # delivery Address
    street_address_1 = models.CharField(max_length=255, verbose_name='Street Address Line 1', null=True)
    street_address_2 = models.CharField(max_length=255, blank=True, null=True, verbose_name='Street Address Line 2 (optional)')
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=20, null=True)
    destination_country = models.CharField(max_length=100, null=True)
    

    additional_info = models.TextField(blank=True)

    # cart and payment
    amount = models.PositiveIntegerField(blank=True)
    ref = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
   
    verified = models.BooleanField(default=False)
    delivery_price = models.IntegerField(default=0)
    delivered = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ('-date_created',)

    def __str__(self) -> str:
        return f'Payment: {self.amount}'

    
    @property
    def amount_value(self) -> int:
        self.amount * 100
        return self.amount*100
    
    @property
    def delivery_actual(self) -> int:
        return self.delivery_price * 16
    
    @property
    def total_actual(self) -> int:
        return self.amount + (self.delivery_price * 16)
    
    @property
    def order_id(self):
        val = str(self.id)
        if len(val) >= 4: # more than 4 values
            return 'PO-' + val
        else:
            loopCount = 4 - len(val)
            for i in range(loopCount):
                val = '0'+ val
            return 'PO-'+ val

class Cart(models.Model):
    payment = models.OneToOneField(Payment,on_delete=models.CASCADE)
    unique_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)


class CartObject(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cart_objects')
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    size = models.CharField(max_length=255)
    quantity = models.IntegerField()

    @property
    def price(self):
        return self.quantity * self.product.price
    

# contact model to store email subject and message
class ContactRequest(models.Model):
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email + ' ' + self.subject
    
class Newsletter(models.Model):
    email = models.CharField(max_length=255)