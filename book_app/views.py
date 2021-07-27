from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from . forms import Registration
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Profile
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


@login_required
def index(request):

    return render (request, 'index.html')

@login_required
def profile(request):
    current_user = request.user
    projects = Project.objects.filter(user_id= current_user.id).all()

    return render(request,'profile.html',{'current_user':current_user,'projects':projects})

@login_required
def update_profile(request):
    current_user = request.user
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST,instance=request.user)
        return redirect('profile')

    else:
        user_form = UpdateUserForm(instance=request.user)
        
    return render(request, 'update_profile.html', {'user_form':user_form , })   
