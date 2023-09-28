from apps.bolsistas.models import Bolsista
from django import forms

class Cadastrar_Bolsista(forms.ModelForm):
    class Meta:
        model = Bolsista
        fields = ['nome', 'cpf', 'eixo', 'cidade_atuacao', 'carga_horaria', 'tipo_bolsa']

        widgets = {
            'nome': forms.TextInput(attrs={"class":"form-control", "label":"Nome"}),
            'cpf': forms.TextInput(attrs={"class":"form-control", "label":"CPF"}),
            'eixo': forms.Select(attrs={"class":"form-control", "label":"Eixo de atuação"}),
            'cidade_atuacao': forms.Select(attrs={"class":"form-control", "label":"Cidade de atuação"}),
            'carga_horaria': forms.Select(attrs={"class":"form-control", "label":"Carga horária semanal"}),
            'tipo_bolsa': forms.Select(attrs={"class":"form-control", "label":"Tipo de bolsa"}),
        }