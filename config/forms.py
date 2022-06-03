from django import forms
from config.models import About

class AboutEditForm(forms.ModelForm):
    info = forms.CharField(widget = forms.Textarea(attrs={'rows':'3', 'cols':'5'}))

    class Meta:
        model = About
        fields = ('name', 'info', 'image',)