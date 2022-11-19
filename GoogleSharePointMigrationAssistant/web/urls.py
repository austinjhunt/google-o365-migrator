"""GoogleSharePointMigrationAssistant URL Configuration"""
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # Account management
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', login_required(LogoutView.as_view()), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup')
]