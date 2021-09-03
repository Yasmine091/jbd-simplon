from django.urls import path, include
from notes import views

urlpatterns = [
    path('notes/', views.getNotes, name="readAll"),
    path('new/', views.newNote, name="create"),
    #, # urls de login, register, etc..
]