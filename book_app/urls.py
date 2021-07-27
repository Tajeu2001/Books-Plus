from django.urls import re_path,path,include
from django.contrib.auth import views as auth_views
from . import views 


urlpatterns = [
  path('accounts/register/',views.register,name='register'),
  path('accounts/login/',views.login,name='login'),
  path('logout/',auth_views.LogoutView.as_view(template_name = 'registration/logout.html'),name='logout'),
  path('',views.index, name='index'),
  path('profile/<username>/', views.profile, name='profile'),
  path('profile/<username>/settings', views.edit_profile, name='edit'),
]