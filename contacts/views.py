from django.shortcuts import render

# Create your views here.
def contacts(request):
    return render(request, 'contacts/contacts.html')


def contact_success(request):
    return render(request, 'contacts/contact_success.html')