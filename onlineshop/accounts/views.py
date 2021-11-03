
from django.contrib import messages
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from .forms import User_login , User_rejister , PhoneloginForm , Code
from django.contrib.auth import authenticate, login, logout
from .models import User, follow
from random import randint
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy



class Userresetpassword(auth_views.PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    success_url =  reverse_lazy ('accounts:password_reset_done')
    email_template_name = 'accounts/password_reset_email.html'


class PasswordResetDone (auth_views.PasswordResetDoneView):
    template_name = 'accounts/reset_done.html'


class password_reset_confirm(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')

class password_reset_complete(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'





# Create your views here.
def accounts_login (request):
    next = request.GET.get('next')
    if request.method == 'POST':
        form = User_login(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None :
                login(request,user)
                messages.success(request,'login succesfuly','info')
                if next :
                    return redirect(next)
                return redirect('shop:shops')
            else:
                messages.error(request,'Your password or email isnt true','danger')
            
    else:
        form = User_login()

    return render(request,'accounts/accounts_login.html',{'form':form})


def accounts_phonelogin (request) :
    if request.method == 'POST':
        form = PhoneloginForm(request.POST)
        if form.is_valid():
            global phone , random_num
            phone = f"+98{form.cleaned_data['phone']}"
            phone1 = f"0{form.cleaned_data['phone']}"
            user = User.objects.filter(phone=phone)
            if user.exists():
                random_num = randint(10000,99999)
                print(random_num)
                # api = KavenegarAPI('5067514C4C68656C5363745333766C47704378634E497A6A644D35414750666F314849346D67744A6B58733D') 
                # params = { 'sender' : '100047778', 'receptor': '09901020713', 'message' :'.وب سرویس پیام کوتاه کاوه نگار' } 
                # response = api.sms_send( params) 
                return redirect ('accounts:phonelogincheack')
            else:
                messages.error(request,'This phone number doesnt signup in website','warning')
    else:
        form = PhoneloginForm()
    return render (request , 'accounts/phonelogin.html', {'form' :form})


def accounts_phonelogincheack (request) :
    if request.method == 'POST':
        form = Code(request.POST)
        if form.is_valid():
            if random_num == form.cleaned_data['code']:
                user = User.objects.get(phone=phone)
                login (request,user)
                return redirect ('shop:shops')
            else :
                messages.error(request,'Verify code is wrong try aggain' , 'danger')
    else :
        form = Code()
    return render(request,'accounts/cheackphone.html',{'form':form})


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



@login_required
def accounts_dashboard(request,user_id):
    user = User.objects.get(pk=user_id)
    is_following = False
    user_cheack = follow.objects.filter(from_user=request.user,to_user=user)
    if user_cheack.exists():
        is_following = True


    return render (request,'accounts/dashboard.html',{'user':user , 'is_following' :is_following})



def accounts_users(request):
    users = User.objects.filter(is_admin=False)
    return render (request,'accounts/all_users.html', {'users':users})




@login_required
def follow_acc (request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        following = User.objects.get(pk=user_id)
        cheack_relation = follow.objects.filter(from_user=request.user,to_user=following)
        if cheack_relation.exists():
            return JsonResponse({'status':'exists'})
        else:
            follow(from_user=request.user,to_user=following).save()
            return JsonResponse({'status':'ok'})

@login_required
def unfollow_acc (request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        following = User.objects.get(pk=user_id)
        cheack_relation = follow.objects.filter(from_user=request.user,to_user=following)
        if cheack_relation.exists():
            cheack_relation.delete()
            return JsonResponse({'status':'ok'})
        else:
            return JsonResponse({'status':'notexists'})