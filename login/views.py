from django.shortcuts import redirect, render
from django.contrib import messages
# from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .models import User
from login.forms import RegistrationForm, EditProfile, ChangePassowrd

# Create your views here.

class PasswordsChangeView(PasswordChangeView):
    form_class = ChangePassowrd
    # form_class = PasswordChangeForm
    success_url = reverse_lazy('index')

def loginUser(request):
    # redirect if authenticated
    if request.user.is_authenticated:
        return redirect('index')

    # Which page to show
    page = 'login'
    errors = 0

    # Login User
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if user exists
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Usuario inexistente')
            errors += 1
            # return redirect('login')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        # If user is logged in
        if errors == 0:
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Contraseña invalida')
                # return redirect('login')

    context = {'page': page}
    return render(request, 'login/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('index')

def registerUser(request):
    # redirect if authenticated
    if request.user.is_authenticated:
        return redirect('index')
        
    context = {}
    # Register a new user
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(username=username, password=raw_password)
            login(request, account)
            return redirect('index')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
        
    return render(request, 'login/login.html', context)

def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            id_form = form.save(commit=False)
            id_form.save()
            return redirect('index')
    
    form = EditProfile(instance=request.user)

    context = {'form': form}
    return render(request, 'login/profile.html', context)

# def change_password(request):
#     form = PasswordChangeView
#     return redirect('index')

# class PasswordsChangeView(PasswordChangeView):
#     form_class = PasswordChangeForm
#     success_url = redirect('index')
