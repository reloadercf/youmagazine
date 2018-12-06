from import_export import  resources
from import_export.fields import Field
from cliente.models import Planesvigentes,Cliente
from directorio.models import Categoriadirectorio,Directorio
from .models import Categorias,Revista
from articulos.models import Articulo

class ClienteResource(resources.ModelResource):
    class Meta:
        model=Cliente

class PlanesResource(resources.ModelResource):
    class Meta:
        model=Planesvigentes

class CategoDirResource(resources.ModelResource):
    class Meta:
        model=Categoriadirectorio

class DirectorioResource(resources.ModelResource):
    class Meta:
        model=Directorio

class CategoRevistaResource(resources.ModelResource):
    class Meta:
        model=Categorias

class RevistaResource(resources.ModelResource):
    class Meta:
        model=Revista

class ArticuloResource(resources.ModelResource):
    class Meta:
        model=Articulo