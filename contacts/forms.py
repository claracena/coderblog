from django import forms
from .models import Contacts

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Escriba su mensaje...'}),
        }

