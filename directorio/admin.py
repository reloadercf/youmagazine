from django.contrib import admin
from .models import Categoriadirectorio,Directorio
from import_export.admin import ImportExportModelAdmin
from revista.resources import CategoDirResource,DirectorioResource
# Register your models here.

@admin.register(Categoriadirectorio)
class AdminCategoDir(ImportExportModelAdmin):
    resource_class = CategoDirResource
    list_display=('categoria','revista','id',)
@admin.register(Directorio)
class AdminDirectorio(ImportExportModelAdmin):
    resource_class = DirectorioResource
    list_display=('nombre_publico','categori','revista_origen','cliente','sitioweb','id',)    