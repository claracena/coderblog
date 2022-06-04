from django.shortcuts import render
from .models import About

# Create your views here.
def about(request):
    person = About.objects.all()
    context = {'about':person}
    return render(request, 'about/about.html', context=context)

