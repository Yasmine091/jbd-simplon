from django.forms import ModelForm, DateTimeInput, TextInput, Textarea, Select
from .models import Note
    
class formulaireNote(ModelForm):
    class Meta:
        model = Note
        fields = ('student', 'date', 'subject', 'note',)
        widgets = {
            'student': Select(attrs={'class': 'form-control'}),
            'date': DateTimeInput(attrs={'type': 'date', 'class': 'date-input'}),
            'subject': TextInput(attrs={'class': 'form-control'}),
            'note': Textarea(attrs={'class': 'form-control'}),
        }