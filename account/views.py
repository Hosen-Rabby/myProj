from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.

# uname = User.objects.filter('username')
def registration(request):
    title = 'Registration'
    form = RegistrationForm(request.POST)


    context = {
        'form' : form,
        'title' : title,
        }
    
    if request.user.is_authenticated:
        return redirect('homeApp:home_page')
    
    else:
        # print('hello reg')
        # form = RegistrationForm()
        
        if request.method == "POST":
            username = request.POST.get('username')
            email = request.POST.get('email')
            pass1 = request.POST.get('password1')
            pass2 = request.POST.get('password2')

            print(username, email, pass1, pass2)
            # user=authenticate(request, username = username)

            def clean_name(self):
                userVal = self.cleaned_data['username']
                print('38', userVal)

            if User.objects.filter(username=username).exists():
                context = {
                    'usererror':'Username or email already exist',
                    }
                return render(request, 'account/registration_form.html', context)
            elif User.objects.filter(email=email).exists():
                context = {
                    'usererror':'email already exist',
                    }
                return render(request, 'account/registration_form.html', context)

            elif pass2 != pass1:
                context = {
                    'passerror':'pass not matched',
                    }
                return render(request, 'account/registration_form.html', context)
            
            else:
                new_user = User.objects.create_user(username, email, pass1)
                new_user.save()
                return redirect('homeApp:home_page')

                

            # form = RegistrationForm(request.POST)
            # print(form)
            # print(form.errors)
            # if form.is_valid():
            #     form.save()
            #     return redirect('accountApp:success')

    return render(request, 'account/registration_form.html', context)

def success(request):
    return render(request, 'account/success.html')


def logoutUser(request):
    logout(request)
    return redirect('homeApp:home_page')

def logintUser(request):
    if request.user.is_authenticated:
        return redirect('homeApp:home_page')
    else:
        print('hello login')
        form = RegistrationForm()
        if request.method == "POST":
            form = RegistrationForm(request.POST)
            print(form)
            if form.is_valid():
                form.save()

    return render(request, 'account/login.html', {'form': form})
