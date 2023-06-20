from rest_framework import serializers
from django.contrib.auth.models import User

from .models import UsuariosComplementos


class UsuariosComplementosSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuariosComplementos
        fields = [
            "id",
            "cpf_cnpj",
            "ramal",
            "departamento",
            "usuario",
            "filial",
        ]


class UsuariosSerializer(serializers.ModelSerializer):
    # complemento = UsuariosComplementosSerializer()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_superuser",
            "is_active",
            # "complemento",
        ]
        delth = 1


class UsuariosSimplesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
        ]
