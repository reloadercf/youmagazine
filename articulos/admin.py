from django.contrib import admin
from .models import Articulo
from revista.resources import ArticuloResource
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Articulo)
class AdminArticulo(ImportExportModelAdmin):
    resources_class=ArticuloResource
    list_display=('id','slug','origen_revista','fecha_creacion','en_portada','categoria','patrocinador','fecha_fin','fecha_modificacion',)