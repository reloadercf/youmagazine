from django.contrib import admin
from .models import Categorias,Revista
from import_export.admin import ImportExportModelAdmin
from .resources import CategoRevistaResource,RevistaResource
# Register your models here.
#admin.site.register(Categorias)
#admin.site.register(Revista)
@admin.register(Categorias)
class AdminCategoriRevistas(ImportExportModelAdmin):
    resources_class=CategoRevistaResource
    list_display=('nombre_categoria','revista_origen','id',)
@admin.register(Revista)
class AdminRevista(ImportExportModelAdmin):
    resources_class=RevistaResource
    list_display=('nombre_revista','tipo','descripcion','id',)    