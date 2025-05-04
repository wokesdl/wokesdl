from django.contrib import admin
from .models import Image, ImageSet, Category,Product, Payment, SizeSet, Size
# Register your models here.


admin.site.register(Image)
admin.site.register(ImageSet)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Payment)
admin.site.register(SizeSet)
admin.site.register(Size)