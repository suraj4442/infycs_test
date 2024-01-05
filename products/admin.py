<<<<<<< HEAD
from django.contrib import admin

# Register your models here.
from .models import Products
from pages import views



admin.site.register(Products)
=======
from django.contrib import admin

# Register your models here.
from .models import Products
from pages import views



admin.site.register(Products)
>>>>>>> 353b946856fb97a7d537db26e21dfea5c82864ee
admin.site.register(views.Subscriber)