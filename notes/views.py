from django.shortcuts import render, redirect
from notes.models import Note
from students.models import Student
from .forms import formulaireNote

# Create your views here.

def getNotes(request):
    if request.user.is_authenticated:
        notes = Note.objects.all()
        return render(request, "notes.html", {"list": notes})
    else:
        return redirect('/')

def newNote(request):
    
    if request.user.is_authenticated:
        form = formulaireNote()
        #notes = Note.objects.all()
        if request.method == 'POST':
            form = formulaireNote(request.POST)
            if form.is_valid:
                form.save()
            return render(request, "new.html", {"form": form, "msg": "Note enregistrée avec succès!"})
            
        return render(request, "new.html", {"form": form})
    
    else:
        return redirect('/')