from django.contrib import admin
from .models import Image, ImageSet, Category,Product
# Register your models here.


admin.site.register(Image)
admin.site.register(ImageSet)
admin.site.register(Product)
admin.site.register(Category)