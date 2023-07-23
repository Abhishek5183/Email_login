from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete= models.CASCADE)
    mobile = models.CharField(max_length=20, primary_key= True)
    img = models.ImageField()
    address = models.TextField()
