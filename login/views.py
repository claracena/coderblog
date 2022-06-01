from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def loginUser(request):
    # Login User
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if user exists
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Usuario inexistente')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            messages.error(request, 'Usuario o contraseña no existen')

    context = {}
    return render(request, 'login/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
