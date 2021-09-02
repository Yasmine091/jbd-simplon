from django.urls import path, include

urlpatterns = [
    path('', include('django.contrib.auth.urls'))
    #, # urls de login, register, etc..
]