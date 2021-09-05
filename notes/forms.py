from django.forms import ModelForm, TextInput, Textarea, SelectMultiple, DateInput, ModelMultipleChoiceField, ModelChoiceField, Select
from datetime import date
from .models import Note
from students.models import Student
    
class formulaireNote(ModelForm):
    class Meta:
        model = Note
        fields = ('student', 'date', 'subject', 'note',)
        student = ModelMultipleChoiceField(queryset=Student.objects.all(), to_field_name="student")
        widgets = {
            'student': SelectMultiple(attrs={'class': 'form-control', 'size': 1}),
            'date': DateInput(attrs={'type': 'date', 'class': 'date-input', 'value': date.today().strftime("%d-%m-%Y")}),
            'subject': TextInput(attrs={'class': 'form-control'}),
            'note': Textarea(attrs={'class': 'form-control'}),
        }