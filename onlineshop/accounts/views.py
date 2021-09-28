
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import User_login , User_rejister
from django.contrib.auth import authenticate, login
from django.conf import settings



# Create your views here.
def accounts_login (request):
    form = User_login()
    if request.method == 'POST':
        form = User_login(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None :
                login(request,user)
                messages.success(request,'login succesfuly','info')
                return redirect('shop:shops')
            else:
                messages.error(request,'Your password or email isnt true','danger')
                return redirect('accounts:login')
    else:
        return render(request,'accounts/accounts_login.html',{'form':form})



def accounts_rejister(request):
    form = User_rejister()
    if request.meyhod== 'POST':
        form = User_rejister(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = settings.AUTH_USER_MODEL.create(email=cd['email'],phone=cd['phone']
            ,password1=cd['password1'],password2=cd['password2'])
            messages.success(request,'Now you create new account','success')
            return redirect('shop:shops')
        else:
            messages.success(request,'Try aggain please','warning')
    else:
        return render(request,'shop/rejister.html',{'form':form})

