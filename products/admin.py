from django.contrib import admin

# Register your models here.
from .models import Products
from pages import views



admin.site.register(Products)
admin.site.register(views.Subscriber)