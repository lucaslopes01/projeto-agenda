from django.shortcuts import render
from contact.models import Contact
from contact.models import Category
def index(request):
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts
    }
    return render(request,'contact/index.html', context )
# Create your views here.
