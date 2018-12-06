from django.db import models

# Create your models here.
class Categorias(models.Model):
    nombre_categoria        =   models.CharField(max_length=80)
    revista_origen          =   models.ForeignKey("revista.Revista", on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_categoria 
    
tipo_revista=[
    ('patrocinada','patrocinada'),
    ('informativa','informativa'),
    ('infosindirrectorio','infosindirrectorio'),
    ('patrosindirectorio','patrosindirectorio'),
]

class Revista(models.Model):
    nombre_revista          =   models.CharField(max_length=80, blank=False, null=False)
    logo                    =   models.ImageField(upload_to="logos_revistas",blank=False, null=False)
    descripcion             =   models.TextField()
    tipo                    =   models.CharField(choices=tipo_revista,max_length=50, blank=False,null=False)
    def __str__(self):
        return self.nombre_revista