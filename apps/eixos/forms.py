from django import forms
from apps.eixos.models import Eixos

class Cadastrar_Eixo(forms.ModelForm):
    class Meta:
        model = Eixos
        fields = ['nome_eixo', 'cidade', 'coordenador_eixo', 'objetivo_eixo']

        widgets = {
            'nome_eixo':forms.TextInput(attrs={'class': 'form-control'}),
            'cidade':forms.Select(attrs={'class': 'form-control'}),
            'coordenador_eixo':forms.TextInput(attrs={'class': 'form-control'}),
            'objetivo_eixo':forms.Textarea(attrs={'class': 'form-control'}),
        }