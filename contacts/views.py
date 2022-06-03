from django.shortcuts import render
from .models import Contacts
from .forms import ContactForm

# Create your views here.
def contacts(request):
    data = {
        'form': ContactForm(),
    }

    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            data['mensaje'] = "Mensaje enviado correctamente"
        else:
            data['form'] = form
    return render(request, 'contacts/contacts.html', data)

