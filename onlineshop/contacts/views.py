from django.shortcuts import redirect, render
from . import forms

# Create your views here.
def contact_us (request) :
    if request.method == 'POST':
        form = forms.ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop:shops')

    else:
        form = forms.ContactsForm()

    return render (request,'contacts/contact.html',{'form':form})