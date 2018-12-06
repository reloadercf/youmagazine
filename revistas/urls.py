"""revistas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from rest_framework import routers
from rest_framework.authtoken import views
from articulos.views import ArticuloViewSet,EspecialArticuloViewSet
from revista.views import CategoriaRevistaViewSet
from accounts.views import UserViewSet, MyUser
from cliente.views import ClienteViewSet, PlanesViewSet
from directorio.views import DirectorioViewSet,CategoriaDirectorioViewSet
from django.views.generic import TemplateView

class inicio(TemplateView):
    template_name = 'index.html'

router = routers.DefaultRouter()
router.register('filtroarticulos', ArticuloViewSet)
router.register('filtroespecialarticulo', EspecialArticuloViewSet)
router.register('filtrocategoria',CategoriaRevistaViewSet)
router.register('users', UserViewSet)
router.register('patrocinadores',ClienteViewSet)
router.register('planesporrevista',PlanesViewSet)
router.register('directorio',DirectorioViewSet)
router.register('categodirectorio',CategoriaDirectorioViewSet)



urlpatterns = [
    path('',inicio.as_view(),name='index'),
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
    path('publicar/', include(router.urls)),
    path('my_user/', MyUser.as_view()),
    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root': settings.MEDIA_ROOT}
    )
]
admin.site.site_header='Youmagazzine'
admin.site.index_title='Panel de control de las revistas'