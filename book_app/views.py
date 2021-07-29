from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from . forms import Registration, UpdateUserForm, UpdateUserProfileForm,BookForm,RatingForm
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Profile,Book,Rating
from django.contrib.auth.models import User
from django.db.models import Avg


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


@login_required(login_url='login')
def profile(request, username):
    return render(request, 'profile.html')


def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    params = {
        'user_prof': user_prof,
    }
    return render(request, 'userprofile.html', params)


@login_required(login_url='login')
def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile', user.username)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form
    }
    return render(request, 'edit.html', params)


@login_required
def booklist(request):
    books = Book.objects.all()
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = request.user.profile
            upload.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = BookForm()
    return render(request, 'booklist.html', {'books': books,'form': form,'users': users,})


@login_required
def search(request):
    current_user = request.user
    all_books = Book.objects.all()
    parameter = request.GET.get('book')
    searched_books = Book.objects.filter(title__icontains=parameter)

    return render(request,'search.html',{'current_user':current_user,'books':searched_books})

@login_required
def about(request):
    return render(request,'about.html')

@login_required
def book(request ,book_id):
    current_user = request.user
    book = Book.objects.filter(id=book_id).first()
    ratings = Rating.objects.filter(book_id=book_id)
    usability_rating = Rating.objects.filter(book_id=book_id).aggregate(Avg('usability'))
    content_rating = Rating.objects.filter(book_id=book_id).aggregate(Avg('content'))
    design_rating = Rating.objects.filter(book_id=book_id).aggregate(Avg('design'))

    title = f'{book.title} details'
    return render(request,'book.html',{'title':title,'book':book,'current_user':current_user,'ratings':ratings,'usability_rating':usability_rating,'content_rating':content_rating,'design_rating':design_rating})   

@login_required(login_url='/accounts/login/')
def rate(request,book_id):
    current_user = request.user
    book = Book.objects.filter(id=book_id).first()
    if request.method == 'POST':
        rate_form = RatingForm(request.POST)
        if rate_form.is_valid():
            rating = rate_form.save(commit=False)
            rating.book = book
            rating.user = current_user
            rating.save()
            return redirect('book', book_id)
    else:
        rate_form = RatingForm()

    return render(request, 'review.html',{'current_user':current_user,'rate_form':rate_form,'book':book})
