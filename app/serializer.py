from django.forms import IntegerField
from rest_framework import serializers 


class colaboradorSerializer(serializers.Serializer):
    id_colaborador = serializers.CharField()
    id_empresa_colab = serializers.CharField()
    cpf = serializers.CharField()
    nome = serializers.CharField()
    email = serializers.CharField()
    telefone = serializers.CharField()
    endereco = serializers.CharField()
    empresa = serializers.CharField()



class EmpresasSerializer(serializers.Serializer):
    id_empresa = serializers.CharField()
    cnpj = serializers.CharField()
    nome = serializers.CharField()
    email = serializers.CharField()
    telefone = serializers.CharField()
    endereco = serializers.CharField()

