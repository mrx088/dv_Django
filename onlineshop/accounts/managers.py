


from django.contrib.auth.models import (
    BaseUserManager
)



class Mymanager(BaseUserManager):
    def create_user(self,email,password,phone,full_name):

        
        if not email :
            raise ValueError('Your email is wrong')
        
        if not phone :
            raise ValueError('Your phone is wrong')
        
        if not full_name :
            raise ValueError('Your name is wrong')

        user = self.model(email=self.normalize_email(email),phone=phone,full_name=full_name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password,phone,full_name):
        
        user = self.create_user(email=email,password=password,phone=phone,full_name=full_name)

        user.is_admin = True

        user.save(using=self._db)
        return user