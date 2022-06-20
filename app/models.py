from django.db import models

class Empresas(models.Model):
    id_empresa = models.CharField(max_length=20,primary_key=True)
    cnpj = models.IntegerField( blank=True, null=True)
    nome = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    telefone = models.IntegerField( blank=True, null=True)
    endereco = models.CharField(max_length=60, blank=True, null=True)


class colaborador(models.Model):
    id_colaborador =  models.AutoField(primary_key=True)
    id_empresa_colab = models.CharField( max_length=20,blank=True, null=True)
    cpf = models.IntegerField( blank=True, null=True)
    nome = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    telefone = models.IntegerField(blank=True, null=True)
    endereco = models.CharField(max_length=60, blank=True, null=True)
    empresa = models.CharField(max_length=60, blank=True, null=True)



