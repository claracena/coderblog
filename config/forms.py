from django import forms
from login.models import User

class AboutEditForm(forms.ModelForm):
    # username = forms.CharField(max_length=100,
    #                            required=True,
    #                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    # first_name = forms.CharField(max_length=100,
    #                            required=False,
    #                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    # last_name = forms.CharField(max_length=100,
    #                            required=False,
    #                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    # bio = forms.CharField(widget = forms.Textarea(attrs={'rows':'3', 'cols':'5', 'max_length': 300}))
    # avatar = forms.FileField(required=False,
    #                          widget=forms.FileInput(attrs={'class': 'form-control', 'accept': ".jpg, .jpeg, .png"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'bio', 'avatar',)