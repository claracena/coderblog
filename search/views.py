from django.shortcuts import render
from login.models import User

# Create your views here.

def search(request):
    user = User.objects.all()
    context = {'user': user}
    return render(request, 'search/search.html', context)