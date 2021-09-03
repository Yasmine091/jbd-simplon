from django.urls import path, include
from notes import views

urlpatterns = [
    path('new/', views.newNote, name="create"),
    path('notes/', views.getNotes, name="readAll"),
    path('note/<int:id>', views.getNote, name="readOne"),
    path('edit/<int:id>', views.editNote, name="update"),
    path('del/<int:id>', views.delNote, name="delete"),
    #, # urls de login, register, etc..
]