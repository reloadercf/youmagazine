from django.shortcuts import render
from .models import Directorio,Categoriadirectorio
from .serializers import DirectorioSerializer,CategoriaSerializer
from rest_framework import viewsets
from .pagination import DirectorioPagination
# Create your views here.

class DirectorioViewSet(viewsets.ModelViewSet):
    queryset            =   Directorio.objects.all()
    serializer_class    =   DirectorioSerializer
    pagination_class    =   DirectorioPagination
    def get_queryset(self,*args,**kwargs):
        origen_revista  =   self.request.GET.get("r")
        nombre_lugar  =   self.request.GET.get("directorio")
        queryset_list   =   super(DirectorioViewSet, self).get_queryset()
        if origen_revista:
            queryset_list   =queryset_list.filter(revista_origen__nombre_revista=origen_revista)
        if nombre_lugar:
            queryset_list   =queryset_list.filter(nombre_publico=nombre_lugar)    
        return queryset_list
    
class CategoriaDirectorioViewSet(viewsets.ModelViewSet):
    queryset            =   Categoriadirectorio.objects.all()
    serializer_class    =   CategoriaSerializer
    pagination_class    =   DirectorioPagination
    def get_queryset(self,*args,**kwargs):
        origen_revista  =   self.request.GET.get("r")
        nombre_categoria  =   self.request.GET.get("categoria")
        queryset_list   =   super(CategoriaDirectorioViewSet, self).get_queryset()
        if origen_revista:
            queryset_list   =queryset_list.filter(revista__nombre_revista=origen_revista)
        if nombre_categoria:
            queryset_list   =queryset_list.filter(categoria=categoria)    
        return queryset_list