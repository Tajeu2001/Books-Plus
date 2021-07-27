from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from . forms import Registration
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            username = form.cleaned_data.get('username')

        messages.success(request,f'Account for {username} created,you can now login')
        return redirect('login')
    else:
        form = Registration()
    return render(request,'registration/registration_form.html',{"form":form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,template_name = "registration/login.html",context={"form":form})
