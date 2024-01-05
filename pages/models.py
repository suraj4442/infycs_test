<<<<<<< HEAD
from django.db import models

# Create your models here.
class Subscriber(models.Model):
    email= models.EmailField(unique=True)

    def __str__(self) -> str:
=======
from django.db import models

# Create your models here.
class Subscriber(models.Model):
    email= models.EmailField(unique=True)

    def __str__(self) -> str:
>>>>>>> 353b946856fb97a7d537db26e21dfea5c82864ee
        return self.email