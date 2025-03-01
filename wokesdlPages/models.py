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
    

    
