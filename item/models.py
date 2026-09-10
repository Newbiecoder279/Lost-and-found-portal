from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    # CATEGORY_CHOICES = [
    #     ('electronics','Electronics'),
    #     ('id','ID Cards'),
    #     ('bags','Bags'),
    #     ('keys','Keys'),
    #     ('others','Others')
    # ]
    name=models.CharField(max_length=150,unique=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    ITEM_TYPE_CHOICES = [
        ('lost','Lost'),
        ('found','Found')
    ]
    STATUS_CHOICES = [
        ('open','Open'),
        ('claimed','Claimed'),
        ('resolved','Resolved')
    ]
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    item_type = models.CharField(max_length=10,choices=ITEM_TYPE_CHOICES)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES)
    location = models.CharField(max_length=250)
    date_occurred = models.DateTimeField()
    image = models.ImageField(upload_to='items',blank=True)
    reported_by = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.name
