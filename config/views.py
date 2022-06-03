from django.shortcuts import render, redirect
# from django.contrib import messages
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
            users = About.objects.all()
        except:
            return redirect('index')
        # imagename = None

        try:
            userselected = request.GET['id']
        except:
            userselected = None

        # if userselected is not None:
        #     if About.objects.filter(id=userselected).exists():
        #         userdata = About.objects.get(id=userselected)
        #     else:
        #         return redirect('config')
        # else:
        #     try:
        #         users = About.objects.all()
        #     except:
        #         return redirect('index')
        # print(userdata._meta.get_field('image'))

        # if request.method == 'POST':
        #     # print(request.FILES['imagen'].__dict__)
        #     id = request.POST.get('uid')
        #     name = request.POST.get('nombre-apellido')
        #     bio = request.POST.get('bio')
        #     if request.FILES['imagen'] != '':
        #         imagename = userdata._meta.get_field('image')
        #     else:
        #         imagename = request.FILES['imagen']
        #     # imagename = request.FILES['imagen'] if 'imagename' in request.FILES else None
            
        #     # if imagename is None:
        #     #     imagename = userdata._meta.get_field('image')

        #     userindb = About.objects.get(id=id)
        #     userindb.name = name
        #     userindb.info = bio
        #     userindb.image = imagename
        #     userindb.save()
        #     return redirect('index')

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
        # context = {'form': form, 'userdata': userdata, 'users': users}
        context = {'form': form, 'userdata': userdata, 'users': users}
        return render(request, 'config/index.html', context)
    else:
        raise PermissionDenied()