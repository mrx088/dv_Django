from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm,UserCreationForm
from .models import User
from django.contrib.auth.models import Group
# Register your models here.
class UserAdmin(BaseUserAdmin):
    
    form = UserChangeForm
    add_form = UserCreationForm


    list_display = ('email','is_active')
    list_filter = ('is_admin',)



    fieldsets =(
        (None,{'fields':('full_name',)}),
        ('Email & Phone',{'fields':('email','phone','password')}),
        ('permissions',{'fields':('is_active','is_admin')}),
    )

    add_fieldsets=(
        (None,{'fields':('full_name',)}),
        ('Email & Phone',{'fields':('email','phone','password1','password2')}),
        ('permissions',{'fields':('is_active','is_admin')}),
    )


    search_fields = ('email','phone')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User,UserAdmin)
admin.site.unregister(Group)