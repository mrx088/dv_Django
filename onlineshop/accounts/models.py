from django.db import models
from django.contrib.auth.models import (
     BaseUserManager, AbstractBaseUser
)
from phonenumber_field.modelfields import PhoneNumberField
from .managers import Mymanager
from django.conf import settings

# Create your models here.


class User(AbstractBaseUser):
    email       =       models.EmailField(max_length=150,unique=True)
    phone       =       PhoneNumberField(region='IR',unique=True)
    full_name   =       models.CharField(max_length=100)
    phone.error_messages['invalid'] =   'Your phone number is wrong please enter a correct phone number (e.g) 09112233444 '
    


    is_active = models.BooleanField(default=True)
    is_admin  = models.BooleanField(default=False)

    objects = Mymanager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('phone','full_name')



    def __str__(self) :
        return self.email

    def has_perm(self, perm, obj= None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    
    @property
    def is_staff(self):
        return self.is_admin



class follow (models.Model) :
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='follow')
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='following')



    def __str__ (self) :
        return f'{self.from_user} follow {self.to_user}'