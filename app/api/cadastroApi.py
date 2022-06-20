from rest_framework import permissions, status, viewsets
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import JsonResponse
from rest_framework.response import Response
from django.core import serializers

from ..models import * 
from ..serializer import *


class CadastroApi(viewsets.ModelViewSet):

    queryset = Empresas.objects.all()
    serializer_class = EmpresasSerializer
    def retrieve_id(self, request):
        try:
            
            result = Empresas.objects.all()
            
        except ObjectDoesNotExist as error:
            return JsonResponse(error, status=status.HTTP_410_GONE)

        print(result)
        serializer = EmpresasSerializer(result, many=True,context={'request': request})

    
        return Response(serializer.data, status=status.HTTP_200_OK)

class addColab(viewsets.ModelViewSet):

    queryset = colaborador.objects.all()
    serializer_class = colaboradorSerializer()
    def retrieve_add(self, request, cpf, nome, email, telefone, endereco, empresa, id_empresa_colab):
        try:
            
            result = colaborador.objects.raw(f"INSERT INTO app_colaborador (cpf, nome, email, telefone, endereco, empresa, id_empresa_colab) values ('{cpf}','{nome}','{email}','{telefone}', '{endereco}', '{empresa}', '{id_empresa_colab}')")
            
        except ObjectDoesNotExist as error:
            return JsonResponse(error, status=status.HTTP_410_GONE)

        print(result)
        serializer = colaboradorSerializer(result, many=True,context={'request': request})

    
        return Response(serializer.data, status=status.HTTP_200_OK)

class BuscarColab(viewsets.ModelViewSet):

    queryset = colaborador.objects.all()
    serializer_class = colaboradorSerializer()
    def retrieve_buscar(self, request, id):
        try:
            
            result = colaborador.objects.filter(id_empresa_colab = id)
            
        except ObjectDoesNotExist as error:
            return JsonResponse(error, status=status.HTTP_410_GONE)

        print(result)
        serializer = colaboradorSerializer(result, many=True,context={'request': request})

    
        return Response(serializer.data, status=status.HTTP_200_OK)


class removeColab(viewsets.ModelViewSet):

    queryset = colaborador.objects.all()
    serializer_class = colaboradorSerializer()
    def retrieve_remove(self, request, id):
        try:
            
            result = colaborador.objects.raw(f"DELETE from  app_colaborador WHERE id_colaborador = {id}")
            
        except ObjectDoesNotExist as error:
            return JsonResponse(error, status=status.HTTP_410_GONE)

        print(result)
        serializer = colaboradorSerializer(result, many=True,context={'request': request})

    
        return Response(serializer.data, status=status.HTTP_200_OK)
