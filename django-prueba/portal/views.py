from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.core.mail import send_mail
from django.conf import settings
from .models import Ofertas


# Create your views here.


def home(request):
    ofertas = Ofertas.objects.all()
    print(ofertas)
    return render(request, 'home.html',{
        'ofertas': ofertas
    })


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                subject = 'NotReply'
                message = 'Se ha creado exitosamente el usuario, ya puedes buscar tu oferta laboral'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['mail']]
                send_mail(subject, message, email_from, recipient_list)
                
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('createduser')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Username already exists'
                })
        return render('signup.html', {
            'form': UserCreationForm,
            'error': 'Password do not match'
        })


def tasks(request):
    return render(request, 'tasks.html')


def signout(request):
    logout(request)
    return redirect('home')


def singin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or passwor is incorrect'
            })
        else:
            login(request, user) #guardar sesion de usuario
            return redirect('tasks')

def createduser(request):
    return render(request, 'createduser.html')