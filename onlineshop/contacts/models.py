from django.db import models
from django.conf import settings 
from accounts.models import User

# Create your models here.
class Contact (models.Model) :
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True , null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    body = models.TextField()

    def __str__(self):
        return self.name





