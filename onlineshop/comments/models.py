from django.db import models
from django.conf import settings
from shop.models import Item

# Create your models here.


class Comments_Model (models.Model) :
    reply = models.ForeignKey('self',on_delete=models.CASCADE,related_name='rcomment',blank=True,null=True)
    is_reply   = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    comment = models.TextField(max_length=150,)
    create = models.DateTimeField(auto_created=True,auto_now=True)


    def __str__(self):
        return str(self.user)