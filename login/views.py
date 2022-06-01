from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from login.forms import RegistrationForm

# Create your views here.

def loginUser(request):
    # Which page to show
    page = 'login'

    # Login User
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if user exists
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Usuario inexistente')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        # If user is loged in
        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            messages.error(request, 'Usuario o contraseña no existen')

    context = {'page': page}
    return render(request, 'login/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
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
            return redirect('login')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
        
    return render(request, 'login/login.html', context)
