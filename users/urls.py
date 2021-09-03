from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from .forms import UserLoginForm
from users import views

urlpatterns = [
    path('', views.defaultHome),
    path('', include('django.contrib.auth.urls')),
    path(
        'login/',
        LoginView.as_view(
            template_name="login.html",
            authentication_form=UserLoginForm
        ),
        name='login'
    ),
    path('signout/', views.logoutPage, name='signout')
    
]
