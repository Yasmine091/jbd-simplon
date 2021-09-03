from django.forms import ModelForm, DateTimeInput
from .models import Note
    
class formulaireNote(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        widgets = {
            'date': DateTimeInput(attrs={'type': 'date'})
        }