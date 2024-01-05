<<<<<<< HEAD
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Subscriber

# from templates import home

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html")

def store_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            Subscriber.objects.create(email=email)
            return HttpResponse("Thank You for subscribing")
    return HttpResponse("Invalid request.")

=======
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Subscriber

# from templates import home

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html")

def store_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            Subscriber.objects.create(email=email)
            return HttpResponse("Thank You for subscribing")
    return HttpResponse("Invalid request.")

>>>>>>> 353b946856fb97a7d537db26e21dfea5c82864ee
  