from rest_framework import serializers

from .models import *


class DatosCorreoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosCorreo
        fields = '__all__'
