from django.shortcuts import render
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
            return render(request, 'contacts/success.html')
        else:
            data['form'] = form
    return render(request, 'contacts/contacts.html', data)

def success(request):
    return render(request, 'contacts/success.html')

