
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import User_login , User_rejister
from django.contrib.auth import authenticate, login, logout
from .models import User



# Create your views here.
def accounts_login (request):
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
            
    else:
        form = User_login()

    return render(request,'accounts/accounts_login.html',{'form':form})



def accounts_rejister(request):
    
    if request.method== 'POST':
        form = User_rejister(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(full_name=cd['full_name'],email=cd['email'],phone=cd['phone'] ,password=cd['password'],)
            user.save()
            messages.success(request,'Now you create new account','success')
            return redirect('shop:shops')
    else:
        form = User_rejister()
    return render(request,'accounts/rejister.html',{'form':form})


def accounts_logout (request):
    logout(request)
    messages.info(request,'Logout successfuly')
    return redirect('shop:shops')




