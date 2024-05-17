from django.shortcuts import render
from contact.models import Contact
from django.http import Http404
from contact.models import Category
from django.shortcuts import get_object_or_404, render

def index(request):
    contacts = Contact.objects.all().filter(show=True).order_by('id')[:10]
    context = {
        'contacts': contacts
    }
    return render(request,'contact/index.html', context )
def contact(request, contact_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    # if single_contact is None:
    #     raise Http404()
    single_contact = get_object_or_404(Contact.objects, pk=contact_id)
    context = {
        'contact': single_contact
    }
    return render(request,'contact/contact.html', context )
# Create your views here.
