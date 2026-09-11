from django.db import models
from item.models import Item
from django.conf import settings
# Create your models here.
class Claim(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    item = models.ForeignKey(Item, on_delete=models.CASCADE,related_name='claims')
    claimant = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                 related_name='claims')
    proof_description = models.TextField(max_length=1000)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                                default='pending')
    reviewed_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.SET_NULL,
                                    blank=True,
                                    null=True,
                                    related_name='reviewed_claims')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f"{self.claimant}-{self.item}"