from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.core.files.storage import FileSystemStorage
from .models import About
from config.forms import AboutEditForm

# Create your views here.
def config(request):
    if request.user.is_superuser:
        users = None
        userselected = None
        userdata = None

        try:
            userselected = request.GET['id']
        except:
            userselected = None

        if userselected is not None:
            userdata = About.objects.get(id=userselected)
            data = {
                'name': userdata.name,
                'info': userdata.info,
                'image': userdata.image
            }
            form = AboutEditForm(data)
        else:
            form = AboutEditForm()
            
        if request.method == 'POST':
            form = AboutEditForm(request.POST, request.FILES, instance=userdata)
            if form.is_valid():
                id_form = form.save(commit=False)
                id_form.save()
                return redirect('index')
            else:
                return redirect('config')

        try:
            users = About.objects.all()
        except:
            return redirect('index')

        context = {'form': form, 'userdata': userdata, 'users': users}
        return render(request, 'config/index.html', context)
    else:
        raise PermissionDenied()