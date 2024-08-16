from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from typing import Any
from contactos.models import contactos
from django.db.models import QuerySet
class ContactListView(generic.ListView):
    model = contactos
    template_name = 'contactos/contact_list.html'
    paginate_by = 5
    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')
        
        if q:
            return contactos.objects.filter(nombre__icontains=q)
        else:
            return super().get_queryset()


class ContactCreateView(generic.CreateView):
    model = contactos
    fields = ('avatar','nombre', 'email', 'fecha', 'telefono')
    success_url = reverse_lazy('contactos_list')

class ContactUpdateView(generic.UpdateView):
    model = contactos
    fields = ('avatar','nombre', 'email', 'fecha', 'telefono')
    success_url = reverse_lazy('contactos_list')
    
class ContactDeleteView(generic.DeleteView):
    model = contactos
    success_url = reverse_lazy('contactos_list')

