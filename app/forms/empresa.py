from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Fieldset, Layout, Submit, Button, HTML
from django import forms

from app.models import Empresas


class EditEmpresa(forms.ModelForm):

    id_empresa = forms.CharField(
        label='Cód. da Empresa',
        required=False
    )
    cnpj = forms.IntegerField(
        label='CNPJ',
        required=True
    )
    telefone = forms.IntegerField(
        label='Telefone:',
        required=True
    )
    endereco = forms.CharField(
        label= 'Endereço:',
        required=True
    )
    nome = forms.CharField(
        label= 'Nome da empresa:',
        required=True
    )
    email = forms.CharField(
        label= 'Email:',
        required=True
    )

    helper = FormHelper()

    helper.form_class = 'form-group'

    helper.layout = Layout(
        Div(
                    Div(
                         HTML('<h1>Edição de empresa</h1>'),
                         HTML('<hr>')
                    ),
            Div(
                Div(
                    Div(
                        Field('id_empresa', css_class='id_empresa'),
                        Field('cnpj', css_class='cnpj'),
                        Field('nome', css_class='nome'),
                        css_class='flex-row'
                    ),
                      Div(
                        Field('email', css_class=' '),
                        Field('telefone', css_class=' '),
                        Field('endereco', css_class=' '),
                        css_class='flex-row'
                    ),
                        
               
                   
                    
                ),
                Div(
                HTML(' <input class="btn-retornar" onclick="javascript:location.href=`/`" type="button" value="Retornar">',
                
                ),
                HTML(' <input class="btn" type="submit" value="Salvar">'),
                css_class='div_btn'
                ),
            ), 
            
        )
    )

    class Meta:
        model = Empresas
        fields = ('__all__')


class Cadastroempresa(forms.ModelForm):

    id_empresa = forms.CharField(
        label='Código da Empresa',
        required=False
    )
    cnpj = forms.IntegerField(
        label='CNPJ',
        required=True
    )
    telefone = forms.IntegerField(
        label='Telefone:',
        required=True
    )
    endereco = forms.CharField(
        label= 'Endereço:',
        required=True
    )
    nome = forms.CharField(
        label= 'Nome da empresa:',
        required=True
    )
    email = forms.CharField(
        label= 'Email:',
        required=True
    )

    helper = FormHelper()

    helper.form_class = 'form-group'

    helper.layout = Layout(
        Div(
            Div(
                Div(
                    Div(
                         HTML('<h1>Cadastro de Empresa</h1>'),
                         HTML('<hr>')

                    ),
                    
                
                    Div(
                        Field('id_empresa', css_class='id_empresa'),
                        Field('cnpj', css_class='cnpj'),
                        Field('nome', css_class='nome'),
                        Field('email', css_class=' '),
                        Field('telefone', css_class=' '),
                        Field('endereco', css_class=' '),
                        css_class='campos'
                    ),
                    css_class='cadata'
                ),
                Div(
                HTML(' <input class="btn-retornar" onclick="javascript:location.href=`/`" type="button" value="Retornar">',
                
                ),
                HTML(' <input class="btn" type="submit" value="Continuar">'),
                css_class='div_btn'
                ),
            ), 
            
        )
    )

    class Meta:
        model = Empresas
        fields = ('__all__')
