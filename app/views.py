from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from app.models import *


# Create your views here.
'''def dummy(request):
    return render(request, 'dummy.html')'''

def registration(request):
    user_obj = Userform()
    profile_obj = Profileform()
    context = {'user_obj' : user_obj, 'profile_obj' : profile_obj}
    if request.method == 'POST' and request.FILES:
        user_data = Userform(request.POST)
        profile_data = Profileform(request.POST, request.FILES)
        if user_data.is_valid() and profile_data.is_valid():
            un_user = user_data.save(commit= False)
            sub_psw = user_data.cleaned_data['password']
            un_user.set_password(sub_psw)
            un_user.save()

            un_profile = profile_data.save(commit= False)
            un_profile.username = un_user
            un_profile.save()

            send_mail('Registration',
                       'Successfully registred',
                       'abhishekvabhishek97@gmail.com',
                       [un_user.email],
                       fail_silently= False)

            return HttpResponse('Data is successfully submited')


    return render(request, 'registration.html', context)

#home page
def home(request):
    if request.session.get('username'):
        username = request.session.get('username')
        img_obj= User.objects.filter(username = username)
        d = {'img_obj' : img_obj}
        return render(request, 'home.html', d)
    return render(request, 'home.html')


#login page
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        auth_obj = authenticate(username = username, password = password)
        if auth_obj:
            if auth_obj.is_active:
                login(request, auth_obj)
                request.session['username']= username
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('User is not active')
        else:
            return HttpResponse('Data is not valid')


    return render(request, 'signup.html')
    
@login_required
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('registration'))
