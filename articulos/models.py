from django.db import models
from revista.models import Revista
from cliente.models import Cliente
from django.contrib.auth.models import User
from .utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save

# Create your models here.
#los choices
status_articulo_choice =(
    ("Publicado","Publicado"),
    ("No Publicado","No publicado")
)
video_choice=(
    ("youtube","youtube"),
    ("vimeo","vimeo"),
    ("sin video","sin video")
)
llamadas=(
    ("Contactar","Contactar"),
    ("Visitar","Visitar"),
    ("Compar","Comprar"),
    ("Llamar","Llamar"),
    ("Sinllamada","Sinllamada")
)
#El modelo

class Articulo(models.Model):
    titulo                  =   models.CharField(max_length=50)
    en_portada              =   models.BooleanField(default=False)
    origen_revista          =   models.ForeignKey("revista.Revista", on_delete=models.CASCADE)
    categoria               =   models.CharField(max_length=100,blank=False,null=False)    
    imagen_destacada_uno    =   models.TextField()
    redactado_por           =   models.CharField(default="Equipo MX",max_length=300,null=True,blank=True)
    status                  =   models.CharField(choices=status_articulo_choice,default="Publicado", max_length=50)
    cuerpo_uno              =   models.TextField(null=False,blank=False)
    imagen_destacada_dos    =   models.TextField()
    cuerpo_dos              =   models.TextField(null=True,blank=True)
    video_tipo              =   models.CharField(choices=video_choice, default="sin video", max_length=50)
    urlvideo                =   models.URLField(blank=True,null=True)
    patrocinador            =   models.ForeignKey(Cliente, related_name='cliente_asignado', on_delete=models.CASCADE)
    llamada_accion_uno      =   models.CharField(choices=llamadas,max_length=50)
    imagen_llamada_uno      =   models.TextField()
    url_llamada_uno         =   models.TextField(blank=True,null=True)
    llamada_accion_dos      =   models.CharField(choices=llamadas,max_length=50)
    imagen_llamada_dos      =   models.TextField()
    url_llamada_dos         =   models.TextField(blank=True,null=True)
    cortesia_de             =   models.CharField(max_length=300,null=True,blank=True)
    link_cortesia           =   models.URLField(blank=True,null=True)
    fecha_mostrada          =   models.DateField(blank=False,null=False)
    fecha_publicacion       =   models.DateTimeField(blank=False,null=False)
    fecha_fin               =   models.DateField(blank=False,null=False)
    fecha_creacion          =   models.DateTimeField(auto_now_add=True)
    fecha_modificacion      =   models.DateTimeField(auto_now=True)
    slug                    =   models.CharField(max_length=200, blank=True, null=True)
    usuario_publicador      =   models.ForeignKey(User, related_name="publicador", on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

# Esta funcion genera un SLUG para cada articulo
def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(rl_pre_save_receiver, sender=Articulo)



# Esta funcion genera un SLUG para cada articulo
def pre_save_articulo(sender, instance, *args, **kwargs):
    if not instance.titulo:
        instance.titulo = '%s' % (instance.articulo.titulo)


pre_save.connect(pre_save_articulo, sender=Articulo)
