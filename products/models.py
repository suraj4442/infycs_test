from django.db import models
# Create your models here.

class Products(models.Model):
    title= models.CharField(max_length=120)  #max_length is required for CharField
    desc=models.TextField()
    resume= models.URLField()
    price= models.DecimalField(max_digits=5, decimal_places=2)
    summary= models.TextField(default= None)
    featured= models.BooleanField()
    Email= models.EmailField(null= True)
class Meta:
    verbose_name_plural="Products"
    verbose_name= "Product"
    