from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
# from app.api import *
# from app.serializer import *
from app.models import *


from app.forms.empresa import Cadastroempresa, EditEmpresa



def empresa(request):
    return render(request, 'empresas.vue')


def cadastro_Empresas(request): 
    form = Cadastroempresa(request.POST or None)

    if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(
                request, f'cadastrado com sucesso'
            )
            return redirect('Empresas')

    else:
        messages.error(request, form.errors)

    return render(request, 'cadastroEmpresa.vue', {'form': form})

def remove_empresa(request, id):
        obj = get_object_or_404(Empresas, id_empresa=id)

        try:
            obj.delete()

            messages.success(
                request, f'Empresa removida com sucesso'
            )
        except Exception as error:
            messages.error(
                request, f'Empresa removida sem sucesso'
            )

        return redirect('Empresas')

def editar_Empresas(request, id):
    context = {}

    obj = get_object_or_404(Empresas, id_empresa=id)

    form = EditEmpresa(request.POST or None, instance=obj)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()


        return redirect('Empresas')


    context["form"] = form

    return render(request, 'editarEmpresa.vue', context)



