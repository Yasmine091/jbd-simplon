from django.contrib.auth.forms import AuthenticationForm
from django import forms
    
class forms(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(forms, self).__init__(*args, **kwargs)

    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))