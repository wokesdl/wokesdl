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
        