from django import forms
from . import models




class ContactsForm(forms.ModelForm) :
    class Meta :
        model = models.Contact
        fields = ('name' , 'email' , 'subject' , 'body')