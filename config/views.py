from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from login.models import User
from config.forms import AboutEditForm
from pprint import pprint

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
            userdata = User.objects.get(id=userselected)
            data = {
                'username': userdata.username,
                'first_name': userdata.first_name,
                'last_name': userdata.last_name,
                'bio': userdata.bio,
                'avatar': userdata.avatar
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
            users = User.objects.all()
        except:
            return redirect('index')

        context = {'form': form, 'userdata': userdata, 'users': users}
        pprint(dir(form.fields))
        return render(request, 'config/index.html', context)
    else:
        raise PermissionDenied()