from django.shortcuts import render
from .models import Contacts
from contacts.forms import ContactForm

# Create your views here.
def contacts(request):
    if request.method == 'POST': # If the form has been submitted...
        contact_form = ContactForm(request.POST) # A form bound to the POST data
        if contact_form.is_valid(): # check if the form is valid
            info = contact_form.cleaned_data # get the cleaned data
            contact = Contacts(name=info['name'], email=info['email'], message=info['message']) # create a new contact message
            contact.save()
            return render(request, 'contacts/contacts.html')

    else:
        contact_form = ContactForm() # an unbound form
    return render(request, 'contacts/contacts.html', {'contact_form': contact_form})

