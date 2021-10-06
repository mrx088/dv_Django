from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from phonenumber_field.formfields import PhoneNumberField




class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    

    
    class Meta :
        model = User
        fields = ('email','phone')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2 :
            raise ValidationError('Psswords are not same please change them')
        return password2


    def save(self, commit=True):
        user= super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    model = User
    fields = ('email','phone','password','is_active','is_admin')



messages = {
    'required':'Try aggain ',
    'invalid':'You enter invalid object',
    'max_length':'The carecters are more'


}

class User_login (forms.Form):
    email = forms.EmailField(max_length=250,error_messages=messages)
    password = forms.CharField(widget=forms.PasswordInput,error_messages=messages)


class User_rejister (forms.Form):
    full_name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=250)
    phone = PhoneNumberField()
    password = forms.CharField(widget=forms.PasswordInput)
    password3 = forms.CharField(widget=forms.PasswordInput)
    

    def clean_password3(self) :
        p1 = self.cleaned_data['password']
        p2 = self.cleaned_data['password3']

        if p1 and p2 and p1 != p2 :
           raise ValidationError ('passwords arent same')
        return p2
