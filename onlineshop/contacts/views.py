from django.shortcuts import redirect, render
from . import forms

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def contact_us (request) :
    if request.method == 'POST':
        form = forms.ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            msg = form.cleaned_data['body']
            email_gmail = form.cleaned_data['email']
            subject = 'Hello sir , you have a new message'
            message = f'This message ({msg}) send by {email_gmail}  '
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['ali.bk0010@gmail.com',]
            send_mail( subject, message, email_from, recipient_list )
            return redirect('shop:shops')

    else:
        form = forms.ContactsForm()

    return render (request,'contacts/contact.html',{'form':form})