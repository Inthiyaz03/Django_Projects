from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.tweet_list,name='tweet_list'),
    path('<int:tweet_id>/edit/', views.tweet_edit,name='tweet_edit'),
    path('create/', views.tweet_create,name='tweet_create'),
    path('<int:tweet_id>/delete/', views.tweet_delete,name='tweet_delete'),
    path('register/', views.register,name='register'),
     path('accounts/logout/', auth_views.LogoutView.as_view(next_page='tweet_list'), name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]