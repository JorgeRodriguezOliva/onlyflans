import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)


class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()
    
    def __str__(self):
        return self.customer_name

#* PROFILE MODEL
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    bio = models.TextField(max_length=500, blank=True) 
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True) 

    def __str__(self):
        return self.user.username
