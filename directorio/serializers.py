from rest_framework import serializers
from .models import Categoriadirectorio,Directorio
from articulos.serializers import SoloRevistaSerializer

class CategoriaSerializer(serializers.ModelSerializer):
    revista=SoloRevistaSerializer(many=False,read_only=True)
    class Meta:
        model   =   Categoriadirectorio
        fields  =   '__all__'

class SoloCategoriaDirSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Categoriadirectorio
        fields  =   ['categoria']

class DirectorioSerializer(serializers.ModelSerializer):
    categori=SoloCategoriaDirSerializer(many=False,read_only=True)
    revista_origen=SoloRevistaSerializer(many=False,read_only=True)
    class Meta:
        model   =   Directorio
        fields  =   '__all__'