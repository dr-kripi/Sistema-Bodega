from webbrowser import get
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy

from apps.proveedor.models import Proveedor
from apps.proveedor.forms import ProveedorForm

# Create your views here.


class ProveedorHome(TemplateView):
    template_name = "proveedores/home.html"

class ProveedorListView(ListView):
    model = Proveedor
    template_name = "proveedores/listar.html"
    success_url = reverse_lazy('index')    
    paginate_by = 5

    def get_queryset(self):
        return self.model.objects.filter(estado = True)


class ProveedorCreateView(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = "proveedor/crear.html"
    success_url = reverse_lazy('proveedor:listar_proveedores')    


class ProveedorUpdateView(UpdateView):
    model = ProveedorForm
    form_class = ProveedorForm
    template_name = "usuarios/crear.html"
    success_url = reverse_lazy('usuario:listar_usuarios')


