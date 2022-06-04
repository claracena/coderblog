from django.shortcuts import render
from login.models import User

# Create your views here.

def search(request):
    user = User.objects.get(id=2)
    context = {'user': user}
    return render(request, 'search/search.html', context)
    # return render(request, 'search/search.html')