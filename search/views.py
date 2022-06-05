from django.shortcuts import render
from login.models import User
from django.db.models import Q

# Create your views here.

# def search(request):
#     user = User.objects.all()
#     context = {'user': user}
#     return render(request, 'search/search.html', context)

def search(request):
    if request.method == 'POST':
        search_text = request.POST.get('search')
        user = User.objects.filter(Q(first_name__contains=search_text) | Q(last_name__contains=search_text) )
        context = {'user': user, 'search': 'resultado'}
        return render(request, 'search/search.html', context)
    else:
        return render(request, 'search/search.html', {'search': 'limpio'})