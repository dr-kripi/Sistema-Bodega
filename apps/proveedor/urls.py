from django.urls import path
from .views import (ProveedorHome,ProveedorCreateView,ProveedorListView,ProveedorUpdateView)
urlpatterns = [
    path('',ProveedorHome.as_view(), name = 'home'),
    path('registrar/',ProveedorCreateView.as_view(), name = 'crear_proveedores'),
    path('listar/',ProveedorListView.as_view(), name = 'listar_proveedores'),
    path('actualizar/<int:pk>',ProveedorUpdateView.as_view(), name = 'actualizar_proveedores'),
    path('eliminar/<int:pk>',ProveedorUpdateView.as_view(), name = 'eliminar_proveedores'),

]