from django.contrib import admin
from .models import Perfil
# Register your models here.

#admin.site.register(Perfil)
@admin.register(Perfil)
class AdminPerfil(admin.ModelAdmin):
    list_display=('user','revista','id',)