from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from .forms import forms
from users import views

urlpatterns = [
    path('', views.defaultHome),
    path('', include('django.contrib.auth.urls')),
    path(
        'login/',
        LoginView.as_view(
            template_name="login.html",
            authentication_form=forms
        ),
        name='login'
    )
]