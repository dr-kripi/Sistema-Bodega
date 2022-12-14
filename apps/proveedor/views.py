from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy

from apps.proveedor.models import Proveedor
from apps.proveedor.forms import ProveedorForm

# Create your views here.


class ProveedorHome(TemplateView):
    template_name = "proveedores/home.html"


class ProveedorActivo(TemplateView):
    template_name = "components/estado_activo.html"


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
    template_name = "proveedores/crear.html"
    success_url = reverse_lazy('proveedor:listar_proveedores')    


class ProveedorUpdateView(UpdateView):
    model = ProveedorForm
    form_class = ProveedorForm
    template_name = "proveedores/crear.html"
    success_url = reverse_lazy('usuario:listar_usuarios')



class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = 'proveedores/prveedor_delete_view.html'
    success_url = reverse_lazy ('proveedor:listar_proveedores')
    
    def post(self, request, pk,*args, **kwargs):
        object = self.model.objects.get(id=pk)

        if object.estado == True:
            return redirect('proveedor:eliminar_proveedores')

        else:
            object.estado = False
            object.delete()
            return redirect('preveedor:listar_proeevodres')