from django.shortcuts import render
from django.core.exceptions import PermissionDenied

# Create your views here.
def config(request):
    if request.user.is_superuser:
        return render(request, 'config/index.html')
    else:
        raise PermissionDenied()
    