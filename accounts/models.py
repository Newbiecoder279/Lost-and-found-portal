from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    college_id = models.CharField(max_length=15)
    phone = models.CharField(max_length=15,blank=True)
    profile_pic = models.ImageField(upload_to='profiles/', blank=True)
