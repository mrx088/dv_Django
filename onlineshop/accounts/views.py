
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import User_login
from django.contrib.auth import authenticate, login


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
    