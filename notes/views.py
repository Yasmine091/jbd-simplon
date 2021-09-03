from django.shortcuts import render, redirect
from django.contrib import messages
from notes.models import Note
from students.models import Student
from .forms import formulaireNote

# Create your views here.

def getNotes(request):
    if request.user.is_authenticated:
        notes = Note.objects.all()
        students = Student.objects.all()
        return render(request, "notes.html", {"list": notes, "choi" : students})
    else:
        return redirect('/')

def newNote(request):
    
    if request.user.is_authenticated:
        form = formulaireNote()
        #notes = Note.objects.all()
        if request.method == 'POST':
            form = formulaireNote(request.POST)
            if form.is_valid:
                new_post = form.save(commit=False)
                new_post.author = request.user
                new_post.save()
            return render(request, "new.html", {"form": form, "msg": "Note enregistrée avec succès!"})
            
        return render(request, "new.html", {"form": form})
    
    else:
        return redirect('/')

def getNote(request, id):
    
    if request.user.is_authenticated:
        note = Note.objects.all().get(id=id)
        form = formulaireNote()
        #notes = Note.objects.all()
        if request.method == 'POST':
            form = formulaireNote(request.POST)
            if form.is_valid:
                new_post = form.save(commit=False)
                new_post.author = request.user
                new_post.save()
                
        return render(request, "note.html", {"note": note})
    
    else:
        return redirect('/')
    
def editNote(request, id):
    if request.user.is_authenticated:
        students = Student.objects.all()
        note = Note.objects.all().get(id=id)
        form = formulaireNote(instance=note)
        if request.method == 'POST':
            form = formulaireNote(request.POST)
            if form.is_valid:
                student = Student.objects.all().get(id=request.POST['student'])
                edit_post = form.save(commit=False)          
                edit_post.author = request.user
                edit_post.student = student
                edit_post.subject = request.POST['subject']
                edit_post.note = request.POST['note']
                edit_post.date = request.POST['date']
                edit_post.save()
                messages.success(request, 'Note modifiée avec succès!')
                return redirect('/note/'+ str(id))
        return render(request, "edit.html", {"note": note, "students": students})
    else:
        return redirect('/')
    
def delNote(request, id):
    if request.user.is_authenticated:
        note = Note.objects.all().get(id=id)
        note.delete()
        messages.success(request, 'Note suprimée avec succès!')
        return redirect('/notes')
    
    else:
        return redirect('/')
    