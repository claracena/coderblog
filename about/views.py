from django.shortcuts import render
from login.models import User

# Create your views here.
def about(request):
    person = User.objects.all()
    context = {'about':person}
    return render(request, 'about/about.html', context=context)

