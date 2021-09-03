from django.urls import path, include
from users import views

urlpatterns = [
    path('', views.defaultHome),
    path('', include('django.contrib.auth.urls'))
    #, # urls de login, register, etc..
]