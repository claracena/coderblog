from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from login.models import User

class RegistrationForm(UserCreationForm):
    username = forms.TextInput()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class EditProfile(UserChangeForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100,
                               required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,
                               required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(widget = forms.Textarea(attrs={'rows':'3', 'cols':'5', 'max_length': 300}))
    avatar = forms.FileField(required=False,
                             widget=forms.FileInput(attrs={'class': 'form-control custom-avatar-input', 'accept': ".jpg, .jpeg, .png"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'bio', 'avatar']

class ChangePassowrd(PasswordChangeForm):
    old_password = forms.CharField(label='Contraseña Actual', widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(label='Contraseña Nueva', widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
