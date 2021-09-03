from django.forms import ModelForm, TextInput, Textarea, Select, DateInput
from datetime import date
from .models import Note
    
class formulaireNote(ModelForm):
    class Meta:
        model = Note
        fields = ('student', 'date', 'subject', 'note',)
        widgets = {
            'student': Select(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'type': 'date', 'class': 'date-input', 'value': date.today().strftime("%d-%m-%Y")}),
            'subject': TextInput(attrs={'class': 'form-control'}),
            'note': Textarea(attrs={'class': 'form-control'}),
        }