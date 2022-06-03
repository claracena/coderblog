from django import forms
from config.models import About

class AboutEditForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ('name', 'info', 'image',)