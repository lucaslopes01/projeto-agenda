from django.shortcuts import render

from contact.models import Contact
from django.shortcuts import get_object_or_404,redirect,render

def index(request):
    contacts = Contact.objects.all().filter(show=True).order_by('id')
    context = {
        'contacts': contacts,
        'site_title':'Contatos - '
    }
    return render(request,'contact/index.html', context )

def search(request):
  
    search_value = request.GET.get('q','').strip() 
    if search_value == '':
        return redirect('contact:index')
        
    print('search_value',search_value)
    contacts = Contact.objects.filter(show=True).filter(first_name__icontains=search_value).order_by('id')
    context = {
        'contacts': contacts,
        'site_title':'Search - '
    }
    return render(request,'contact/index.html', context )
def contact(request, contact_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    # if single_contact is None:
    #     raise Http404()
    single_contact = get_object_or_404(Contact.objects, pk=contact_id)
    site_title = f'{single_contact.first_name} {single_contact.last_name} - '
    context = {
        'contact': single_contact,
        'site_title': site_title
    }
    return render(request,'contact/contact.html', context )
# Create your views here.
