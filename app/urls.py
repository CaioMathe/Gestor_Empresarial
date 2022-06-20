from django.urls import path
from app.views import *
from app.api.cadastroApi import *

urlpatterns = [

    path('', empresa, name='Empresas'),
    path('empresas/editar/<id>', editar_Empresas, name='editar_Empresas'),
    path('empresas/editar/remover/<id>', remove_empresa, name='remove_empresa'),
    path('empresas/cadastro', cadastro_Empresas, name='cadastro_Empresas'),

    

    # -----------------API-----------------------
    path('empresas/cadatros/numID', CadastroApi.as_view(actions={"get":"retrieve_id"}), name='retrieve_id',),
    path('empresas/editar/colaborador/<str:cpf>/<str:nome>/<str:email>/<str:telefone>/<str:endereco>/<str:empresa>/<str:id_empresa_colab>', addColab.as_view(actions={"get":"retrieve_add"}), name='retrieve_add',),
    path('empresas/cadastro/colaborador/<str:cpf>/<str:nome>/<str:email>/<str:telefone>/<str:endereco>/<str:empresa>/<str:id_empresa_colab>', addColab.as_view(actions={"get":"retrieve_add"}), name='retrieve_add',),
    path('empresas/editar/api/<str:id>', BuscarColab.as_view(actions={"get":"retrieve_buscar"}), name='retrieve_buscar',),
    path('empresas/editar/api/remove/<str:id>', removeColab.as_view(actions={"get":"retrieve_remove"}), name='retrieve_remove',),


]