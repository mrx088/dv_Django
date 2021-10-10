from django.db import models
from django.conf import settings 

# Create your models here.
class Contact (models.Model) :
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True , null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    body = models.TextField()